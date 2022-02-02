<template>
    <div>
        <div class="row d-flex justify-content-between">
            <div class="col-md-9 mb-3">
                <input type="text" class="form-control" placeholder="Filter pull request">
            </div>
            <div class="col-md-3 mb-3 d-grid">
                <button type="button" class="btn btn-success" @click="viewCreatePullRequest()">New pull request</button>
            </div>
        </div>
        <div class="card">
            <ul v-if="pull_requests.length != 0" class="list-group list-group-flush">
                <li v-for="(pr, id) in pull_requests" :key="id" class="list-group-item py-2">
                    <div class="d-flex justify-content-between py-1">
                        <div class="">
                            <a href="#" class="link-list">
                                {{ pr.name }}
                            </a>
                            <br>
                            <span class="badge text-dark">{{ pr.author_name }}</span>
                            <span class="badge text-muted">created at 27/10/2021</span>
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
            pull_requests: [
                {name: '1er pull request', author_name: 'alejandro rafael chavez'},
                {name: '2do pull request', author_name: 'Pablo rafael chavez'}
            ]
        }
    },
    methods: {
        viewCreatePullRequest(){
            this.$emit('newPullRequest');
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