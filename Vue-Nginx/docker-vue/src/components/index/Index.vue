<template>
	<div id="index" class="col-md-12">
		<router-view name="views"></router-view>
    </div>
</template>

<script>
export default {
	name: 'Index',
}
</script>

<style>
#index {
	background: #dddddd url(../../assets/background.jpeg) no-repeat fixed center;
	background-size: cover;
	padding: 0;
}
</style>
