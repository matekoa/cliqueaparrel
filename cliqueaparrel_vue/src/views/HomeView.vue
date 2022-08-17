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

        <ProductBox
          v-for="product in latestProducts"
          v-bind:key="product.id"
          v-bind:product="product" />

      </div>
  </div>
</template>

<script>
// Use Axios To create a function that gets data from the backend
import axios from 'axios'

import ProductBox from '@/components/ProductBox'

  export default {
    name: 'Home',

    data() {
      return {
        latestProducts: []
      }
    },

    components: {
      ProductBox,
    },

    mounted() {
      this.getLatestProducts()
      document.title = 'Home | CliqueApparel'
    },

    methods: {
      async getLatestProducts(){
        this.$store.commit('setIsLoading',true)

        await axios
          .get('api/v1/latest-products/')
          .then(response => {
            this.latestProducts = response.data

            document.title = this.product.name + '| CliqueApparel'
          })
          .catch(error => {
            console.log(error) //To fix later
          })

          this.$store.commit('setIsLoading',false)
      }
    }
  }
</script>

