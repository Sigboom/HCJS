<template>
	<div class="signIng col-md-5">
		<div class="status-box col-md-12"
		:class="{ 'load-color': load, 'bingo-color': success, 'duang-color': error }">
			<div class="loading col-xs-12" v-if="load">
				<span></span>
				<span></span>
				<span></span>
				<span></span>
				<span></span>
			</div>
			<div class="bingo col-xs-12" v-else-if="success"></div>
			<div class="duang col-xs-12" v-else></div>
		</div>
		<div class="status-text col-xs-12"> 
			<p class="load-text col-xs-12" v-if="load"> 正在登陆...</p>
			<p class="bingo-text col-xs-12" v-if="success"> 登陆成功 </p>
			<p class="duang-text col-xs-12" v-if="error"> 登录失败 </p>
			<div class="notFound col-xs-12" v-if="backError">
				<p>不要着急，工程师正在抢修...</p>
			</div>
			<div class="notFound col-xs-12" v-if="wrong">
				<p>账号或密码错误!</p>
			</div>
		</div>
		<button class="back-button col-xs-12" @click="$router.back(-1)" v-if="load || error">返回</button>
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: 'signIng',
	data() {
		return {
			formData: {
				userName: this.$route.params.userName,
				userEmail: this.$route.params.userEmail,
				password: this.$route.params.password
			},
			load: true,
			success: false,
			backError: false,
			error: false,
			wrong: false
		}
	},
	created () { 
		let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
		var csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
		var config = {
			headers: {
				'X-Requested-With':'XMLHttpRequest',
				'Content-Type': 'application/x-www-form-urlencoded',
				'X-CSRFToken': csrfToken
			}
		}; 
		
		let formData = this.formData;
		//console.log(formData);
		this.$axios.post('/signIn', qs.stringify(formData), config).then(
			res => {
				this.load = false;
				switch (res.data.status) {
					case "OK!":
						//console.log(res.data)
						this.$store.commit('SET_TOKEN', csrfToken);
						this.$store.commit('SET_USERID', res.data.userId)
						this.$store.commit('SET_USERNAME', res.data.userName)
						this.success = true;
						setTimeout(() => {
							this.$router.push({path: '/home'});
						}, 2500);
						break;
					case "Wrong!":
					case "EmptyWrong":	
						this.error = true;
						this.wrong = true;
						break;
					default:
						this.error = true;
						this.backError = true;
						break;
				}
			}).catch(err => {
				//console.log(err);
				this.load = false;
				this.error = true;
				this.backError = true;
			});
	}
}
</script>

<style>

.signIng {
	height: 360px;
	background-color:#ffffff;
	padding:30px 25px;
	border-radius: 10px;
}

.status-box{
	width: 60%;
	height: 47%;
	position: relative;
	margin: 0 16%;
	border-radius: 50%;
}

.status-text {
	margin: 20px auto;
	font-size: 18px;
	font-weight: 500;
	text-align: center;
}

.load-color {
	background:#edb700;
}

.bingo-color {	
	background: #00ED70;
}

.duang-color {	
	background: #ed5f00;
}

.bingo {
	width:80px;
	height:40px;
	position:absolute;
	left:60%;
	top:60%;
	margin:-40px 0 0 -50px;
	-webkit-transform:rotate(-45deg);
	transform:rotate(-45deg);
	overflow:hidden
}

.duang {
	width: 88px;
	height: 90px;
	position:absolute;
	left: 20%;
	top: 18%;
	overflow:hidden
}

.duang:before, .duang:after {
	width:10px;
	height:100px;
	content:"";
	position:absolute;
	background: #fff;
	border-radius:5px
}

.bingo:before, .bingo:after {
	width:8px;
	height:50px;
	content:"";
	position:absolute;
	background:#fff;
	border-radius:5px
}

.duang:before {
	
	-webkit-transform:rotate(-45deg);
	transform:rotate(-45deg);	
	
	-webkit-animation:topLeft 0.5s linear 0s 1 both;
	animation:topLeft 0.5s linear 0s 1 both
}

.duang:after {
	-webkit-transform:rotate(45deg);
	transform:rotate(45deg);	
	-webkit-animation:topRight 0.5s linear 0.2s 1 both;
	animation:topRight 0.5s linear 0.2s 1 both
}

@keyframes topLeft{
	0%{
		top: -120px;
		left: -80px;
	}
	100%{
		top: 0;
		left: 40px;
	}
}

@-webkit-keyframes topLeft{
	0%{
		top: -120px;
		left: -80px;
	}
	100%{
		top: 0;
		left: 40px;
	}
}

@keyframes topRight{
	0%{
		top: -120px;
		right: -80px;
	}
	100%{
		top: 0px;
		right: 40px;
	}
}

@-webkit-keyframes topRight{
	0%{
		top: -120px;
		right: -80px;
	}
	100%{
		top: 0px;
		right: 40px;
	}
}

.bingo:before{
	width:8px;
	height:50px;
	left:0;
	-webkit-animation:dgLeft 0.5s linear 0s 1 both;
	animation:dgLeft 0.5s linear 0s 1 both
}

.bingo:after{
	width: 90px;
	height:10px;
	bottom:0;
	-webkit-animation:dgRight 0.5s linear 0.5s 1 both;
	animation:dgRight 0.5s linear 0.5s 1 both
}

@-webkit-keyframes dgLeft{
	0%{
		top:-125%
	}
	100%{
		top:-25%
	}
}

@keyframes dgLeft{
	0%{
		top:-125%
	}
	100%{
		top:-25%
	}
}

@-webkit-keyframes dgRight{
	0%{
		left:-120%
	}
	100%{
		left:0%
	}
}

@keyframes dgRight{
	0%{
		left:-120%
	}
	100%{
		left:0%
	}
}

.back-button {
    height:40px;
    border-radius: 2em;
    color: #fff;
    background-color: #4fc08d;
    line-height: 16px;
    font-size: 20px;
    text-decoration: none;
}

.duang-text {
	font-size: 18px;
}

.notFound {
	font-size: 16px;	
	padding: 0;
}

.loading-text {
	margin-left: 25%;
	margin-top: 20px;
}

.loading{
	width:100px;
	height:50px;
	position:absolute;
	left:50%;
	top:60%;
	margin:-40px 0 0 -50px;
	text-align:center;
}

.loading span {
    width:10px;
    height:100%;
    display:inline-block;
    background:#fff;
    animation: mymove 1.2s infinite ease-in-out;
    -webkit-animation:mymove 1.2s infinite ease-in-out;
}

.loading >span:nth-child(2){
    -webkit-animation-delay:-1.0s;
    animation-delay:-1.0s;
}
.loading >span:nth-child(3){
    -webkit-animation-delay:-0.9s;
    animation-delay:-0.9s;
}
.loading >span:nth-child(4){
    -webkit-animation-delay:-0.8s;
    animation-delay:-0.8s;
}
.loading >span:nth-child(5){
    -webkit-animation-delay:-0.7s;
    animation-delay:-0.7s;
}
@keyframes mymove{
    0%{transform:scaleY(0.4);}
    25%{transform:scaleY(1.0);}
    50%{transform:scaleY(0.4);}
    75%{transform:scaleY(0.4);}
    100%{transform:scaleY(0.4);}
}
@-webkit-keyframes mymove{
    0%{transform:scaleY(0.4);}
    25%{transform:scaleY(1.0);}
    50%{transform:scaleY(0.4);}
    75%{transform:scaleY(0.4);}
    100%{transform:scaleY(0.4);}
}
</style>
