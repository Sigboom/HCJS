<template>
	<div class="teamBox col-md-12">
		<div class="teamManager col-md-9">
			<div class="teamChoose col-md-12">
				<h4>管理<span><h6>(仅管理员可见)</h6></span></h4>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>编辑公告
				</a>
				<span class="col-md-1"></span>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>管理成员
				</a>
				<span class="col-md-1"></span>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>文档授权
				</a>
				<span class="col-md-1"></span>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>团队消息
				</a>
			</div>
			<div class="teamFiles col-md-12">
				<h4>团队文档</h4>
				<div class="teamFileContiner col-md-12">
					<p class="showPot col-md-12" v-show="this.$store.state.teamteamFileCounter == 0">{{ this.msg }}</p>
					<div class="thumbnail col-md-12"
					@mouseenter="askMenu(id)" @mouseleave="noAskMenu(id)"
					v-for="(file, id) in this.$store.state.teamFileList" :key="file.id" v-show="!file.filter">
						<div class="filePic col-md-1">
							<span class="glyphicon" :class="file.icon" aria-hidden="true"></span>
						</div>
						<div class="caption col-md-5">
							<h4>{{ file.name }}</h4>
							<p>{{ file.commitMsg }}</p>
						</div>
						<div class="menuField col-md-6">
							<span class="floatRight col-md-4" v-show="file.showMenu || file.star">
								<a class="btn btn-default" role="button" @click="starChange(id, file.id)">
									<span class="glyphicon" :class="file.starChangeIcon" aria-hidden="true"></span>Star
								</a>
							</span>
							<span class="floatRight col-md-4" v-show="file.showMenu">
								<a class="btn btn-primary" role="button" @click="download(id, file.id)">
									<span class="glyphicon" :class="file.downloadChangeIcon" aria-hidden="true"></span>Download
								</a>
							</span>
							<span class="floatRight col-md-2" v-show="file.showMenu">
								<a class="btn btn-default dropdown-toggle" data-toggle="dropdown" role="button"
								aria-haspopup="true" aria-expanded="false">
								<span class="glyphicon dropdown glyphicon-option-vertical" aria-hidden="true"></span>
								</a>
								<ul class="dropdown-menu">
									<li><a href="#">Action</a></li>
									<li><a href="#">Another action</a></li>
									<li><a href="#">Something else here</a></li>
									<li role="separator" class="divider"></li>
									<li><a href="#">Separated link</a></li>
									<li role="separator" class="divider"></li>
									<li><a @click="deleteFile(id, file.id)">
										<span class="glyphicon glyphicon-trash" aria-hidden="true">&nbsp;删除</span>
									</a></li>
								</ul>
							</span>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="teamMsg col-md-3">
			{{ msg }}
		</div>
	</div>
</template>

<script>

export default {
	name: 'teamBox',
	data() {
		return {
			msg: "暂无信息",
		}
	},
	methods: {
		askMenu(i) {
			this.$store.state.teamFileList.splice(i, 1, {
					...this.$store.state.teamFileList[i],
					'showMenu': true,
					'starChangeIcon': {
							"glyphicon-star-empty": !this.$store.state.teamFileList[i].star,
							"glyphicon-star": this.$store.state.teamFileList[i].star,
						},
					})
		},
		noAskMenu(i) {
			this.$store.state.teamFileList.splice(i, 1, {
					...this.$store.state.teamFileList[i],
					'showMenu': false,
					})
		},
		download(i, fileId) {
			let a = document.createElement('a')
			let userId = this.$store.state.userId;
			let fileID = fileId;
			a.href = "/getDownloadFile?userId=" + userId + "&&fileId=" + fileId;
			a.click();
		},
		starChange(i, id) {
			let stat = !this.$store.state.teamFileList[i].star;
		
			var	params = {
				userId: this.$store.state.userId,
				fileId: id,
				star: stat,
			};
			axios.get('/getStar', { params: params }).then(res => {
				if (res.data == 'OK') {
					this.$store.state.teamFileList.splice(i, 1, {
							...this.$store.state.teamFileList[i],
							'star': stat,
							'starChangeIcon': {
								"glyphicon-star-empty": !stat,
								"glyphicon-star": stat,
							},
						});
					this.$store.commit('SET_STARFILE', stat);
					//console.log(this.$store.state.teamFileList[i]);
				} else {
					console.log(res.data);
				}
			}).catch(err => {
				console.log(err);
			});
		},
		deleteFile(index, id) {
			if (this.$store.state.userId) {
				var	params = {
					userId: this.$store.state.userId,
					fileID: id
				}
				axios.get('/deleteFile', { params: params }).then(res => {
					if (res.data.state == 'ok') {
						this.$store.commit('DELETE_FILE', index);
					} else {
						console.log(res.data);
					}
				}).catch(err => {
					console.log(err);
				});
			} else {
				alert('非法访问')
			}
		},
		getTeamFileList() {
			if (this.$store.state.userId) {
				this.$axios.get('/getTeamFileList', {
					params: {
						teamId: this.$store.state.teamId,
						userId: this.$store.state.userId,
					}
				}).then(res => {
					var fileList = res.data.teamFileList;
					if (fileList.length != this.$store.state.teamFileList.length) {
						this.$store.commit('setTeamFileList', fileList);
						this.$store.commit('addTeamFileListVar', {
							'filter': false,
							'showMenu': false,
							'optionChangeIcon': { "glyphicon-option-vertical": true },
							'downloadChangeIcon': { "glyphicon-save": true }
						});
						console.log(this.$store.state.teamFileList)
						console.log('获取列表成功')
					} else {
						console.log('列表已更新')
					}
				}).catch(err => {
					console.log(err);
				});
			} else {
				console.log('非法访问');
				alert('非法访问');
				axios.push('/index');
			}
		},
	},
	watch: {
		watchUpload(teamFileCounter) {
			let that = this;
			that.getTeamFileList();
		},
	},
	computed: {
		watchUpload() {
			return this.$store.state.teamFileCounter;
		},
		fileList() {
			return this.store.state.teamFileList;
		}
	},
	created() {
		let that = this;
		that.getTeamFileList();
	}
}
</script>

<style>

.teamFileContiner {
padding: 0;
	height: 440px;
	overflow: auto;
}

.menuField {
	padding: 0;
	padding-top: 20px;
}

.floatRight {
	float: right;
}

.fillHeight {
	height: 440px;
}

.filePic {
	padding: 25px 16px;
    font-size: 28px;
    line-height: 1.3333333;
}

.newMessage {
	background-color: #ddd;
	border: 1px solid #c2c2c2eb;
	overflow: auto;
	border-radius: 4px;
}

</style>
