<template>
	<div class="friendsMenu col-md-12">
		<div class="menuHeadTabs col-md-12">
			<ul class="nav nav-tabs">
				<li role="presentation" v-for="(follow, i) in followMenu"
				class="menuTab col-md-6" :class="active[i]">
					<a role="button" @click="change(i)">{{ follow.nameCN }}</a>
				</li>
			</ul>
		</div>
		<router-view :name="showMenu.name"></router-view>
		<div class="followMenuBtn btn-group col-md-12" role="group">
			<router-link class="btn btn-default col-md-6" :to="showMenu.followTo">{{ showMenu.btnCN }}</router-link>
			<router-link class="btn btn-default col-md-6" to="/home/friends/setter">设置</router-link>
		</div>
	</div>
</template>

<script>
export default {
	name: 'friendsMenu',
	data() {
		return {
			showMenu: {
				'name': "follower",
				'followTo': "/home/friends/find",
				'btnCN': "查找好友",
			},
			followMenu: [{
				'name': "follower", 'nameCN': "关注列表",
				'btnCN': "查找好友",
				'followTo': "/home/friends/find",
			}, {
				'name': "following", 'nameCN': "粉丝列表",
				'btnCN': "管理粉丝",
				'followTo': "/home/friends/find",
			}],
			active: [{
				active: true,
			}, {
				active: false,
			}],
			idx: 0,
		};
	},
	methods: {
		change(id) {
			this.showMenu = this.followMenu[id];
			this.active[this.idx].active = false;
			this.active[id].active = true;
			this.idx = id;
		}
	}
}
</script>

<style>
.friendsMenu {
	padding: 0;	
}

.menuHeadTabs, .menuTab {
	padding: 0;
}

.menuTab>a {
	text-align: center;
}
</style>
