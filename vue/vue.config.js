
module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
	  proxy: "http://127.0.0.1:8000"  
  },
};


/*
module.exports = {  
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://localhost: 8000',
        ws: true,
        changeOrigin: true
      }
    }
  }
}
*/