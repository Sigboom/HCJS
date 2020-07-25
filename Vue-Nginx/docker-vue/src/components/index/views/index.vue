<template>
	<div class="indexView">
		<div class="blankTop col-md-12"></div>
        <div class="title col-md-6">
            <h1>{{ title }}<br></h1><h2>{{ subtitle }}</h2>
        </div>
		<div class="sign col-md-6">
			<div class="col-md-3"></div>
			<transition name="flip" mode="out-in">
				<router-view name="sign"></router-view>
			</transition>
			<div class="col-md-3"></div>
		</div>
        <div class="describe col-sm-12">
            <div class="inner col-sm-12">
                <span class="inner-point col-md-4" v-for="point in desmap">
                    <h2>{{ point.header }}</h2>
                    <h4>{{ point.des }}</h4>
                </span>
            </div>
		</div>
	</div>
</template>

<script>
const indexView = {
	name: "indexView",
	data() {
		return  {
			msg: "暂无信息",
            title: "Sig文档整理",
            subtitle: "尝试最轻松的文档整理方式",
			desmap: [
				{ header: "智能方便", des: "显示自己的文档的情况，提供消息通知功能，及时查看属于自己的文件" },
				{ header: "快速高效", des: "及时整理自己的文档，生成个性化整理文件存储方案！即刻整理自己的文件" },
				{ header: "个人合作", des: "快速了解个人知识结构，及时掌握社会核心竞争力" }
			]
		}
	}
}

export default indexView
</script>

<style>
.indexView {
	
}

.h1, h1 {
	font-size: 42px;
	margin-top: 0;
}

/* CSS for Phone */

@media (max-width: 767px){
	.title {
		padding-top: 80px;
	}
}

/* CSS for PC */

@media (min-width: 768px) {
	.title {
		padding-top: 8%;
		padding-left: 12%;
	}
}

.sign {
	padding: 10px 0; 
}

.blankTop {
	height: 60px; 
}

.flip-enter, .flip-leave-to {
	transform: scaleX(0)
}

flip-leave, .flip-enter-to {
	transform: scaleX(1)
}

.flip-enter-active {
  transition: all .2s;
}

.flip-leave-active {
  transition: all .5s;
}

.title-h {
	margin-left: 100px;
	display: inline-block;
	margin-block-start: 0em;
	margin-block-end: 0em;
	padding-bottom: 20px;
	font-size: 3em;
}

.inner {
    margin:0 auto;
}

.inner-point {
    text-align: center;
    display: inline-block;
    vertical-align: top;
    box-sizing: border-box;
    padding: 1% 4%;
}

.inner-point h2{
    margin:5px 0;
}

.describe {
	background: #fff;
}
</style>
