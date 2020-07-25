<template>
	<div id="knowNetView" class="col-md-12">
		<h3>个人知识网络</h3>
		<hr />
		<div class="col-md-9">
			<div id="myChart" class="baseNet col-md-12"></div>
		</div>
		<div class="col-md-3">
			<div class="nodeState col-md-12">
				<div class="col-md-12">
					{{ nodeMsg }}
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'knowNet',
	data() {
		return {
			nodeMsg: "暂无数据"
		}
	},
	methods: {
		drawNet() {
			let myChart = this.$echarts.init(document.getElementById('myChart'));
			//获取数据
			/*
			this.$axios.get('/getNetJson', {
				params: {
					userId: this.$store.state.userID
				}
			}).then(res => {
				if (res.data.status == "OK") {
					myChart.setOption(res.data.knowNet);
				} else {
					console.log(res.data);
				}
			}).catch(err => {
				console.log(err);
			});
			*/
			var categories = [];
			for (var i = 0; i < 2; i++) {
				categories[i] = {
					name: (i + 1) + '级分类'
				};
			}
			let option = {
				title: {
					text: '知识网络图'
				},
				// 提示框的配置
				tooltip: {
					formatter: function (x) { return x.data.des; }
				},
				toolbox: {
					// 显示工具箱
					show: true,
					feature: {
						mark: { show: true },
						// 还原
						restore: { show: true },
						// 保存为图片
						saveAsImage: { show: true }
					}
				},
				legend: [{
					// selectedMode: 'single',
					data: categories.map(function (a) { return a.name; })
				}],
				series: [{
					type: 'graph', // 类型:关系图
					layout: 'force', //图的布局，类型为力导图
					symbolSize: 40, // 调整节点的大小
					//roam: true, // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移,可以设置成 'scale' 或者 'move'。设置成 true 为都开启
					edgeSymbol: ['circle', 'arrow'],
					edgeSymbolSize: [2, 10],
					edgeLabel: {
						normal: {
							textStyle: { fontSize: 20 }
						}
					},
					force: {
						repulsion: 2500,
						edgeLength: [10, 50]
					},
					draggable: true,
					lineStyle: {
						normal: {
							width: 2,
							color: '#4b565b',
						}
					},
					edgeLabel: {
						normal: {
							show: true,
							formatter: function (x) { return x.data.name; }
						}
					},
					label: {
						normal: {
							show: true,
							textStyle: {}
						}
					},
					// 数据
					data: [{
						name: '代码',
						des: '文件数9',
						symbolSize: 90,
						category: 0,
					}, {
						name: 'python',
						des: '文件数3',
						symbolSize: 50,
						category: 1,
					}, {
						name: 'C/C++',
						des: '文件数1',
						symbolSize: 20,
						category: 1,
					}, {
						name: 'shell',
						des: '文件数2',
						symbolSize: 40,
						category: 1,
					}, {
						name: 'html',
						des: '文件数3',
						symbolSize: 50,
						category: 1,
					}],
					links: [{
						source: '代码',
						target: 'python',
						//name: 'link01',
						des: 'link01des'
					}, {
						source: '代码',
						target: 'C/C++',
						//name: 'link02',
						des: 'link02des'
					}, {
						source: '代码',
						target: 'shell',
		                //name: 'link03',
		                des: 'link03des'
		            }, {
		                source: '代码',
		                target: 'html',
		                //name: 'link04',
		                des: 'link05des'
		            }],
		            categories: categories,
		        }]
		    };
			myChart.setOption(option);
		}
	},
	mounted() {
		let that = this;
		that.drawNet();
	}
}
</script>

<style>

#knowNetView {
}

.baseNet {
	width:800px;
	height:500px
}

.nodeState {
	background-color: #ddd;
    border: 1px solid #c2c2c2eb;
    overflow: auto;
    border-radius: 4px;
}
</style>
