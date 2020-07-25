<template>
	<div class="friendInfo col-md-12">
		<div class="headPosition col-md-12">
			<div class="portrait col-md-12">
				<img class="headPic col-md-12" src="../../../../assets/default-head.jpg"  alt="用户头像" />
			</div>
		</div>
		<div class="friendMsg">
			<span class="col-md-3"></span>
			<a role="button" class="btn btn-primary col-md-6">编辑个人资料</a>
			<span class="col-md-3"></span>
			<span class="col-md-12">&nbsp;</span>
			<span class="label col-md-6">用户名&nbsp;</span>
			<p class="friendName col-md-6">{{ show.userName }}</p>
			<span class="label col-md-6">职业&nbsp;</span>
			<p class="friendName col-md-6">{{ show.note }}</p>
			<span class="label col-md-6">公开文档数&nbsp;</span>
			<p class="friendName col-md-6">{{ show.fileCounter }}</p>	
			<span class="label col-md-6">知识网络&nbsp;</span>
			<p class="friendName col-md-6">{{ show.knowNet }}</p>		
			<span class="label col-md-4">个人简介&nbsp;</span>
			<p class="friendName col-md-8">{{ show.state }}</p>		
		</div>
	</div>
</template>

<script>

export default {
	name: "friendCard",
	data() {
		return { 
			msg: "暂无信息",
			show: {
				'userName': this.$store.state.userName,
				'note': '学生',
				'fileCounter': this.$store.state.fileCounter,
				'knowNet': 5,
				'state': '喜欢思考新鲜事物'
			}
		}
	}
}

</script>

<style>

.friendInfo {
	height: 572px;
	background-color: #fff;
padding: 0;
}

.headPosition {
	padding: 30px 110px 30px;
}

.headPosition .portrait {
	margin: 0;
	padding: 0;
	height: 160px;	
	border: 2px solid #e6e6e6;
	border-radius: 50%;
	background-size: cover;
	overflow: hidden;
}

.headPic {
	padding: 0;
}

.friendMsg {
	font-size: 18px;
}

.label {
	padding: 0;
	padding-bottom: 10px;
	font-size: 85%;
	line-height: 1.643;
	color: gray;
	text-align: right;
}

.friendName {
	padding-bottom: 10px;
	margin: 0;
}

</style>
