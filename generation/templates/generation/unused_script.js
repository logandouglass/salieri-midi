const App = {
    // the data property is a function that returns an object
    data() {
      return {

      }
    },

    methods: {





       
    },
}
Vue.createApp(App).mount('#app')

//////////////////////////////////////////////////
// code from mdn wed docs


let downloading = browser.downloads.download({
    url : downloadUrl,
    filename : 'my-image-again.png',
    conflictAction : 'uniquify'
  });