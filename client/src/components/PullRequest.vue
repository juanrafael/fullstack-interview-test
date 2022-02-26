<template>
    <div>
        <div class="row d-flex justify-content-between">
            <div class="col-md-9 mb-3">
                <input type="text" class="form-control" placeholder="Filter pull request" v-model="pr_filter">
            </div>
            <div class="col-md-3 mb-3 d-grid">
                <button type="button" class="btn btn-success" @click="viewCreatePullRequest()">New pull request</button>
            </div>
        </div>
        <div class="card">
            <ul v-if="filterPR.length != 0" class="list-group list-group-flush">
                <li v-for="(pr, id) in filterPR" :key="id" class="list-group-item py-2">
                    <div class="d-flex justify-content-between py-1">
                        <div class="">
                            <a href="#" class="link-list">
                                {{ pr.title }}
                            </a>
                            <br>
                            <span class="badge text-dark">{{ pr.author }}</span>
                            <span class="badge text-muted">created at {{ pr.created_at }}</span>
                        </div>
                    </div>
                </li>
            </ul>
            <div v-else class="d-flex justify-content-center align-items-center" style="min-height: 200px;">
                No records...
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PullRequest',
    data(){
        return {
            pull_requests: [],
            pr_filter: ''
        }
    },
    computed: {
        filterPR(){
            return this.pull_requests.filter(pr => pr.title.toLowerCase().includes(this.pr_filter.toLowerCase()));
        }
    },
    created(){
        this.getPullRequests();
    },
    methods: {
        viewCreatePullRequest(){
            this.$emit('newPullRequest');
        },
        getPullRequests(){
            this.$axios.get('pull_request')
            .then(response => {
                this.pull_requests = response.data.data;
            })
            .catch(error => console.log(error.data));
        }
    }
}
</script>

<style scoped>
a.link-list {
    color: #303030 !important;
    text-decoration: none;
    font-weight: 600;
    font-size: 1rem;
}

span.badge{
    font-weight: 400;
}

a.link-list:hover {
    text-decoration: underline;
}
</style>