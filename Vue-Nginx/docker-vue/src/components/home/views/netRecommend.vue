<template>
	<div class="netRecommendView row">
		<div class="col-md-8">
			<div :class="view.class" v-for="view in views">
				<router-view :name="view.name"></router-view>
			</div>
		</div>
		<div class="msgList col-md-4">
			<router-view name="recommend"></router-view>
		</div>
    </div>
</template>

<script>
export default {
	name: 'homeView',
	data() {
		return {
			views: [
				{name: "knowNet", class: "col-sm-12"},
				{name: "dynamic", class: "col-sm-12"},
			]
		}
	},
}
</script>

<style>
.netRecommend {
	padding: 0;
}
</style>
