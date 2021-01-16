<template>
	<form v-on:submit.prevent="submit" class="form-inline mt-2 mt-md-0">
            <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" v-model="testBody">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
</template>

<script> 
export default { 
    mounted() { 
        console.log('Component Search is here.') 
    },
    data(){
    	return{
    	 	testBody:'hello'

    	}
    },
    methods: {
	    submit: function() {
        	console.log('Component Search is here. button click') 
	        this.$emit("tprop", this.testBody);
	        this.testBody = "";

	    }
  }
} 
</script>

<style>
</style>
