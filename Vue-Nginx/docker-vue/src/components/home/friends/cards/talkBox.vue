<template>
	<div class="talkBox col-md-12">
		<div class="showBox col-md-12">
			<div class="showBoxHead">
				<p class="headMsg">{{ this.$store.state.talkToName }}</p>
			</div>
			<div class="messagePot col-md-12" v-for="msg in sortMessageList">
				<span class="msgSelfPot col-md-6" v-if="msg.self">
					<span class="headPicPosition col-md-3">
						<span class="portrait col-md-12">
							<img class="headPic col-md-12" src="../../../../assets/default-head.jpg"  alt="用户头像" />
						</span>
					</span>
					<span class="msgPosition col-md-9">
						<span class="msgSubpot">{{ msg.message }}</span>
					</span>
				</span>
				<span class="msgPot col-md-6" v-else>
					<span class="headPicPosition col-md-3">
						<span class="portrait col-md-12">
							<img class="headPic col-md-12" src="../../../../assets/default-head.jpg"  alt="用户头像" />
						</span>
					</span>
					<span class="msgPosition col-md-9">
						<span class="msgSubpot">{{ msg.message }}</span>
					</span>
				</span>
			</div>
		</div>
		<div class="editBox col-md-12">
			<div class="auxiliaryBox col-md-12">
				<p>这是辅助栏</p>
			</div>	
			<form class="messageBox col-md-12">
				<textarea class="sendMsgBox col-md-12" spellcheck="false" v-model="message"></textarea>
				<a role="button" @click="sendMsg" class="submitBtn btn btn-default">发送</a>
			</form>
		</div>
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: "talkBox",
	data() {
		return {
			message: "",
			messageList: [],
		}
	},
	methods: {
		sendMsg() {
			let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
			var csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
			var config = {
			headers: {
				'X-Requested-With':'XMLHttpRequest',
				'Content-Type': 'application/x-www-form-urlencoded',
				'X-CSRFToken': csrfToken
			}
		}; 
			var msgData = {
				'userFromId': this.$store.state.userId,
				'userToId': this.$store.state.talkTo,
				'message': this.message,
			}

			this.messageList.push({
				'sender': this.$store.state.userName,
				'self': true,
				'message': this.message,
				'time': '9999-99-99T99:99:99'
			});	
			this.$axios.post('/sendMsg', qs.stringify(msgData), config).then(res => {
				if (res.data.state == "OK") {
					console.log("send OK");
				} else {
					console.log("send error");
				}
			}).catch(err => {
				console.log(err);
			});
			this.message = "";
		},
		getMsgHistory() {	
			if (this.$store.state.userId) {
				let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
				var csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
				var config = {
					headers: {
						'X-Requested-With':'XMLHttpRequest',
						'Content-Type': 'application/x-www-form-urlencoded',
						'X-CSRFToken': csrfToken
					}
				}; 
				var msgData = {
					'userFromId': this.$store.state.userId,
					'userToId': this.$store.state.talkTo,
				}

				this.$axios.post('/getMsgHistory', qs.stringify(msgData), config).then(res => {
					if (res.data.state == "OK") {
						this.messageList = []
						var msgList = res.data.msgList;
						for (let i = 0; i < msgList.length; ++i) {
							if (msgList[i].sender == this.$store.state.userName) {
								this.messageList.push({
									...msgList[i],
									self: true,
								});	
							} else {	
								this.messageList.push({
									...msgList[i],
									self: false,
								});	
							}
						}
						console.log(this.messageList)
						console.log('聊天记录更新');
					} else {
						console.log('更新完成');	
					}
				}).catch(err => {
					console.log(err);
				});
			}
		}
	},	
	watch: {
		watchMsgHistory(talkTo) {
			let that = this;
			that.getMsgHistory();
		}
	},
	computed: {
		watchMsgHistory() {
			return this.$store.state.talkTo;
		},
		sortMessageList: function() {
			return this.messageList.sort(function(a, b) {
				for(let i = 0; i < a.time.length && i < b.time.length; ++i) {
					if (a.time[i] == b.time[i]) continue;
					return a.time[i] - b.time[i];
				}
			});
		}
	},
	created() {
		let that = this;
		that.getMsgHistory();
	}
}

</script>

<style>

.talkBox {
	height: 572px;
	background-color: #dcdce7bf;
	padding: 0;
}

.showBox {
	height: 70%;
	border: 0px solid gray;
	overflow: auto;
}

.showBoxHead .headMsg{
	color: #fff;
	font-size: 24px;
	line-height: 50px;
	margin-bottom: 0;
	border-bottom: 1px solid #eee;
}

.editBox {
	height: 30%;
	padding-right: 20px;
}

.auxiliaryBox {
	padding: 0;
	height: 20%;	
	border-top: 1px solid gray;
}

.messageBox {
	padding: 0;
	height: 50%; 
}

.sendMsgBox {
	padding: 2px;
	height: 100%;
	font-size: 18px;
	border-width: 0;
	background-color: transparent;
}

.messagePot {
	line-height: 30px;
}

.msgPot {
}

.msgSubpot {
	max-width: 60%;
	word-break: break-all;
	padding: 3px 10px;
	border-radius: 8px;
	background-color: #fff;
	color: black;
	font-size: 20px;
}

.msgPosition {
	padding: 30px 0 0;
}
.headPicPosition {
	padding: 10px 10px 0;
}

.msgSelfPot,
.msgSelfPot .headPicPosition, .msgSelfPot .msgSubpot {
	float: right;
}

.headPicPosition>.portrait {
	border: 2px solid #e6e6e6;
	border-radius: 50%;
	padding: 0;
	overflow: hidden;
	height: 58px;
}

.submitBtn {
	float: right;
}

textarea {
	outline:none;	
	resize:none;

}

</style>
