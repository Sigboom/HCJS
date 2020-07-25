<template>
	<div id="home" class="col-md-12">
		<div class="blankTop col-md-12"></div>
		<nav class="menu col-sm-2">
			<router-view name="menu"></router-view>
		</nav>
		<nav class="views col-sm-10">
			<router-view name="views"></router-view>
		</nav>
	</div>
</template>

<script>
export default {
	name: 'Home',
	data() {
		return {		
		}
	},
}
</script>

<style>

#home {	
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
	}
}

.menu {
	margin: 0;
	padding: 0;
	background-color: #c2c2c2eb;
}

.views {
	margin: 0;
	padding: 0;
}
</style>
