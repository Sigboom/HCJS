<template>
	<div class="signUp col-md-5">
		<form class="sign-register col-md-12 row" methods="POST">
			<p class="register-head col-md-8">注册Sig账号</p>
			<router-link class="signBack col-md-4" to="/index">已有账号</router-link>
			<div class="form-body row col-xs-12">
				<p class="userNameWarning" v-if="this.userNameCheckList.iEmpty">用户名不能为空</p>
				<p class="userNameWarning" v-else-if="this.userNameCheckList.iIllegal">只能包含英文字母、数字及下划线</p>
				<p class="userNameWarning" v-else-if="this.userNameCheckList.iLength">长度不超过20</p>
				<p class="userNameWarning" v-else-if="this.userNameCheckList.iUnique">该用户名已注册</p>
				<p class="userNameSuccess" v-else-if="this.userNameCheckList.iSuccess">该用户名可用</p>
				<p class="blank" v-else>&nbsp;</p>
				<input type="text" class="col-xs-12" :class="userNameCheckList"
				v-model='signUpData.userName' placeholder="新用户名" autocomplete="off"
				@blur.prevent="userNameCheck" @input="userNameIllegalCheck"></input>

				<p class="userEmailWarning" v-if="this.userEmailCheckList.iEmpty">邮箱不能为空</p>
				<p class="userEmailWarning" v-else-if="this.userEmailCheckList.iIllegal">邮箱格式不正确</p>
				<p class="userEmailWarning" v-else-if="this.userEmailCheckList.iUnique">该邮箱已注册</p>
				<p class="userEmailSuccess" v-else-if="this.userEmailCheckList.iSuccess">该邮箱可用</p>
				<p class="blank" v-else>&nbsp;</p>
				<input type="text" class="col-xs-12" :class="userEmailCheckList"
				v-model="signUpData.userEmail" placeholder="你的邮箱" autocomplete="off"
				@blur.prevent="userEmailCheck" @input="userEmailEmptyCheck"></input>

				<p class="newPasswdWarning" v-if="this.newPasswdCheckList.iLength">密码长度应在6-20位</p>
				<p class="newPasswdSuccess" v-else-if="this.newPasswdCheckList.iSuccess">密码长度应在6-20位</p>
				<p class="blank" v-else>密码长度应在6-20位</p>
				<input type="password" class="col-xs-12" :class="newPasswdCheckList"
				v-model="signUpData.newPasswd" placeholder="新密码" autocomplete="off"
				@blur.prevent="newPasswdCheck" @input="newPasswdIllegalCheck"></input>

				<p class="verificationSuccess" v-if="this.verificationCheckList.iSuccess">验证成功</p>
				<p class="verificationWarning" v-else-if="this.verificationCheckList.iError">验证失败</p>
				<p class="blank" v-else>&nbsp;</p>
				<div v-if="checkShow">
					<input type="text" class="col-xs-6" :class="verificationCheckList"
					v-model="verificationCode" placeholder="验证码" autocomplete="off"
					@blur.prevent="verificationCheck"></input>
					<div class="verificationButton col-xs-6" v-if="checkTime">已发送&nbsp;({{ this.checkTime }})</div>
					<button class="reCheckButton col-xs-6" v-else @click="reCheck($event)">重新发送</button>
				</div>
				<button class="form-button col-xs-12" @click="submitForm($event)">
					注&nbsp;册&nbsp;并&nbsp;登&nbsp;录
				</button>
			</div>
			<div class="form-footer">
			</div>
		</form>
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: 'Sign_up',
	data() {
		return {
			signUpData: {
				userName: "",
				userEmail: "",
				newPasswd: ""
			},
			checkShow: false,
			checkTime: null,
			timeCounter: null,
			verificationCode: "",
			userNameCheckList: {
				iBase: true,
				iEmpty: false,
				iError: false,
				iLength: false,
				iUnique: false,
				iIllegal: false,
				iSuccess: false
			},
			userEmailCheckList: {
				iBase: true,
				iEmpty: false,
				iError: false,
				iUnique: false,
				iIllegal: false,
				iSuccess: false
			},
			newPasswdCheckList: {
				iBase: true,
				iError: false,
				iLength: false,
				iSuccess: false
			},
			verificationCheckList: {
				iBase: true,
				iError: false,
				iSuccess: false
			}
		}
	},
	methods: {
		reCheck(event) {
			event.preventDefault(); //阻止事件的默认行为
			this.countDown();
			axios.get('/signUp/reCheckUserEmail', {
				params: { userEmail: this.signUpData.userEmail }
			}).then(res => {
				switch (res.data.status) {
					case "OK!":
						break;
					case "Wrong!":
						break;
					case "EmptyWrong":	
						break;
					default:
						break;
				}
			}).catch(err => {
				console.log(err);
				return false;
			});
		},
		secondString (s) {
			this.checkTime = s >= 10 ? s : '0' + s;
		},
		countDown() {
			var time = 30;
			const self = this;
			self.secondString(time);
			self.timeCounter = setTimeout(countDownStart, 1000);
			
			function countDownStart() {
				if (self.timeCounter == null) return false;
				time--;
				self.secondString(time);
				if (time <= 0) {
					clearTimeout(self.timeCounter);
					self.checkTime = null;
				} else {
					self.timeCounter = setTimeout(countDownStart, 1000);
				}
			}
		},
		userNameCheck() {
			return this.userNameUniqueCheck();
		},
		userNameUniqueCheck() {
			if(!this.userNameIllegalCheck()) return false;
			this.$axios.get('/signUp/checkUserName', {
				params: { userName: this.signUpData.userName }
			}).then(res => {
				switch (res.data.status) {
					case "OK!":
						this.userNameCheckList.iUnique = false;
						this.userNameCheckList.iSuccess = true;
						break;
					case "Wrong!":
						this.userNameCheckList.iSuccess = false;
						this.userNameCheckList.iUnique = true;
						break;
					case "EmptyWrong":	
						break;
					default:
						break;
				}
			}).catch(err => {
				console.log(err);
				return false;
			});
			return true;
		},
		userNameIllegalCheck() {
			if (!this.userNameEmptyCheck()) return false;
			var userName = this.signUpData.userName;
			var regex=/^[A-Za-z0-9_\u4e00-\u9fa5]+$/g;
			if (!regex.test(userName)) {
				this.userNameCheckList.iSuccess = false;
				this.userNameCheckList.iUnique = false;
				this.userNameCheckList.iIllegal = true;
				return false;
			} else {
				this.userNameCheckList.iIllegal = false;
			}
			var regex_length=/^[A-Za-z0-9_\u4e00-\u9fa5]{1,20}$/g;
			if (!regex_length.test(userName)) {
				this.userNameCheckList.iSuccess = false;
				this.userNameCheckList.iLength = true;
				return false;
			} else {
				this.userNameCheckList.iLength = false;
			}
			return true;
		},
		userNameEmptyCheck() {
			var userName = this.signUpData.userName;
			if (userName == "") {
				this.userNameCheckList.iSuccess = false;
				this.userNameCheckList.iUnique = false;
				this.userNameCheckList.iEmpty = true;
				return false;
			} else {
				this.userNameCheckList.iEmpty = false;
			}
			return true;
		},
		
		userEmailCheck() {
			return this.userEmailUniqueCheck();
		},
		userEmailUniqueCheck() {
			if(!this.userEmailIllegalCheck()) return false;
			axios.get('/signUp/checkUserEmail', {
				params: { userEmail: this.signUpData.userEmail }
			}).then(res => {
				switch (res.data.status) {
					case "OK!":
						this.checkShow = true;
						this.countDown();
						this.userEmailCheckList.iUnique = false;
						this.userEmailCheckList.iSuccess = true;
						break;
					case "Wrong!":
						this.userEmailCheckList.iSuccess = false;
						this.userEmailCheckList.iUnique = true;
						break;
					case "EmptyWrong":	
						break;
					default:
						break;
				}
			}).catch(err => {
				console.log(err);
				return false;
			});
			return true;
		},
		userEmailIllegalCheck() {
			if (!this.userEmailEmptyCheck()) return false;
			var userEmail = this.signUpData.userEmail;
			var regex=/^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
			if (!regex.test(userEmail)) {
				this.userEmailCheckList.iSuccess = false;
				this.userEmailCheckList.iUnique = false;
				this.userEmailCheckList.iIllegal = true;
				return false;
			} else {
				this.userEmailCheckList.iIllegal = false;
			}
			return true;
		},
		userEmailEmptyCheck() {
			this.checkShow = false;
			var userEmail = this.signUpData.userEmail;
			if (userEmail == "") {
				this.userEmailCheckList.iSuccess = false;
				this.userEmailCheckList.iUnique = false;
				this.userEmailCheckList.iEmpty = true;
				return false;
			} else {
				this.userEmailCheckList.iEmpty = false;
			}
			return true;
		},
		
		newPasswdCheck() {
			return this.newPasswdIllegalCheck();
		},
		newPasswdIllegalCheck() {
			this.newPasswdCheckList.iSuccess = false;
			var newPasswd = this.signUpData.newPasswd;
			var regex=/[\S]{6,20}/g;
			if (!regex.test(newPasswd)) {
				this.newPasswdCheckList.iLength = true;
				return false;
			} else {
				this.newPasswdCheckList.iLength = false;
				this.newPasswdCheckList.iSuccess = true;
			}
			return true;
		},

		verificationCheck() {
			if(!this.verificationIllegalCheck()) return false;
			axios.get('/signUp/checkVerificationCode', {
				params: { 
					userEmail: this.signUpData.userEmail,
					verification: this.verificationCode
				}
			}).then(res => {
				switch (res.data.status) {
					case "OK!":
						this.verificationCheckList.iError = false;
						this.verificationCheckList.iSuccess = true;
						break;
					case "Wrong!":
					case "EmptyWrong":	
						this.verificationCheckList.iSuccess = false;
						this.verificationCheckList.iError = true;
						break;
					default:
						break;
				}
			}).catch(err => {
				console.log(err);
				return false;
			});
			return true;
		},
		verificationIllegalCheck() {	
			var verification = this.verificationCode;
			let regex=/^\d{6}$/;
			if (!regex.test(verification)) {
				this.verificationCheckList.iSuccess = false;
				this.verificationCheckList.iError = true;
				return false;
			}
			return true;
		},

		checkFalse() {
			return !this.newPasswdCheck()
				|| !this.verificationCheck()
				|| !this.userNameCheck()
				|| !this.userEmailCheck()
		},
		submitForm(event) {
			event.preventDefault(); //阻止事件的默认行为
			if (this.checkFalse()) return false;
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
				...this.signUpData,
				'verificationCode': this.verificationCode
			}
			
			//console.log(formData)
			axios.post('/signUp', qs.stringify(formData), config).then(res => {
				axios.get('/getCsrftoken');
				this.$router.push({ 
					name: 'signIng', 
					params: {
						userName: this.signUpData.userName,
						userEmail: this.signUpData.userEmail,
						password: this.signUpData.newPasswd,
					}
				});
			}).catch(err => {
				this.error = true;
			}); 
		}
	}
}
</script>

<style>

.signUp {
	height: 360px;
	background-color:#ffffff;
	padding:30px 25px;
	border-radius: 10px;
}

.register-head {
	font-weight: 600;
	font-size: 18px;
	margin: 0;
}

.signBack {
	padding: 0;
	line-height: 24px;
	text-align: right;
}

.iBase {
	height: 35px;
	border-radius: 15px;
	border-width: 2px;
	border-color: #bbbbbb;
}

.iEmpty, .iError, .iIllegal, .iLength, .iUnique {
	border-color: red;
}

.iSuccess {
	border-color: green;
}

.form-body {
	margin-left: 8%;
	padding: 0;
}

.userNameWarning, .userEmailWarning, .newPasswdWarning, .verificationWarning,
.userNameSuccess, .userEmailSuccess, .newPasswdSuccess, .verificationSuccess,
.blank {
	margin: 4px;
	font-size: 12px;
}

.userNameWarning, .userEmailWarning, .newPasswdWarning, .verificationWarning {
	color: red;
}

.userNameSuccess, .userEmailSuccess, .newPasswdSuccess, .verificationSuccess {
	color: green;
}

.reCheckButton {
	height: 35px;
	font-size: 14px;
    background-color: #4fc08d;
	line-height: 35px;
	border-radius: 2em;
    color: #fff;
}

.verificationButton {
	height: 35px;
	font-size: 14px;
    background-color: #4fc08d;
	line-height: 35px;
	border-radius: 2em;
    color: #fff;
}

.form-button {
	margin: 5% 0;	
    height:40px;
    border-radius: 2em;
    color: #fff;
    background-color: #4fc08d;
    line-height: 40px;
    font-size: 16px;
	text-align: center;
    text-decoration: none;
}

</style>
