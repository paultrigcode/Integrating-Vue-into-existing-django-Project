<template>
	<form v-on:submit.prevent="submit" class="form-inline mt-2 mt-md-0">
            <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" v-model="testBody">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
</template>

<script> 
import axios from 'axios';
export default { 
    mounted() { 
        console.log('Component Search is here.') 
    },
    data(){
    	return{
    	 	testBody:'hello',
    	 	result:[]

    	}
    },
    methods: {
	    submit: function() {
        	console.log('Component Search is here. button click') 
        	axios.get(`/search/`, {
        		params:{
        			title:this.testBody
    			}
    		})
    		.then((response)=>{
    			this.result = response.data
		        this.$emit("tprop", this.result);

    		})

	        this.testBody = "";

	    }
  }
} 
</script>

<style>
</style>
