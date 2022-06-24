<template>
  <div class="main" v-if="model=='main'">
    <div class="main-photo">
      <p type="primary" class="main-submit">提交图片</p>
      <input ref="class" class="main-upload" type="file" :multiple="multiple" :accept="accept" @change="handleFiles"/>
<!--      <button type="primary"  class="main-select">-->
<!--        <--选择图片-->
<!--      </button>-->
    </div>
  </div>
  <div class="person" v-if="model=='person'">
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
  <div class="goods" v-if="model=='goods'">
    <button class="backToHome" @click="model='main'">返回首页</button>
    <div class="blockMain">
      <!--      图片位置-->
      <div class="block-three"></div>

      <button type="primary"  class="download2">一键下载</button>
    </div>
  </div>
  <div class="identity" v-if="model=='identity'">
    <button class="backToHome" @click="model='main'">返回首页</button>
    <div class="blockMain">

      <div class="block-one"></div>
      <div class="block-two"></div>
      <button type="primary"  class="download2">一键下载</button>
      <button type="primary"  class="download3">添加背景</button>
    </div>
  </div>
  <div>
<!--    <img :src=newIcon />-->
    <div class="middle">
      <div >
        <button class="personBtn" @click="a_func"></button>
      </div>

      <div>
        <button class="goodsBtn" @click="model='goods'"></button>
      </div>

      <div>
        <button class="identityBtn" @click="model='identity'"></button>
      </div>
    </div>

    <!--下面部分-->
    <div class="down">
      <div class="down-photo1">
      </div>

      <div class="down-photo3">
      </div>

      <div class="down-photo2">
      </div>
    </div>

    <!--真的最下面了-->
    <div class="bottom">
      <p class="text1">不同场景，无所不能</p>
      <p class="text2">释放无限创意</p>
    </div>
  </div>
</template>

<script>

import Header from "../components/Header";
// import upload from './uplode';
// import {debounce} from 'lodash/function';

export default {
  name: 'Home',
  components: {
    Header
  },data(){
    return{
      model:"main",
      accept:'.jpg,.jpeg,.png,.gif',
      multiple:false,
      uploadFinished:true,
      startIndex:0,
      maxSize:10*1024*1024,
      list:[],
      // newIcon:'',

    }
  },methods:{
    a_func(){
      this.model="person"
      // var sr='/src/assets/1.png'
      // this.b_fun(sr);
    },
    // b_fun(String){
    //   this.newIcon=require(String);
    // },
    reset(){
      this.list=[];
      this.source.cancel();
      this.startIndex=0;
      this.uploadFinished=true;
      this.$ref.input && (this.$ref.input.value=null);
    },
    // handleUpClick:debounce(function () {
    //   this.$ref.input.click();
    // },300),
    handleFiles(e){
      const files=e?.target?.files;
      this.readFiles(files);
    },
    readFiles(files) {
      if (!files || files.length <= 0) {
        return;
      }
      for (const file of files) {
        const url = window.URL.createObjectURL(file);
        const obj = {
          title: file.name.replace(/(.*\/)*([^.]+).*/ig, '$2'), // 去掉文件后缀
          url,
          file,
          fileType: file.type,
          status: 0, // 状态 -> 0 等待中，1 完成， 2 正在上传，3 上传失败
          percent: 0, // 上传进度
        };
        // 提前在 data 中定义 list，用来保存需要上传的文件
        this.list.unshift(obj);
        this.$emit('fileList', this.list);
        this.newIcon=require('url')
      }
      // 在 data 中定义 startIndex 初始值为 0，上传完成后更新，用于追加上传文件
      // this.startUpload(this.startIndex);
    },
  }
}


</script>
