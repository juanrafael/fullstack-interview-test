<template>
    <div class="row justify-content-start">
        <div class="col-4 p-3 d-flex justify-content-start">
            <span>Branch: </span>
            <select class="form-select" v-model="branch">
                <option v-for="(branch, id) in branches" :key="id" :value="branch.name">
                    {{ branch.name }}
                </option>
            </select>
        </div>
    </div>
</template>

<script>

export default {
    name: 'BranchList',
    props: {
        branches: Array,
    },
    data(){
        return {
            branch: ''
        }
    },
    watch: {
        branch(){
            this.changeBranch();
        }
    },
    created(){
        this.changeBranch();
        this.branch = this.branches[0].name;
    },
    methods: {
        changeBranch(){
            this.$emit("selectBranch", this.branch);
        }
    }
}

</script>
