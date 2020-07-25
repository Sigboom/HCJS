<template>
	<div class="friendFinder">
		<div class="findHeader col-md-12">
			<h3>查找用户</h3>
		<hr/>
		</div>
		<form class="findForm col-md-12">
			<input type="text" class="findInput col-md-8" placeholder="用户名/邮箱/用户id"
			v-model="userInfo" autocomplete="off"></input>
			<a role="button" class="btn btn-default col-md-4" @click="findUser">查找</a>
		</form>
		<div class="findSelf col-md-12" v-show="findBlank">
			<p>请输入查找信息后再点击查找</p>
		</div>
		<div class="findSelf col-md-12" v-show="findSelf">
			<p>这只能查到你自己{{ userInfo }}</p>
		</div>
		<div class="col-md-12" v-if="finded">
			<div class="emptyFind col-md-12" v-show="emptyFind">
				<p>未查找到关于"{{ userInfo }}"的相关信息</p>
			</div>
			<div v-for="user in findUserList" v-show="!emptyFind">
				<div class="headPosition col-md-12">
					<div class="portrait col-md-12">
						<img class="headPic col-md-12" src="../../../../assets/default-head.jpg"  alt="用户头像" />
					</div>
				</div>
				<div class="friendMsg col-md-12">
					<span class="label col-md-6">用户名&nbsp;</span>
					<p class="friendName col-md-6">{{ user.name }}</p>
					<span class="label col-md-6">公开文档数&nbsp;</span>
					<p class="friendName col-md-6">0</p>	
					<span class="label col-md-6">知识网络&nbsp;</span>
					<p class="friendName col-md-6">0</p>		
				</div>
				<div class="col-md-12 btn-group">
					<router-link class="btn btn-default col-md-6" :to="'/other/' + user.name">访问主页</router-link>
					<a role="button" class="btn btn-primary col-md-6" @click="addFollower(user.id)" v-if="!added">加关注</a>	
					<a role="button" class="btn btn-primary col-md-6"  disabled="added" v-else>已关注</a>	
				</div>
			</div>
		</div>
	</div>
</template>

<script>

export default {
	name: "friendFinderCard",
	data() {
		return { 
			msg: "暂无信息",
			finded: false,
			emptyFind: false,
			findSelf:false,
			findBlank:false,
			userInfo: "",
			findUserList: [],
			added: false,
		}
	},
	methods: {
		addFollower(id) {
			this.$axios.get('/getAddFollower', {
				params: {
					userId: this.$store.state.userId,
					friendId: id,
				}
			}).then(res => {
				if (res.data.state == "OK") {
					this.added = true;
					this.$store.commit('addFollowerCounter');
					console.log('发送申请成功');
				} else {
					console.log('发送申请失败');
				}
			}).catch(err => {
				console.log(err);
			});
		},
		checkSelf() {
			this.findSelf = false;
			this.findBlank = false;
			if (this.userInfo == '') this.findBlank = true;
			if (this.userInfo == this.$store.state.userName ||
				this.userInfo == this.$store.state.userId + "" ||
				this.userInfo == this.$store.state.userEmail) {
				this.findSelf = true;
			}
			return this.findBlank || this.findSelf;
		},
		findUser() {
			this.finded = false;
			this.emptyFind = false;

			if (this.checkSelf()) return ;
			if (this.$store.state.userId) {
				axios.get('/getFindUser', {
					params: {
						userId: this.$store.state.userId,
						findUser: this.userInfo,
					}
				}).then(res => {
					if (res.data.state == "OK") {
						this.finded = true;
						this.findUserList = res.data.userList;
						if (this.findUserList.length) {
							this.added = false;
							for (let i = 0; i < this.$store.state.followerCounter; i++) {
								if (this.findUserList[0].id == this.$store.state.followerList[i].id) {
									this.added = true;
									break;
								}
							}
							console.log(this.$store.state.followerList)
							console.log(this.added);
							console.log('查找成功');
						} else { 
							this.emptyFind = true;
							console.log('未查找到');
						}
					} else {
						// ERROR
						console.log(err);
					}
				}).catch(err => {
					console.log(err);
				});
			} else {
				console.log('非法访问!')
			}
		}
	}
}

</script>

<style>

.friendFinder {
	height: 572px;
	background-color: #fff;
}

.findHeader {
	text-align: center;
}

.findInput {
	line-height: 28px;
}

.emptyFind, .findSelf {
	padding: 30px;
	text-align: center;
}

.headPosition {
	padding: 30px 93px 30px;
}

.headPosition .portrait {
	margin: 0;
	padding: 0;
	height: 160px;	
	border: 2px solid #e6e6e6;
	border-radius: 50%;
	background-size: cover;
	overflow: hidden;
}

.headPic {
	padding: 0;
}

.friendMsg {
	font-size: 18px;
}

.label {
	padding: 0;
	padding-bottom: 10px;
	font-size: 85%;
	line-height: 1.643;
	color: gray;
	text-align: right;
}

.friendName {
	padding-bottom: 10px;
	margin: 0;
}

</style>

