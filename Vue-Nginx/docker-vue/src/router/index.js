import Vue from 'vue'
import Router from 'vue-router'
import store from '../Vuex/index'

const Header = ()=>import('@/components/public/Header')
const Footer = ()=>import('@/components/public/Footer')
const Error = ()=>import('@/components/public/Error')
const Index = ()=>import('@/components/index/Index')

const indexView = ()=>import('@/components/index/views/index')

const signInCard = ()=>import('@/components/index/cards/signIn')
const signUpCard = ()=>import('@/components/index/cards/signUp')
const signIngCard = ()=>import('@/components/index/cards/signIng')

import homeRouter from '@/router/home'
import fileManagerRouter from '@/router/fileManager'
import knowNetRouter from '@/router/knowNet'
import teamsRouter from '@/router/teams'
import setterRouter from '@/router/setter'

Vue.use(Router);

const defaultRouter = {
	path: '/', 
	components: {
		header: Header,
		main: Index,
		footer: Footer,
		default: Index,
	},
	children: [{
		path: '',
		components: {
			default: indexView, views: indexView 
		},
		children: [{
			path: '', name: 'default',
			components: {
				sign: signInCard,
				default: signInCard,
			}
		}]
	}]
}

const indexRouter = {
	path: '/index', 
	components: {
		header: Header,
		main: Index,
		footer: Footer,
		default: Index,
	},
	children: [{
		path: '',
		components: {
			default: indexView, views: indexView 
		},
		children: [{
			path: '', name: 'index',
			components: {
				sign: signInCard,
				default: signInCard,
			}
		}]
	}, {
		path: 'signIn',
		components: {
			default: indexView, views: indexView 
		},
		children: [{
			path: '', name: 'signIn',
			components: {
				sign: signInCard,
				default: signInCard,
			}
		}]
	}, {
		path: 'signUp',
		components: {
			default: indexView, views: indexView 
		},
		children: [{
			path: '', name: 'signUp',
			components: {
				sign: signUpCard,
				default: signUpCard,
			}
		}]
	}, {
		path: 'signIng',
		components: {
			default: indexView, views: indexView 
		},
		children: [{
			path: '', name: 'signIng',
			components: {
				sign: signIngCard,
				default: signIngCard,
			}
		}]
	}]
}

const errorRouter = {
	path: '*',
	components: {
		header: Header,
		main: Error,
		footer: Footer,
		default: Error,
	},
}

const router = new Router({
	mode: 'history',
	routes: [
		defaultRouter, indexRouter, errorRouter, 
		fileManagerRouter, knowNetRouter, teamsRouter,
		setterRouter, homeRouter,
	],
})

// 注册全局钩子用来拦截导航 VueX
router.beforeEach((to, from, next) => {
  const token = store.state.token
  if (to.meta.requireauth) { // 判断该路由是否需要登录权限
    if (token) { // 通过vuex state获取当前的token是否存在
      //console.log(token)
      next()
    } else {
      console.log('该页面需要登陆')
      next({
        path: '/index'
        // query: {redirect: to.fullPath} // 将跳转的路由path作为参数，登录成功后跳转到该路由
      })
    }
  } else {
	if (token) {
		if (to.path == '/' || to.path == '/index') {
			next({ path: '/home' })
		}
	}
	next()
  }
})

export default router

