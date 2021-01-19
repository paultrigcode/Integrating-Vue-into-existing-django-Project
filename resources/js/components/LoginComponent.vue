<template>
<div class="container">
	<p id="demo"></p>
    <div class="row">
        <div class="col-md-offset-5 col-md-3">
            <div class="form-login">
            <h4>Welcome back...Do you want to <a class="btn btn-primary" href="/signup-view/" role="button">signup</a>?</h4>
            <input v-model="username" type="text" id="userName" class="form-control input-sm chat-input" placeholder="username" />
            </br>
            <input v-model="password" type="password" id="userPassword" class="form-control input-sm chat-input" placeholder="password" />
            </br>
            <div class="wrapper">
            <span class="group-btn">     
                <a href="#" @click='submit' class="btn btn-primary btn-md">login <i class="fa fa-sign-in"></i></a>
            </span>
            </div>
            </div>
              <a href="/oauth/login/github/" class="btn btn-block btn-social btn-github">
    				<span class="fa fa-github"></span> Sign in with Github
				</a>


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
	    			iziToast.success({
                        title: 'OK',
                        message: 'Successfully LoggedIn!',
                        position:'topCenter',
                        onClosed: function () {
                            window.location.href = '/'
                        }
                    });
	    		})
	    		.catch(function (error) {
				    if (error.response.status = 401) {
				      // Request made and server responded
				      document.getElementById("demo").innerHTML = error.response.data
				      console.log(error.response.data);
				      iziToast.error({
                        title: 'Error',
                        message: error.response.data,
                       	position:'topCenter',
                        onClosed: function () {
                            window.location.href = '/'
                        }
                    });		
				      console.log(error.response.status);
				      console.log(error.response.headers);
				    } else if (error.request) {
				      // The request was made but no response was received
				      console.log(error.request);
				    } else {
				      // Something happened in setting up the request that triggered an Error
				      console.log('Error', error.message);
				    }

  				});


		    }
	  }
	} 
</script>
