<template>
	<div id="teamMaker">
		<div class="teamHead col-md-12">
			<h2>新建/加入团队</h2>
			<hr/>
		</div>
		<div class="teamContainer col-md-5">
			<form class="teamFormer col-md-12 row" methods="POST">
				<h4>团队名称</h4>
				<p class="warning" v-if="teamNameCheckList.iEmpty">团队名不能为空</p>
				<p class="warning" v-else-if="teamNameCheckList.iIllegal">团队名不能包含特殊符号</p>
				<p class="warning" v-else-if="teamNameCheckList.iLength">团队名长度不超过20个字符</p>
				<p class="warning" v-else-if="teamNameCheckList.iUnique">团队名已存在</p>
				<p class="success" v-else-if="teamNameCheckList.iSuccess">该团队名可用</p>
				<p class="blank" v-else>&nbsp;</p>
				<input type="text" class="teamNameInput col-md-12" :class="teamNameCheckList"
				placeholder="新团队名称" autocomplete="off" v-model="teamName"
				@blur.prevent="teamNameCheck" @input="teamNameIllegalCheck"></input>
				<br/><hr/>
				<h4>团队成员</h4>
				<div class="teamMember col-md-2">
					<div class="teamMemberHead col-md-12">
						<img class="headPic col-md-12" src="../../../assets/default-head.jpg"  alt="用户头像" />
					</div>	
					<p class="teamMemberName col-md-12">{{ this.$store.state.userName }}</p>
				</div>
				<div class="teamMember col-md-2" v-for="teamer in teamMembers">
					<div class="teamMemberHead col-md-12">
						<img class="headPic col-md-12" src="../../../assets/default-head.jpg"  alt="用户头像" />
					</div>	
					<p class="teamMemberName col-md-12">{{ teamer.name }}</p>
				</div>
				<div class="teamMember col-md-2" v-for="teamer in askMembers">
					<div class="teamMemberHead col-md-12">
						<img class="headPic col-md-12" src="../../../assets/default-head.jpg"  alt="用户头像" />
					</div>	
					<p class="teamMemberName col-md-12">{{ teamer.name }}</p>
				</div>
				<div class="col-md-12">
					<a role="button" class="btn btn-default col-md-3" @click="$router.back(-1)">返回</a>
					<span class="col-md-2"></span>
					<a role="button" class="btn btn-primary col-md-7" @click="buildTeam">创建团队</a>
				</div>
			</form>
		</div>	
		<div class="followList col-md-3">
			<div class="menuHeadTabs col-md-12">
				<ul class="nav nav-tabs">
					<li role="presentation" v-for="(follow, i) in followMenu"
					class="menuTab col-md-6" :class="follow.class">
						<a role="button" @click="change(i)">{{ follow.nameCN }}</a>
					</li>
				</ul>
			</div>
			<ul class="col-md-12 followersList" v-if="idx==0">
				<li class="col-md-12" v-if="this.$store.state.followerCounter == 0">
					<p class="emptyfollowers col-md-12">关注列表空空如也</p>
				</li>
				<li v-for="(follow, index) in followerInTeam" :key="index" class="followerLi col-md-12">
					<div class="followerListPot col-xs-12" role="button">
						<div class="btnRoom col-md-3">
						<a role="button" class="btn btn-default col-md-12"
						@click="addUser(follow, index)" v-show="!follow.inTeam">
							<span class="glyphicon glyphicon-plus" aria-hidden="true"></span>&nbsp;邀请
						</a>
						<a role="button" class="btn btn-danger col-md-12"
						@click="moveUser(follow, index)" v-show="follow.inTeam">
							<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>&nbsp;删除
						</a>
						</div>
						<div class="followerHeadRoom col-md-4">
							<span class="followerHead col-md-12">
							<img class="followerHeadPic col-md-12" src="../../../assets/default-head.jpg"  alt="用户头像" />
						</span>
						</div>
						<span class="followInfo col-md-5">
							<p class="col-md-12">{{ follow.name }}</p>
						</span>
					</div>
				</li>
			</ul>
			<ul class="col-md-12 followingsList" v-if="idx==1">
				<li class="col-md-12" v-if="followingCounter == 0">
					<p class="emptyfollowers col-md-12">粉丝列表空空如也</p>
				</li>
				<li v-for="(follow, index) in followingInTeam" :key="index" class="followingLi col-md-12">
					<div class="followerListPot col-xs-12" role="button">
						<div class="btnRoom col-md-3">
						<a role="button" class="btn btn-default col-md-12"
						@click="addUser(follow, index)" v-show="!follow.inTeam">
							<span class="glyphicon glyphicon-plus" aria-hidden="true"></span>&nbsp;添加
						</a>
						<a role="button" class="btn btn-danger col-md-12"
						@click="moveUser(follow, index)" v-show="follow.inTeam">
							<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>&nbsp;删除
						</a>
						</div>
						<div class="followerHeadRoom col-md-4">
							<span class="followerHead col-md-12">
							<img class="followerHeadPic col-md-12" src="../../../assets/default-head.jpg"  alt="用户头像" />
						</span>
						</div>
						<span class="followInfo col-md-5">
							<p class="col-md-12">{{ follow.name }}</p>
						</span>
					</div>
				</li>
			</ul>
		</div>
		<div class="teamsList col-md-4">
			<h4>推荐团队列表</h4>
			<hr/>
			<ul class="col-md-12 teamsBox">
				<li class="col-md-12" v-if="followTeamList.length == 0">暂时无推荐</li>
				<li class="col-md-12 teamBox" v-for="(team, index) in followTeamList">
					<div class="teamPot col-md-12">
						<span class="col-md-5">
							<a role="button" class="btn btn-default" @click="askJoin(team, index)"
							:disabled="team.disabled">{{ team.info }}</a>
						</span>
						<span class="col-md-7">{{ team.name }}</span>
					</div>
				</li>
			</ul>
		</div>
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: 'teamworkerView',
	data() {
		return {
			followingCounter: 6,
			msg: "暂无数据",
			showMenu: {
				'name': "following"
			},
			teamList: [{
				name: "样例团队",
			}],
			followTeamList: [{
				name: "一起嗨皮",
				info: "申请加入",
			}, {
				name: "测试事业部",
				info: "申请加入",
			}],
			followMenu: [{
				'name': "follower", 'nameCN': "关注列表",
				'class': {
					active: false
				}
			}, {
				'name': "following", 'nameCN': "粉丝列表",
				'class': {
					active: true
				}
			}],
			teamNameCheckList: {
				iBase: true,
				iEmpty: false,
				iError: false,
				iLength: false,
				iUnique: false,
				iIllegal: false,
				iSuccess: false
			},
			teamName: "",
			followerInTeam: [ 
			],
			followingInTeam: [],
			teamMembers: [],
			askMembers: [],
			csrfToken: "",
			idx: 1,
		}
	},
	methods: {
		askJoin(team, index) {
			if (this.followTeamList[index].disabled) return ;
			let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
			this.csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
			var formData = new window.FormData();
			formData.append('userId', this.$store.state.userID);
			formData.append('teamId', team.id);

			this.$axios.post('/askJoinTeam', formData, {
				headers: {
					'X-Requested-With':'XMLHttpRequest',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-CSRFToken': this.csrfToken,
				}
			}).then(res => {
				if (res.data.status == "OK") {	
					this.followTeamList[index].disabled = true;
					this.followTeamList[index].info = "已申请";
				} else {
					console.log("申请失败");
				}
			}).catch(err => {
				console.log(err);
			});
		},
		teamNameCheck() {
			return this.teamNameUniqueCheck();
		},
		teamNameUniqueCheck() {
			if (!this.teamNameIllegalCheck()) return false;
			this.$axios.get('/checkTeamName', {
				params: { 
					userId: this.$store.state.userId,
					teamName: this.teamName,
				}
			}).then(res => {
				switch (res.data.status) {
					case "OK!":
						this.teamNameCheckList.iUnique = false;
						this.teamNameCheckList.iSuccess = true;
						break;
					case "Wrong!":
						this.teamNameCheckList.iSuccess = false;
						this.teamNameCheckList.iUnique = true;
					case "EmptyWrong":	
					default:
						return false;
				}
			}).catch(err => {
				console.log(err);
			});
			return true;
		},
		teamNameIllegalCheck() {	
			if (!this.teamNameEmptyCheck()) return false;
			var teamName = this.teamName;
			var regex=/^[A-Za-z0-9_\u4e00-\u9fa5]+$/g;
			if (!regex.test(teamName)) {
				this.teamNameCheckList.iSuccess = false;
				this.teamNameCheckList.iUnique = false;
				this.teamNameCheckList.iIllegal = true;
				return false;
			} else {
				this.teamNameCheckList.iIllegal = false;
			}
			var regex_length=/^[A-Za-z0-9_\u4e00-\u9fa5]{1,20}$/g;
			if (!regex_length.test(teamName)) {
				this.teamNameCheckList.iSuccess = false;
				this.teamNameCheckList.iLength = true;
				return false;
			} else {
				this.teamNameCheckList.iLength = false;
			}
			return true;
		},
		teamNameEmptyCheck() {
			var teamName = this.teamName;
			if (teamName == "") {
				this.teamNameCheckList.iSuccess = false;
				this.teamNameCheckList.iUnique = false;
				this.teamNameCheckList.iEmpty = true;
				return false;
			} else {
				this.teamNameCheckList.iEmpty = false;
			}
			return true;
		},
		checkFalse() {
			return !this.teamNameCheck();
		},
		buildTeam() {	
			event.preventDefault();
			if (this.checkFalse()) return false;
			let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
			this.csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
			
			var formData = new window.FormData();
			formData.append('userId', this.$store.state.userId);
			formData.append('teamName', this.teamName);
			for (let i = 0; i < this.teamMembers.length; i++) {
				formData.append('teamMembers', this.teamMembers[i]['id']);	
			}
			for (let i = 0; i < this.askMembers.length; i++) {
				formData.append('askMembers', this.askMembers[i]['id']);	
			}

			this.$axios.post('/buildTeam', formData, {
				headers: {
					'X-Requested-With':'XMLHttpRequest',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-CSRFToken': this.csrfToken,
				}
			}).then(res => {
				this.$router.push('/teams');
				console.log(res.data);
			}).catch(err => {
				console.log(err);
			});
		},
		change(id) {
			this.followMenu[this.idx].class.active = false;
			this.followMenu[id].class.active = true;
			this.idx = id;
		},
		askUser(user, index) {	
			console.log(user);
			this.followerInTeam.splice(index, 1, {
				...this.followerInTeam[index],
				'inTeam': true,
			});	
			this.askMembers.push(user);
			console.log("ask OK");
		},
		moveAskUser(user, index) {
			console.log(user);
			this.followerInTeam.splice(index, 1, {
				...this.followerInTeam[index],
				'inTeam': false,
			});	
			this.askMembers.splice(this.askMembers.indexOf(user), 1);
			console.log("move OK");
		},
		addUser(user, index) {
			console.log(user);
			this.followingInTeam.splice(index, 1, {
				...this.followingInTeam[index],
				'inTeam': true,
			});	
			this.teamMembers.push(user);
			console.log("add OK");
		},
		moveUser(user, index) {
			console.log(user);
			this.followingInTeam.splice(index, 1, {
				...this.followingInTeam[index],
				'inTeam': false,
			});	
			this.teamMembers.splice(this.teamMembers.indexOf(user), 1);
			console.log("move OK");
		},
		initFollowerTeam(followList) {
			var canInTeam = [];
			for (let i = 0; i < followList.length; ++i) {
				canInTeam.push({
					...followList[i],
					'inTeam': false,
				});	
			}
			this.followerInTeam = canInTeam;
		},
		initFollowingTeam(followList) {
			var canInTeam = [];
			for (let i = 0; i < followList.length; ++i) {
				canInTeam.push({
					...followList[i],
					'inTeam': false,
				});
			}
			this.followingInTeam = canInTeam;
		},
		getFollowList() {
			if (this.$store.state.userId) {
				this.$axios.get('/getFollower', {
					params: { userId: this.$store.state.userId }
				}).then(res => {
					let followerList = res.data.followerList;
					this.$store.commit('setFollowerList', followerList);
					this.initFollowerTeam(followerList);
					console.log('关注者列表已更新');
				}).catch(err => {
					console.log(err);
				});
				this.$axios.get('/getFollowing', {
					params: { userId: this.$store.state.userId }
				}).then(res => {
					let followingList = res.data.followingList;
					this.$store.commit('setFollowingList', followingList);
					this.initFollowingTeam(followingList);
					console.log(followingList);
					console.log('粉丝列表已更新');
				}).catch(err => {
					console.log(err);
				});
			}
		},
		initFollowTeamList(teamList) {
			for (let i = 0; i < teamList.length; ++i) {
				teamList.splice(i, 1, {
					...teamList[i],
					'info': "申请加入",
					'disabled': false,
				});
			}
			this.followTeamList = teamList;
		},
		getFollowTeamList() {
			if (this.$store.state.userId) {
				this.$axios.get('/getFollowTeamList', {
					params: { userId: this.$store.state.userId }
				}).then(res => {
					let followTeamList = res.data.followTeamList;
					this.followTeamList = followTeamList
					this.$store.commit('setFollowTeamList', followTeamList);

					this.initFollowTeamList(followTeamList);
					console.log(followTeamList)
					console.log('推荐团队列表已更新');
				}).catch(err => {
					console.log(err);
				});
			}
		}
	},
	mounted() {
		let that = this;
		that.getFollowList();
		that.getFollowTeamList();
	}
}
</script>

<style>
.followerHeadRoom {
	padding: 0;
}

.followerHead {
	padding: 0;
}

.btnRoom>.btn {
	padding-left: 4px;
}

.btnRoom {
	padding: 0;
	padding-top: 15px;
	padding-left: 5px;
}

.followerListPot {
	padding-top: 10px;
	background-color: #c7c7c7;
	border: 1px solid #565656;
}

.followerHeadRoom>.followerHead {
	margin-left: 10px;
	height: 80px;
	border-radius: 50%;
	border: 1px solid #565656;
	overflow: hidden;
}

.followerHeadPic {
	padding: 0;
}

.followInfo>p {
	color: #fff;
	font-size: 20px;
	margin-top: 20px;
	margin-left: 10px;
}

.followerMsg {
	padding: 0;
}

#teamMaker {
	padding: 0;
}

.followInfo {
	padding: 0px;
}

.teamHead {
	background-color: #fff;
}

.teamContainer {
	height: 538px;
	background-color: #fff;
}

.teamFormer {
	padding: 0 80px;
}

.teamFormer>.warning {
	color: red;
}

.teamFormer>.success {
	color: green;
}

.teamFormer>.warning, .teamFormer>.success,
.teamFormer>.blank {
	margin: 4px;
	font-size: 12px;
}

.iBase {
	height: 35px;
	border-radius: 15px;
	border-width: 2px;
	border-color: #bbbbbb;
}

.iEmpty, .iError, .iIllegal, .iLength, .iUnique {
	border-color: red;
}

.iSuccess {
	border-color: green;
}

.teamNameInput {
	padding: 6px 12px;
}

.teamMember {
	padding: 20px 0;
}

.teamMemberHead {
	padding: 0;
	height: 47px;
    border: 2px solid #e6e6e6;
    border-radius: 50%;
    background-size: cover;
    overflow: hidden;
}

.teamMemberName {
	padding: 0;
	text-align: center;
}

.followList {
padding: 0;
	height: 538px;
	background-color: #fff;	
	overflow: auto;
}

.friend {
	margin-bottom: 10px;
}

.friendToTeam {
	padding: 0;
	line-height: 70px;
}

.friendMemberName {
	margin: 0;
	text-align: center;
	font-size: 18px;
	line-height: 70px;
}

.friendMemberHead {	
	padding: 0;
	height: 70px;
    border: 2px solid #e6e6e6;
    border-radius: 50%;
    background-size: cover;
    overflow: hidden;
}

.checkBlankTop {
	height: 42px;
}

.followerLi, .followingLi {
padding: 0;
}

.addDelBtn {
	padding: 24px 0;
}
.menuTab {
	padding: 0px;
}
.teamPot {
	padding: 10px;
}

.teamsBox>.teamBox {
	background-color: #c7c7c7;
	border: 1px solid #565656;
}

.teamsBox {
	padding: 0;
}

</style>
