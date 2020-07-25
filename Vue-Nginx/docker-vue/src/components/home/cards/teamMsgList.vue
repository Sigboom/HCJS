<template>
	<div class="teamMsgList row">
		<p class="teamMsgTitle">团队消息</p>
		<p class="showPot col-sm-12" v-show="teamMsgList.length ==  0">{{ this.msg }}</p>
		<div class="teamBtn col-sm-12">
			<span class="teams" v-for="(teamItem, index) in teamList">
				<span><a role="button" class="btn btn-default" :class=teamBtnActive[index]>{{ teamItem.name }}</a></span>
			</span>
		</div>
		<div class="msgShow col-sm-12">
			<div class="teamMsgRoom col-sm-12" v-for="(message, index) in teamMsgList">
				<a role="button" @click="askMenu(index)" class="btn btn-default col-md-12">
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
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: 'teamMsgList',
	data() {
		return {
			msg: "暂时没有新消息",
			teamMsgList: [{
				'message': "请求加入内测团队",
				'sender': "李玲",
			}, {
				'message': "请求加入内测团队",
				'sender': "王勤明",
			}, {
				'message': "已退出内测团队",
				'sender': "曹操",
			}, {
				'message': "邀请曹操加入内测团队",
				'sender': "陈坤",
			}, {
				'message': "邀请刘备加入内测团队",
				'sender': "陈坤",
			}],
			teamList: [{
				'name': "内测团队",
			}, {
				'name': "正式团队"
			}],
			teamBtnActive: [{
				'active': true,
			}, {
				'active': false,
			}],
			menu:[{
				'show': false,
			},{
				'show': false,
			},{
				'show': false,
			},{
				'show': false,
			},{
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
		getTeamMsgList() {
			if (this.$store.state.userId) {
				let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
				this.csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
				let formData = { 
					'userId': this.$store.state.userId,
					'msgType': 'team',
				}
				
				this.$axios.post('/getTeamMsgList', qs.stringify(formData), {
					headers: {
						'X-Requested-With':'XMLHttpRequest',
						'Content-Type': 'application/x-www-form-urlencoded',
						'X-CSRFToken': this.csrfToken 
					}
				}).then(res => {
					this.msgList = res.data.msgList;
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

.teamMsgList {
	margin: 10px 0;
	padding: 10px;
	background-color: #fff;
	border: 1px solid #e6e6e6;
	border-radius: 10px;
}

.teamMsgTitle {
	padding-left: 10px;
	font-size: 14px;
}

/*
	CSS for Phone
*/
@media(max-width: 767px) {
	.teamMsgList {
	}
}

/*
   CSS for PC
*/
@media(min-width: 768px) {
	.teamMsgList {
		min-height: 200px;
	}

}

.teamMsgRoom {
	padding: 0px;
}

.msgShow {
	width: 100%;
	height: 150px;
	overflow: auto;
	padding: 0px;
	background-color: #e6e6e6;
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
