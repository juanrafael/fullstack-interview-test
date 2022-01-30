<template>
    <div v-if="branches.length != 0">
        <select class="form-select" v-model="branch">
            <option v-for="(branch, id) in branches" :key="id" :value="branch.name">
                {{ branch.name }}
            </option>
        </select>
    </div>
</template>

<script>

export default {
    name: 'BranchList',
    props: {
        branches: Array,
        selected_branch: String
    },
    data(){
        return {
            branch: ''
        }
    },
    watch: {
        branch(){
            this.changeBranch();
        },
        branches(){
            this.branch = this.selected_branch;
        }
    },
    created(){
        this.changeBranch();
    },
    methods: {
        changeBranch(){
            this.$emit("selectBranch", this.branch);
        }
    }
}

</script>
