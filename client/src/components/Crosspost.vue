<template>
    <div class="container">
        <form @submit.prevent="validateForm">
            <h2>My Own Little Cross-Poster (v.{{ version }})</h2>
            <textarea id="text" v-model="text" required @input="updateCharacterCount"></textarea><br>
            <p>Character count: <span id="characterCount">{{ characterCount }}</span></p>
            <p id="warningMessage" v-show="characterCount > 240" style="color: red;">Character count exceeds 240!</p>
            <input type="file" id="fileControl" multiple accept="image/*" @change="processFiles">
            <br>
            <div id="fileList"></div>
            <input type="checkbox" id="hashtagCheckbox" v-model="hashtagCheckbox" @click="updateCharacterCount">
            <label for="hashtagCheckbox">add hashtags?</label><br><br>
            <input type="text" id="txt_hashtags" v-model="hashtags" @input="updateCharacterCount">
            <!-- Rest of the form here -->
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            text: '',
            files: [],
            hashtagCheckbox: true,
            hashtags: '',
            // Rest of the data properties here
        };
    },
    computed: {
        characterCount() {
            let count = this.text.length;
            if (this.hashtagCheckbox) {
                count += this.hashtags.length;
            }
            return count;
        },
        // Rest of the computed properties here
    },
    methods: {
        handleFiles(files) {
            this.files = [...files];
        }
        // Handle the files here
    },
    validateForm() {
        // Validate the form here
    },
    // Rest of the methods here
}
</script>

<style scoped>
/* Your CSS styles here */
</style>