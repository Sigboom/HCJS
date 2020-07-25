<template>
	<div id="follower" class="col-md-12">
		<ul class="col-sm-12 followersList">
			<li class="col-md-12" v-show="this.$store.state.followerCounter == 0">
				<p class="emptyfollowers col-md-12">关注列表空空如也</p>
			</li>
			<li v-for="(follower, index) in this.$store.state.followerList" :key="index" class="col-md-12">
				<div class="followerListPot col-xs-12" @click="askForTalk(index, follower)" role="button">
					<span class="followerHead col-md-4">
						<img class="followerHeadPic col-md-12" src="../../../../assets/default-head.jpg"  alt="用户头像" />
					</span>
					<span class="col-md-8">
						<p class="followerName col-md-12">{{ follower.name }}</p>
						<p class="followerMsg col-xs-12">{{ follower.latestMsg }}</p>
					</span>
				</div>
			</li>
		</ul>
	</div>
</template>

<script>
export default {
	name: 'follower',
	data() {
		return {
		};
	},
	methods: {
		askForTalk(index, user) {
			this.$store.commit('setTalkBox', {
				box: "talkBox",
				userId: user.id,
				userName: user.name,
			});
		},
		getFollowerList() {
			if (this.$store.state.userId) {
				this.$axios.get('/getFollower', {
					params: { userId: this.$store.state.userId}
				}).then(res => {
					let followerList = res.data.followerList;
					this.$store.commit('setFollowerList', followerList);
					console.log(followerList)
					console.log('关注者列表更新');
				}).catch(err => {
					console.log(err);
				});
			}
		}
	},
	watch: {
		watchUpload(followerCounter) {
			let that = this;
			that.getFollowerList();
		},
	},
	computed: {
		watchUpload() {
			return this.$store.state.followerCounter;
		},
	},
	created() {
		let that = this;
		that.getFollowerList();
	}
}
</script>

<style>
#follower {
	padding: 0;
}

.followersMenuHead {
	padding: 10px;
}
.followerMenuBtn {
	padding: 0;
}

.followerMenuBtn a {
	padding: 6px ;
}

.user-msg::before {	
}

.user-bg {
}

ul li {
	list-style: none;
}

.user-msg {
	display: flow-root;
	filter: blur(20px);
	z-index: -1;
	background-image: url(../../../../assets/defaultHome.jpg);
	background-attachment: fixed;
}

.user-msg::after {
}

/* CSS for Phone */

@media(max-width: 767px) {
	.followersList {
		margin: 0;
	}
}

/* CSS for PC */

@media(min-width: 768px) {
	.followersList {	
		padding: 0;
		height: 450px;
	}
}

.followersList>li {
	padding: 0;
}

.followersList>li>a {
	font-size: 18px;
	text-decoration: none;
	padding: 10px 20px;
}

.menu-router {	
	text-decoration: none;
}

.emptyfollowers {
	line-height: 450px;
	height: 450px;
	font-weight: 500;
	color: #fff;
	font-size: 16px;
	text-align: center;
}

.followerListPot, followerList>.activeNow, followerList>.active {
	font-weight: 500;
	border: 1px solid #565656;
}

.followerListPot {
	font-size: 18px;
	padding: 10px 0px;
	background-color: #939393;
}

.followerListPot:active {
	background-color: #e7e7e7;
}

.followerListPot:hover {
	background-color: #c2c2c2eb;
	text-decoration: none;
}

.followerMsg {
	font-size: 14px;
	color: #e8e3e3;
	margin: 0;
	padding: 0;
	max-width: 100%;
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}

.menu-text {
	margin: 0 auto;	
	color: #fff;
	text-decoration: none;
}

.followerName {
	padding: 0;
}

.followerListPot>.followerHead {
	padding: 0;
	border: 2px solid #e6e6e6;
	border-radius: 50%;
	background-size: cover;
	overflow: hidden;
}

.followerHeadPic {
	padding: 0;
}

.userName {
	margin: 0px auto 10px;
	text-align: center;
	color: #fff;
}

.userStatus, .userShow {
	margin: 10px auto;
	color: #fff;
	text-align: center;
	margin-block-start: 0;
	margin-block-end: 0;
}

@media (max-width: 767px) {
	.disNavbarToggle {
		display: none;
	}
}


nav .dropdown-toggle>.caret {
	transform: rotate(0) !important;
}
  
nav .open>.dropdown-toggle>.caret {
	transform: rotate(180deg) !important;
}
  

  nav .menuList .dropdown.open .dropdown-menu,
  nav .menuList .dropdown.open .dropdown-menu>.dropdown-submenu.open>.dropdown-menu {
    max-height: 100vh;
  }

  nav .menuList .dropdown>.dropdown-menu,
  nav .menuList .dropdown>.dropdown-menu>.dropdown-submenu>.dropdown-menu {
    display: block !important;
    position: static;
    float: none;
    max-height: 0;
    margin: 0;
    padding: 0;
    border: none;
    box-shadow: none;
    overflow: hidden;
    transition: all .5s ease-in-out;
  }

</style>
