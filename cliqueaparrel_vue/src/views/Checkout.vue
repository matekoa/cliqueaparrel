<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
        </div>
    </div>

    <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key="item.product.id">
                            
                            <td>{{item.product.name}}</td>    
                            <td>${{item.product.price}}</td> 
                            <td>{{item.quantity}}</td> 
                            <td>${{getItemTotal(item).toFixed(2)}}</td> 
                        </tr>

                    </tbody>
                </table>
    </div>

    <div class="column is-12 box">
        <h2 class="subtitle">Shipping Details</h2>

        <p class="has-text-grey mb-4">*All fields are required</p>
        <div class="columns is-multiline">

            <div class="column is-6">
                <div class="field">
                    <label>First Name*</label>
                    <div class="control">
                        <input type="text"  class="input" v-model="first_name">
                    </div>
                </div>


                <div class="field">
                    <label>Last Name*</label>
                    <div class="control">
                        <input type="text"  class="input" v-model="last_name">
                    </div>
                </div>

                <div class="field">
                    <label>Email*</label>
                    <div class="control">
                        <input type="email"  class="input" v-model="email">
                    </div>
                </div>

                <div class="field">
                    <label>Phone*</label>
                    <div class="control">
                        <input type="text"  class="input" v-model="phone">
                    </div>
                </div>
            </div>

            <!--Right Side-->
            <div class="column is-6">
                <div class="field">
                    <label>Address*</label>
                    <div class="control">
                        <input type="text"  class="input" v-model="address">
                    </div>
                </div>


                <div class="field">
                    <label>Zip Code*</label>
                    <div class="control">
                        <input type="text"  class="input" v-model="zipcode">
                    </div>
                </div>

                <div class="field">
                    <label>Place*</label>
                    <div class="control">
                        <input type="text"  class="input" v-model="place">
                    </div>
                </div>
            </div>


            <div class="notification is danger" v-if="errors.length">
                    <p v-for="error in errors">{{ error }}</p>
            </div>
            <hr>
            <div id="card-element" class="mb-5">
            </div>

            <template v-if="cartTotalLength">

                <hr>
                <button class="button is-dark" @click="submitForm">Pay With Stripe</button>
            </template>

        </div>
    </div>
</template>


<script>
import axios from 'axios'
    export default {
        name: 'Checkout',

        data() {

            return {
                cart: {
                    items: []
                },
                stripe: {},
                card: {},
                first_name: '',
                last_name: '',
                email: '',
                phone: '',
                address: '',
                zipcode: '',
                place: '',
                errors: []
            }
        },

        mounted() {
            document.title = 'Checkout | Clique Apparel'

            this.cart = this.$store.state.cart
        },

        methods: {
            getItemTotal(item) {
                return item.quantity * item.product.price
            },

            submitForm(){
                this.errors = []

                //validate username
                if (this.first_name === '') {
                    this.errors.push ('The first name field is missing!')
                }

                if (this.last_name === '') {
                    this.errors.push ('The last name field is missing!')
                }

                if (this.email === '') {
                    this.errors.push ('The email field is missing!')
                }

                if (this.phone === '') {
                    this.errors.push ('The phone field is missing!')
                }

                if (this.address === '') {
                    this.errors.push ('The address field is missing!')
                }

                if (this.zipcode === '') {
                    this.errors.push ('The zip code field is missing!')
                }

                if (this.place === '') {
                    this.errors.push ('The place field is missing!')
                }

                               
            },
        },

        computed: {
            cartTotalLength(){
                return this.cart.items.reduce((acc, curVal) => {
                    return acc += curVal.quantity

                }, 0)
            },

            cartTotalPrice(){
                return this.cart.items.reduce((acc, curVal) => {
                    return acc += curVal.product.price * curVal.quantity

                }, 0)
            },
        }
    }
</script>