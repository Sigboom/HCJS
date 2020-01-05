<template>
  <div>
    this is the news page.the transform param is {{userId}}
    {{ name }}
  </div>
</template>
<script>
export default {
    props: ['userId'],
    data() {
        return {
            name: this.$route.params.userId
        }
    }
}

</script>
