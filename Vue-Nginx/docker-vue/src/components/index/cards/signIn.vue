<template>
	<div class="signIn col-md-5">
		<form class="col-xs-12">
			<label class="login-head col-xs-12">帐号密码登录</label>
			<div class="input-group">
				<input type="text" class="nameEmailInput col-xs-12"
				v-model="nameEmail" placeholder="用户名/邮箱" autocomplete="off">
			</div>
			<div class="input-group">
				<input type="password" class="passwordInput col-xs-12"
				v-model="passwd" placeholder="密码" autocomplete="off">
			</div>
		</form>

		<form class="col-xs-12">
		<input class="memberPasswd col-xs-1" type="checkbox" name="memberPass" checked="checked">
		<label class="label-memberPasswd col-xs-11" for="memberPasswd">下次自动登录</label>
		</br>
		<button class="login-bu col-xs-12" type="submit" @click="submitForm($event)">登&nbsp;录</button>
		<a class="login-fgtpwd col-xs-6" href="page-recoverpw.html">忘记密码?</a>
		<a class="a-button has-icon col-xs-6" href="https://github.com/Sigboom/HCJS">
			<svg viewBox="0 0 24 24">
				<title>GitHub Dark icon</title>
				<path fill="#7f8C8D" d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"></path>
			</svg>GitHub
		</a>
		<router-link class="a-register col-xs-12" to="/index/signUp">还没有账号？快注册一个吧！</router-link>
	</form>
	</div>
</template>

<script>
export default {
	name: 'signIn',
	data() {
		return {
			nameEmail:"",
			passwd: ""
		}
	},
	methods: {
		submitForm(event) {
			event.preventDefault(); //阻止事件的默认行为
			var regex=/^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
			if (regex.test(this.nameEmail)) {
				var params = {
					userName: "",
					userEmail: this.nameEmail,
					password: this.passwd,
				}
			} else {
				var params = {
					userName: this.nameEmail,
					userEmail: "",
					password: this.passwd,
				}
			}
			axios.get('/getCsrftoken');
			this.$router.push({
				name: 'signIng',
				params: params,
			});
		}
	}
}
</script>

<style>

.signIn {
	height: 360px;
	background-color:#ffffff;
	padding:30px 25px;
	border-radius: 10px;
}

.login-head {
	font-size: 18px;
	text-align: left;
}

.nameEmailInput, .passwordInput {
	height: 35px;
	margin: 5% 0;
	border-radius: 15px;
	border-width: 2px;
	border-color: #bbbbbb;
}

.login-bu {
	margin: 5% 0;
    height:40px;
    border-radius: 2em;
    color: #fff;
    background-color: #4fc08d;
    line-height: 16px;
    font-size: 20px;
    text-decoration: none;
}

.has-icon > svg {
    left: 0.4em;
    top: 0.4em;
    width:1.2em;
}

.a-button {
    padding: 4px 0;
    display: inline-block;
    line-height:20px;
    font-size:20px;
    border-radius: 2em;
    background-color: #4fc08c7a;
    text-align: center;
    color: #7f8c8d;
    text-decoration: none;
}

.login-fgtpwd {
    color: #7f8c8d;
	line-height:20px;
    text-decoration: none;
	padding-top: 4%;
	padding-right: 0;
}

.a-register {
    font-size: 14px;
    color: #54bd8eed;
    text-decoration: none;
	margin-top: 6%;
	padding: 0;
}

.input-group {
	display: block;
}

</style>
