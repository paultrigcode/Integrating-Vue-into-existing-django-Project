<template>
<div class="container register">
                <div class="row">
                    <div class="col-md-3 register-left">
                        <img src="https://image.ibb.co/n7oTvU/logo_white.png" alt=""/>
                        <h3>Welcome</h3>
                        <p>You are 30 seconds away from registering a new customer</p>
                    </div>
                    <div class="col-md-9 register-right">
                            
                            <div class="tab-pane fade show" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                                <h3  class="register-heading">Register a New Customer</h3>
                                <div class="row register-form">
                                    <div class="col-md-6">
                                        <div class="form-group">
                                            <input type="text" required="required" v-model="first_name" class="form-control" placeholder="First Name *" value="" />
                                        </div>
                                        <div class="form-group">
                                            <input type="text" required="required" v-model="last_name" class="form-control" placeholder="Last Name *" value="" />
                                        </div>
                                        <div class="form-group">
                                            <input type="tel" required="required" v-model="phone_number" maxlength="10" minlength="10" class="form-control" placeholder="Phone number *" value="" />
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="form-group">
                                            <input type="text" required="required" v-model="street" class="form-control" placeholder="street *" value="" />
                                        </div>
                                        <div class="form-group">
                                            <input type="number" required="required" v-model="house_number" class="form-control" placeholder="House no *" value="" />
                                        </div>
                                        <input type="submit" @click="submit" class="btnRegister"  value="Register"/>
                                    </div>
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
                street:'',
                first_name:'',
                last_name:'',
                phone_number:'',
                house_number:'',


            }
        },
        methods: {
            submit: function() {
                console.log('Component Search is here. button click') 
                axios.get(`/recycler/create/`, {
                    params:{
                        street:this.street,
                        first_name:this.first_name,
                        last_name:this.last_name,
                        phone_number:this.phone_number,
                        house_number:this.house_number,
                        }
                    })
                .then((response)=>{
                    console.log(response)
                    if (response.status ==200){
                        console.log(response)
                        iziToast.success({
                            title: 'OK',
                            message: 'Successfully Registered Customer! Your Customer Number is : '+response.data,
                            position:'topCenter',
                            timeout: 1000000,

                        });
                    }

                })
                .catch(function (error) {
                    if (error.response.status = 409) {
                      // Request made and server responded
                      console.log(error.response.data);
                      iziToast.error({
                        title: 'Error',
                        message: error.response.data,
                        position:'topCenter',
                    });     
                      console.log(error.response.status);
                      console.log(error.response.headers);
                    }
                    else if (error.response.status = 409) {
                      // Request made and server responded
                      iziToast.error({
                        title: 'error',
                        message: error.response.data,
                        position:'topCenter',
                        
                    });
                    }
                    else if (error.response.status = 500) {
                      // Request made and server responded
                      iziToast.error({
                        title: 'error',
                        message: error.response.data,
                        position:'topCenter',
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

<style>
.register{
    background: -webkit-linear-gradient(left, #3931af, #00c6ff);
    margin-top: 3%;
    padding: 3%;
}
.register-left{
    text-align: center;
    color: #fff;
    margin-top: 4%;
}
.register-left input{
    border: none;
    border-radius: 1.5rem;
    padding: 2%;
    width: 60%;
    background: #f8f9fa;
    font-weight: bold;
    color: #383d41;
    margin-top: 30%;
    margin-bottom: 3%;
    cursor: pointer;
}
.register-right{
    background: #f8f9fa;
    border-top-left-radius: 10% 50%;
    border-bottom-left-radius: 10% 50%;
}
.register-left img{
    margin-top: 15%;
    margin-bottom: 5%;
    width: 25%;
    -webkit-animation: mover 2s infinite  alternate;
    animation: mover 1s infinite  alternate;
}
@-webkit-keyframes mover {
    0% { transform: translateY(0); }
    100% { transform: translateY(-20px); }
}
@keyframes mover {
    0% { transform: translateY(0); }
    100% { transform: translateY(-20px); }
}
.register-left p{
    font-weight: lighter;
    padding: 12%;
    margin-top: -9%;
}
.register .register-form{
    padding: 10%;
    margin-top: 10%;
}
.btnRegister{
    float: right;
    margin-top: 10%;
    border: none;
    border-radius: 1.5rem;
    padding: 2%;
    background: #0062cc;
    color: #fff;
    font-weight: 600;
    width: 50%;
    cursor: pointer;
}
.register .nav-tabs{
    margin-top: 3%;
    border: none;
    background: #0062cc;
    border-radius: 1.5rem;
    width: 28%;
    float: right;
}
.register .nav-tabs .nav-link{
    padding: 2%;
    height: 34px;
    font-weight: 600;
    color: #fff;
    border-top-right-radius: 1.5rem;
    border-bottom-right-radius: 1.5rem;
}
.register .nav-tabs .nav-link:hover{
    border: none;
}
.register .nav-tabs .nav-link.active{
    width: 100px;
    color: #0062cc;
    border: 2px solid #0062cc;
    border-top-left-radius: 1.5rem;
    border-bottom-left-radius: 1.5rem;
}
.register-heading{
    text-align: center;
    margin-top: 8%;
    margin-bottom: -15%;
    color: #495057;
}
</style>