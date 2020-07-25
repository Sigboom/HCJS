<template>
	<div class="fileList row">
		<p class="fileListTitle col-xs-12">最近文档</p>
		<div class="showBox col-xs-12">
		<p class="showPot col-sm-12" v-show="this.lastFileList.length == 0">{{ this.msg }}</p>
		<div class="fileShow col-sm-12" v-for="(file, i) in this.lastFileList" :key="file.id">
			<button class="fileNameShow col-xs-12" @click="askMenu(i)"> {{ file.name }}</button>
			<span class="fileMenu col-xs-12" v-show="showMenu[i].showMenu">
				<button class="fileDelete col-xs-6" @click="deleteFile(i, file.id)">删除</button>
				<button class="fileDownload col-xs-6" @click="getDownloadFile(file.id)"><span class="glyphicon glyphicon-save" aria-hidden="true"></span>下载</button>
			</span>
		</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'fileList',
	data() {
		return {
			msg: "文件列表空空如也",
			lastFileList: [],
			showMenu:[],
		}
	},
	methods: {
		initShow() {
			this.showMenu = []
			for(let i = 0; i < this.lastFileList.length; ++i) {
				this.showMenu.push({'showMenu': false})
			}
			console.log(this.showMenu)
		},
		getDownloadFile(id) {
			let a = document.createElement('a')
			let userId = this.$store.state.userId;
			a.href = "/getDownloadFile?userId=" + userId + "&&fileId=" + id;
			a.click();
		},
		askMenu(i) {
			var showAction = !this.showMenu[i].showMenu;
			this.showMenu.splice(i, 1, {'showMenu': showAction})
		},
		getLastFileList() {
			console.log("getFileList:", this.$store.state.fileList);
			if (this.$store.state.userId) {
				this.$axios.get('/getFileList', {
					params: { 
						userId: this.$store.state.userId,
						dirId: -1, 
					}
				}).then(res => {
					var fileList = res.data.fileList;
					this.$store.commit('SET_FILELIST', fileList);	
					function compare(val1,val2){
						return val1-val2;
					};
					this.lastFileList = fileList.sort(compare).slice(0, 7);
					this.initShow();
					console.log("获取列表成功");
				}).catch(err => {
					console.log(err);
				});
			} else {
				console.log('非法访问');
				alert('非法访问');
				this.$axios.push('/index');
			}
		},
		deleteFile(index, id) {
			//console.log(id);
			if (this.$store.state.userId) {
				var	params = {
					userId: this.$store.state.userId,
					fileId: id,
				}
				this.$axios.get('/deleteFile', { params: params 
				}).then(res => {
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
		}
	},
	watch: {
		watchUpload(fileCounter) {
			let that = this;
			that.getLastFileList();
		}
	},
	computed: {
		watchUpload() {
			return this.$store.state.fileCounter;
		}
	},
	created() {
		let that = this;
		that.getLastFileList();
	}
}
</script>

<style>

.fileList {
	margin: 10px 0;
	padding: 10px;
	background-color: #fff;
	border: 1px solid #e6e6e6;
	border-radius: 10px;
}

/*
	CSS for Phone
*/
@media(max-width: 767px) {
	.fileList {
	}
}

/*
   CSS for PC
*/
@media(min-width: 768px) {
	.fileList {
		min-width: 200px;
	}
}

.fileList>.showBox {
	padding: 0px;
	height: 180px;
	overflow: auto;
}

.fileShow {
	width: 100%;
	padding:0;
}

.fileNameShow {
	display: inline-block;
}

.fileList .fileMenu {
padding: 0;
	text-align: center;
}

.fileDelete {
	margin: 0 auto;
	width: 45%;
}

.fileDownload {	
	margin: 0 auto;
}

</style>
