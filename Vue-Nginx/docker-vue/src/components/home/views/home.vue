<template>
	<div class="homeView">
		<div class="workTable col-md-9">
			<div :class="view.class" v-for="view in views">
				<router-view :name="view.name"></router-view>
			</div>
		</div>
		<div class="msgList col-md-3">
			<router-view name="teamMsgList"></router-view>
			<router-view name="msgList"></router-view>
		</div>
    </div>
</template>

<script>
export default {
	name: 'homeView',
	data() {
		return {
			views: [
				{name: "upLoad", class: "col-sm-4"},
				{name: "fileList", class: "col-sm-3"},
				{name: "showFiles", class: "col-sm-5"},
				{name: "netRecommend", class: "col-sm-12"},
			]
		}
	},
	created() {
		let that = this;
		console.log('userMenuIndex', this.$store.state.userMenuIndex, '=> 0');
		that.$store.commit('setUserMenuIndex', 0);
	}

}
</script>

<style>

.homeView {	
	padding: 0;
}

.workTable {
	padding: 0;
}
</style>
