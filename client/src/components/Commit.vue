<template>
    <div class="">
        <div class="row d-flex justify-content-between">
            <div class="col-md-4 mb-3">
                <BranchList
                :branches="branches"
                @selectBranch="changeBranch"></BranchList>
            </div>
            <div class="col-md-4 mb-3">
                <input type="text" class="form-control" placeholder="Search by message" v-model="commit_filter">
            </div>
        </div>
        <div v-for="(commits, i) in formatCommits" :key="i" class="">
            <div class="">
                <div class="bg-secondary bg-opacity-10 p-2 mx-3 border-bottom border-2">Commits on {{ commits.date }}</div>
            </div>
            <ul class="list-group list-group-flush">
                <li v-for="(commit, id) in commits.commits" :key="id" class="list-group-item py-2">
                    <div class="d-flex justify-content-between py-2">
                        <div class="d-flex align-items-center">
                            <div class="p-2"><i class="far fa-user fa-2x"></i></div>
                            <div class="">
                                <a href="#" class="link-list">{{ commit.message }}</a>
                                <br>
                                <span class="badge text-dark">{{ commit.author.name }}</span>
                                <span class="badge text-muted">committed on {{ formatDatetime(commit.datetime) }}</span>
                            </div>
                        </div>
                        <div>
                            <button type="button" class="btn btn-light border border-2">{{ commit.hexsha }}</button>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
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
            commit_filter: '',
        }
    },
    computed: {
        formatCommits(){
            let new_commits = [];
            let dates = [];
            this.filterCommits.forEach((commit, i) => {
                const datetime = new Date(commit.datetime);
                const date_format = datetime.toLocaleString('en-us', {month: 'short', year: 'numeric', day: 'numeric'});
                if (dates.includes(date_format)) {
                    const indice = dates.indexOf(date_format);
                    new_commits[indice].commits.push(commit);
                }else{
                    dates.push(date_format);
                    new_commits.push({
                        date: date_format,
                        commits: [],
                    });
                    new_commits[i].commits.push(commit);
                }
            });
            return new_commits;
        },
        filterCommits(){
            return this.commits.filter(commit => commit.message.toLowerCase().includes(this.commit_filter.toLowerCase()));
        }
    },
    created(){
        this.getBranches();
    },
    watch: {
        branch(){
            this.commit_filter = '';
            this.commits = [];
            this.getCommits(this.branch);
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
        changeBranch(branch){
            this.branch = branch
        },
        formatDatetime(datetime){
            const date_format = new Date(datetime);
            return date_format.toLocaleTimeString('en-us', { month: 'short', year: 'numeric', day: 'numeric', hour12: false });
        }
    }
}

</script>

<style scoped>
a.link-list {
    color: #303030 !important;
    text-decoration: none;
    font-weight: 600;
    font-size: .9rem;
}

span.badge{
    font-weight: 400;
}

a.link-list:hover {
    text-decoration: underline;
}
</style>