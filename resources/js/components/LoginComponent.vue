<template>

<div class="container">
    <div class="row">
        <div class="col-md-offset-5 col-md-3">
            <div class="form-login">
            <h4>Welcome back.</h4>
            <input v-model="username" type="text" id="userName" class="form-control input-sm chat-input" placeholder="username" />
            </br>
            <input v-model="password" type="text" id="userPassword" class="form-control input-sm chat-input" placeholder="password" />
            </br>
            <div class="wrapper">
            <span class="group-btn">     
                <a href="#" @click='submit' class="btn btn-primary btn-md">login <i class="fa fa-sign-in"></i></a>
            </span>
            </div>
            </div>
        
        </div>
    </div>
</div>
</template>


<script>
	import axios from 'axios';
	export default { 
	    mounted() { 
	        console.log('Component Search is here.') 
	    },
	    data(){
	    	return{
	    	 	username:'',
	    	 	password:''

	    	}
	    },
	    methods: {
		    submit: function() {
	        	console.log('Component Search is here. button click') 
	        	axios.get(`/login/`, {
	        		params:{
	        			username:this.username,
	        			password:this.password
	    			}
	    		})
	    		.then((response)=>{
	    			console.log(response)
	    			if(response.status = 200){
                    	window.location.href = '/hello/'

	    			}

	    		})


		    }
	  }
	} 
</script>
