// const App = {
//     // the data property is a function that returns an object
//     data() {
//       return {
//         debug: 'helloworld',
//         chord1Vis: true,
//         chord2Vis: false,
//         chord3Vis: false,
//         chord4Vis: false,
//         chord5Vis: false,
//         obliterate: false,
//         chordCurrent: 1,

//       }
//     },

//     //

//     delimiters: ["[[", "]]"],

//     //
    
//     methods: {

//       updatePage() {

//         if (this.chordCurrent == 1)
//         {(this.chordCurrent = 2)
//           (this.chord1Vis = false) 
//           (this.chord2Vis = true)}
//         else if (this.chordCurrent == 2)
//         {(this.chordCurrent = 3)
//         (this.chord2Vis = false)
//         (this.chord3Vis = true)}
//         else if (this.chordCurrent == 3)
//         {(this.chordCurrent = 4)
//         (this.chord3Vis = false)
//         (this.chord4Vis = true)}
//         else if (this.chordCurrent == 4)
//         {(this.chordCurrent = 5)
//         (this.chord4Vis = false)
//         (this.chord5Vis = true)}
//         console.log(`${this.chord2Vis}`)}


//       },

//         //

//     }
    
//     //

//   //
//   const app = Vue.createApp(App)
//   app.mount('#app')


const App = {
    // the data property is a function that returns an object
    data() {
      return {
        debug: 'helloworld',
        chord1Vis: true,
        chord2Vis: false,
        chord3Vis: false,
        chord4Vis: false,
        chord5Vis: false,
        obliterate: false,
        chordCurrent: 1,

      }
    },

    //

    delimiters: ["[[", "]]"],

    //
    
    methods: {

      updatePage() {

        console.log("here0")
        if (this.chordCurrent == 1)
        {
          console.log("here1")
          console.log("here1.25")
          this.chordCurrent = 2
          console.log("here1.5")
          this.chord1Vis = false
          console.log("here1.75") 
          this.chord2Vis = true
          console.log("here2")
        }
        
        else if (this.chordCurrent == 2){
        this.chordCurrent = 3
        this.chord2Vis = false
        this.chord3Vis = true
        }

        else if (this.chordCurrent == 3){
        this.chordCurrent = 4
        this.chord3Vis = false
        this.chord4Vis = true
        }
        else if (this.chordCurrent == 4){
        this.chordCurrent = 5
        this.chord4Vis = false
        this.chord5Vis = true
      }
        // console.log(`${this.chord2Vis}`)}


      },

        

    }
    
}


  const app = Vue.createApp(App)
  app.mount('#app')