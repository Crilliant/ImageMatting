<template>
<!--  <div class="home">-->
<!--    <img alt="Vue logo" src="../assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--  </div>-->
  <!--上面部分-->
  <div class="up" v-if="model=='main'">
    <div class="in1">
      <p class="p1">提交图片</p>
      <button type="primary"  class="b1">
        选择图片
      </button>
    </div>
  </div>
  <div v-if="model=='person_photo'" class="person_block">

  </div>
  <div v-if="model=='goods_photo'" class="goods_block">

  </div>
  <div v-if="model=='identification'" class="identity_block">

  </div>
  <!--中间三个控件-->
  <div class="middle">
    <div >
      <button class="b2" @click="model='person_photo'"></button>
    </div>

    <div>
      <button class="b3" @click="model='goods_photo'"></button>
    </div>

    <div>
      <button class="b4" @click="model='identification'"></button>
    </div>
  </div>

  <!--下面部分-->
  <div class="down">
    <div class="d1">
    </div>

    <div class="d3">
    </div>

    <div class="d2">
    </div>
  </div>

  <!--真的最下面了-->
  <div class="bottom">
    <p class="p2">不同场景，无所不能</p>
    <p class="p3">释放无限创意</p>
  </div>
</template>

<script>
// @ is an alias to /src
//先把图片上传显示出来
//加一个a标签，获取图片的流，点download下载就好了
export default {
  name: 'HomeView',
  components: {

  },data(){
    return{
      model:"main"
    }
  },watch:{
      // scwj(val){
      // this.img = val}
  },methods:{
    xztp() {
      var bqa = document.createElement("a");
      console.log(bqa);
      bqa.setAttribute("href", URL.createObjectURL(filename.files[0]));
      bqa.setAttribute("download", filename.name);
      bqa.click();
    }
  }
}

</script>
<style>
/*上面整个组件*/
.up{
  width: 80%;
  height: 490px;
  background-image: url('../assets/1.png');
  background-repeat: no-repeat;
  background-size: 100% 100%;
  position: relative;
  margin-left: 10%;
}
.in1{
  width: 300px;
  height: 200px;
  background-image: url('../assets/2.png');
  background-size: 100% 100%;
  margin-left:60% ;
  position: absolute;
  margin-top: 120px;
}

.p1{
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 30px;
  font-weight: 500;
  color: aqua;
  position: absolute;
  margin-top: 100px;
  margin-left: 90px;
}

/*选择图片按钮*/
.b1{
  width: 150px;
  height: 50px;
  color: white;
  background-color: rgb(69, 69, 198);
  position: absolute;
  margin-top: 220px;
  margin-left: 75px;
  border-radius: 12px;
}

.b1:hover{
  background-color: rgb(53, 132, 201);
}
/*人物模块*/
.person_block {
  width: 80%;
  height: 490px;
  background: aqua;
}
/*物品模块*/
.goods_block {
  width: 80%;
  height: 490px;
  background: black;
}
/*证件照模块*/
.identity_block {
  width: 80%;
  height: 490px;
  background:yellow;
}
/* 中间三个控件*/
.middle{
  position: absolute;
  width: 80%;
  height: 200px;
  margin-left: 10%;
}

.b2{
  width: 150px;
  height: 150px;
  background-image: url('../assets/5.jpg');
  background-size: 100% 100%;
  position: absolute;
  margin-left: 30%;
  margin-top: 20px;
  border-width: 3px;
  border-color: aqua;
}

.b3{
  width: 150px;
  height: 150px;
  background-image: url('../assets/3.jpg');
  background-size: 100% 100%;
  position: absolute;
  margin-left: 45%;
  margin-top: 20px;
  border-width: 3px;
  border-color: aqua;
}

.b4{
  width: 150px;
  height: 150px;
  background-image: url('../assets/4.jpg');
  background-size: 100% 100%;
  position: absolute;
  margin-left: 60%;
  margin-top: 20px;
  border-width: 3px;
  border-color: aqua;
}

/*下面部分*/
.down{
  width: 80%;
  height: 600px;
  margin-left: 10%;
  margin-top: 200px;
  position: absolute;
  background-size: 100% 100%;
  background-color: rgb(245, 246, 246);
}

.d1{
  width: 300px;
  height: 400px;
  position: absolute;
  margin-left: 13%;
  margin-top: 100px;
  background-image: url('../assets/6.jpg');
}

.d3{
  width: 250px;
  height: 250px;
  position: absolute;
  margin-top: 150px;
  margin-left: calc(50% - 110px);
  background-image: url('../assets/8.png');
  background-size: 100% 100%;
}

.d2{
  width: 300px;
  height: 400px;
  position: absolute;
  margin-left: 65%;
  margin-top: 100px;
  background-image: url('../assets/7.jpg');
}

/*最下面*/
.bottom{
  width: 80%;
  height: 400px;
  position: absolute;
  margin-left: 10%;
  margin-top: 800px;
  background-color:white;
}

.p2{
  font-size: 80px;
  position: absolute;
  margin-top: 120px;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  margin-left: calc(50% - 360px);
}

.p3{
  font-size: 40px;
  position: absolute;
  margin-top: 250px;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  margin-left: calc(50% - 120px);
}
</style>