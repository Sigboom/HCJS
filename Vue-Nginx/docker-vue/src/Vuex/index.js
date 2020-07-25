import Vue from 'vue'
import Vuex from 'vuex'

import {fileListManager, fileMutations} from '@/Vuex/fileManager'
import {home, homeMutations} from '@/Vuex/home'
import {teams, teamsMutations} from '@/Vuex/teams'
import {knowNet, nodeMutations} from '@/Vuex/knowNet'
import {setter, setterMutations} from '@/Vuex/setter'

Vue.use(Vuex)

// 初始化时用sessionStore.getItem('token'),这样子刷新页面就无需重新登录
const state = {
	userId: window.sessionStorage.getItem('userId'),
	userName: window.sessionStorage.getItem('userName'),
	token: window.sessionStorage.getItem('token'),
	...fileListManager,
	...home,
	...teams,
	...knowNet,
	...setter,
}

const mutations = {
	//将token保存到sessionStorage里，token表示登陆状态
	SET_TOKEN: (state, data) => {
		state.token = data
		window.sessionStorage.setItem('token', data)
	},
	//获取用户ID
	SET_USERID: (state, data) => {
		// 把用户ID存起来
		state.userId = data
		window.sessionStorage.setItem('userId', data)
	},
	//获取用户名
	SET_USERNAME: (state, data) => {
		// 把用户名存起来
		state.userName = data
		window.sessionStorage.setItem('userName', data)
	},
	//登出
	LOGOUT: (state) => {
		// 登出的时候要清除token
		state.token = null
		state.userId = null
		state.userName = null
		window.sessionStorage.removeItem('token')
		window.sessionStorage.removeItem('userId')
		window.sessionStorage.removeItem('userName')
	},
	...fileMutations,
	...homeMutations,
	...teamsMutations,
	...nodeMutations,
	...setterMutations,
}

const actions = {
}

export default new Vuex.Store({
	state: state,
	mutations: mutations,
	actions,
})
