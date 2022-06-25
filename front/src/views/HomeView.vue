<template>
  <!--  <div class="home">-->
  <!--    <img alt="Vue logo" src="../assets/logo.png">-->
  <!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  <!--  </div>-->
<!--  新增导航栏-->
  <div class="daohang">
    <div class="mm">

    </div>
  </div>
  <!--上面部分-->
  <div class="up" v-if="model=='main'">
    <div class="in1">
      <form enctype="multipart/form-data" method="post">
        <p type="primary" class="main-submit">提交图片</p>
        <input ref="relFile" name="file" class="main-upload" type="file" :multiple="multiple" :accept="accept" @change="loadpic" >
        <div class="imgBox">
          <img id="cropedBigImg" :src="url_of_local_load" value='custom' alt="lorem ipsum dolor sit" data-address='' title="自定义背景"/>
        </div>
      </form>
      <button @click="loadpic_button" class="b1">点击上传图片</button>
    </div>
    <div class="d1">
    </div>

    <div class="d3">
    </div>

    <div class="d2">
    </div>
  </div>
  <div v-if="model=='person_photo'" class="person">
    <button class="backToHome" @click="model='main'">返回首页</button>
    <div class="blockMain">
      <!--      图片位置-->
      <div class="block-one">
        <img id="result_img_1" :src="url_for_person_process" value='custom' alt="lorem ipsum dolor sit" data-address='' title="自定义背景"/>
      </div>
      <div class="block-two"></div>

      <div class="select-BGColor" v-cloak>
      </div>

      <button type="primary"  class="download1">一键下载</button>
      <div class="pe1">
      </div>
      <div class="pe2">
      </div>
      <div class="pe3">
      </div>
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
    <div class="bg1"></div>
    <div class="bg2"></div>
    <div class="bg3"></div>
    <div class="bg4"></div>
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

    <div>
      <button class="b5" @click="process_identification"></button>
    </div>
  </div>

  <!--下面部分-->
  <div class="down">
    <div style="width:800px;height:1px;margin:70px auto;
    padding:0px;background-color:#D5D5D5;overflow:hidden;">
    </div>
<!--    <div class="d1">-->
<!--    </div>-->

<!--    <div class="d3">-->
<!--    </div>-->

<!--    <div class="d2">-->
<!--    </div>-->
  </div>

  <!--真的最下面了-->
  <div class="bottom">
    <p class="p2">不同场景，无所不能</p>
    <p class="p3">释放无限创意</p>
    <p class="p4">联系我们</p>
    <p class="p5">E-mail:3054229818@qq.com</p>
    <p class="p6">QQ:3054229818</p>
    <p class="p7">Tel:18672782521</p>
    <div style="width:1000px;height:1px;margin:350px auto;
    padding:0px;background-color:#D5D5D5;overflow:hidden;">
    </div>
    <div class="p8">
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
//先把图片上传显示出来
//加一个a标签，获取图片的流，点download下载就好了
import request from "@/utils/request";
import axios from "axios";

export default {
  name: 'HomeView',
  components: {

  },data(){
    return{
      model:"main",
      url_of_local_load:"",
      url_for_person_process:"",
      src_of_result:""
    }
  },watch:{


  },methods:{
    send_message(){
      request.post('/user',{}).then()
    },
    translateBase64ImgToFile(base64,filename,contentType){
      let arr = base64.split(',')  //去掉base64格式图片的头部
      let bstr = atob(arr[1])   //atob()方法将数据解码
      let length = bstr.length
      let u8arr = new Uint8Array(length);
      while(length--){
        u8arr[length] =  bstr.charCodeAt(length) //返回指定位置的字符的 Unicode 编码
      }
      return new File([u8arr],filename,{type:contentType})
    },
    process_person(){
      this.model='person_photo';
      let file = this.translateBase64ImgToFile(this.url_of_local_load, 'test.png', 'image/png')
      let param = new FormData();
      param.append('file',file,file.name)
      request.post('/api/image/upload',param).then(res=>{
          if(res.status=='success'){
            var r=confirm("照片处理中，请稍后");
            this.src_of_result = res.message
          }else {
            var r=confirm("上传有误");
          };
        this.load_result_pic()
      })
      //request.post('/test').then()


    },
    load_result_pic(){
      axios.post(' http://127.0.0.1:5000/api/image/download',
          {  //body参数
            filename:'1.png'}, {headers: {  //头部参数
              'Content-Type': 'application/json',

            }
          }
      ).then(res=> { //请求成功
        console.log(res)
        this.url_for_person_process = res.data
        console.log(this.url_for_person_process)
          })

      },
    process_goods(){
      this.model='goods_photo'
    },
    process_identification(){
      this.model='identification'
    },
    loadpic(e){
      //console.log(e.target.files[0])
      const reader = new FileReader()

      reader.readAsDataURL(e.target.files[0])

      reader.onload = () => {
        const _base64 = reader.result
        this.url_of_local_load = _base64 //将_base64赋值给图片的src，实现图片预览
        //console.log(_base64)
        console.log(this.url_of_local_load)
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
/*导航栏*/
.daohang{
  width: 80%;
  height: 40px;
  margin-left: 10%;
  z-index:999;
  background-color: aliceblue;
}
.mm{
  width: 40px;
  height: 40px;
  background-image: url('../assets/1.png');
  /*background-image: url('../assets/22.png');*/
  background-repeat: no-repeat;
  background-size: 100% 100%;
  position: relative;
  margin-left: 1%;
  z-index:999;
}
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
  width: 250px;
  height: 300px;
  background-image: url('../assets/2.png');
  background-size: 100% 100%;
  margin-left:60% ;
  position: absolute;
  margin-top: 70px;
}

.main-submit{
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 30px;
  font-weight: 500;
  color: #0099FF;
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
  color: #0099FF;
  position: absolute;
  width: 100%;
  height: 100%;
  outline: none;
  filter:alpha(opacity=0);
  -moz-opacity:0;
  -khtml-opacity: 0;
  opacity: 0;
}
.imgBox{
  display: table-cell;
  vertical-align: middle;
  height: 300px;
  width: 400px;
}
#cropedBigImg{
  width: 250px;
}
/*选择图片按钮*/
.b1{
  width: 150px;
  height: 50px;
  color: white;
  background-color: #0099FF;;
  position: absolute;
  margin-top: 10px;
  margin-left: 60px;
  border-radius: 12px;
}

.b1:hover{
  background-color: rgb(0, 119, 255);
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
  background-color: aliceblue;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  border: none;
  outline: none;
}

.blockMain{
  width: 90%;
  height: 400px;
  background-color: rgb(255, 250, 230);
  position: absolute;
  margin-top: 20px;
  margin-left: 5%;
  border-radius: 12px;
}

.block-one{
  width: 25%;
  height: 300px;
  background-color: white;
  position: absolute;
  margin-top: 40px;
  margin-left: 10%;
  display: table-cell;
  vertical-align: center;
}
#result_img_1{
  width: 100%;
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
  background-color: #0099FF;
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
  background-color: #0099FF;
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
/* 中间4个控件*/
.middle{
  position: absolute;
  width: 80%;
  height: 200px;
  margin-left: 10%;
  background-color: #F7F9FB;
}

.b2{
  width: 150px;
  height: 150px;
  background-image: url('../assets/5.jpg');
  background-size: 100% 100%;
  position: absolute;
  margin-left: 33%;
  margin-top: 40px;
  border-width: 3px;
  border: none;
  box-shadow: 0px 0px 10px #888888;
}
.b2:hover{
  box-shadow: 0px 0px 10px #5E5D5D;
}
.b2:active{
  box-shadow: 0px 0px 10px #888888;
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
  border: none;
  box-shadow: 0px 0px 10px #888888;
}
.b3:hover{
  box-shadow: 0px 0px 10px #5E5D5D;
}
.b3:active{
  box-shadow: 0px 0px 10px #888888;
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
  border: none;
  box-shadow: 0px 0px 10px #888888;
}
.b4:hover{
  box-shadow: 0px 0px 10px #5E5D5D;
}
.b4:active{
  box-shadow: 0px 0px 10px #888888;
}

.b5{
  width: 150px;
  height: 150px;
  background-image: url('../assets/1.png');
  /*background-image: url('../assets/9.png');*/
  background-size: 100% 100%;
  position: absolute;
  margin-left: 68%;
  margin-top: 40px;
  border-width: 3px;
  border: none;
  box-shadow: 0px 0px 10px #888888;
}
.b5:hover{
  box-shadow: 0px 0px 10px #5E5D5D;
}
.b5:active{
  box-shadow: 0px 0px 10px #888888;
}
/*下面部分*/
.down{
  width: 80%;
  height: 400px;
  margin-left: 10%;
  margin-top: 200px;
  position: absolute;
  background-size: 100% 100%;
  background-color: #F7F9FB;
}
#swiper-roll .roll-wrapper{
  width:100%;
  overflow: hidden;
  height: 130px;
  margin: 0 auto;
  position: relative;
}
.roll-wrapper li{
  float: left;
  list-style: none;
  width: 150px;
  height: 130px;
}
.roll-wrapper ul{
  position: absolute;
  top: 0;
  left: 0;
}
.d1{
  width: 300px;
  height: 150px;
  background-size: 100% 100%;
  position: absolute;
  margin-left: 6%;
  margin-top: 830px;
  z-index:999;
  background-image: url('../assets/6.jpg');
  /*background-image: url('../assets/10.png');*/
}

.d3{
  width: 300px;
  height: 150px;
  background-size: 100% 100%;
  position: absolute;
  margin-top: 830px;
  margin-left: calc(46% - 110px);
  /*background-image: url('../assets/11.png');*/
  background-size: 100% 100%;
  z-index:999;
  background-image: url('../assets/8.png');
}

.d2{
  width: 300px;
  height: 150px;
  background-size: 100% 100%;
  position: absolute;
  margin-left: 65%;
  margin-top: 810px;
  /*background-image: url('../assets/12.png');*/
  z-index:999;
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
.p4{
  font-size: 30px;
  position: absolute;
  margin-top: 460px;
  margin-left: 60%;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  color: #837F7F;
}
.p5{
  font-size: 30px;
  position: absolute;
  margin-top: 520px;
  margin-left: 60%;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  color: #837F7F;
}
.p6{
  font-size: 30px;
  position: absolute;
  margin-top: 580px;
  margin-left: 60%;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  color: #837F7F;
}
.p7{
  font-size: 30px;
  position: absolute;
  margin-top: 640px;
  margin-left: 60%;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  color: #837F7F;
}
.p8{
  width: 80px;
  height: 80px;
  background-image: url('../assets/1.png');
  /*background-image: url('../assets/13.png');*/
  background-size: 100% 100%;
  position: absolute;
  margin-left: 60%;
  margin-top: 0px;
  border: none;
  box-shadow: 0px 0px 10px #888888;
}
.pe1{
  width: 300px;
  height: 150px;
  background-size: 100% 100%;
  position: absolute;
  margin-left: 6%;
  margin-top: 450px;
  z-index:999;
  background-image: url('../assets/1.png');
  /*background-image: url('../assets/15.png');*/
}
.pe2{
  width: 150px;
  height: 220px;
  background-size: 100% 100%;
  position: absolute;
  margin-left: 45%;
  margin-top: 450px;
  z-index:999;
  background-image: url('../assets/1.png');
  /*background-image: url('../assets/17.png');*/
}
.pe3{
  width: 150px;
  height: 220px;
  background-size: 100% 100%;
  position: absolute;
  margin-left: 65%;
  margin-top: 450px;
  z-index:999;
  background-image: url('../assets/1.png');
  /*background-image: url('../assets/16.png');*/
}
.bg1{
  width: 150px;
  height: 220px;
  background-size: 100% 100%;
  position: absolute;
  margin-left: 15%;
  margin-top: 730px;
  z-index:999;
  background-image: url('../assets/1.png');
  /*background-image: url('../assets/18.png');*/
}
.bg2{
  width: 150px;
  height: 220px;
  background-size: 100% 100%;
  position: absolute;
  margin-left: 35%;
  margin-top: 730px;
  z-index:999;
  background-image: url('../assets/1.png');
  /*background-image: url('../assets/19.png');*/
}
.bg3{
  width: 150px;
  height: 220px;
  background-size: 100% 100%;
  position: absolute;
  margin-left: 50%;
  margin-top: 730px;
  z-index:999;
  /*background-image: url('../assets/20.png');*/
  background-image: url('../assets/1.png');
}
.bg4{
  width: 150px;
  height: 220px;
  background-size: 100% 100%;
  position: absolute;
  margin-left: 70%;
  margin-top: 730px;
  z-index:999;
  background-image: url('../assets/1.png');
  /*background-image: url('../assets/21.png');*/
}
</style>
