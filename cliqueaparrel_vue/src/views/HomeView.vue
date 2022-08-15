<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
          <p class="title mb-6">Welcome To Clique Apparel</p>

          <p class="subtitle"> Fashion at your convenience</p>
        </div>
      </section>


      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest Products</h2>
        </div>
      </div>

      <!--Bind unique key for each product-->
      <div class="column is-3" 
            v-for="products in latestProducts"
            v-bind:key="products.id"
            >

            <div class="box">
                <figure class="image mb-4">
                    <img v-bind:src="products.get_thumbnail" alt="Product for sale">
                </figure>
                <h3 class="is-size-4">{{ products.name }}</h3>
                <p class="is-size-6 has-text-grey">${{ products.price }}</p>

                View Details
            </div>
      </div>


        
  </div>
</template>

<script>
// Use Axios To create a function that gets data from the backend
import axios from 'axios'

  export default {
    name: 'Home',
    data() {
      return {
        latestProducts: []
      }
    },
    components: {
      
    },

    mounted() {
      this.getLatestProducts()
    },
    methods: {
      getLatestProducts(){
        axios
          .get('api/v1/latest-products/')
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error) //To fix later
          })
      }
    }
  }
</script>

<!--Style for the images-->
<style scoped>
    .image {
      margin-top: -1.25rem;
      margin-left: -1.25rem;
      margin-right: -1.25rem;
    }
</style>
