<template>
	<div class="dynamic row">
		<p class="dynamicTitle">最新动态</p>
		<p class="showPot col-sm-12" v-show="askMsgList.length ==  0">{{ this.msg }}</p>
		<div class="fileShow col-sm-12" v-for="(message, index) in askMsgList">
			<a role="button" @click="askMenu(index)" class="btn btn-default dynamicShow col-md-12">
			<p class="dySender col-md-6">{{ message.sender}}{{ message.message }}</p>
			<p class="col-md-6">{{ message.time }}</p>
			<div class="dyDetail col-md-12">{{ message.detail }}</div>
			<a role="button" class="fullText col-md-12">显示全文</a>
		</a>
		<div class="fileMenu col-md-12" v-show="menu[index].show">
				<span v-if="message.category == 'reply'">
					<span class="col-md-6"></span>
					<a role="button" class="btn btn-primary col-md-6" @click="replyAsk(index, message)">知道了</a>
				</span>
				<span v-else>
					<a role="button" class="btn btn-default col-md-6" @click="refuseAsk(index, message)">拒绝</a>
					<a role="button" class="btn btn-primary col-md-6" @click="agreeAsk(index, message)">同意</a>
				</span>
			</div>
		</div>
	</div>
</template>

<script>
import qs from 'qs'

export default {
	name: 'askMsgList',
	data() {
		return {
			msg: "暂时没有新消息",
			askMsgList: [{
				message: "更新了 数学 网络节点",
				sender: "烧饼",
				time: "2020年5月10日",
				detail: "解二元一次方程可将方程组中一个方程的某..."
			}],
			menu:[{
				'show': false
			}],
			csrfToken: "",
		}
	},
}
</script>

<style>

.dynamic {
	margin: 10px 0;
	padding: 10px;
	background-color: #fff;
	border: 1px solid #e6e6e6;
	border-radius: 10px;
}

.dynamicTitle {
	padding-left: 10px;
	font-size: 14px;
}

/*
	CSS for Phone
*/
@media(max-width: 767px) {
	.dynamic {
	}
}

/*
   CSS for PC
*/
@media(min-width: 768px) {
	.dynamic {
		min-height: 360px;
	}
}

.fileShow {
	width: 100%;
}

.dynamicShow {
	height: 90px;
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

.fullText {
	text-align: left;
}

.dyDetail {
width: 30px;
	word-wrap:break-word;
	word-break: break-all;
}

</style>
