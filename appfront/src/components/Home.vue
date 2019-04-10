<template>
    <el-container>
        <el-header style="background:#909399;text-align:center;color:#FFF">
            <h2>Demo for Uploading!</h2>
        </el-header>
        <el-main>
            <el-row :gutter="10">
                <el-col :span="12">
                    <div class="grid-content bg-purple">
                        <!-- <i class="el-icon-picture" ref='input_icon'></i> -->
                        <img v-bind:src="input_image" width="500px">
                        <p>Input image</p>
                    </div>
                </el-col>
                <el-col :span="12">
                    <div class="grid-content bg-purple">
                        <!-- <i class="el-icon-picture-outline" ref='result_icon'></i> -->
                        <img v-bind:src="result_image" width="500px">
                        <p>Result image</p>
                    </div>
                </el-col>
            </el-row>
            <el-upload
            drag
            :on-progress="handleProgress"
            :on-success="handleSuccess"
            :show-file-list="false"
            action="http://202.114.114.96:8050/upload/">
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            </el-upload>
        </el-main>
    </el-container>
</template>

<script>
export default {
  name: 'upload',
  data () {
    return {
      input_image: '',
      result_image: ''
    }
  },
  methods: {
    handleProgress () {
      this.$refs.input_icon.style.display = 'none'
      this.$refs.result_icon.style.display = 'none'
    },
    handleSuccess (response, file, fileList) {
      this.input_image = response['file_path']
      this.result_image = response['result_path']
    }
  }
}
</script>
