<template>
    <div>
        <div class="row">
            <div class="col mb-3">
                <h5>New pull request</h5>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6 mb-3">
                <div class="card">
                    <div class="card-header">
                        Source branch
                    </div>
                    <div class="card-body">
                        <BranchList
                        :branches="branches"
                        :selected_branch="select_branch_source"
                        @selectBranch="changeBranchSource"></BranchList>
                    </div>
                </div>
            </div>
            <div class="col-md-6 mb-3">
                <div class="card">
                    <div class="card-header">
                        Target branch
                    </div>
                    <div class="card-body">
                        <BranchList
                        :branches="branches"
                        :selected_branch="select_branch_target"
                        @selectBranch="changeBranchTarget"></BranchList>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col mb-3">
                <div class="card">
                    <div class="card-body">
                        <form>
                            <div class="mb-3 row">
                                <label for="title_pull_request" class="col-md-2 col-form-label text-md-end">Title:</label>
                                <div class="col-md-10">
                                    <input type="text" class="form-control" id="title_pull_request" v-model="title">
                                </div>
                            </div>
                            <div class="mb-3 row">
                                <label for="description_pull_request" class="col-md-2 col-form-label text-md-end">Description:</label>
                                <div class="col-md-10">
                                    <textarea id="description_pull_request" class="form-control" cols="30" rows="5" v-model="description"></textarea>
                                </div>
                            </div>
                            <div class="mb-3 row">
                                <div class="col">
                                    <button
                                    type="button"
                                    class="btn btn-success float-end"
                                    :disabled="disabledButton"
                                    @click="savePullRequest()">Create pull request</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import BranchList from './BranchList.vue';
import iziToast from 'izitoast';

export default {
    name: 'CreatePullRequest',
    components: {
        BranchList,
    },
    props: {
        branch_name: String
    },
    data(){
        return {
            branches: [],
            select_branch_source: '',
            select_branch_target: '',
            title: '',
            description: '',
        }
    },
    created(){
        this.getBranches();
    },
    computed:{
        disabledButton(){
            if (
                this.select_branch_source == '' ||
                this.select_branch_target == '' ||
                this.title.length == 0 ||
                this.description.length == 0
            ) {
                return true;
            }

            return false;
        }
    },
    methods: {
        getBranches() {
            this.$axios
            .get('branches')
            .then(data => {
                const branches = data.data.data;
                this.branches = branches;

                if (!this.branch_name || this.branch_name == "") {
                    this.select_branch_source = this.branches[0].name;
                }else{
                    this.select_branch_source = this.branch_name;
                }

                this.select_branch_target = this.branches[0].name;
            })
            .catch(error => {
                console.error(error.data);
            });
        },
        changeBranchSource(branch) {
            this.select_branch_source = branch;
        },
        changeBranchTarget(branch){
            this.select_branch_target = branch;
        },
        savePullRequest(){
            this.$axios
            .post('pull_request',
            {
                branch_source: this.select_branch_source,
                branch_target: this.select_branch_target,
                title: this.title,
                description: this.description
            })
            .then(response => {
                iziToast.success({
                    title: 'Success',
                    message: response.data.message
                })

                this.$emit("viewPullRequests", 'PullRequest');
            })
            .catch(error => {
                iziToast.error({
                    title: 'Error',
                    message: error.data.message
                })
            });
        }
    }
}
</script>