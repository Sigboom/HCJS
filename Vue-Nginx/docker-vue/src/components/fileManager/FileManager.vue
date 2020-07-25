<template>
	<div id="fileManager" class="col-md-12">
		<div class="blankTop col-md-12"></div>
		<nav class="menu col-md-2">
			<router-view name="menu"></router-view>
		</nav>
		<nav class="views col-md-10">
			<router-view name="views"></router-view>
		</nav>
    </div>
</template>

<script>
export default {
	name: 'FileManager',
}
</script>

<style>
#fileManager {
	padding: 0;
	background-image: url("../../assets/defaultHome.jpg"); 
}

.blankTop {
	height: 60px;
}

/* for phone CSS */
@media(max-width: 767px) {
	.menu {
	}
}

/* for PC CSS */
@media(min-width: 768px) {
	.menu {
		height: 572px;
		margin: 0;
		padding: 0;
		background-color: #c2c2c2eb;
	}
}

.views {
	margin: 0;
	padding: 0;
}
</style>
