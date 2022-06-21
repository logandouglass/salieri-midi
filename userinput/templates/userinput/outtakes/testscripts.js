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
      chord1Style: undefined,
      chord1Denom: undefined,
      chord1Mut: undefined,
      chord2Style: undefined,
      chord2Denom: undefined,
      chord2Mut: undefined,
      chord3Style: undefined,
      chord3Denom: undefined,
      chord3Mut: undefined,
      chord4Style: undefined,
      chord4Denom: undefined,
      chord4Mut: undefined,
      chord5Style: undefined,
      chord5Denom: undefined,
      chord5Mut: undefined,
      //chord1StyleLabel: undefined,
      //chord1DenomLabel: undefined,
      //chord1MutLabel: undefined,
      //chord2StyleLabel: undefined,
      //chord2DenomLabel: undefined,
      //chord2MutLabel: undefined,
      //chord3StyleLabel: undefined,
      //chord3DenomLabel: undefined,
      //chord3MutLabel: undefined,
      //chord4StyleLabel: undefined,
      //chord4DenomLabel: undefined,
      //chord4MutLabel: undefined,
      //chord5StyleLabel: undefined,
      //chord5DenomLabel: undefined,
      //chord5MutLabel: undefined,



    }
  },

  //

  delimiters: ["[[", "]]"],

  //

  //mounted () {

    //this.$refs.chord1Tonic.focus()

  //},

  //
  
  methods: {

    updatePage() {




      console.log("here0")
      if (this.chordCurrent == 1)
      {
        //console.log("here1")
        //console.log("here1.25")
        this.chordCurrent = 2
        //console.log("here1.5")
        this.chord1Vis = false
        //console.log("here1.75") 
        this.chord2Vis = true
        //console.log("here2")
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

  toChord1() {
    this.chordCurrent = 1
    this.chord1Vis = true
    this.chord2Vis = false
    this.chord3Vis = false
    this.chord4Vis = false
    this.chord5Vis = false


    },
  
}

}

const app = Vue.createApp(App)
app.mount('#app')