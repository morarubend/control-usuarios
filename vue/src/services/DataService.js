//import http from "../http-common";
import axios from "axios";

const http = axios.create({
  //baseURL: 'http://tuapi.com/api',
  baseURL: "http://127.0.0.1:8000/api",

  headers: {
    'Content-type': 'Application/json'
  }
});


/*
var axiosx = require("axios");
const axiosInstance = axiosx.create({
  headers: {
    "Access-Control-Allow-Origin": "*"
  }
});
*/


class DataService {
  getAll() {
    return http.get("/clientes");
  }

  get(id) {
    return http.get(`/clientes/${id}`);
  }

  create(data) {
    return http.post("/clientes", data);
  }

  update(id, data) {
    return http.put(`/tutorials/${id}`, data);
  }

  delete(id) {
    console.log("delete()", id);
    return http.delete(`/clientedelete/${id}`);
  }

  deleteAll() {
    return http.delete(`/tutorials`);
  }

  findByName(name) {
    console.log("BUSCAR NOMBRE", name);
    return http.get(`/tutorials?name=${name}`);
  }
}

export default new DataService();