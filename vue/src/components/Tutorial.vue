<template>
  <div v-if="currentTutorial" class="edit-form py-3">
    <p class="headline">Editar Cliente</p>

    <v-form ref="form" lazy-validation>
      <v-text-field
        v-model="currentTutorial.name"
        :rules="[(v) => !!v || 'Nombres es requerido']"
        label="Nombre"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentTutorial.surname"
        :rules="[(v) => !!v || 'Apellidos son requeridos']"
        label="Apellidos"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentTutorial.email"
        :rules="[(v) => !!v || 'Correo es requerido']"
        label="Correo"
        required
      ></v-text-field>

      <v-divider class="my-5"></v-divider>

      <v-btn color="error" small class="mr-2" @click="deleteTutorial">
        Eliminar
      </v-btn>

      <v-btn color="success" small @click="updateTutorial">
        Actualizar
      </v-btn>

      <v-btn color="success" small @click="cancelarTutorial">
        Cancelar
      </v-btn>

    </v-form>

    <p class="mt-3">{{ message }}</p>
  </div>

  <div v-else>
    <p>Please click on a Tutorial...</p>
  </div>
</template>

<script>
import DataService from "../services/DataService";

export default {
  name: "tutorial",
  data() {
    return {
      currentTutorial: null,
      message: "",
    };
  },
  methods: {
    getTutorial(id) {
      DataService.get(id)
        .then((response) => {
          this.currentTutorial = response.data;
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },

    updatePublished(status) {
      var data = {
        id: this.currentTutorial.id,
        title: this.currentTutorial.title,
        description: this.currentTutorial.description,
        published: status,
      };

      DataService.update(this.currentTutorial.id, data)
        .then((response) => {
          this.currentTutorial.published = status;
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },

    updateTutorial() {
      DataService.update(this.currentTutorial.id, this.currentTutorial)
        .then((response) => {
          console.log(response.data);
          this.message = "The tutorial was updated successfully!";
        })
        .catch((e) => {
          console.log(e);
        });
    },

    cancelarTutorial() {
      this.$router.push({ name: "tutorials" });
    },

    deleteTutorial() {
      DataService.delete(this.currentTutorial.id)
        .then((response) => {
          console.log(response.data);
          this.$router.push({ name: "tutorials" });
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  mounted() {
    this.message = "";
    this.getTutorial(this.$route.params.id);
  },
};
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>
