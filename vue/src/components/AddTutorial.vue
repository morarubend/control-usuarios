<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Crear Cliente</p>

    <div v-if="!submitted">
      <v-form ref="form" lazy-validation>
        <v-text-field
          v-model="tutorial.name"
          :rules="[(v) => !!v || 'Nombres son requeridos']"
          label="Nombre"
          required
        ></v-text-field>

        <v-text-field
          v-model="tutorial.surname"
          :rules="[(v) => !!v || 'Apellidos son requeridos']"
          label="Apellidos"
          required
        ></v-text-field>

      <v-text-field
          v-model="tutorial.email"
          :rules="[(v) => !!v || 'Correo son requeridos']"
          label="Correo"
          id="email"
          type="email"
          required
        ></v-text-field>

        <v-text-field
          v-model="tutorial.password"
          :rules="[(v) => !!v || 'Clave es requerida']"
          label="Clave"
          required
        ></v-text-field>

        <v-text-field
          v-model="tutorial.fchnace"
          :rules="[(v) => !!v || 'Fecha de nacimiento es requerida']"
          label="Fecha de nacimiento"
          required
        ></v-text-field>
      </v-form>

      <v-btn color="primary" small @click="saveTutorial">Enviar</v-btn>
      <v-btn color="success" small @click="cancelarTutorial">
        Cancelar
      </v-btn>
    </div>

    <div v-else>
      <v-card class="mx-auto">
        <v-card-title>
          Cliente Creado!
        </v-card-title>

        <v-card-subtitle>
          Click eb el boton para crear un nuevo cliente.
        </v-card-subtitle>

        <v-card-actions>
          <v-btn color="success" @click="newTutorial">Add</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
import DataService from "../services/DataService";

export default {
  name: "add-tutorial",
  data() {
    return {
      tutorial: {
        id: null,
        name: "",
        surname: "",
        email: "",
        password: "",
        fchnace: ""        
      },
      submitted: false,
    };
  },
  methods: {
    saveTutorial() {
      var data = {
        name: this.tutorial.name,
        surname: this.tutorial.surname,
        email: this.tutorial.email,
        password: this.tutorial.password,
        fchnace: this.tutorial.fchnace,
      };

      DataService.create(data)
        .then((response) => {
          this.tutorial.id = response.data.id;
          console.log('Response:', response.data);
          this.submitted = true;
        })
        .catch((error) => {
          if (error.response) {
             console.log('Error response:', error.response);
          } else if (error.request) {
             console.log('Error request:', error.request);
          } else {
             console.log('Error message:', error.message);
          }
        this.submitted = true;
        });
    },

    cancelarTutorial() {
      this.$router.push({ name: "tutorials" });
    },

    newTutorial() {
      this.submitted = false;
      this.tutorial = {};
    },
  },
};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
