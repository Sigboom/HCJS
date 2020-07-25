<template>
	<div class="recommend row">
		<h5 class="askMsgTitle">每日推荐</h5>
		<hr>
		<!--
		<p class="showPot col-sm-12" v-show="askMsgList.length ==  0">{{ this.msg }}</p>
		-->
		<img :src="showPic"  style="width:100%; height:130px">
		<center><h3 class="col-md-12">{{ showTitle }}</h3></center>
		</div>
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: 'recommend',
	data() {
		return {
			msg: "暂时没有新消息",
			showPic:"./static/img/tuijianPic.jpeg",
			showTitle: "不如\"重启\"自己"
		}
	},
	methods: {
	}
}
</script>

<style>

.recommend {
	margin: 10px 0;
	padding: 10px;
	background-color: #fff;
	border: 1px solid #e6e6e6;
	border-radius: 10px;
}

.recommendTitle {
	padding-left: 10px;
	font-size: 14px;
}

/*
	CSS for Phone
*/
@media(max-width: 767px) {
	.recommend {
	}
}

/*
   CSS for PC
*/
@media(min-width: 768px) {
	.recommend {
		min-height: 300px;
	}
}

.fileShow {
	width: 100%;
}

.fileNameShow {
	display: inline-block;
}

.fileMenu {
	text-align: center;
}

.fileDelete {
	margin: 0 auto;
}

.fileDownload {	
	margin: 0 auto;
}

</style>
