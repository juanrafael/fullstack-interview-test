<template>
    <div class="card">
        <div class="card-header fs-5">
            <BranchList :branches="branches" @selectBranch="selectBranch"></BranchList>
        </div>
        <ul class="list-group list-group-flush">
            <li v-for="(commit, id) in commits" :key="id" class="list-group-item py-3">
                <div class="d-flex justify-content-between">
                    <a href="#">
                        <span class="badge bg-light text-dark">{{ commit.message }}</span>
                    </a>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>

import BranchList from './BranchList.vue';

export default {
    name: 'Commit',
    components: {
        BranchList
    },
    data(){
        return {
            branches: [],
            commits: [],
            branch: '',
        }
    },
    created(){
        this.getBranches();
    },
    watch: {
        branch(){
            this.getCommits(this.branch)
        }
    },
    methods: {
        getBranches() {
            this.$axios
            .get('branches')
            .then(data => {
                const branches = data.data.data;
                this.branches = branches
            })
            .catch(error => {
                console.log(error.data);
            });
        },
        getCommits(branch){
            this.$axios
            .get(`branches/${branch}/commits`)
            .then(data => {
                const commits = data.data.data;
                this.commits = commits
            })
            .catch(error => {
                console.log(error.data);
            });
        },
        selectBranch(branch){
            this.branch = branch
        }
    }
}

</script>