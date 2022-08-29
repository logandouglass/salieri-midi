const App = {

    data() {
      return {
        debug: 'helloworld',

        chord1Vis: true,
        chord2Vis: false,
        chord3Vis: false,
        chord4Vis: false,
        chord5Vis: false,

        chordCurrent: 1,

        currentChordDict: {
          1: `"f${this.chord1Style} ${this.chord1Denom}"`,
          2: `"f${this.chord1Style} ${this.chord1Denom}"`,
          3: `"f${this.chord1Style} ${this.chord1Denom}"`,
          4: `"f${this.chord1Style} ${this.chord1Denom}"`,
          5: `"f${this.chord1Style} ${this.chord1Denom}"`,
          },
  
        currentChordDisplay: undefined,
        chord1Tonic:"",
        chord1Quality:"",
        chord1Bars:0,
        chord2Tonic:"",
        chord2Quality:"",
        chord2Bars:0,
        chord3Tonic:"",
        chord3Quality:"",
        chord3Bars:0,
        chord4Tonic:"",
        chord4Quality:"",
        chord4Bars:0,
        chord5Tonic:"",
        chord5Quality:"",
        chord5Bars:0,

        chord1Added: false,
        chord2Added: false,
        chord3Added: false,
        chord4Added: false,
        chord5Added: false,
        noneAdded: true,
        
        chordsAdded: [1], // maybe unnecessary
        noChords:1,

        }
    },


    delimiters: ["[[", "]]"],

  
    methods: {

      addChord(){
        if (this.noChords == 1) {

          this.noChords += 1

          // set current chord & display
          this.chordCurrent = 2
          this.currentChordDisplay = this.currentChordDict[this.chordCurrent]
          
          // adj visibility
          this.chord1Vis = false
          this.chord2Vis = true
          this.chord3Vis = false
          this.chord4Vis = false
          this.chord5Vis = false

        }

        else if (this.noChords == 2) {

          this.noChords += 1

          // set current chord & display
          this.chordCurrent = 3
          this.currentChordDisplay = this.currentChordDict[this.chordCurrent]
          
          // adj visibility
          this.chord1Vis = false
          this.chord2Vis = false
          this.chord3Vis = true
          this.chord4Vis = false
          this.chord5Vis = false

        }

        else if (this.noChords == 3) {

          this.noChords += 1
          
          // set current chord & display
          this.chordCurrent = 4
          this.currentChordDisplay = this.currentChordDict[this.chordCurrent]
          
          // adj visibility
          this.chord1Vis = false
          this.chord2Vis = false
          this.chord3Vis = false
          this.chord4Vis = true
          this.chord5Vis = false

        }

        else if (this.noChords == 4) {

          this.noChords += 1
          
          // set current chord & display
          this.chordCurrent = 5
          this.currentChordDisplay = this.currentChordDict[this.chordCurrent]
          
          // adj visibility
          this.chord1Vis = false
          this.chord2Vis = false
          this.chord3Vis = false
          this.chord4Vis = true
          this.chord5Vis = false

        }


      },

      toChord1() {
        this.chordCurrent = 1
        this.chord1Vis = true
        this.chord2Vis = false
        this.chord3Vis = false
        this.chord4Vis = false
        this.chord5Vis = false
        this.currentChordDisplay = this.currentChordDict[this.chordCurrent]
      },

      toChord2() {
        this.chordCurrent = 2
        this.chord1Vis = false
        this.chord2Vis = true
        this.chord3Vis = false
        this.chord4Vis = false
        this.chord5Vis = false
        this.currentChordDisplay = this.currentChordDict[this.chordCurrent]
      },

      toChord3() {
        this.chordCurrent = 3
        this.chord1Vis = false
        this.chord2Vis = false
        this.chord3Vis = true
        this.chord4Vis = false
        this.chord5Vis = false
        this.currentChordDisplay = this.currentChordDict[this.chordCurrent]
      },

      toChord4() {
        this.chordCurrent = 4
        this.chord1Vis = false
        this.chord2Vis = false
        this.chord3Vis = false
        this.chord4Vis = true
        this.chord5Vis = false
        this.currentChordDisplay = this.currentChordDict[this.chordCurrent]
      },

      toChord5() {
        this.chordCurrent = 5
        this.chord1Vis = false
        this.chord2Vis = false
        this.chord3Vis = false
        this.chord4Vis = false
        this.chord5Vis = true
        this.currentChordDisplay = this.currentChordDict[this.chordCurrent]
      },

    //

    }, // methods

}

const app = Vue.createApp(App)
app.mount('#app')