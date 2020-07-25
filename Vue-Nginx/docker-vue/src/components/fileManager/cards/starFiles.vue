<template>
	<div class="starFiles row">
		<div class="fileContiner col-sm-8 col-md-8 col-xs-12">
			<p class="showPot col-md-12" v-show="this.$store.state.fileList.length == 0">{{ this.msg }}</p>
			<div class="thumbnail col-md-12"
			@mouseenter="askMenu(id)" @mouseleave="noAskMenu(id)"
			v-for="(file, id) in this.$store.state.fileList" :key="file.id" v-show="file.star">
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
				<div class="col-sm-4 col-md-4 col-xs-0">
				<div class="newMessage fillHeight">
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'starFilesCard',
	data() {
		return {
			msg: "您没有星标文件",
		}
	},
	methods: {	
		askMenu(i) {
			this.$store.state.fileList.splice(i, 1, {
					...this.$store.state.fileList[i],
					'showMenu': true,
					'starChangeIcon': {
							"glyphicon-star-empty": !this.$store.state.fileList[i].star,
							"glyphicon-star": this.$store.state.fileList[i].star,
						},
					})
		},
		noAskMenu(i) {
			this.$store.state.fileList.splice(i, 1, {
					...this.$store.state.fileList[i],
					'showMenu': false,
					})
		},
		download(i, fileId) {
			let a = document.createElement('a')
			let userId = this.$store.state.userId;
			a.href = "/getDownloadFile?userId=" + userId + "&&fileId=" + fileId;
			a.click();
		},
		starChange(i, id) {
			let temp = !this.$store.state.fileList[i].star;
		
			var	params = {
				userId: this.$store.state.userId,
				fileId: id,
				star: temp,
			};
			axios.get('/getStar', { params: params }).then(res => {
				if (res.data == 'OK') {
					this.$store.state.fileList.splice(i, 1, {
							...this.$store.state.fileList[i],
							'star': temp,
							'starChangeIcon': {
								"glyphicon-star-empty": !temp,
								"glyphicon-star": temp,
							},
						});
					//console.log(this.$store.state.fileList[i]);
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
					fileId: id
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
		getFileList() {
			if (this.$store.state.userId) {
				this.$axios.get('/getFileList', {
					params: {
						userId: this.$store.state.userId
					}
				}).then(res => {
					var fileList = res.data.fileList;
					if (fileList.length != this.$store.state.fileList.length) {
						this.$store.commit('SET_FILELIST', fileList);
						this.$store.commit('ADD_FILELISTVAR', {
							'filter': false,
							'showMenu': false,
							'optionChangeIcon': { "glyphicon-option-vertical": true },
							'downloadChangeIcon': { "glyphicon-save": true }
						});
						console.log(this.$store.state.fileList)
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
		watchUpload(fileCounter) {
			let that = this;
			that.getFileList();
		},
	},
	computed: {
		watchUpload() {
			return this.$store.state.fileCounter;
		},
		fileList() {
			return this.store.state.fileList;
		}
	},
	created() {
		let that = this;
		that.getFileList();
	}
}
</script>

<style>

/* CSS for PC */
@media(min-width: 768px) {
	.starFiles {
		min-height: 440px;
		padding-top: 10px; 
		padding-left: 10px;
	}
}

.starFiles {
}

.starFiles .fileContiner {
	height: 440px;
	overflow: auto;
}

.menuField {
	padding: 20px;
}

.floatRight {
	float: right;
}

.starFiles .fillHeight {
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
