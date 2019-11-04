<template >
    <table >
        <tr>
            <th width="150px">회사 이름</th>
            <th width="200px">제목</th>
        </tr>
        <tr v-for="complaint in user.complaints" :key="complaint.title">
            <td width="150px" >{{complaint.name}}</td>
            <td width="200px" >{{complaint.title}}</td>
        </tr>
    </table>
</template>
<script>
export default {
    name: 'ComplaintList',
    data () {
        return {
            user : {
                complaints : {
                    1 : {
                        title : 'title1',
                        content : 'content1',
                        name : 'name1'
                    },
                    2 : {
                        title : 'title2',
                        content : 'content2',
                        name : 'name2'
                    },
                    3 : {
                        title : 'title3',
                        content : 'content3',
                        name : 'name3'
                    }
                }
            }
        }
    },
    // mounted() {
    //     this.getUser()
    // },
    // methods: {
    //     getUser() {
    //         this.user = firebase.auth().currentUser;
    //         console.log(this.user)
    //     }
    // }    
}
</script>
<style scoped>
#a {
    position: absolute;
    top: 550px;
    left:130px
}
table {
  border-collapse: collapse;
  width: 90%;
  margin-left: auto; 
  margin-right: auto;
  margin-top: 50px;
}
th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  text-align: center;
}
tr:hover {
    background-color:#f5f5f5;
}
</style>