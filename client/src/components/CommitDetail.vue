<template>
    <div>
        <div v-if="message.length != 0">
            <div class="card">
                <div class="card-header fs-4 fw-bold">
                    {{ message }}
                </div>
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center flex-md-row flex-column">
                        <div class="d-flex align-items-center">
                            <div class="p-2"><i class="far fa-user fa-2x"></i></div>
                            <div class="mx-3">
                                <span class="fw-bold">{{ author_name }}</span><br/>
                                <span class="">{{ author_email }}</span>
                            </div>
                        </div>
                        <div class="col-md-6"><span>committed on {{ datetime }}</span></div>
                        <div>
                            <span class="text-muted badge">Commit</span> {{ hexsha }}
                        </div>
                    </div>
                </div>
            </div>
            <div class="container my-2 my-3">
                Showing <span class="text-primary fw-bold">{{ number_file_changed }} changed files</span> with <span class="text-success fw-bold">{{ files_additions }} additions</span> and <span class="text-danger fw-bold">{{ files_deletions }} deletions</span>
            </div>
            <ul class="list-group list-group-flush">
                <li v-for="(file, id) in files" :key="id" class="list-group-item py-2">
                    <div class="d-flex align-items-center py-1">
                        <span class="fas fa-code"></span>
                        <span class="badge text-dark">{{ file.name }}</span>
                    </div>
                </li>
            </ul>
        </div>
        <div v-else class="text-center">
            No hay datos que mostrar
        </div>
    </div>
</template>

<script>
export default {
    name: 'CommitDetail',
    props: {
        get_hexsha: String
    },
    data(){
        return {
            author_name: '',
            author_email: '',
            datetime: '',
            files_additions: 0,
            files_deletions: 0,
            files: [],
            number_file_changed: 0,
            message: '',
            hexsha: '',
        }
    },
    created(){
        this.getCommit();
    },
    methods: {
        getCommit(){
            this.$axios
            .get(`commits/${this.get_hexsha}`)
            .then(data => {
                const commit = data.data.data;
                this.author_name = commit.author.name;
                this.author_email = commit.author.email;
                this.datetime = (new Date(commit.datetime)).toLocaleTimeString('en-us', { month: 'short', year: 'numeric', day: 'numeric', hour12: false });
                this.files_additions = commit.files_changed.additions;
                this.files_deletions = commit.files_changed.deletions;
                this.files = commit.files_changed.files;
                this.number_file_changed = commit.files_changed.number_file_changed;
                this.message = commit.message;
                this.hexsha = commit.hexsha;
            })
            .catch(error => {
                console.log(error.data);
            });
        }
    }
}
</script>