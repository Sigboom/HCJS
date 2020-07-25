<template>
	<div class="sig">
		<router-view name="header"></router-view>
		<router-view name="main"></router-view>
		<router-view name="footer"></router-view>
	</div>
</template>

<script>


export default {
	name: 'App'
}
</script>

<style>
* {
	margin: 0;
}

input, button {
	outline: none
}

</style>
