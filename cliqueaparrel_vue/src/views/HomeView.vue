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

        <!--Bind unique key for each product-->
        <div class="column is-3" 
             v-for="products in latestProducts"
             v-bind:key="product.id"
             ></div>
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="product.get_thumbnail" alt="Product Thumbnail">
          </figure>

          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-text-grey">${{ product.price }}</p>

          View Details
        </div>
      </div>
  </div>
</template>

<script>
</script>
