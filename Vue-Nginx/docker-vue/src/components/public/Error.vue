<template>
	<div class="ErrorPage col-md-12">
		<div class="blankTop col-md-12"></div>
		<h1 class="notFound col-md-12">走丢了吗？这里有一些路标:</h1>
		<router-link class="lost-link col-md-12" to="/index">返回首页</router-link>
	</div>
</template>

<script>
	export default {
		name: 'Error',
	}
</script>

<style>

@media(min-width: 768px) {
	.ErrorPage {
		height: 600px;
	}
}

.blankTop {
	height: 60px;
}

.notFound {
	padding: 50px 0;
}

.lost-link {
	font-size: 18px;
	color: black;
	text-decoration: none;
}
</style>
