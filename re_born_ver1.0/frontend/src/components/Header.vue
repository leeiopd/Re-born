<template>
    <div>
        <v-toolbar
            absolute
            color="#B3D996"
            dark
            flat
            scroll-off-screen
            scroll-target="#scrolling-techniques"
        >
            <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
            <v-toolbar-title style="font-family: 'Poiret One', cursive; font-weight: bolder;">Re-born</v-toolbar-title>
        </v-toolbar>
        <v-navigation-drawer
            color="#B3D996"
            v-model="drawer"
            absolute
            temporary
        >
        <v-list class="pt-0" dense>
            <v-list-tile
            v-for="item in items"
            :key="item.title"
            @click=""
            >
            <v-list-tile-action>
                <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>

            <v-list-tile-content>
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </v-list-tile-content>
            </v-list-tile>
        </v-list>
        </v-navigation-drawer>
    </div>
</template>

<script>
import FirebaseServices from '../services/FirebaseServices.js'
import firebase from 'firebase'

export default {
  name: 'Header',
  data () {
    return {
        user: null,
        drawer: false,
        items: [
            { title: 'Dashboard', icon: 'dashboard' },
            { title: 'Account', icon: 'account_box' },
            { title: 'Admin', icon: 'gavel' }
        ]
    }
  },
  methods: {
  }
}
</script>

