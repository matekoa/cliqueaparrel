<template>
   <div id="wrapper">
      <nav class="navbar is-dark">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item"><strong>Clique Apparel</strong></router-link>
          <!--Hamburger menu for small Devices-->
          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <!--Two divs below because we want menu to be on one side of the page and the logo on the other side-->
        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            <router-link to="/summer" class="navbar-item">Summer</router-link>
            <router-link to="/winter" class="navbar-item">Winter</router-link>
          
          <!--Cart-->
          <div class="navbar-item">
              <div class="buttons">
                <router-link to="/log-in" class="button is-light">Login</router-link>
                
                <router-link to="/cart" class="button is-success">
                  <span class="icon"><i class="fas fa-shopping-cart"></i> </span>
                  <span>Cart</span>
                </router-link>
              </div>
          </div>
          </div>
        </div>
      </nav>
      <section class="section">
        <!--Router View Is Where All the content Is placed-->
        <router-view/>
      </section>

      <footer class="footer">
        <p class="has-text-centered">Copyright (c) 2022</p>
        
        </footer>
   </div>
</template>

<!--Vue JS Script To configure Hamburger Menu-->
<script>
  export default {
    data() {
      return {
        showMobileMenu: false,
      }
    }
  }
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
