<template>
    <div id="app">
        {{ msg }}
        <form @submit.prevent="submitNote">
            <label>Title</label>
            <input type="text" v-model="formData.title"/>
            <label>Content</label>
            <textarea type="text" v-model="formData.content"></textarea>

            <br/>
            <button type="submit">Submit</button>
        </form>

        <br/>
        <p>{{ fullName }}</p>
        <h1>All Notes</h1>
        <ul>
            <li v-for="(note, index) in notes" :key="index">
                <h3>{{ note.title }}</h3>
                <h5>Created on {{ note.created }}</h5>
                <p>{{ note.context }}</p>
            </li>
        </ul>
    </div>
</template>

<script>
import api from './api/index.js'

export default {
    name: 'app',
    data () {
        return {
            msg: '',
            formData: {
                title: '',
                content: ''
            },
            notes: []
        }
    },
    methods: {
        submitNote () {
            api.fetchNotes('post', null, this.formData).then(res => {
                this.msg = 'Saved'
            }).catch((e) => {
                this.msg = e.response
            })
        },
        fetchAllNotes () {
            api.fetchNotes('get', null, null).then(res => {
                this.notes = res.data
                console.log(this.notes)
            }).catch((e) => {
                console.log(e)
            })
        }
    },
    mounted () {
        this.fetchAllNotes()
    }
}
</script>

<style>
#app {
    max-width: 500px;
    margin: 0 auto;
    text-align: left;
}
input, textarea {
    width: 100%;
    display: block;
    padding: 6px 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
}
label {
    margin-top: 15px;
    display: block;
}
button {
    background: #000;
    color: white;
    border-radius: 3px;
    padding: 6px 10px;
}
</style>
