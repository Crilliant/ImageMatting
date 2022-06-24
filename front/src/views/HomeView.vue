<template>
<!--  <div class="home">-->
<!--    <img alt="Vue logo" src="../assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--  </div>-->
  <!--上面部分-->
  <div class="up" v-if="model=='main'">
    <div class="in1">
      <p type="primary" class="main-submit">提交图片</p>
      <input ref="relFile" class="main-upload" type="file" :multiple="multiple" :accept="accept" @change="loadpic" >
      <div class="imgBox">
        <img id="cropedBigImg" :src="imageUrl" value='custom' alt="lorem ipsum dolor sit" data-address='' title="自定义背景"/>
      </div>
      <button @click="loadpic_button" class="b1">点击上传图片</button>
    </div>
  </div>
  <div v-if="model=='person_photo'" class="person">
      <button class="backToHome" @click="model='main'">返回首页</button>
      <div class="blockMain">
        <!--      图片位置-->
        <div class="block-one"></div>
        <div class="block-two"></div>

        <div class="select-BGColor" v-cloak>
        </div>
        <button type="primary"  class="download1">一键下载</button>
      </div>
  </div>
  <div v-if="model=='goods_photo'" class="goods">
      <button class="backToHome" @click="model='main'">返回首页</button>
      <div class="blockMain">
        <!--      图片位置-->
        <div class="block-three"></div>

        <button type="primary"  class="download2">一键下载</button>
      </div>

  </div>
  <div v-if="model=='identification'" class="identity">
      <button class="backToHome" @click="model='main'">返回首页</button>
      <div class="blockMain">

        <div class="block-one"></div>
        <div class="block-two"></div>
        <button type="primary"  class="download2">一键下载</button>
        <button type="primary"  class="download3">添加背景</button>
      </div>
  </div>
  <!--中间三个控件-->
  <div class="middle">
    <div >
      <button class="b2" @click="process_person"></button>
    </div>

    <div>
      <button class="b3" @click="process_goods"></button>
    </div>

    <div>
      <button class="b4" @click="process_identification"></button>
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
import request from "@/utils/request";

export default {
  name: 'HomeView',
  components: {

  },data(){
    return{
      model:"main",
      imageUrl:"https://img-blog.csdnimg.cn/c2a88529e4d942aa8f561498826057ba.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAU3V5dW9h,size_20,color_FFFFFF,t_70,g_se,x_16"


    }
  },watch:{


  },methods:{
    send_message(){
      request.post('/user',{}).then()
    },
    process_person(){
      this.model='person_photo'
    },
    process_goods(){
      this.model='goods_photo'
    },
    process_identification(){
      this.model='identification'
    },
    loadpic(e){
      console.log(e.target.files[0])
      const reader = new FileReader()

      reader.readAsDataURL(e.target.files[0])

      reader.onload = () => {
        const _base64 = reader.result

        this.imageUrl = _base64 //将_base64赋值给图片的src，实现图片预览

      }
    },
    loadpic_button() {
      this.$refs.relFile.dispatchEvent(new MouseEvent('click'))
    },
    fileChange() {
      // 上传文件
    }
    // loadpic(){
    //   var filePath = $(this).val(),         //获取到input的value，里面是文件的路径
    //       fileFormat = filePath.substring(filePath.lastIndexOf(".")).toLowerCase(),
    //       src = window.URL.createObjectURL(this.files[0]); //转成可以在本地预览的格式
    //
    //   // 检查是否是图片
    //   if( !fileFormat.match(/.png|.jpg|.jpeg/) ) {
    //     error_prompt_alert('上传错误,文件格式必须为：png/jpg/jpeg');
    //     return;
    //   }
    //
    //   $('#cropedBigImg').attr('src',src);
    // }
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

.main-submit{
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 30px;
  font-weight: 500;
  color: aqua;
  position: absolute;
  margin-top: 100px;
  margin-left: 90px;
}

.main-submit:hover{
  transition: background 180ms;
}
.main-upload{
  cursor: pointer;
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 30px;
  font-weight: 500;
  color: aqua;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  outline: none;
  filter:alpha(opacity=0);
  -moz-opacity:0;
  -khtml-opacity: 0;
  opacity: 0;
}
.imgBox{
  height: 300px;
  width: 400px;
}
#cropedBigImg{
  width: 100%;
  height:auto;
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
/*扣人模块*/
.person{
  width: 80%;
  height: 490px;
  position: relative;
  background:linear-gradient(rgb(153, 244, 244) 0%,white 100%);
  background-size: 100% 100%;
  margin-left: 10%;
  border-radius: 12px;
}

.identity{
  width: 80%;
  height: 490px;
  position: relative;
  background:linear-gradient(rgb(153, 244, 244) 0%,white 100%);
  background-size: 100% 100%;
  margin-left: 10%;
  border-radius: 12px;
}

.goods{
  width: 80%;
  height: 490px;
  position: relative;
  background:linear-gradient(rgb(153, 244, 244) 0%,white 100%);
  background-size: 100% 100%;
  margin-left: 10%;
  border-radius: 12px;
}

.backToHome{
  margin-top:30px;
  margin-left:25px;
  font-size: 25px;
  border-radius: 8px;
  background-color: rgb(153, 244, 244);
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  border: none;
  outline: none;
}

.blockMain{
  width: 80%;
  height: 400px;
  background-color: rgb(255, 250, 230);
  position: absolute;
  margin-top: 30px;
  margin-left: 10%;
  border-radius: 12px;
}

.block-one{
  width: 25%;
  height: 300px;
  background-color: white;
  position: absolute;
  margin-top: 40px;
  margin-left: 10%;
}

.block-two{
  width: 25%;
  height: 300px;
  background-color: white;
  position: absolute;
  margin-top: 40px;
  margin-left: 40%;
}

.select-BGColor{
  margin-left: 77%;
  margin-top: 130px;
}

.download1{
  margin-left: 77%;
  margin-top: 70px;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 25px;
  color: white;
  border-radius: 8px;
  background-color: cornflowerblue;
  border: none;
  outline: none;
}
/*扣物模块*/
.block-three{
  width: 30%;
  height: 300px;
  background-color: white;
  position: absolute;
  margin-top: 40px;
  margin-left: 30%;
}

.download2{
  margin-left: 77%;
  margin-top: 180px;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 25px;
  color: white;
  border-radius: 8px;
  background-color: cornflowerblue;
  border: none;
  outline: none;
}

/*证件照模块*/
.download3{
  margin-left: 77%;
  margin-top: 50px;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 25px;
  color: white;
  border-radius: 8px;
  background-color: cornflowerblue;
  border: none;
  outline: none;
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