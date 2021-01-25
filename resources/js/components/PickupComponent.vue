<template>
<div class="container">
    <div class="row clearfix">
    	 <div class="search-box">
            <i class="material-icons">&#xE8B6;</i>
            <input v-on:keyup.enter="Recyclersearch" type="text" v-model="keyword" class="form-control" placeholder="Search Customer;">
        </div>
        <form @submit.prevent="" method="post">

	    	<div class="col-md-12 table-responsive">
				<table class="table table-bordered table-hover table-sortable" id="tab_logic">
					<thead>
						<tr >
							<th class="text-center">
								Customer Number
							</th>
							<th class="text-center">
								First Name
							</th>
							<th class="text-center">
								Last Name
							</th>
	    					<th class="text-center">
								PET
							</th>
							<th class="text-center">
								Sachet
							</th>
							<th class="text-center">
								Can
							</th>
							<th class="text-center">
								Delete
							</th>
	        				<th class="text-center">
	        				 Action
							</th>
						</tr>
					</thead>
					<tbody>
						<tr v-for="(recycler,index) in recyclers">
						<td data-name="mail">
							{{recycler.customer_number}}	
						</td>
							<td data-name="mail">
							{{recycler.first_name}}
							</td>
							<td data-name="desc">
							{{recycler.last_name}}
							</td>
							<td data-name="mail">
							    <input type="text" v-model="items.PET[index]" name='mail0' placeholder='PET value' class="form-control"/>
							</td>
							<td data-name="mail">
							    <input type="text" v-model="items.Sachet[index]" name='mail0' placeholder='Sachet value' class="form-control"/>
							</td>
							<td data-name="mail">
							    <input type="text" v-model="items.Can[index]" name='mail0' placeholder='Can Value' class="form-control"/>
							</td>
	                        <td data-name="del">
	                            <button name="del0" class='btn btn-danger glyphicon glyphicon-remove row-remove'><span aria-hidden="true">×</span></button>
                            </td>
	                        <td data-name="del">
	                        	<button @click="sendPickup(recycler.id,index)" type="button" class="btn btn-primary">Save Pickup</button>
                        	</td>
						</tr>
					</tbody>
				</table>
			</div>
		</form
		</div>
	</div>
	<a id="add_row" class="btn btn-primary float-right">Add Row</a>
</div>
</template>

<script>
    import axios from 'axios';
    export default { 
        mounted() { 
            console.log('Component Search is here.') 
            this.getRecyclers()
        },
        data(){
            return{
                recyclers:[],
                keyword:'',
                pickups:[],
                items:{
                	PET:[],
                	Sachet:[],
                	Can:[],
            	}
            }
        },
        methods: {
        	sendPickup(id,index){
            	if(confirm("Do you really want to Send This Pickup?")){
                	axios.post(`/${id}/pickup/send/`,{
                			PET:this.items.PET[index],
                			Sachet:this.items.Sachet[index],
                			Can:this.items.Can[index]
                	})
                    .then((response) => {
                    	iziToast.success({
                        title: 'Success',
                        message: response.data,
                        position:'topCenter',
                    });   
                    })

            	}
            	this.items.PET[index]='';
                this.items.Sachet[index]='';
                this.items.Can[index]=''  
       		 },
            getRecyclers() {
                console.log('Component Search is here. button click') 
                axios.get(`/recyclers/list/`
                )
                .then((response)=>{
                    console.log(response)
                    this.recyclers = response.data;
                })
                .catch(function (error) {
                    if (error.response.status = 401) {
                      // Request made and server responded
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
            },
            Recyclersearch() {
                console.log('Component Search is here. button click') 
                axios.get(`/recyclers/list/`,{
                    params: {
                        keyword: this.keyword,
                    }
                })
                .then((response)=>{
                    console.log(response)
                    this.recyclers = response.data;
                    if (response.status == 204){
                        iziToast.info({
                        title: 'Empty Search result',
                        message: "No house Household details matches the search query,phone_number,customer-number,names, and current point",
                        position:'topCenter',
                    });     

                    }
                })

            },
        }
    } 
</script>
<style>
.table-sortable tbody tr {
    cursor: move;
}

</style>