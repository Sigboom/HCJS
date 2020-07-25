<template>
	<div class="upLoadCard col-md-12">
		<form class="loadForm col-sm-12">
			<input class="upLoadMsg col-xs-12 col-sm-8"
			placeholder="tag 信息" v-model="commitMsg"
			v-show="fileList.length" :disabled="canCommit"></input>
			<a type="submit" role="button" class="btn btn-default col-xs-12 col-sm-4"
			@click="commitMsgFunc" v-show="fileList.length && !canCommit">提交</a>
			<a type="submit" role="button" class="btn btn-primary col-xs-12 col-sm-4"
			@click="backUpload" v-show="fileList.length && canCommit">返回</a>
			<input ref="file" id="myfile" type="file"
			multiple style="display: none"
			@change="upload($event)"></input>
			<input ref="files" id="myfiledir" type="file"
			multiple directory mozdirectory webkitdirectory
			style="display: none" @change="upload($event)"></input>
			<div class="loadBtns col-md-12" v-if="!this.fileList.length"
			@mouseleave="noshowDirChoice">
				<a class="btn btn-primary col-xs-12" role="button"
				@mouseover="showDirChoice"
				onclick="$('input[id=myfile]').click();">
					<i class="fa fa-folder-open">上传文件</i>
				</a>
				<a class="btn btn-primary col-xs-12" role="button"
				onclick="$('input[id=myfiledir]').click();" v-show="showDirBtn">
					<i class="fa fa-folder-open">上传文件夹</i>
				</a>
			</div>
			<div class="upLoadQueue" v-else>
				<a class="btn col-xs-12" v-for="(file, index) in this.fileList" :class="uploadState[index]" >
					{{ file.name }}<span class="nameError">&nbsp;文件名冲突</span>
				</a>
			</div>
		</form>
	</div>
</template>

<script>

export default {
	name: 'upload',
	data() {
		return {
			fileList: [],
			fileId: [],
			commitMsg: '',
			canCommit: true,
			outFileBtn: true,
			showDirBtn: false,
			uploadState: [],
		}
	},
	methods: {
		showDirChoice() {
			this.outFileBtn = false;
			this.showDirBtn = true;
		},
		noshowDirChoice() {
			this.showDirBtn = false;
		},
		backUpload() {
			this.fileList = [];
		},
		upload(event) {
			event.preventDefault(); //阻止事件的默认行为
			var formData = new window.FormData();
			var files = event.target.files;
			
			if (files.length == 0) return ;
			console.log(files);
			
			for (var i = 0; i < files.length; i++) {
				this.fileList.push(files[i]);
				this.uploadState.push({
					'btn-warning': true,
					'btn-success': false,
					'btn-danger': false,
				});
			}

			formData.append('userId', this.$store.state.userId);
			console.log(this.fileList);
			for (var i = 0; i < this.fileList.length; i++) {
				formData.append('userfiles', this.fileList[i]);
			}
			//formData 控制台打印无效
			
			let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
			var csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
			var config = {
				headers: {
					'Content-Type': 'multipart/form-data',
					'X-CSRFToken': csrfToken
				}
			};
			axios.post('/upload', formData, config)
			.then(res => {
				if (res.data.status == 'OK') {
					this.fileId = res.data.fileId;
					this.canCommit = false;
					for (let i = 0; i < this.fileId.length; ++i) {
						this.uploadState.splice(i, 1, {	
							'btn-warning': false,
							'btn-success': true,
							'btn-danger': false,
						});
					}
					console.log("传输成功");
				} else if (res.data.status == 'NameWrong') {	
					var fileExcept = res.data.fileExcept;
					for (let i = 0; i < fileExcept.length; ++i) {
						for (let j = 0; j < this.fileList.length; ++j) {
							if (this.fileList[j].name == fileExcept[i]) {
								var index = j;
								break;
							}
						}
						this.uploadState.splice(index, 1, {
							'btn-warning': false,
							'btn-success': false,
							'btn-danger': true,
						});
					}
					var j = 0;
					for (let i = 0; i < this.fileId.length; ++i, ++j) {
						this.canCommit = false;
						while (this.uploadState[j]['btn-danger']) ++j;
						this.uploadState.splice(i, 1, {
							'btn-warning': false,
							'btn-success': true,
							'btn-danger': false,
						});
					}
					console.log("ID传输失败");
				} else {
					console.log(res.data.status);
					console.log("传输有误");
				}
			}).catch(err => {
				console.log(err);
			});
			this.$refs.file.value='';//reset input file
			this.$refs.files.value='';//reset input file
		},
		commitMsgFunc() {
			event.preventDefault(); //阻止事件的默认行为
			var fileData = new window.FormData();
			fileData.append('userId', this.$store.state.userId);
			fileData.append('commitMsg', this.commitMsg);
			for (var i = 0; i < this.fileId.length; i++) {
				fileData.append('fileId', this.fileId[i]);
			}
			
			let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
			var csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
			var config = {
				headers: {
					'Content-Type': 'multipart/form-data',
					'X-CSRFToken': csrfToken
				}
			};
			
			axios.post('/commitFile', fileData, config
				).then(res => {
					if (res.data.state == 'ok') {
						this.$store.commit('SET_COUNTER', this.$store.state.fileCounter + res.data.change);
						console.log("提交成功");
					}
					console.log(res.data);
				}).catch(err => {
					console.log("提交有误");
					console.log(err);
				});
			this.fileList = [];
			this.fileId = [];
			this.commitMsg = '';
		},
		getUploadList() {
			console.log("uploadList:", this.$store.state.uploadList);
			if (this.$store.state.userId) {
				this.$axios.get('/getUploadList', {
					params: { 
						userId: this.$store.state.userId,
					}
				}).then(res => {
					var fileList = res.data.fileList;
					this.$store.commit('SET_FILELIST', fileList);
					this.$store.commit('ADD_FILELISTVAR', {'showMenu': false});
					console.log('列表已更新');
				}).catch(err => {
					console.log(err);
				});
			} else {
				console.log('非法访问');
				alert('非法访问');
				this.$axios.push('/index');
			}
		}
	},
	created() {
		/*
		let that = this;
		that.getUploadList();
		*/
	}
}
</script>

<style>
/*
	CSS for Phone
*/
@media(max-width: 767px) {
	.upLoadCard {
	}
}

/*
   CSS for PC
*/
@media(min-width: 768px) {
	.upLoadCard {
		max-height: 300px;
		overflow: auto;
		margin-top: 10px;
		border-radius: 8px;
		padding: 10px;
		background-color: #fff;
	}

}

.upLoadMsg {
	height: 34px;
	border: 1px solid #cecece;
	font-size: 14px;
	border-radius: 4px;
}

.loadForm {
	padding: 0;
}

.drag-area {
      height: 200px;
      width: 300px;
      border: dashed 1px gray;
      margin-bottom: 10px;
      color: #777;
    }

.upLoadInput {
	display: none;
}

.loadBtns {
	padding: 0;
}

.btn-danger>.nameError {
	display:inline-block;
}

.nameError {
	display: none;
}

</style>
