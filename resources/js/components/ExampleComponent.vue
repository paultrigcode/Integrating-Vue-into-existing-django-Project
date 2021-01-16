<template> 
    <div class="container"> 
        <div class="row justify-content-center"> 
            <div class="col-md-8"> 
                <div class="card"> 
                    <div>Example Component</div> 
                    <div> 
                        I'm an example component. 
                    </div> 
                    <div v-for="i in propfa"> 
                        {{i.title}}
                    </div> 
                </div> 
            </div> 
        </div> 
    </div> 
</template> 
<script> 
export default { 
    mounted() { 
        console.log('Component mounty.') 
        
    } ,
    props: ['propfa'],
    data(){
        return{
        body:'hello'

        }
    },
    methods: {
        
    }
} 
</script>