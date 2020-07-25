<template>
	<div class="cloudFiles row">
		<div class="fileContiner col-sm-8 col-md-8 col-xs-12">
			<p class="showPot col-md-12" v-show="this.$store.state.fileCounter + this.$store.state.dirCounter == 0">
				<span v-show="this.$store.state.nowDir">
					{{ this.emptyDir }}
				</span>
				<span v-show="!this.$store.state.nowDir">
					{{ this.emptyMsg }}
				</span>
			</p>
			<div class="thumbnail col-md-12" v-show="!file.filter"
			@mouseenter="askMenu(id)" @mouseleave="noAskMenu(id)"
			v-for="(file, id) in this.$store.state.fileList" :key="file.id">
				<div class="filePic col-md-1">
					<span class="glyphicon" :class="file.icon" aria-hidden="true"></span>
				</div>
				<div class="caption col-md-5">
					<h4 v-show="!file.setRename">{{ file.name }}</h4>
					<span v-show="file.setRename">
						<input class="renameInput col-md-9"
						:placeholder="file.name" v-model="renameBuffer"></input>
						<a role="button" class="btn btn-primary col-md-3" @click="rename(id)">保存</a>
					</span>
					<p class="col-md-12">{{ file.commitMsg }}</p>
				</div>
				<div class="menuField col-md-6">
					<span class="floatRight col-md-6" v-show="file.showMenu || file.star">
						<a class="floatRight btn btn-default" role="button" @click="starChange(id, file.id)" v-if="file.type != 100">
							<span class="glyphicon" :class="file.starChangeIcon" aria-hidden="true"></span>Star
						</a>	
						<a class="floatRight btn btn-default" role="button" @click="dirChange(id, file.id)" v-else>
							<span class="glyphicon glyphicon-folder-open" aria-hidden="true"></span>&nbsp;打开
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
							<li><a role="button" @click="setRename(id)" >重命名</a></li>
							<li><a href="#">Another action</a></li>
							<li><a href="#">Something else here</a></li>
							<li role="separator" class="divider"></li>
							<li><a role="button" data-toggle="modal" data-target="#moveModal"
								@click="getDirList(0)">移动到</a></li>
							<li role="separator" class="divider"></li>
							<li><a @click="deleteFile(id, file.id)">
								<span class="glyphicon glyphicon-trash" aria-hidden="true">&nbsp;删除</span>
							</a></li>
						</ul>
					</span>
				</div>
				<div class="modal fade col-md-12" id="moveModal" tabindex="-1" role="dialog"
				aria-labelledby="moveModalLabel" aria-hidden="true">
					<div class="modal-dialog col-md-12">
						<div class="col-md-4"></div>
						<div class="modal-content col-md-4">
							<div class="modal-header">
								<button type="button" class="close" data-dismiss="modal" aria-hidden="true">
									&times;
								</button>
								<h4 class="modal-title" id="moveModalLabel">移动到</h4>
							</div>
							<div class="modal-body col-md-12">
								<ul class="dirList" v-if="dirList.length != 0">
									<li v-for="(dir, index) in dirList">
										<button class="col-md-9" :class="dirStat[index]"
										@click="chooseDir(dir.id, index)" @dblclick="getDirList(dir.id)" >
											{{ dir.name }}
										</button>
									</li>
								</ul>
								<span v-else>没有文件夹</span>
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-default" @click="mkdir()">
									新建文件夹
								</button>
								<button type="button" class="btn btn-primary" data-dismiss="modal"
								@click="moveToDir(file.id)">
									确定
								</button>
								<button type="button" class="btn btn-default" data-dismiss="modal">
									关闭
								</button>
							</div>
						</div>
						<div class="col-md-4"></div>
					</div>
				</div>
			</div>
		</div>
		<div class="col-sm-4 col-md-4 col-xs-0">
			<div class="newMessage fillHeight">
				<span>当前文件夹共有:</span><br/>
				<span>{{ this.$store.state.dirCounter }}个文件夹</span><br/>
				<span>{{ this.$store.state.fileCounter }}个文件</span><br/>
			</div>
		</div>
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: 'cloudFilesCard',
	data() {
		return {
			renameBuffer: "",
			emptyMsg: "您没有上传任何文件",
			emptyDir: "文件夹为空",
			dirList: [],
			dirstat: [],
			chooseDirId: 0,
			chooseDirIndex: -1,
			nowDirId: 0,
			
		}
	},
	methods: {
		moveToDir(fileId) {	
			let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
			var csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
			let config = {
				headers: {
					'X-Requested-With':'XMLHttpRequest',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-CSRFToken': csrfToken 
				}
			};  
			let formData = {
				'userId': this.$store.state.userId,
				'fileId': fileId,
				'dirId': this.chooseDirId,
			}
			
			//console.log(formData)
			this.$axios.post('/askMoveToDir', qs.stringify(formData), config)
			.then(res => {
				this.getFileList();
			}).catch(err => {
				console.log(err);
			}); 
		},
		mkdir() {
			var	params = {
				userId: this.$store.state.userId,
				dirId: this.nowDirId,
			};
			axios.get('/getMkdir', { params: params }).then(res => {
				if (res.data.status == 'OK') {
					this.getDirList(this.nowDirId);
					console.log('创建成功')
				} else {
					console.log(res.data);
				}
			}).catch(err => {
				console.log(err);
			});
		},
		chooseDir(dirId, index) {
			this.chooseDirId = dirId;
			if (this.chooseDirIndex != -1) {
				this.dirStat[this.chooseDirIndex].active = false;
			}
			this.chooseDirIndex = index;
			this.dirStat[index].active = true;
		},
		dirChange(i, fileId) {
			this.$store.commit('CHANGE_DIR', i);
			this.getFileList();
		},
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
			let stat = !this.$store.state.fileList[i].star;
		
			var	params = {
				userId: this.$store.state.userID,
				fileID: id,
				star: stat,
			};
			axios.get('/getStar', { params: params }).then(res => {
				if (res.data == 'OK') {
					this.$store.state.fileList.splice(i, 1, {
							...this.$store.state.fileList[i],
							'star': stat,
							'starChangeIcon': {
								"glyphicon-star-empty": !stat,
								"glyphicon-star": stat,
							},
						});
					this.$store.commit('SET_STARFILE', stat);
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
					userId: this.$store.state.userID,
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
		setRename(index) {
			this.$store.commit('SET_RENAME', index);
		},
		rename(index) {
			let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
			var csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
			let config = {
				headers: {
					'X-Requested-With':'XMLHttpRequest',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-CSRFToken': csrfToken 
				}
			};  
		
			let formData = {
				'userId': this.$store.state.userId,
				'fileId': this.$store.state.fileList[index].id,
				'rename': this.renameBuffer
			}
			
			//console.log(formData)
			this.$axios.post('/askRename', qs.stringify(formData), config)
			.then(res => {
				this.$store.commit('RENAME', { 
					'index': index,
					'newName': this.renameBuffer
				});
				this.renameBuffer = "";
			}).catch(err => {
				console.log(err);
			}); 
		},
		getDirList(dirId) {
			if (this.$store.state.userId) {
				this.$axios.get('/getFileList', {
					params: { 
						userId: this.$store.state.userId,
						dirId: dirId,
					}
				}).then(res => {
					var fileList = res.data.fileList;
					var j = 0; 
					this.dirList = [];
					this.dirStat = [];
					this.nowDirId = dirId;
					for (let i = 0; i < fileList.length; ++i) {
						if (fileList[i].type == 100) {
							this.dirList.splice(j, 1, fileList[i]);
							this.dirStat.splice(j, 1, {'active': false});
							j++;
						}
					}
					console.log(this.dirList)
					console.log('获取文件夹列表成功')
				}).catch(err => {
					console.log(err);
				});
			} else {
				console.log('非法访问');
				alert('非法访问');
				axios.push('/index');
			}
		},
		getFileList() {
			if (this.$store.state.userId) {
				this.$axios.get('/getFileList', {
					params: { 
						userId: this.$store.state.userId,
						dirId: this.$store.state.nowDir.slice(-1)[0],
					}
				}).then(res => {
					var fileList = res.data.fileList;
					this.dirList = [];
					this.dirStat = [];
					this.$store.commit('SET_FILELIST', fileList);
					this.$store.commit('ADD_FILELISTVAR', {
						'filter': false,
						'showMenu': false,
						'rename': false,
						'optionChangeIcon': { "glyphicon-option-vertical": true },
						'downloadChangeIcon': { "glyphicon-save": true }
					});
					var j = 0; 
					for (let i = 0; i < fileList.length; ++i) {
						if (fileList[i].type == 100) {
							this.dirList.splice(j, 1, fileList[i]);
							this.dirStat.splice(j, 1, {'active': false});
							j++;
						}
					}
					console.log('获取列表成功')
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
		watchNowDir(nowDir) {
			let that = this;
			that.getFileList();
		},
	},
	computed: {
		watchNowDir() {
			return this.$store.state.nowDir;
		},
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
	.cloudFiles {
		min-height: 440px;
		padding-top: 10px; 
		padding-left: 10px;
	}
}

.cloudFiles {
}

.fileContiner {
	height: 440px;
	overflow: auto;
}

.menuField {
	padding: 20px;
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

.renameInput {
	font-size: 15px;
	padding: 0 10px;
	height: 35px;
}

.modal-dialog {
	width: 100%;
}

.dirList .active {
	border-color: red;
}

.thumbnail .caption>h4{
	max-width: 100%;
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}

</style>
