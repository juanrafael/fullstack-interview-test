<template>
    <div class="">
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Search branches..." v-model="branch_filter">
        </div>
        <ul v-if="filterBranches.length != 0" class="list-group list-group-flush">
            <li v-for="(branch, id) in filterBranches" :key="id" class="list-group-item py-2">
                <div class="d-flex justify-content-between">
                    <div class="d-flex align-items-center">
                        <span class="fas fa-code-branch"></span>
                        <a href="#" @click="clickBranch(branch.name)">
                            <span class="badge bg-light text-dark">{{ branch.name }}</span>
                        </a>
                    </div>
                    <div class="">
                        <button type="button" class="btn btn-outline-success btn-sm me-3" @click="clickBranch(branch.name)">View commits</button>
                        <button type="button" class="btn btn-outline-secondary btn-sm">New pull request</button>
                    </div>
                </div>
            </li>
        </ul>
        <div v-else class="text-center">
            No branches found matching <b>"{{ branch_filter }}"</b>.
        </div>
    </div>
</template>

<script>

export default {
    name: 'Branch',
    data(){
        return {
            branches: [],
            branch_filter: '',
        }
    },
    computed: {
        filterBranches(){
            return this.branches.filter(branch => branch.name.toLowerCase().includes(this.branch_filter.toLowerCase()));
        }
    },
    created(){
        this.getBranches();
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
        clickBranch(branch_name){
            this.$emit("clickBranch", branch_name);
        }
    }
}

</script>