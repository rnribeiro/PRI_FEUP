module.exports = {
  devServer: {
    proxy: {
      '/solr': {
        target: 'http://localhost:8983',
        changeOrigin: true,
        pathRewrite: {
          '^/solr': '/solr'
        }
      }
    }
  }
};
