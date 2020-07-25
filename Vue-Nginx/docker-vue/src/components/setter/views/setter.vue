<template>
	<div id="setterView" class="col-md-12">
		<h3 class="col-md-12">账号设置</h3>
		<hr class="col-md-12"/>
		<div class="setterblock col-md-6">
			<h4>修改用户名</h4>
			<p class="userNameWarning" v-if="this.userNameCheckList.iEmpty">用户名不能为空</p>
			<p class="userNameWarning" v-else-if="this.userNameCheckList.iIllegal">只能包含英文字母、数字及下划线</p>
			<p class="userNameWarning" v-else-if="this.userNameCheckList.iLength">长度不超过20</p>
			<p class="userNameWarning" v-else-if="this.userNameCheckList.iUnique">该用户名已注册</p>
			<p class="userNameSuccess" v-else-if="this.userNameCheckList.iSuccess">该用户名可用</p>
			<p class="blank" v-else>&nbsp;</p>
			<input type="text" id="userRename" class="col-md-6" :class="userNameCheckList"
			@blur.prevent="userNameCheck" @input="userNameIllegalCheck" v-model="signUpData.userName"></input>
			<a class="btn col-md-2" :class="userRenameBtn" role="button" @click="changeSave('userName')">{{ userRenameBtnInfo }}</a>
		</div>
		<div class="setterblock col-md-6">
			<h4>修改邮箱</h4>
				<p class="userEmailWarning" v-if="this.userEmailCheckList.iEmpty">邮箱不能为空</p>
				<p class="userEmailWarning" v-else-if="this.userEmailCheckList.iIllegal">邮箱格式不正确</p>
				<p class="userEmailWarning" v-else-if="this.userEmailCheckList.iUnique">该邮箱已注册</p>
				<p class="userEmailSuccess" v-else-if="this.userEmailCheckList.iSuccess">该邮箱可用</p>
				<p class="blank" v-else>&nbsp;</p>
			<input type="text" id="emailRename" class="col-md-6" :class="userEmailCheckList"
			@blur.prevent="userEmailCheck" @input="userEmailEmptyCheck"
			:placeholder="this.$store.state.userEmail" :disabled="emailRenameDisabled" v-model="signUpData.userEmail"></input>
			<input type="text" class="col-md-2 iBase" v-if="userEmailCheckList.iSuccess" placeholder="已发送"></input>
			<p class="col-md-2" v-else>&nbsp;</p>
			<a class="btn col-md-2" :class="emailRenameBtn" role="button" @click="emailRenameFunc">{{ emailRenameBtnInfo }}</a>
		</div>
		<p class="col-md-12">&nbsp;</p>
		<div class="setterblock col-md-6">
			<h4>修改密码</h4>
			<div class="col-md-12">
				<span class="col-md-2">&nbsp;</span>
				<span class="col-md-10">
					<p class="blank" v-if="this.rePasswdStat == ''">&nbsp</p>
					<p class="newPasswdWarning" v-else-if="this.rePasswdStat != 'OK'">修改失败</p>
					<p class="newPasswdSuccess" v-else>修改成功</p>
				</span>
				<label class="col-md-2" for="oldPasswd">原密码</label>
				<input type="password" id="oldPasswd" class="iBase col-md-6"
				v-model="signUpData.oldPasswd"></input>
			</div>
			<div class="col-md-12">
				<span class="col-md-2">&nbsp;</span>
				<span class="col-md-10">
					<p class="newPasswdWarning" v-if="this.newPasswdCheckList.iLength">密码长度应在6-20位</p>
					<p class="newPasswdSuccess" v-else-if="this.newPasswdCheckList.iSuccess">密码长度应在6-20位</p>
					<p class="blank" v-else>密码长度应在6-20位</p>
				</span>
				<label class="col-md-2" for="newPasswd">新密码</label>
				<input type="password" id="newPasswd" class="col-md-6" :class="newPasswdCheckList"
				@blur.prevent="newPasswdCheck" @input="newPasswdIllegalCheck"
				v-model="signUpData.newPasswd"></input>
			</div>
			<span class="col-md-12">&nbsp;</span>
			<div class="col-md-12">
				<span class="col-md-1"></span>
				<a class="btn col-md-3" :class="rePasswdBtn" role="button" @click="cancel">取消</a>
				<span class="col-md-1"></span>
				<a class="btn col-md-3" :class="rePasswdBtn" role="button" @click="rePasswd">{{ rePasswdBtnInfo }}</a>
				<span class="col-md-1"></span>
			</div>
		</div>
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: 'setterView',
	data() {
		return {
			signUpData: {
				userName: this.$store.state.userName,
				userEmail: "",
				oldPasswd: "",
				newPasswd: ""
			},
			msg: "暂无数据",
			userRenameDisabled: true,
			userRenameBtnInfo: "保存",
			userRenameBtn: "btn-primary",
			emailRenameDisabled: true,
			emailRenameBtnInfo: "修改",
			emailRenameBtn: "btn-default",
			rePasswdBtn: "btn-default",
			rePasswdBtnInfo: "确认修改",
			rePasswdStat: "",
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
		emailRenameFunc() {
			if (this.emailRenameDisabled == false) {
				if (!this.changeSave('email')) return ;
				this.emailRenameDisabled = true;
				this.emailRenameBtnInfo = "修改";
				this.emailRenameBtn = "btn-default";
			} else {
				this.emailRenameDisabled = false;
				this.emailRenameBtnInfo = "保存";
				this.emailRenameBtn = "btn-primary";
			}
		},
		cancel() {
			this.signUpData.oldPasswd = "";
			this.signUpData.newPasswd = "";
			this.newPasswdCheckList.iError = false;
			this.newPasswdCheckList.iLength = false;
			this.newPasswdCheckList.iSuccess = false;
		},
		rePasswd() {
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
				'oldPasswd': this.signUpData.oldPasswd,
				'newPasswd': this.signUpData.newPasswd,
			}
			
			axios.post('/changePasswd', qs.stringify(formData), config).then(res => {
				this.cancel()
				if (res.data.status == "OK") {
					this.rePasswdStat = "OK"
					console.log('修改成功')
				} else if (res.data.status == "PasswdError") {
					this.rePasswdStat = "NOTOK"
					console.log('密码错误')
				} else {
					this.rePasswdStat = "NOTOK"
					console.log('未知错误')	
				}
			}).catch(err => {
				console.log(err);
			}); 
		},
		changeSave(key) {
			if (key == "userName") {
				if (!this.userNameCheck()) { return false; }
				var value = this.signUpData.userName;
			} else if (key == "email") {
				if (!this.userEmailCheck()) { return false; }
				var value = this.signUpData.userEmail;
			} else { return ; }

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
				key: key,
				value: value,
			}
			
			axios.post('/changeInfo', qs.stringify(formData), config).then(res => {
				if (res.data.status == "OK") {
					if (key == "userName") {
						this.$store.commit('SET_USERNAME', res.data.newName)
						this.userNameCheckList.iSuccess = false;
					} else if (key == "email") {
						console.log('email changed')
						this.userEmailCheckList.iSuccess = false;
					}
				}
			}).catch(err => {
				console.log(err);
				this.error = true;
			}); 
		},
		userNameCheck() {
			if (this.signUpData.userName == this.$store.state.userName) {
				this.userNameCheckList.iSuccess = false;
				return false;
			}
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
	}
}
</script>

<style>

#setterView {
	padding: 0;
}

.renameInput {
	height: 34px;
	font-size: 14px;
	line-height: 1.42857;
	color: #555;
	border: 1px solid #ccc;
	border-radius: 4px;
	box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
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
</style>
