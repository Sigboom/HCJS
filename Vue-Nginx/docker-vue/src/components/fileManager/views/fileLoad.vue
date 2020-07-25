<template>
	<div id="fileLoadView" class="col-md-12">
		<div class="loadHead nav col-md-12">
			<div class="managerTabs col-md-12">
				<ul class="nav nav-tabs">
					<li role="presentation" v-for="(card, i) in cardList"
					:class="active[i]" class="">
						<a role="button" class="" @click="changeCard(i, showCard.id)">
							{{ card.liName }}
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
				name: "upload",
				id: 0,
				viewClass: {
					"viewClass": true,
					"col-sm-12": true
				}
			},
			cardList: [{
				name: "upload", liName: "上传",
			}, {
				name: "download", liName: "下载",
			}],
			active: [{
				active: true,
			}, {
				active: false,
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
		changeCard(cardTo, cardFrom) {
			this.showCard.name = this.cardList[cardTo].name;
			this.showCard.id = cardTo;
			this.active[cardFrom].active = false;
			this.active[cardTo].active = true;
		}
	},
	created() {
		let that = this;
		console.log(this.$store.state.userMenuIndex);
		that.$store.commit('setUserMenuIndex', 1);
	}
}
</script>

<style>

#fileLoadView {
	padding: 10px 0;
	background-color: #c2c2c2eb;
}

.loadHead {
	padding: 10px 0;
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

</style>
