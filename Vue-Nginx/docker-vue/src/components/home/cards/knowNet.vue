<template>
	<div class="knowNet row">
		<p class="knowNetTitle col-md-12">
			网络节点<!-- <a role="button" class="btn btn-primary mkPot">新建节点</a> -->
		</p>
		<p class="showPot col-sm-12" v-show="this.$store.state.fileCounter == 0">{{ this.msg }}</p>
		<div class="potShow col-md-12">
		<div class="netPotBox col-sm-6" v-for="(pot, i) in this.$store.state.nodeList">
			<a role="button" class="btn btn-default fileNameShow col-xs-12" @click="askNode(i)"> {{ pot.name }}</a>
		</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'knowNet',
	data() {
		return {
			msg: "未生成节点列表",
		}
	},
	methods: {
		askNode(index) {
			console.log(index);
		},
		getNodeList() {	
			this.$axios.get('/getNodeList', {
				params: { userId: this.$store.state.userId }
			}).then(res => {
				var nodeList = res.data.nodeList;
				this.$store.commit('SET_NODELIST', nodeList);	
				console.log("获取节点成功");
			}).catch(err => {
				console.log(err);
			});
		}
	},
	watch: {
		watchUpload(fileCounter) {
			let that = this;
			that.getNodeList();
		}
	},
	computed: {
		watchUpload() {
			return this.$store.state.fileCounter;
		}
	},
	created() {
		let that = this;
		that.getNodeList();
	}
}
</script>

<style>

.knowNet {
	margin: 10px 0;
	padding: 10px;
	background-color: #fff;
	border: 1px solid #e6e6e6;
	border-radius: 10px;
}

/*
	CSS for Phone
*/
@media(max-width: 767px) {
	.knowNet {
	}
}

/*
   CSS for PC
*/
@media(min-width: 768px) {
	.knowNet {
		min-width: 200px;
		min-height: 90px;
	}
}

.fileShow {
	width: 100%;
}

.fileNameShow {
	display: inline-block;
	max-width: 100%;
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}

.mkPot {
	float: right;
}

.fileMenu {
	text-align: center;
}

.fileDelete {
	margin: 0 auto;
	width: 45%;
}

.potShow {
	height: 120px;
	overflow: auto;
}
.netPotBox {
	padding: 0;
}
</style>
