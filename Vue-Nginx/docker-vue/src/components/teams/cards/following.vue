<template>
	<div id="following" class="col-md-12">
		<ul class="col-sm-12 followingList">
			<li class="col-md-12" v-if="this.$store.state.followingCounter == 0">
				<p class="emptyfollowing col-md-12">粉丝列表空空如也</p>
			</li>
			<li v-for="(following, index) in this.$store.state.followingList" :key="index" class="col-md-12">
				<div class="followingListPot col-xs-12"
				@click="askForTalk(index, following)" role="button">
					<span class="userHead col-md-3">
						<img class="userHeadPic col-xs-12" src="../../../assets/default-head.jpg"  alt="用户头像" />
					</span>
					<span class="col-xs-8">
						<p class="col-xs-12">{{ following.name }}</p>
						<p class="followingMsg col-xs-12">{{ following.latestMsg }}</p>
					</span>
				</div>
			</li>
		</ul>
	</div>
</template>

<script>
export default {
	name: 'following',
	data() {
		return {
		};
	},
	methods: {
		askForTalk(index, user) {
			this.$store.commit('setTalkBox', {
				box: "talkBox",
				userID: user.id,
				userName: user.name,
			});
		},
		getFollowingList() {
			if (this.$store.state.userID) {
				this.$axios.get('/getFollowing', {
					params: {
						userID: this.$store.state.userID
					}
				}).then(res => {
					let followingList = res.data.followingList;
					this.$store.commit('setFollowingList', followingList);
					console.log('粉丝列表更新');
				}).catch(err => {
					console.log(err);
				});
			}
		}
	},
	watch: {
		watchUpload(followingCounter) {
			let that = this;
			that.getFollowingList();
		},
	},
	computed: {
		watchUpload() {
			return this.$store.state.followingCounter;
		},
	},
	created() {
		let that = this;
		that.getFollowingList();
	}
}
</script>

<style>
#following {
	padding: 0;
}

.followingMenuHead {
	padding: 10px;
}
.followingMenuBtn {
	padding: 0;
}

.followingMenuBtn a {
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
	background-image: url(../../../assets/defaultHome.jpg);
	background-attachment: fixed;
}

.user-msg::after {
}

/* CSS for Phone */

@media(max-width: 767px) {
	.followingList {
		margin: 0;
	}
}

/* CSS for PC */

@media(min-width: 768px) {
	.followingList {	
		padding: 0;
		height: 450px;
	}
}

.followingList>li {
	padding: 0;
}

.followingList>li>a {
	font-size: 18px;
	text-decoration: none;
	padding: 10px 20px;
}

.menu-router {	
	text-decoration: none;
}

.emptyfollowing {
	line-height: 450px;
	height: 450px;
	font-weight: 500;
	color: #fff;
	font-size: 16px;
	text-align: center;
}

.followingListPot, followingList>.activeNow, followingList>.active {
	font-weight: 500;
	border: 1px solid #565656;
}

.followingListPot {
	font-size: 18px;
	padding: 10px 20px;
	background-color: #939393;
}

.followingListPot:active {
	background-color: #e7e7e7;
}

.followingListPot:hover {
	background-color: #c2c2c2eb;
	text-decoration: none;
}

.followingMsg {
	font-size: 14px;
	color: #494a50;
	margin: 0;
	padding: 0;
}

.menu-text {
	margin: 0 auto;	
	color: #fff;
	text-decoration: none;
}

.userHead {
	height: 0;	
	padding-top: 23%;
	border: 2px solid #e6e6e6;
	border-radius: 50%;
	background-size: cover;
	overflow: hidden;

}

.userHead>.userHeadPic {
	position: absolute;
	padding: 0;
	top: 0;
	left: 0;
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
