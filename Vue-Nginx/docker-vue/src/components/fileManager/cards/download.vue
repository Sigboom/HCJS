<template>
	<div class="uploadCard col-md-12">
		<form class="loadForm col-sm-12">
			<input class="uploadMsg col-xs-12 col-sm-8"
			placeholder="tag 信息" v-model="commitMsg"
			v-show="fileList.length"></input>
			<a type="submit" role="button" class="btn btn-default col-xs-12 col-sm-4"
			@click="commitMsgFunc" v-show="fileList.length">提交</a>
			<input ref="file" id="myfile" type="file"
			multiple style="display: none"
			@change="upload($event)"></input>
			<input ref="file" id="myfiledir" type="file"
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
				<a class="btn btn-default col-xs-12" v-for="file in this.fileList">{{ file.name }}</a>
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
			fileID: [],
			commitMsg: '',
			outFileBtn: true,
			showDirBtn: false,
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
		upload(event) {
			event.preventDefault(); //阻止事件的默认行为
			var formData = new window.FormData();
			var files = event.target.files;
			
			console.log(files);
			for (var i = 0; i < files.length; i++) {
				this.fileList.push(files[i]);
				//可添加对文件类型的判断
				//对文件名进行判定
			/*
				console.log(files[i][0]);
				axios.get('/upload/checkFileName', {
					params: { 
						userID: this.$store.state.userID,
						fileName: files[i][0]
					}
				}).then(res => {
					if (res.data.status == "ok") {
						this.fileList[i]['upLoading'] = true;
					} else if (res.data.status == "repeat") {
						this.fileList[i]['repeat'] = true;
					}
				}).catch(err => {
					console.log(err);
				});
				*/
			}

			formData.append('userID', this.$store.state.userID);
			//console.log(this.fileList);
			for (var i = 0; i < this.fileList.length; i++) {
				formData.append('userfiles', this.fileList[i]);
			}
			//formData 控制台打印无效
			//console.log(formData);
			
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
					if (res.data.state == 'ok') {
						this.fileID = res.data.fileID;
						console.log("传输成功");
					} else {	
						console.log("ID传输失败");
					}
				}).catch(err => {
					console.log("传输有误");
				});
		},
		commitMsgFunc() {
			event.preventDefault(); //阻止事件的默认行为
			var fileData = new window.FormData();
			fileData.append('userID', this.$store.state.userID);
			fileData.append('commitMsg', this.commitMsg);
			for (var i = 0; i < this.fileID.length; i++) {
				fileData.append('fileID', this.fileID[i]);
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
			this.$refs.file.value='';//reset input file
			this.fileList = [];
			this.fileID = [];
			this.commitMsg = '';
		}
	}
	
}
</script>

<style>
/*
	CSS for Phone
*/
@media(max-width: 767px) {
	.uploadCard {
	}
}

/*
   CSS for PC
*/
@media(min-width: 768px) {
	.uploadCard {
		margin-top: 10px;
		border-radius: 8px;
		padding: 10px;
		background-color: #fff;
	}

}

.uploadMsg {
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

</style>


