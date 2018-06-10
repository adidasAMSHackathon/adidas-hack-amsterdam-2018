<template>
      <div class="md-layout md-alignment-center">
        <div class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100">
          <form novalidate class="md-layout md-alignment-center" @submit.prevent="validateUser">
            <md-card class="md-layout-item md-size-50 md-small-size-100">
              <md-card-header>
                <md-icon class="md-size-4x">account_circle</md-icon>
              </md-card-header>

              <md-card-content>
                <div class="md-layout md-gutter">
                  <div class="md-layout-item md-small-size-100">
                    <md-field :class="getValidationClass('firstName')">
                      <label for="first-name">First Name</label>
                      <md-input name="first-name" id="first-name" autocomplete="given-name" v-model="form.firstName" :disabled="sending" />
                      <span class="md-error" v-if="!$v.form.firstName.required">The first name is required</span>
                      <span class="md-error" v-else-if="!$v.form.firstName.minlength">Invalid first name</span>
                    </md-field>
                  </div>

                  <div class="md-layout-item md-small-size-100">
                    <md-field :class="getValidationClass('lastName')">
                      <label for="last-name">Last Name</label>
                      <md-input name="last-name" id="last-name" autocomplete="family-name" v-model="form.lastName" :disabled="sending" />
                      <span class="md-error" v-if="!$v.form.lastName.required">The last name is required</span>
                      <span class="md-error" v-else-if="!$v.form.lastName.minlength">Invalid last name</span>
                    </md-field>
                  </div>
                </div>

                <div class="md-layout-item md-small-size-100">
                    <md-field :class="getValidationClass('age')">
                      <label for="age">Age</label>
                      <md-input type="number" id="age" name="age" autocomplete="age" v-model="form.age" :disabled="sending" />
                      <span class="md-error" v-if="!$v.form.age.required">The age is required</span>
                      <span class="md-error" v-else-if="!$v.form.age.maxlength">Invalid age</span>
                    </md-field>
                </div>

                <md-field :class="getValidationClass('email')">
                  <label for="email">Email</label>
                  <md-input type="email" name="email" id="email" autocomplete="email" v-model="form.email" :disabled="sending" />
                  <span class="md-error" v-if="!$v.form.email.required">The email is required</span>
                  <span class="md-error" v-else-if="!$v.form.email.email">Invalid email</span>
                </md-field>
                <div>
                  <label for="sharing-services">Share data from: </label>
                  <div id="sharing-services" class="md-layout md-align-center">
                    <div class="md-layout-item md-align-center">
                      <md-checkbox v-model="form.authenticate" value="Facebook">Facebook</md-checkbox>
                    </div>
                    <div class="md-layout-item md-align-center">
                      <md-checkbox v-model="form.authenticate" value="Under Armour">Under Armour</md-checkbox>
                    </div>
                    <div class="md-layout-item md-align-center">
                      <md-checkbox v-model="form.authenticate" value="Google Fit">Google Fit</md-checkbox>
                    </div>
                  </div>
                </div>

                <md-field :class="getValidationClass('faceimage')">
                  <label>Add an image of your face here</label>
                  <md-file v-model="form.faceimage" />
                  <span class="md-error" v-if="!$v.form.faceimage.required">The email is required</span>
                </md-field>

              </md-card-content>

              <md-progress-bar md-mode="indeterminate" v-if="sending" />

              <label for="submit-button" id="data-sharing-notice"> By registering, you allow us to use the data you have willingly shared above
              to improve your in-store experience at any of our outlets. </label>
              <md-card-actions id="submit-button">
                <md-button type="submit"  class="md-primary" :disabled="sending">Register</md-button>
              </md-card-actions>
            </md-card>

            <md-snackbar :md-active.sync="userSaved">The user {{ lastUser }} was saved with success!</md-snackbar>
          </form>
        </div>
      </div>
</template>

<script>
/* eslint-disable indent */

  import { validationMixin } from 'vuelidate'
  import {
    required,
    email,
    minLength,
    maxLength
  } from 'vuelidate/lib/validators'

  export default {
    name: 'FormValidation',
    mixins: [validationMixin],
    data: () => ({
      form: {
        firstName: null,
        lastName: null,
        age: null,
        email: null,
        authenticate: [],
        faceimage: null
      },
      userSaved: false,
      sending: false,
      lastUser: null,
      token: ''
    }),
    validations: {
      form: {
        firstName: {
          required,
          minLength: minLength(3)
        },
        lastName: {
          required,
          minLength: minLength(3)
        },
        age: {
          required,
          maxLength: maxLength(3)
        },
        email: {
          required,
          email
        },
        faceimage: {
          required
        }
      }
    },
    methods: {
      getValidationClass (fieldName) {
        const field = this.$v.form[fieldName]

        if (field) {
          return {
            'md-invalid': field.$invalid && field.$dirty
          }
        }
      },
      clearForm () {
        this.$v.$reset()
        this.form.firstName = null
        this.form.lastName = null
        this.form.age = null
        this.form.email = null
      },
      saveUser () {
        this.sending = true
        if (this.form.authenticate.includes('Facebook')) {
          this.authenticate('facebook')
          this.sending = false
//          let userId = 0
//          let accessToken = 0
//          switch (this.form.firstName) {
//            case 'Aayush':
//              userId = '1227781447248169'
//              accessToken = 'EAACEdEose0cBADQboxDCV7QDwZC5faXVYa8RZCBRIpeVMZAasUVgWMZByM4n1k5mYlkfcz6XXcUlPp0qoOOtTJhnNBZAxBCDW3LAPrUhBLIbsCdl8mWWqXiZBhRpS4ZADiPQaZCmIVJ4aOBKtW8ZCl92PgP5rMtUNW7jZCRQgvQSrLEY18wJO7TD9jl5ZC7ZBOHUVtFHOtc12ZBeIiQZDZD'
//              break
//            case 'Sami':
//              userId = '100005684656915'
//              accessToken = ''
//              break
//            default:
//              userId = '1227781447248169'
//              accessToken = 'EAACEdEose0cBADQboxDCV7QDwZC5faXVYa8RZCBRIpeVMZAasUVgWMZByM4n1k5mYlkfcz6XXcUlPp0qoOOtTJhnNBZAxBCDW3LAPrUhBLIbsCdl8mWWqXiZBhRpS4ZADiPQaZCmIVJ4aOBKtW8ZCl92PgP5rMtUNW7jZCRQgvQSrLEY18wJO7TD9jl5ZC7ZBOHUVtFHOtc12ZBeIiQZDZD'
//              break
//          }
//
//          const requestUrl = `https://graph.facebook.com/v3.0/${userId}?fields=likes,events,birthday&access_token=${accessToken}`

//          this.axios.get(requestUrl).then((response) => {
//            console.log(response.data)
//          })
        }
        // Instead of this timeout, here you can call your API
      },
      validateUser () {
        this.$v.$touch()

        if (!this.$v.$invalid) {
          this.saveUser()
        }
      },
      authenticate: function (provider) {
        this.$auth.authenticate(provider).then(function () {
          // Execute application logic after successful social authentication
          let token = this.$auth.getToken()
          this.token = token
          this.sending = false
          alert(this.token)
        })
      }
    }
  }
</script>

<style lang="scss" scoped>
  .md-progress-bar {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
  }
  form {
    margin: 5rem;
  }

  .md-checkbox {
    display: flex;
    align: center;
  }

  #data-sharing-notice {
    font-family: "Cooper Black";
    font-size: 12px;
  }

</style>
