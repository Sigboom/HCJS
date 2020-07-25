<template>
	<div class="friendsView col-md-12">
		<div class="infoBox col-md-4">
			<router-view name="friendInfo"></router-view>
		</div>
		<div class="talkBox col-md-8">
			<router-view :name="this.$store.state.talkBoxState"></router-view>
		</div>
    </div>
</template>

<script>
export default {
	name: 'homeView',
	data() {
		return {
			friendCard: {
				name: "张三", id: 123
			},
			talkCard: {
				name: "李四", id: 456
			},
		}
	},
	created() {
		let that = this;
		that.$store.commit('setHeaderIndex', 1);
	}
}
</script>

<style>

.friendsView {	
padding: 0;
}

.infoBox {
	padding: 0;
}

.talkBox {
	padding: 0;
}
</style>
