<template>
    <div class="card">
        <div class="card-header fs-5">
            All branches
        </div>
        <ul class="list-group list-group-flush">
            <li v-for="(branch, id) in branches" :key="id" class="list-group-item py-3">
                <div class="d-flex justify-content-between">
                    <a href="#">
                        <span class="badge bg-light text-dark">{{ branch.name }}</span>
                    </a>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>

export default {
    name: 'Branch',
    data(){
        return {
            branches: [],
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
        }
    }
}

</script>