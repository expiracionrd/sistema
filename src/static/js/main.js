import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
    
createApp({
    data() {
        return {
            open: false,
        }
    },
    methods: {
        openModal(id_editing){
            this.open = true
        }
    }
}).mount('#app')