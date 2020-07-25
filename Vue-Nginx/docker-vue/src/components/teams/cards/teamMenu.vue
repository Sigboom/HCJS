<template>
	<div class="teamList col-md-12">
		<h4 class="teamListHead col-md-12">团队列表</h4>
		<ul class="teamListEpoch navbar-nav col-md-12">
			<li class="teamListPot col-md-12">
				<span class="ownerTeamHead col-md-12">您创建的团队</span>
				<ul class="ownerTeam col-md-12">
					<li class="col-md-12" v-for="(team, index) in this.ownerTeam">
						<a role="button" @click="teamWork(index, team)" class="col-md-12">{{ team.name }}</a>
					</li>
				</ul>
			</li>
			<!--
			<li class="teamListPot col-md-12">
				<span class="ownerTeamHead col-md-12">您管理的团队</span>
				<ul class="ownerTeam col-md-12">
					<li class="col-md-12" v-for="(team, index) in this.managerTeam">
						<a role="button" @click="teamWork(index, team)" class="col-md-12">{{ team.name }}</a>
					</li>
				</ul>
			</li>
			-->
			<li class="teamListPot col-md-12">
				<span class="ownerTeamHead col-md-12">您加入的团队</span>
				<ul class="ownerTeam col-md-12">
					<li class="col-md-12" v-for="(team, index) in this.joinTeam">
						<a role="button" @click="teamWork(index, team)" class="col-md-12">{{ team.name }}</a>
					</li>
				</ul>
			</li>
		</ul>
	</div>
</template>

<script>
export default {
	name: 'teamMenu',
	data() {
		return {
			msg: "暂无数据",
			ownerTeam: [],
			managerTeam: [],
			joinTeam: [],
		}
	},
	methods: {
		teamWork(index, team) {
			this.$store.commit('setTeamBox', {
				teamId: team.id,
				teamName: team.name,
				teamOwner: team.owner,
			});
		},
		classifyTeam() {
			var teamList = this.$store.state.teamList;
			var userName = this.$store.state.userName;
			for(let i = 0; i < teamList.length; ++i) {
				if (teamList[i].owner == userName) {
					this.ownerTeam.push(teamList[i]);
			//	} else if (teamList[i].manager.includes(userName)) {
		//			this.managerTeam.push(teamList[i]);
				} else {
					this.joinTeam.push(teamList[i]);
				}
			}
		}
	},
	created() {
		let that = this;
		that.classifyTeam();
	}
}
</script>

<style>

.teamListEpoch {
	padding: 0;
}

</style>
