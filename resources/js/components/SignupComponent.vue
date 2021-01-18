<template>
	<div class="signup-form">
    <form v-on:submit.prevent="submit" method="post">
		<h2>Sign Up</h2>
		<p>Please fill in this form to create an account!</p>
		<hr>
        <div class="form-group">
			<div class="input-group">
				<div class="input-group-prepend">
					<span class="input-group-text">
						<span class="fa fa-user"></span>
					</span>                    
				</div>
				<input v-model=username type="text" class="form-control" name="username" placeholder="Username" required="required">
			</div>
        </div>
        <div class="form-group">
			<div class="input-group">
				<div class="input-group-prepend">
					<span class="input-group-text">
						<span class="fa fa-user"></span>
					</span>                    
				</div>
				<input v-model="first_name" type="text" class="form-control" name="first name" placeholder="First Name" required="required">
			</div>
        </div>
        <div class="form-group">
			<div class="input-group">
				<div class="input-group-prepend">
					<span class="input-group-text">
						<span class="fa fa-user"></span>
					</span>                    
				</div>
				<input v-model="last_name" type="text" class="form-control" name="last name" placeholder="Last Name" required="required">
			</div>
        </div>
        <div class="form-group">
			<div class="input-group">
				<div class="input-group-prepend">
					<span class="input-group-text">
						<i class="fa fa-paper-plane"></i>
					</span>                    
				</div>
				<input v-model="email" type="email" class="form-control" name="email" placeholder="Email Address" required="required">
			</div>
        </div>
		<div class="form-group">
			<div class="input-group">
				<div class="input-group-prepend">
					<span class="input-group-text">
						<i class="fa fa-lock"></i>
					</span>                    
				</div>
				<input v-model="password" type="password" class="form-control" name="password" placeholder="Password" required="required">
			</div>
        </div>
		<div class="form-group">
			<div class="input-group">
				<div class="input-group-prepend">
					<span class="input-group-text">
						<i class="fa fa-lock"></i>
						<i class="fa fa-check"></i>
					</span>                    
				</div>
				<input type="password" v-model="password2" class="form-control" name="confirm_password" placeholder="Confirm Password" required="required">
			</div>
        </div>
        <div class="form-group">
			<label class="form-check-label"><input type="checkbox" required="required"> I accept the <a href="#">Terms of Use</a> &amp; <a href="#">Privacy Policy</a></label>
		</div>
		<div class="form-group">
            <button type="submit" class="btn btn-primary btn-lg">Sign Up</button>
        </div>
    </form>
	<div class="text-center">Already have an account? <a class="btn btn-primary" href="/login-view/">Login here</a></div>
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
	    	 	first_name:'',
	    	 	last_name:'',
	    	 	email:'',
	    	 	password2:'',
	    	 	password:''

	    	}
	    },
	    methods: {
		    submit: function() {
	        	console.log('Component Search is here. button click') 
	        	axios.get(`/signup/`, {
	        		params:{
	        			username:this.username,
			    	 	first_name:this.first_name,
			    	 	last_name:this.last_name,
			    	 	email:this.email,
			    	 	password2:this.password2,
			    	 	password:this.password
	    			}
	    		})
	    		.then((response)=>{
	    			console.log(response)
	    			iziToast.success({
                        title: 'OK',
                        message: 'Successfully SignedUp!',
                        position:'topCenter',
                        onClosed: function () {
                            window.location.href = '/login-view/'
                        }
                    });
	    		})
	    		.catch(function (error) {
				    if (error.response.status = 500) {
				      // Request made and server responded
				      iziToast.error({
                        title: 'error',
                        message: error.response.data,
                        position:'topCenter',
                        onClosed: function () {
                            window.location.href = '/signup-view/'
                        }
                    });
				      console.log(error.response.data);
				      console.log(error.response.status);
				      console.log(error.response.headers);
				    }
				    else if (error.response.status = 500) {
				      // Request made and server responded
				      iziToast.error({
                        title: 'error',
                        message: error.response.data,
                        position:'topCenter',
                        onClosed: function () {
                            window.location.href = '/signup-view/'
                        }
                    });
			      	}
			      	else if (error.response.status = 409) {
				      // Request made and server responded
				      iziToast.error({
                        title: 'error',
                        message: error.response.data,
                        position:'topCenter',
                        onClosed: function () {
                            window.location.href = '/signup-view/'
                        }
                    });
			      	}
			      	else if (error.response.status = 401) {
				      // Request made and server responded
				      iziToast.error({
                        title: 'error',
                        message: error.response.data,
                        position:'topCenter',
                        onClosed: function () {
                            window.location.href = '/signup-view/'
                        }
                    });
			      	}
				    else if (error.request) {
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


<style scoped>
body {
	color: #fff;
	background: #19aa8d;
	font-family: 'Roboto', sans-serif;
}
.form-control {
	font-size: 15px;
}
.form-control, .form-control:focus, .input-group-text {
	border-color: #e1e1e1;
}
.form-control, .btn {        
	border-radius: 3px;
}
.signup-form {
	width: 400px;
	margin: 0 auto;
	padding: 30px 0;		
}
.signup-form form {
	color: #999;
	border-radius: 3px;
	margin-bottom: 15px;
	background: #fff;
	box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
	padding: 30px;
}
.signup-form h2 {
	color: #333;
	font-weight: bold;
	margin-top: 0;
}
.signup-form hr {
	margin: 0 -30px 20px;
}
.signup-form .form-group {
	margin-bottom: 20px;
}
.signup-form label {
	font-weight: normal;
	font-size: 15px;
}
.signup-form .form-control {
	min-height: 38px;
	box-shadow: none !important;
}	
.signup-form .input-group-addon {
	max-width: 42px;
	text-align: center;
}	
.signup-form .btn, .signup-form .btn:active {        
	font-size: 16px;
	font-weight: bold;
	background: #19aa8d !important;
	border: none;
	min-width: 140px;
}
.signup-form .btn:hover, .signup-form .btn:focus {
	background: #179b81 !important;
}
.signup-form a {
	color: #fff;	
	text-decoration: underline;
}
.signup-form a:hover {
	text-decoration: none;
}
.signup-form form a {
	color: #19aa8d;
	text-decoration: none;
}	
.signup-form form a:hover {
	text-decoration: underline;
}
.signup-form .fa {
	font-size: 21px;
}
.signup-form .fa-paper-plane {
	font-size: 18px;
}
.signup-form .fa-check {
	color: #fff;
	left: 17px;
	top: 18px;
	font-size: 7px;
	position: absolute;
}
</style>