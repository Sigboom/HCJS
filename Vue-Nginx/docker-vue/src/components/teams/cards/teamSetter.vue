<template>
	<div class="teamSetter col-md-12">
		<div class="base col-md-12" v-show="this.$store.state.teamOwner == this.$store.state.userName">
			<h4>基本设置</h4>
			<div class="col-md-12">
				<label class="col-md-12" for="teamRename">团队名称</label>
				<input type="text" id="teamRename" class="renameInput col-md-3"
				:placeholder="this.$store.state.teamName" :disabled="renameDisabled"></input>
				<a class="btn" :class="renameBtn" role="button" @click="rename">{{ renameBtnInfo }}</a>
			</div>
		</div>
		<!-- <div class="permission col-md-12">
			<h4>团队成员</h4>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>lala
				</a>
				<span class="col-md-1"></span>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>lala
				</a>
				<span class="col-md-1"></span>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>lala
				</a>
				<span class="col-md-1"></span>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>lala
				</a>
		</div>
		-->
		<div class="teamMsgSetter col-md-12">
			<h4>消息设置</h4>
				<p>当前设定为: 接收消息并提醒</p>
				<a class="btn btn-success col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>接收消息并提醒
				</a>
				<span class="col-md-1"></span>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>接收消息不提醒
				</a>
				<span class="col-md-1"></span>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>收入团队盒不提醒
				</a>
				<span class="col-md-1"></span>
				<a class="btn btn-default col-md-2" role="button">
					<span class="glyphicon glyphicon-th" aria-hidden="true"></span>不接收消息
				</a>
		</div>
		<div class="base col-md-12" v-show="this.$store.state.teamOwner == this.$store.state.userName">
			<div class="dangerZone col-md-12">
				<h4>危险区</h4>
				<ul class="chooseGroup col-md-8">
					<li class="chooseBox col-md-12">
						<span class="setterMsg col-md-9">
							<label class="col-md-12">转让这个团队</label>
							<p class="col-md-12">转让团队后，团队将不再属于您</p>
						</span>
						<span class="setterBtnGroup col-md-3">
							<a role="button" class="btn btn-warning">转让团队</a>
						</span>
					</li>
					<li class="chooseBox col-md-12">
						<div class="sureDelete col-md-12" v-if="makeSure">
							<span class="sureInfo col-md-6">
								<label class="col-md-12">您确定要删除这个团队吗?</label>
								<p class="col-md-12">请输入"{{ this.$store.state.teamName }}"进行确认</p>
							</span>
							<span class="col-md-6">
								<input type="text" class="checkName col-md-12" v-model="checkTeam"
								@input="checkDelete"></input>
								<a role="button" class="btn btn-danger col-md-9"
								:disabled="deleteDisabled" @click="deleteTeam">我了解后果, 删除团队</a>
								<a role="button" class="btn btn-default col-md-3" @click="notMakeSure">返回</a>
							</span>
						</div>
						<div class="deleteBox col-md-12" v-else>
							<span class="setterMsg col-md-9">
								<label class="col-md-12">删除这个团队</label>
								<p class="col-md-12">删除团队后，团队将不再存在，无法恢复</p>
							</span>
							<span class="setterBtnGroup col-md-3">
								<a role="button" class="btn btn-danger" @click="makeSureBtn">删除团队</a>
							</span>
						</div>
					</li>
				</ul>
			</div>
		</div>
		<div class="base col-md-12" v-show="this.$store.state.teamOwner != this.$store.state.userName">
			<div class="dangerZone col-md-12">
				<h4>危险区</h4>
				<ul class="chooseGroup col-md-8">
					<li class="chooseBox col-md-12">
						<div class="sureDelete col-md-12" v-if="makeSure">
							<span class="sureInfo col-md-6">
								<label class="col-md-12">您确定要退出这个团队吗?</label>
								<p class="col-md-12">请输入"{{ this.$store.state.teamName }}"进行确认</p>
							</span>
							<span class="col-md-6">
								<input type="text" class="checkName col-md-12" v-model="checkTeam"
								@input="checkDelete"></input>
								<a role="button" class="btn btn-danger col-md-9"
								:disabled="deleteDisabled" @click="deleteTeam">我了解后果, 退出团队</a>
								<a role="button" class="btn btn-default col-md-3" @click="notMakeSure">返回</a>
							</span>
						</div>
						<div class="deleteBox col-md-12" v-else>
							<span class="setterMsg col-md-9">
								<label class="col-md-12">退出这个团队</label>
								<p class="col-md-12">退出团队后，团队将不再存在于团队列表</p>
							</span>
							<span class="setterBtnGroup col-md-3">
								<a role="button" class="btn btn-danger" @click="makeSureBtn">退出团队</a>
							</span>
						</div>
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>

<script>

export default {
	name: 'teamSetter',
	data() {
		return {
			msg: "暂无信息",
			renameDisabled: true,
			renameBtnInfo: "重命名",
			renameBtn: "btn-default",
			makeSure: false,
			deleteDisabled: true,
			checkTeam: "",
		}
	},
	methods: {
		rename() {
			let state = !this.renameDisabled
			this.renameDisabled = state;
			this.renameBtnInfo = state ? "重命名" : "保存";
			this.renameBtn = state ? "btn-default" : "btn-primary";
		},
		notMakeSure() {
			this.makeSure = false;	
		},
		makeSureBtn() {
			this.makeSure = true;	
		},
		checkDelete() {
			if (this.checkTeam == this.$store.state.teamName) {
				this.deleteDisabled = false;
				return true;
			}
			this.deleteDisabled = true;
			return false;
		},
		deleteTeam() {
			if (!this.checkDelete()) return ;
			let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
			this.csrfToken =  document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
			var formData = new window.FormData();
			formData.append('userId', this.$store.state.userID);
			formData.append('teamId', this.$store.state.teamId);

			this.$axios.post('/deleteTeam', formData, {
				headers: {
					'X-Requested-With':'XMLHttpRequest',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-CSRFToken': this.csrfToken,
				}
			}).then(res => {
				if (res.data.status == "OK") {	
					console.log("删除成功");
				} else {
					console.log("删除失败");
				}
			}).catch(err => {
				console.log(err);
			});

		}
	},
	created() {
	}
}
</script>

<style>

.teamSetter {
	padding: 0;
}

.renameInput {
	height: 34px;
	font-size: 14px;
	line-height: 1.42857;
	color: #555;
	border: 1px solid #ccc;
	border-radius: 4px;
	box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
}

.dangerZone>.chooseGroup {
	border: 1px solid red;
	border-radius: 8px;
	padding: 10px;
}

.chooseBox {
	padding: 10px;
}

.chooseBox+.chooseBox {
	border-top: 1px solid #cecece; 
}

.deleteBox {
	padding: 0;
	padding-top: 9px;
}

.sureDelete>.sureInfo {
	padding: 0;
	padding-top: 5px;
}

.checkName {
	height: 30px;
	font-size: 14px;
	line-height: 1.49;
	border: 1px solid #ccc;
	border-radius: 4px;
}

.permission, .base, .teamMsgSetter {
	padding: 10px;
}

</style>
