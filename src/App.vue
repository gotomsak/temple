<template>

 <v-app id="app">
   <v-toolbar>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>Title</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat>Link One</v-btn>
      <v-btn flat>Link Two</v-btn>
      <v-btn flat>Link Three</v-btn>
    </v-toolbar-items>
  </v-toolbar>
   <router-view></router-view>
  </v-app>

</template>


<script>
  export default {
    name: 'App',
    // data: () => ({
    //   admins: [
    //     ['Management', 'people_outline'],
    //     ['Settings', 'settings'],
    //   ],
    //   cruds: [
    //     ['Create', 'add'],
    //     ['Read', 'insert_drive_file'],
    //     ['Update', 'update'],
    //     ['Delete', 'delete'],
    //   ],
    // }),
  }
</script>

<style>
/*body {*/
  /*margin: 0;*/
/*}*/

/*#app {*/
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
   /*-webkit-font-smoothing: antialiased;*/
   /*-moz-osx-font-smoothing: grayscale;*/
  /*color: #2c3e50;*/
/*}*/

/*main {*/
  /*text-align: center;*/
  /*margin-top: 40px;*/
/*}*/

/*header {*/
  /*margin: 0;*/
  /*height: 56px;*/
  /*padding: 0 16px 0 24px;*/
  /*background-color: #35495E;*/
  /*color: #ffffff;*/
/*}*/

/*header span {*/
  /*display: block;*/
  /*position: relative;*/
  /*font-size: 20px;*/
  /*line-height: 1;*/
  /*letter-spacing: .02em;*/
  /*font-weight: 400;*/
  /*box-sizing: border-box;*/
  /*padding-top: 16px;*/
/*}*/
</style>
