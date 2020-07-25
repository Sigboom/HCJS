<template>
	<nav class="navbar navbar-default navbar-fixed-top header">
        <div class="container">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#menuHeader" aria-expanded="false">
					<span class="menu-icon"></span>
					<span class="menu-icon"></span>
					<span class="menu-icon"></span>
				</button>
				<button type="button" class="userMenu-toggle collapsed"
				data-toggle="collapse" data-target="#userMenu"
				v-show="this.$store.state.userId">
					<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="-1 -1 26 26" id="nav-user" x="26" y="27"><g fill="#FFF"><path d="M12 14a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 2a5 5 0 1 1 0-10 5 5 0 0 1 0 10z"/><path d="M12 24C5.373 24 0 18.627 0 12S5.373 0 12 0s12 5.373 12 12-5.373 12-12 12zm0-2c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="M12 22a9.972 9.972 0 0 0 7.142-3A9.972 9.972 0 0 0 12 16a9.972 9.972 0 0 0-7.142 3A9.972 9.972 0 0 0 12 22zm0-8c4.015 0 7.57 1.972 9.748 5A11.984 11.984 0 0 1 12 24c-4.015 0-7.57-1.972-9.748-5C4.43 15.972 7.985 14 12 14z"/></g></svg>
				</button>
				<button type="button" class="search-toggle collapsed" data-toggle="collapse" data-target="#search">
					<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="-1 -1 26 26" id="nav-search" y="27"><g fill="none" fill-rule="evenodd"><path d="M0 0h24v24H0z"/><path fill="#FFF" fill-rule="nonzero" d="M11 18a7 7 0 1 0 0-14 7 7 0 0 0 0 14zm7.032-1.382l4.692 4.692a1 1 0 0 1-1.414 1.414l-4.692-4.692a9 9 0 1 1 1.414-1.414z"/></g></svg>
				</button>
				<router-link class="navbar-brand" to="/index" v-if="!this.$store.state.userId">
					<img alt="logo" class="logo" src="../../assets/logo.png">
				</router-link>
				<router-link class="navbar-brand" to="/home" v-else>
					<img alt="logo" class="logo" src="../../assets/logo.png">
				</router-link>
          </div>

		<div class="search col-xs-12 collapse" id="search">
            <form class="navbar-form col-xs-12" role="search">
              <div class="form-group col-xs-9">
                <input type="text" class="form-control" placeholder="搜索内容">
              </div>
              <button type="submit" class="btn btn-default col-xs-3">Sigboom</button>
            </form>
		</div>
        <div class="collapse navbar-collapse" id="menuHeader">
            <ul class="nav navbar-nav" v-if="this.$store.state.userId">
				<li v-for="(menu, index) in nav" :class="active[index]" >
					<router-link @click.native="activeCommit(index)" :to="menu.href">{{ menu.name }}</router-link>
				</li>
		  <!-- <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">可扩展<span class="caret"></span></a>
                <ul class="dropdown-menu">
                  <li><a href="#">Action</a></li>
                  <li><a href="#">Another action</a></li>
                  <li><a href="#">Something else here</a></li>
                  <li role="separator" class="divider"></li>
                  <li><a href="#">Separated link</a></li>
                  <li role="separator" class="divider"></li>
                  <li><a href="#">One more separated link</a></li>
                </ul>
              </li> -->
			</ul>
            <ul class="nav navbar-nav" v-else>
				<li v-for="(menu, index) in unLogin" :class="active[index]" >
					<router-link @click.native="activeCommit(index)" :to="menu.href">{{ menu.name }}</router-link>
				</li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
				<li><router-link to="/index" v-show="!this.$store.state.userId">登录</router-link></li>
				<li><router-link to="/index/sign_up" v-show="!this.$store.state.userId">注册</router-link></li>
			</ul>
			<ul class="nav navbar-nav navbar-right" v-show="this.$store.state.userId">
				<li class="dropdown">
					<a href="#" class="user-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ this.$store.state.userName }}<span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><router-link to="/home">个人中心</router-link></li>
						<li><a href="#">Something else here</a></li>
						<li role="separator" class="divider"></li>
						<li><a @click="signOut">注销登录</a></li>
					</ul>
				</li>
            </ul>
				<form class="search navbar-form float-right" role="search">
					<div class="form-group">
						<input type="text" class="form-control" placeholder="搜索内容">
					</div>
					<button type="submit" class="btn btn-default">Sigboom</button>
				</form>
			</div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
		<div class="cover"></div>
	</nav>
</template>


<script>

$(function() {
  $('button.navbar-toggle').click(function(){
    $('body').toggleClass('out');
    $('nav.header').toggleClass('out');
	$('div.cover').toggleClass('discover');
    if ($('body').hasClass('out')) {
      $(this).focus();
    } else {
      $(this).blur();
    }
  });
});

$(document).click(function(e) {
  if (!$(e.target).closest('.navbar-collapse, button.navbar-toggle').length && $('body').hasClass('out')) {
    e.preventDefault();
    $('button.navbar-toggle').trigger('click');
  }
}).keyup(function(e) {
  if (e.keyCode == 27 && $('body').hasClass('out')) {
    $('button.navbar-toggle').trigger('click');
  }
});

$(function() {
  $('button.userMenu-toggle').click(function(){
    $('body').toggleClass('right');
	$('nav.header').toggleClass('right');
	$('div.cover').toggleClass('discover');
    if ($('body').hasClass('right')) {
      $(this).focus();
    } else {
      $(this).blur();
    }
  });
});

$(document).click(function(e) {
  if (!$(e.target).closest('.userMenu, button.userMenu-toggle').length && $('body').hasClass('right')) {
    e.preventDefault();
    $('button.userMenu-toggle').trigger('click');
  }
}).keyup(function(e) {
  if (e.keyCode == 27 && $('body').hasClass('right')) {
    $('button.userMenu-toggle').trigger('click');
  }
});

export default {
	name: 'Header',
	data() {
		return {		
			nav: [
				{ name: '个人中心', href: '/home', },
				{ name: '关系', href: '/home/friends', },
				{ name: '使用教程', href: '/home', },
				{ name: '感谢', href: '#', },
			],
			unLogin: [
				{ name: '首页', href: '/index', },
				{ name: '使用教程', href: '/index', },
				{ name: '感谢', href: '#', },
			],
			active: [],
			activeNow: 0,
		}
	},
	methods: {
		signOut() {
			//console.log(this.$store.state.userId);
			this.$store.commit('LOGOUT');
			this.$router.push('/index');
		},
		activeCommit(toIndex) {	
			this.$store.commit('setHeaderIndex', toIndex);
		},
		activeChange() {
			let now = this.$store.state.headerIndex;
			if (this.activeNow == now) return ;
			this.active.splice(this.activeNow, 1, { active: false });
			this.active.splice(now, 1, { active: true });
			this.activeNow = now;
		},
		initActive() {
			this.active.push({ active: true });
			for (let i = 1; i < this.nav.length; ++i) {
				this.active.push({ active: false });
			}
		}
	},
	created() {
		let that = this;
		that.initActive();
	},
	watch: {
		watchActive(headerIndex) {
			let that = this;
			that.activeChange();
		},
	},
	computed: {
		watchActive() {
			return this.$store.state.headerIndex;
		},
	},
}

</script>

<style>

.header {
    background-color: #c2c2c2eb; 
	margin-bottom: 0;
}

.float-right {
	float: right!important;
}

.navbar-brand {
    margin: 0 20px;
	padding: 0;
	height: 60px;
	width: 100px;
}


.logo {
    height: 100%;
    width: 100%;
	transform:scale(0.8);
}

@media(min-width: 768px) {
	.userMenu-toggle, .search-toggle {
		display: none;
	}
}

.navbar-toggle {	
    padding: 10px;
}

.userMenu-toggle, .search-toggle {
	background: #c2c2c2eb;
	position: relative;
    float: right;
    padding: 3px 10px 0px 10px;
    margin-top: 8px;
    margin-right: 12px;
    background-color: transparent;
    border: 1px solid transparent;
    border-radius: 4px;
	border-color: #ddd;
}

.menu-icon {
	background-color: #fff;
	transition: all 500ms ease-in-out;
	display: block;
    width: 22px;
    height: 2px;
    border-radius: 1px;
}

.menu-icon+.menu-icon {
	margin-top: 4px;
}

@media (max-width: 767px) {
	nav .navbar-toggle .menu-icon {
		 transition: all 500ms ease-in-out;
	}

	body.out nav .navbar-toggle .menu-icon:nth-of-type(1) {
		transform: translate3d(0,6px,0) rotate(45deg);
	}

	body.out nav .navbar-toggle .menu-icon:nth-of-type(2) {
		opacity: 0;
	}

	body.out nav .navbar-toggle .menu-icon:nth-of-type(3) {
		transform: translate3d(0,-6px,0) rotate(-45deg);
	}

	body.right nav .navbar-toggle .menu-icon:nth-of-type(1) {
		transform: translate3d(0,6px,0) rotate(45deg);
	}

	body.right nav .navbar-toggle .menu-icon:nth-of-type(2) {
		opacity: 0;
	}

	body.right nav .navbar-toggle .menu-icon:nth-of-type(3) {
		transform: translate3d(0,-6px,0) rotate(-45deg);
	}
}

.navbar-nav>li>a {
	padding: 20px 10px;
	font-size: 16px;
}

.navbar-form {
	margin-top: 14px;
	padding: 0;
}

.search .form-control {
    padding-left: 25px;
    border: 0px;
    background: #fff url(../../assets/search.png) 5px 8px no-repeat;
    background-size: 20px;
}

@media (max-width: 767px) {
	.navbar-form .form-group {
		display: inline-block;
	}
}

nav .dropdown-toggle>.caret, nav .user-toggle>.caret {
    transform: rotate(0) !important;
}
  
nav .open>.dropdown-toggle>.caret, nav .open>.user-toggle>.caret {
    transform: rotate(180deg) !important;
}
  
/*!
 * Bootstrap Off-Canvas Nav (http://github.com/marcandrews/bootstrap-off-canvas-nav)
 * Copyright (c) 2015 Marc Andrews
 * Licensed under the MIT license
 */

@media (max-width: 767px) {

	.cover {
		display: none;
	}

	.discover {
		display: block;
		position: absolute;
		width: 100%;
		height: 10000px;
		z-index: 2000;
		top:-60px;
		background: #000;
		opacity:0.5;
	}
  body {
    position: absolute;
    left: 0;
    right: 0;
    overflow-x: hidden;
    backface-visibility: hidden;
    transition: all 0.3s ease-in-out;
    transition-delay: 0s;
  }

  body.out {
    left: -275px;
    right: 275px;
    overflow: hidden;
  }
  
  body.off-canvas-nav-left.out {
    left: 275px;
    right: -275px;
  }

  .container-fluid>.navbar-collapse,
  .container>.navbar-collapse {
    margin-left: 0;
    margin-right: 0;
  }
  
  nav.navbar-fixed-top {
    transition: all 0.3s ease-in-out;
    transition-delay: 0s;
  }

  nav.header.out {
    transform: translate3d(-275px,0,0);
  }

  body.off-canvas-nav-left nav.navbar-fixed-top.out {
    transform: translate3d(275px,0,0);
    transition-delay: 0.3s;
  }
  

  nav .navbar-toggle {
    transition: all 500ms ease-in-out;
  }
  
  nav.header.out .navbar-toggle {
		z-index: 10000;
  }

	.navbar-default .navbar-toggle:focus, .navbar-default .navbar-toggle:hover {
		background-color: transparent;
	}

  body.off-canvas-nav-left nav .navbar-toggle {
    float: left;
	margin-left: 15px;
	margin-right: 0;
  }

  nav .navbar-collapse {
    display: block !important;
    position: fixed;
    top: 0;
    right: -275px;
    bottom: 0;
    z-index: 10000;
    width: 275px;
    height: 100vh !important;
    margin: 0;
    background-color: inherit;
    border: none;
    box-shadow: none;
    border-left: 1px solid #e7e7e7;
    transition: all 0.3s ease-in-out;
  }
 
  body.out nav .navbar-collapse {
    box-shadow: -10px 0px 50px 0px rgba(0,0,0,0.75);
    transform: translate3d(-275px,0,0);
  }
  
  nav.navbar-fixed-top .navbar-collapse {
	right: -275px !important;
    max-height: none;
  }

  body.out nav.navbar-fixed-top .navbar-collapse {
    box-shadow: -10px 0px 50px 0px rgba(0,0,0,0.75);
    transform: none;
  }
  
  body.off-canvas-nav-left nav .navbar-collapse {
    left: -275px;
    right: auto;
    border: none;
    border-right: 1px solid #e7e7e7;
  }

  body.off-canvas-nav-left.out nav .navbar-collapse {
    box-shadow: 10px 0px 50px 0px rgba(0,0,0,0.75);
    transform: translate3d(275px,0,0);
  }

  body.off-canvas-nav-left.out nav.navbar-fixed-top .navbar-collapse {
    box-shadow: 10px 0px 50px 0px rgba(0,0,0,0.75);
    transform: none;
  }
  
  nav .navbar-collapse .dropdown-menu>li>a:focus, .dropdown-menu>li>a:hover {
      background-color: #eee !important;
  }

  nav .navbar-collapse .dropdown>.dropdown-menu,
  nav .navbar-collapse .dropdown>.dropdown-menu>.dropdown-submenu>.dropdown-menu {
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

  nav .navbar-collapse .dropdown .dropdown-menu li a,
  nav .navbar-collapse .dropdown .dropdown-menu li.dropdown-header {
    padding: 5px 15px 5px 25px;
    color: rgb(119, 119, 119);
  }

  nav .navbar-collapse .dropdown.open .dropdown-menu,
  nav .navbar-collapse .dropdown.open .dropdown-menu>.dropdown-submenu.open>.dropdown-menu {
    max-height: 100vh;
  }

  nav .navbar-form {
    margin-top: 0;
    margin-bottom: 0;
    border: none;
    box-shadow: none;
  }


  body.right {
    left: 275px;
    right: -275px;
    overflow: hidden;
  }
  
  nav.userMenu {
    transition: all 0.3s ease-in-out;
    transition-delay: 0s;
  }

  nav.userMenu.right {
    transform: translate3d(-275px,0,0);
  }

  nav .userName {
    transition: all 500ms ease-in-out;
  }
  
  body.right nav.userMenu-toggle {
    background-color: #ddd;
  }
  
  nav.header.right {
    transform: translate3d(275px,0,0);
  }

  nav.header.right .navbar-toggle {
		z-index: 10000;
		transform: translate3d(-280px,0,0);
  }

	nav.userMenu {
		display: block !important;
		position: fixed;
		top: 0;
		left: -275px;
		bottom: 0;
		z-index: 10000;
		width: 275px;
		height: 100vh !important;
		margin: 0;
		border: none;
		box-shadow: none;
		border-left: 1px solid #e7e7e7;
		transition: all 0.3s ease-in-out;
	}
 
	body.right nav.userMenu {
	   box-shadow: -10px 0px 50px 0px rgba(0,0,0,0.75);
	    transform: translate3d(275px,0,0);
	}
  
  nav.navbar-fixed-top .navbar-collapse {
	right: -275px !important;
    max-height: none;
  }

#menuHeader .search {
	display: none;
}
  nav .navbar-collapse .dropdown-menu>li>a:focus, .dropdown-menu>li>a:hover {
      background-color: #eee !important;
  }

  nav .navbar-collapse .dropdown>.dropdown-menu,
  nav .navbar-collapse .dropdown>.dropdown-menu>.dropdown-submenu>.dropdown-menu {
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

  nav .navbar-collapse .dropdown .dropdown-menu li a,
  nav .navbar-collapse .dropdown .dropdown-menu li.dropdown-header {
    padding: 5px 15px 5px 25px;
    color: rgb(119, 119, 119);
  }

  nav .navbar-collapse .dropdown.open .dropdown-menu,
  nav .navbar-collapse .dropdown.open .dropdown-menu>.dropdown-submenu.open>.dropdown-menu {
    max-height: 100vh;
  }

  nav .navbar-form {
    margin-top: 0;
    margin-bottom: 0;
    border: none;
    box-shadow: none;
  }
}

</style>
