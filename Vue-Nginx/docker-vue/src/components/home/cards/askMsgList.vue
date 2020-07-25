<template>
	<div class="askMsgList row">
		<p class="askMsgTitle">个人消息</p>
		<p class="showPot col-sm-12" v-show="askMsgList.length ==  0">{{ this.msg }}</p>
		<div class="fileShow col-sm-12" v-for="(message, index) in askMsgList">
			<a role="button" @click="askMenu(index)" class="btn btn-default fileNameShow col-md-12">
				{{ message.sender}}{{ message.message }}
			</a>
			<div class="fileMenu col-md-12" v-show="menu[index].show">
				<span v-if="message.category == 'reply'">
					<span class="col-md-6"></span>
					<a role="button" class="btn btn-primary col-md-6" @click="replyAsk(index, message)">知道了</a>
				</span>
				<span v-else>
					<a role="button" class="btn btn-default col-md-6" @click="refuseAsk(index, message)">拒绝</a>
					<a role="button" class="btn btn-primary col-md-6" @click="agreeAsk(index, message)">同意</a>
				</span>
			</div>
		</div>
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: 'askMsgList',
	data() {
		return {
			msg: "暂时没有新消息",
			askMsgList: [{
				message: "发来3条信息",
				sender: "李红",
			}],
			menu:[{
				'show': false,
			}],
			csrfToken: "",
		}
	},
	methods: {
		replyAsk(index, message) {
			console.log("agree");
			let formData = { 
				'userId': this.$store.state.userId,
				'msgId': message.id,
				'state': 'reply',
			}
			
			this.$axios.post('/getAnsMsgList', qs.stringify(formData), {
				headers: {
					'X-Requested-With':'XMLHttpRequest',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-CSRFToken': this.csrfToken 
				}
			}).then(res => {
				if (res.data.status == "OK") {
					this.askMsgList.splice(index, 1);
					console.log("处理消息列表成功");
				} else {
					console.log("处理消息列表失败");
				}
			}).catch(err => {
				console.log(err);
			}); 
		},
		agreeAsk(index, message) {
			console.log("agree");
			let formData = { 
				'userId': this.$store.state.userId,
				'msgId': message.id,
				'state': 'agree',
			}
			
			this.$axios.post('/getAnsMsgList', qs.stringify(formData), {
				headers: {
					'X-Requested-With':'XMLHttpRequest',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-CSRFToken': this.csrfToken 
				}
			}).then(res => {
				if (res.data.status == "OK") {
					this.askMsgList.splice(index, 1);
					console.log("处理消息列表成功");
				} else {
					console.log("处理消息列表失败");
				}
			}).catch(err => {
				console.log(err);
			}); 
		},
		refuseAsk(index, message) {
			console.log("refuse");
			let formData = { 
				'userId': this.$store.state.userId,
				'msgId': message.id,
				'state': 'refuse',
			}
			
			this.$axios.post('/getAnsMsgList', qs.stringify(formData), {
				headers: {
					'X-Requested-With':'XMLHttpRequest',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-CSRFToken': this.csrfToken 
				}
			}).then(res => {
				if (res.data.status == "OK") {
					this.askMsgList.splice(index, 1);
					console.log("处理消息列表成功");
				} else {
					console.log("处理消息列表失败");
				}
			}).catch(err => {
				console.log(err);
			}); 
		},
		askMenu(index) {
			var show = !this.menu[index].show;
			this.menu.splice(index, 1, {
				'show': show,
			});
		},
		initMenu() {
			for(let i = 0; i < this.askMsgList.length; ++i) {
				this.menu.push({ 'show': false });
			}
		},
		getAskMsgList() {
			if (this.$store.state.userId) {
				let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
				this.csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
				let formData = { 'userId': this.$store.state.userId }
				
				this.$axios.post('/getAskMsgList', qs.stringify(formData), {
					headers: {
						'X-Requested-With':'XMLHttpRequest',
						'Content-Type': 'application/x-www-form-urlencoded',
						'X-CSRFToken': this.csrfToken 
					}
				}).then(res => {
					var msgList = res.data.askMsgList;
					this.askMsgList = msgList;
					this.initMenu();
					console.log("获取消息列表成功");
				}).catch(err => {
					console.log(err);
				}); 
			} else {
				console.log('非法访问');
				alert('非法访问');
				this.$axios.push('/index');
			}
		},
	},
	created() {
		/*
		let that = this;
		that.getAskMsgList();
		*/
	}
}
</script>

<style>

.askMsgList {
	margin: 10px 0;
	padding: 10px;
	background-color: #fff;
	border: 1px solid #e6e6e6;
	border-radius: 10px;
}

.askMsgTitle {
	padding-left: 10px;
	font-size: 14px;
}

/*
	CSS for Phone
*/
@media(max-width: 767px) {
	.askMsgList {
	}
}

/*
   CSS for PC
*/
@media(min-width: 768px) {
	.askMsgList {
		min-height: 360px;
	}
}

.fileShow {
	width: 100%;
}

.fileNameShow {
	display: inline-block;
}

.fileMenu {
	text-align: center;
}

.fileDelete {
	margin: 0 auto;
}

.fileDownload {	
	margin: 0 auto;
}

</style>
