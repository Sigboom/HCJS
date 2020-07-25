<template>
        <div id="footer">
            <ul class="footer-ul">
                <li class="footer-li-head"><a class="b-lnk" v-bind:href=logo.href>{{ logo.name }}</a></li>
                <li class="footer-li" v-for="blink in nav"><a class="b-lnk" v-bind:href="blink.href">{{ blink.name }}</a></li>
            </ul>      
        </div>
</template>

<script>
	export default {
		name: 'Header',
		data() {
			return {		
				logo: {name: 'Copyright©2019-2020', href: '#'},
				nav:[
					{name: 'Sig 文档整理', href: '#'},
					{name: 'Doni Daniel', href: 'http://sigboom.github.io'},
                    {name: '黑ICP备19005781号-1', href: 'http://beian.miit.gov.cn'}
                ]
			}
		}
	}
</script>

<style>
#footer { 
    display:block;
    font-size: 14px;

}

.footer-li-head {
    display: inline;
}

.footer-li {
    text-align:center;
    display:inline;
    padding: 0 12px;
    border-left: 1px solid #b6bac3;
    line-height: 1.1;
}

.b-lnk {
    color: #999;
    text-decoration: none;
}

.footer-ul {
    text-align:center;
}
</style>
