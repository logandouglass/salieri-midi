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

//     delimiters: ["[[", "]]"],

//     methods: {

//         update() {

//           if (chordCurrent == 1)
//           {(chordCurrent = 2)  && (chord1Vis = false) && (chord2Vis = true)}
//           else if (chordCurrent == 2)
//           {(chordCurrent = 3)  && (chord2Vis = false) && (chord3Vis = true)}
//           else if (chordCurrent == 3)
//           {(chordCurrent = 4)  && (chord3Vis = false) && (chord4Vis = true)}
//           else if (chordCurrent == 4)
//           {(chordCurrent = 5)  && (chord4Vis = false) && (chord5Vis = true)}


//         },

//     }



//   }
//   // this is how you create & mount the app in Vue 3:
//   Vue.createApp(App).mount('#app')

//   // //updatePage() {

//   //   if (this.chordCurrent == 1)
//   //   {(this.chordCurrent = 2)  && (this.chord1Vis = false) && (this.chord2Vis = true)}
//   //   else if (this.chordCurrent == 2)
//   //   {(this.chordCurrent = 3)  && (this.chord2Vis = false) && (this.chord3Vis = true)}
//   //   else if (this.chordCurrent == 3)
//   //   {(this.chordCurrent = 4)  && (this.chord3Vis = false) && (this.chord4Vis = true)}
//   //   else if (this.chordCurrent == 4)
//   //   {(this.chordCurrent = 5)  && (this.chord4Vis = false) && (this.chord5Vis = true)}
//   //   console.log(`${this.chord2Vis}`)


//   // },