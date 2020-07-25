<template>
	<div class="showFilesCard row">
		<div id="fileCounter" class="fileCounterE col-md-12"></div>
	</div>
</template>

<script>

export default {
	name: 'showFiles',
	data() {
		return {
			msg: '暂无数据'
		}
	},
	methods: {
		drawCard() {
			var myChart = this.$echarts.init(document.getElementById('fileCounter'));
			var xdata = ["图片", "文档", "表格", "演示", "视频", "其他"];
			var data = [0, 0, 0, 0, 0, 0];
			for (let i = 0; i < this.$store.state.fileList.length; ++i) {	
				var type = this.$store.state.fileList[i].type;
				data[type - 1] += 1;
			}
			var option = {
				title: {
					text: '各类文档数目'
				},
				tooltip: {
					trigger: 'axis',
					axisPointer: {
						label: {
							backgroundColor: '#283b56'
						}
					}
				},
				legend: {
					data:['文档数量']
				},
				xAxis: {
					type: 'category',
					name: '类型',
					data: xdata,
					axisLabel: { interval:0 },
					axisPointer: { type: 'shadow' }
				},
				yAxis: {
					min:0,
					minInterval :1,
					type: 'value',
					name: '文件数量'
				},
				series: [{
					type: 'bar',
					data: data,
				}],
				grid:{ x:25, y:60, x2:40, y2:40 }
			};
			myChart.setOption(option);
		}
	},
	watch: {
		watchUpload(fileCounter) {
			let that = this;
			this.drawCard()
		}
	},
	computed: {
		watchUpload() {
			return this.$store.state.fileList.length;
		}
	},
	mounted() {
		let that = this;
		this.drawCard()
	}
}

</script>

<style>

.showFilesCard {
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
	.showFilesCard {
	}
}

/*
   CSS for PC
*/
@media(min-width: 768px) {
	.showFilesCard {
		min-width: 200px;
		min-height: 235px;
	}
}

.fileCounterE {
	height: 200px;
}

</style>
