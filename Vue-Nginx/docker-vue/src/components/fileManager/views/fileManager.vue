<template>
	<div id="fileManagerView">
		<div class="filesHead nav">
			<div class="managerTabs col-sm-12 col-xs-12">
				<ul class="nav nav-tabs">
					<li role="presentation" v-for="(card, i) in cardList" :class="card.active" class="">
						<a role="button" class="" @click="changeCard(i, showCard.id)">{{ card.liName }}</a>
					</li>
				</ul>
			</div>
			<div class="btn-group col-sm-2 col-xs-6" role="group">
				<button type="button" class="btn btn-default col-sm-4 col-xs-4">
					<span class="glyphicon glyphicon-arrow-left" aria-hidden="true"></span>
				</button>
				<button type="button" class="btn btn-default col-sm-4 col-xs-4">
					<span class="glyphicon glyphicon-arrow-right" aria-hidden="true"></span>
				</button>
				<button type="button" @click="outsideDir"
				class="btn btn-default col-sm-4 col-xs-4">
					<span class="glyphicon glyphicon-arrow-up" aria-hidden="true"></span>
				</button>
			</div>
			<div class="col-md-6 col-xs-12">
				<ol class="filePath breadcrumb col-sm-12 col-xs-12">
					<li v-for="(path, id) in this.$store.state.dirPath">
						<a href="#">{{ path }}</a>
					</li>
				</ol>
			</div>
			<div class="btn-group mkdir col-md-1" role="group">
				<a role="button" class="btn btn-default col-sm-12 dropdown-toggle" data-toggle="dropdown"
				aria-haspopup="true" aria-expanded="false">
					<span class="glyphicon glyphicon-plus dropdown" aria-hidden="true"></span>
				</a>
				<ul class="dropdown-menu">
					<li class="col-md-12 mkdirLi">
						<a role="button" class="btn btn-default filterButton" @click="mkdir">创建文件夹</a>
					</li>
				</ul>
			</div>
			<div class="btn-group filter col-md-1" role="group">
				<a role="button" class="btn btn-default col-sm-12 dropdown-toggle" data-toggle="dropdown"
				aria-haspopup="true" aria-expanded="false">
					<span class="glyphicon glyphicon-filter dropdown" aria-hidden="true"></span>
				</a>
				<ul class="dropdown-menu">
				<!--
					<li class="col-md-12"><p class="col-md-12">排序</p></li>
					<li class="col-md-12 filterLi"><a role="button" class="btn btn-default filterButton">名称</a></li>
					<li class="col-md-12 filterLi"><a role="button" class="btn btn-default filterButton">大小</a></li>
					<li class="col-md-12 filterLi"><a role="button" class="btn btn-default filterButton">上传时间</a></li>
					<li role="separator" class="divider col-md-12"></li>
				-->
					<li class="col-md-12"><p class="col-md-12">文件类型</p></li>
					<li class="col-md-6 filterLi">
						<a role="button" class="btn filterbutton" :class="pictureClass" @click="filterChange(1)">
							<span class="glyphicon glyphicon-inbox" aria-hidden="true"></span>&nbsp;图片
						</a>	
					</li>
					<li class="col-md-6 filterLi">
						<a role="button" class="btn filterbutton" :class="textClass" @click="filterChange(2)">
							<span class="glyphicon glyphicon-inbox" aria-hidden="true"></span>&nbsp;文档
						</a>	
					</li>
					<li class="col-md-6 filterLi">
						<a role="button" class="btn filterButton" :class="sheetClass" @click="filterChange(3)">
							<span class="glyphicon glyphicon-th" aria-hidden="true"></span>&nbsp;表格
						</a>	
					</li>
					<li class="col-md-6 filterLi">
						<a role="button" class="btn filterButton" :class="forShowClass" @click="filterChange(4)">
							<span class="glyphicon glyphicon-blackboard" aria-hidden="true"></span>&nbsp;演示
						</a>	
					</li>
					<li class="col-md-6 filterLi">
						<a role="button" class="btn filterButton" :class="videoClass" @click="filterChange(5)">
							<span class="glyphicon glyphicon-facetime-video" aria-hidden="true"></span>&nbsp;视频
						</a>
					</li>
					<li class="col-md-6 filterLi">
						<a role="button" class="btn filterButton" :class="unknowClass" @click="filterChange(6)">
							<span class="glyphicon glyphicon-question-sign" aria-hidden="true"></span>&nbsp;其他
						</a>
					</li>
				</ul>
			</div>
		</div>
		<div :class="showCard.viewClass">
			<router-view :name="showCard.name"></router-view>
		</div>
	</div>
</template>

<script>
export default {
	name: 'fileManagerView',
	data() {
		return {
			msg: "暂无数据",
			showCard: { 
				name: "cloudFiles",
				basePath: "云文档",
				id: 0,
				viewClass: {
					"viewClass": true,
					"col-sm-12": true
				}
			},
			cardList: [{
				name: "cloudFiles", liName: "云文档",
					  active: { "active": true }
			}, {
				name: "starFiles", liName: "星标",
					  active: { "active": false }	
			}, {
				name: "shareFiles", liName: "共享",
					  active: { "active": false }	
			}],
			textClass: "btn-default",
			sheetClass: "btn-default",
			forShowClass: "btn-default",
			pictureClass: "btn-default",
			videoClass: "btn-default",
			unknowClass: "btn-default",
		}
	},
	methods: {
		outsideDir() {
			this.$store.commit('OUTSIDE_DIR');
		},
		mkdir() {
			var	params = {
				userId: this.$store.state.userId,
				dirId: this.$store.state.nowDir.slice(-1)[0],
			};
			axios.get('/getMkdir', { params: params }).then(res => {
				if (res.data.status == 'OK') {
					this.$store.commit('ADD_MKDIR');
				} else {
					console.log(res.data);
				}
			}).catch(err => {
				console.log(err);
			});
		},
		filterChange(rules) {
			let addCmd = ""
			switch(rules) {
				case 2: 
					if (this.textClass == "btn-info") {
						this.textClass = "btn-default"
						addCmd = "D";
					} else {
						this.textClass = "btn-info"	
					}
					break;
				case 3: 
					if (this.sheetClass == "btn-info") {
						this.sheetClass = "btn-default"
						addCmd = "D";
					} else {
						this.sheetClass = "btn-info"	
					}
					break;
				case 4: 
					if (this.forShowClass == "btn-info") {
						this.forShowClass = "btn-default"
						addCmd = "D";
					} else {
						this.forShowClass = "btn-info"	
					}
					break;
				case 1: 
					if (this.pictureClass == "btn-info") {
						this.pictureClass = "btn-default"
						addCmd = "D";
					} else {
						this.pictureClass = "btn-info"	
					}
					break;
				case 5: 
					if (this.videoClass == "btn-info") {
						this.videoClass = "btn-default"
						addCmd = "D";
					} else {
						this.videoClass = "btn-info"	
					}
					break;
				default: 
					if (this.unknowClass == "btn-info") {
						this.unknowClass = "btn-default"
						addCmd = "D";
					} else {
						this.unknowClass = "btn-info"	
					}
			}
			if (addCmd == "D") {
				rules *= -1;
			}
			if (!this.$store.state.filterStat) {
				this.$store.commit('SET_FILTERSTAT', true);
			}

			if (addCmd == "D") {
				if (this.textClass != "btn-info" && this.sheetClass != "btn-info"
					&& this.forShowClass != "btn-info" && this.pictureClass != "btn-info"
					&& this.videoClass != "btn-info" && this.unknowClass != "btn-info") {
					rules = "";
					this.$store.commit('SET_FILTERSTAT', false);
				}
			}
			console.log("set_filter", rules);
			this.$store.commit('SET_FILTER', rules);	
		},
		changeCard(cardTo, cardFrom) {
			this.showCard.name = this.cardList[cardTo].name;
			this.showCard.id = cardTo;
			this.$store.commit('CHANGE_CARD', this.cardList[cardTo].liName);
			this.cardList[cardFrom].active.active = false;
			this.cardList[cardTo].active.active = true;
		}
	},
	created() {
		let that = this;
		console.log(this.$store.state.userMenuIndex);
		that.$store.commit('setUserMenuIndex', 1);
		that.addPath = [];
	}
}
</script>

<style>

#fileManagerView {
	padding: 20px 0;
	background-color: #c2c2c2eb;
}

.filesHead {
	padding-bottom: 10px;
}

.managerTabs {
	margin-bottom: 10px;
}

.nav-tabs>li>a {
	font-size: 16px;
}

.viewClass {
	background-color: #fff;
}

.mkdir {
	padding-right: 0;
}

.mkdirLi {
	padding: 0 1px;	
}

.filter {
	padding-left: 0;
}

.filterLi {
	padding: 3px;
}

.filterButton {
padding: 3px 0;
}

.filePath {
	margin-bottom: 0;
	border: 1px solid #c2c2c2eb;
}

</style>
