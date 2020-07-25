<template>
	<div class="container col-xs-12">
		<div class="portrait">
			<img class="headPic col-xs-12" src="../../../assets/default-head.jpg"  alt="用户头像" />
		</div>
		<p class="userName col-sm-12" v-if="!this.$store.state.userId">游客</p>
		<p class="userName col-sm-12" v-else>{{ this.$store.state.userName }}</p>
		<p class="userStatus col-sm-12">当前心情</p>
		<p class="userShow col-sm-12">个人介绍</p>
		<ul class="col-sm-12 navbar-nav menuList">
			<li v-for="(lnkPage, index) in pages" :key="index" class="dropdown col-xs-12" :class="active[index]">
				<div class="menuListPot userMenuStyle dropdown-toggle col-xs-12" :class="lnkPage.pageClass"
				data-toggle="dropdown" role="button"
				aria-haspopup="true" aria-expanded="false" v-if="lnkPage.dropdown">
					<span :class="lnkPage.icon" aria-hidden="true"></span>
					{{ lnkPage.name }}<span class="caret"></span>
				</div>
				<router-link class="menuListPot userMenuStyle col-xs-12" :class="lnkPage.pageClass"
				role="button" :to="lnkPage.url" @click.native="activeCommit(index)" v-else>
					<span :class="lnkPage.icon" aria-hidden="true"></span>&nbsp;{{ lnkPage.name }}
				</router-link>
				<ul class="dropdown-menu" v-if="lnkPage.dropdown">
					<li v-for="(link, id) in lnkPage.sublink" @click="activeCommit(index)">
						<router-link class="menu-router" :to="link.url" :id="id">
							<p>{{ link.name }}</p>
						</router-link>
					</li>
					<!--
					<li role="separator" class="divider"></li>
					<li><a href="#">One more separated link</a></li>
					-->
				</ul>
			</li>
		</ul>
	</div>
</template>

<script>
export default {
	name: 'User_card',
	data() {
		return {
			pages: [{ 
				name: "个人中心", icon: "glyphicon glyphicon-home", url: "/home", dropdown: false,
			}, {
				name: "我的文档", icon: "glyphicon glyphicon-folder-open", dropdown: true,
				sublink: [{
					name: "文档列表", url:"/fileManager",
				}, {
					name: "上传下载", url:"/fileManager/fileLoad"
				}],
			}, {
				name: " 知识网络", icon: "glyphicon glyphicon-th", dropdown: true,
				sublink: [{
					name: "个人网络", url:"/knowNet"
				}],
			}, {
				name: "我的团队", icon: "glyphicon glyphicon-tower", dropdown: true,
				sublink: [{
					name: "团队概况", url:"/teams"
				}, {
					name: "新建/加入团队", url:"/teams/maker"
				}, {
					name: "团队设置", url:"/teams/setter"
				}],
			}, {
				name: "个人设置", icon: "glyphicon glyphicon-cog", dropdown: true,
				sublink: [{
					name: "账号设置", url:"/setter"
				}],
			}],
			active: [],
			activeNow: 0,
		};
	},
	methods: {
		activeCommit(toIndex) {
			this.$store.commit('setUserMenuIndex', toIndex);
		},
		activeChange() {
			let now = this.$store.state.userMenuIndex;
			console.log('activeChange', this.activeNow, "=>", now);
			if (this.activeNow == now) return ;
			this.active.splice(this.activeNow, 1, { active: false });
			this.active.splice(now, 1, { active: true });
			this.activeNow = now;
		},
		initActive() {
			let now = this.$store.state.userMenuIndex;
			this.activeNow = now;
			for (let i = 0; i < now; ++i) {
				this.active.push({ active: false });
			}
			this.active.push({ active: true });
			for (let i = now + 1; i < this.pages.length; ++i) {
				this.active.push({ active: false });
			}
		},
	},	
	created() {
		let that = this;
		that.initActive();
	},
	watch: {
		watchActive(userMenuIndex) {
			let that = this;
			that.activeChange();
		},
	},
	computed: {
		watchActive() {
			return this.$store.state.userMenuIndex;
		},
	},
}
</script>

<style>
.headPic {
	padding: 0;
}

.container {
	padding: 0;
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

@media(max-width: 767px) {
	.menuList {
		margin: 0;
	}
}

.menuList, .menuList>li {
	padding: 0;
}

.menuList>li>a {
	font-size: 18px;
	text-decoration: none;
	padding: 10px 20px;
}

.menu-router {	
	text-decoration: none;
}

.menuListPot {
	text-align: center;
	font-weight: 500;
	border: 1px solid #565656;
	background-color: #939393;
}

.menuList .menuListPot:hover {	
	background-color: #cacaca;
}

.menuList>.active>.menuListPot {
	background-color: #e7e7e7;
}

.userMenuStyle {
	font-size: 18px;
	padding: 10px 20px;
}

.menu-text {
	margin: 0 auto;	
	color: #fff;
	text-decoration: none;
}

.portrait {
	margin: 6% 20%;
	height: 20%;	
	border: 2px solid #e6e6e6;
	border-radius: 50%;
	background-size: cover;
	overflow: hidden;
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
