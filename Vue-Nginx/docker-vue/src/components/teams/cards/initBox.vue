<template>
	<div class="teamManager col-md-12">
		<div class="teamBaseMsg col-md-9">
			<div class="baseMsg col-md-4">
				团队总数: {{ this.$store.state.teamCounter }}
			</div>
			<div class="baseMsg col-md-4">
				文档总数:
			</div>
			<div class="baseMsg col-md-4">
				成员总数:
			</div>
			<div class="activeMsg col-md-4">
				活跃用户数:
			</div>
			<div class="activeMsg col-md-4">
				文档复用比:
			</div>
			<div class="activeMsg col-md-4">
				团队贡献比:
			</div>
		</div>

		<div class="teamMsg col-md-3">
			<h3>暂无信息</h3>
		</div>
	</div>
</template>

<script>

export default {
	name: 'teamInitBox',
}
</script>
