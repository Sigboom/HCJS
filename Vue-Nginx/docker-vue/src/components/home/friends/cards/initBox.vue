<template>
	<div class="initBox">
		<div class="showBox col-md-12">
			<span class="envelopeBg glyphicon glyphicon-envelope col-md-12"  aria-hidden="true"></span>
			<span class="sendBg glyphicon glyphicon-send col-md-12"  aria-hidden="true"></span>
		</div>
		<div class="textBox col-md-12">
			<h3>分享自己的世界</h3>
			<h5>分享让世界更精彩</h5>
		</div>
	</div>
</template>

<script>

export default {
	name: "talkBox",
	data() {
		return {
			msg: "暂无信息",
		}
	}
}

</script>

<style>

.initBox {
	height: 572px;
	background-color: #b3b3b4;
}

.initBox>.showBox {
	color: #3a8bd8ba;
}

.envelopeBg {	
	opacity: 0.4;
	padding: 150px 290px 0px; 
	font-size: 100px;
}

.sendBg {
	opacity: 0.8;
	padding-left: 300px; 
	top: -75px;
	font-size: 140px;
}

.textBox {
	text-align: center;
}

</style>
