<template>
  <v-row align="center" class="list px-3 mx-auto">
    <v-col cols="12" md="3">
      <v-text-field v-model="name" label="Busqueda por Nombre"></v-text-field>
    </v-col>

    <v-col cols="12" md="4">
      <v-btn small @click="searchTitle">
        Buscar
      </v-btn>
    </v-col>

    <v-col cols="12" sm="12">
      <v-card class="mx-auto" tile>
        <v-card-title>Clientes</v-card-title>

        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="tutorials"
          :items-per-page="5"
          :single-select="false"
          :loading="loading"
          item-key="name"
          show-select
          class="elevation-1"          
        >
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon small class="mr-2" @click="editTutorial(item.id)">mdi-pencil</v-icon>
            <v-icon small @click="deleteTutorial(item.id)">mdi-delete</v-icon>
          </template>
        </v-data-table>

        <v-card-actions v-if="tutorials.length > 1000000">
          <v-btn small color="error" @click="removeAllTutorials">
            Eliminar Todo
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>
 
<script>
import DataService from "../services/DataService";
export default {
  name: "tutorials-list",
  data() {
    return {
      tutorials: [],
      title: "",
      name: "",
      loading: "",
      selected: "",
      headers: [
        { text: "Id", align: "start", sortable: false, value: "id" },
        { text: "Nombre", align: "start", sortable: false, value: "name" },
        { text: "Apellido", value: "surname", sortable: false },
        { text: "Correo", value: "email", sortable: false },
        { text: "Fecha Nace", value: "fchnace", sortable: false },
        { text: "Clave", value: "password", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
      ],
    };
  },

  methods: {
    retrieveTutorials() {
      this.loading = true;
      console.log("retrieveTutorials()");
      DataService.getAll()
        .then((response) => {
          console.log('Response:',response.data);
          this.tutorials = response.data.map(this.getDisplayTutorial);
          this.loading = false;
        })
        .catch((e) => {
          console.log(e);
          this.loading = false;
        });
    },

    refreshList() {
      this.retrieveTutorials();
    },

    removeAllTutorials() {
      DataService.deleteAll()
        .then((response) => {
          console.log(response.data);
          this.refreshList();
        })
        .catch((e) => {
          console.log(e);
        });
    },

    searchTitle() {
      console.log("searchTitle()", this.name);
      DataService.findByName(this.name)
        .then((response) => {
          this.tutorials = response.data.map(this.getDisplayTutorial);
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },

    editTutorial(id) {
      this.$router.push({ name: "tutorial-details", params: { id: id } });
    },

    deleteTutorial(id) {
      DataService.delete(id)
        .then(response => {
          console.log(response.data);
          console.log('Response:', response.data);
          this.refreshList();
        })
        .catch((error) => {
          if (error.response) {
             console.log('Error response:', error.response);
          } else if (error.request) {
             console.log('Error request:', error.request);
          } else {
             console.log('Error message:', error.message);
          }
      this.refreshList();
        });
    },

    getDisplayTutorial(tutorial) {
      return {
        id: tutorial.id,
        name: tutorial.name.length > 30 ? tutorial.name.substr(0, 30) + "..." : tutorial.name,
        surname: tutorial.surname.length > 30 ? tutorial.surname.substr(0, 30) + "..." : tutorial.surname,
        email: tutorial.email,
        fchnace: tutorial.fchnace,
        password: tutorial.password,
      };
    },
  },
  mounted() {
    this.retrieveTutorials();
  },
};
</script>

<style>
.list {
  max-width: 1200px;
}
</style>
