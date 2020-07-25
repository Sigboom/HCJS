<template>
	<div id="teamsView">
		<div class="teamBody col-md-12" v-if="!this.$store.state.teamCounter">
			<div class="col-md-8">
				<h2>您未加入或创建任何团队</h2>
				<router-link class="btn btn-primary col-md-12" to="/teams/maker">立即创建团队</router-link>
			</div>
			<div class="friendTeamList col-md-4">
				<h3>好友团队列表</h3>	
			</div>
		</div>
		<div class="teamBody col-md-12" v-else>
			<div class="teamMenu col-md-2">
				<router-view name="teamMenu"></router-view>
			</div>
			<div class="teamBox col-md-10">
				<div class="teamHead col-md-12">
					<a role="button" class="teamHeadText" @click="backToInit">团队主页</a>
				<hr/>
				</div>
				<router-view :name="this.$store.state.teamBoxState"></router-view>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'teamsView',
	data() {
		return {
			msg: "暂无数据",
		}
	},
	methods: {
		backToInit() {
			this.$store.commit('setInitBox');
		},
		getTeamList() {
			if (this.$store.state.userId) {
				this.$axios.get('/getTeamList', {
					params: { userId: this.$store.state.userId }
				}).then(res => {
					var teamList = res.data.teamList;
					this.$store.commit('setTeamList', teamList);
					console.log(this.$store.state.teamList);
				}).catch(err => {
					console.log(err);
				});
			} else {
				console.log('非法访问');
				alert('非法访问');
				this.$axios.push('/index');
			}
		},
		teamWork(index, team) {
		
		}
	},
	created() {
		let that = this;
		that.getTeamList();
	}
}
</script>

<style>

#teamsView {
	padding: 0;
}

.teamHead {
	padding-top: 20px;
}

.teamHeadText {
	color: black;
	font-size: 20px;
}

.teamHeadText:hover {
	text-decoration: none; 
}

.teamBody {
padding: 0;
	background-color: #fff;
}

.friendTeamList {	
	height: 538px;
	background-color: #fff;
}

.teamMenu {
	padding: 0;
}

.teamBox {
	padding: 0;
}

.teamMsg {
	height: 400px;
	background-color: #fff;
}

.teamList {
	height: 500px;
	overflow: auto;
	padding: 0;
}

.teamListHead {
	margin: 0;
	padding: 15px;
	font-weight: 550;
	background-color: #c2c2c2c2;
}

.teamListPot {
	padding: 0;
}

.ownerTeamHead {
	padding: 0;
	background-color: #e3e3e3e3;
	text-align: center;
	font-size: 16px;
	font-weight: 550;
}

.ownerTeam {
padding: 0;
	background-color: #e3e3e375;	
	font-size: 15px;
}

.teamBaseMsg {
	height: 200px;
}

.teamActiveMsg {
	height: 200px;
}
</style>

