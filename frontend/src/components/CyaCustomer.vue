<template>
  <div>
    <el-row>
      <h3>查询</h3>
    </el-row>
    <el-row>
      <el-form :inline="true" :model="queryCusForm" :rules="queryCusRules" ref="queryCusForm" label-width="100px" class="demo-form-inline">
        <el-form-item label="身份证号" prop="custom_id">
          <el-input v-model="queryCusForm.custom_id" placeholder="客户身份证号"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="custom_name">
          <el-input v-model="queryCusForm.custom_name" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="custom_phone">
          <el-input v-model="queryCusForm.custom_phone" placeholder="手机号"></el-input>
        </el-form-item>
        <el-form-item label="地址" prop="custom_address">
          <el-input v-model="queryCusForm.custom_address" placeholder="家庭住址"></el-input>
        </el-form-item>
        <el-form-item label="联系人姓名" prop="contact_name">
          <el-input v-model="queryCusForm.contact_name" placeholder="联系人姓名"></el-input>
        </el-form-item>
        <el-form-item label="联系人电话" prop="contact_phone">
          <el-input v-model="queryCusForm.contact_phone" placeholder="联系人电话"></el-input>
        </el-form-item>
        <el-form-item label="联系人邮箱" prop="contact_email">
          <el-input v-model="queryCusForm.contact_email" placeholder="联系人邮箱"></el-input>
        </el-form-item>
        <el-form-item label="二者关系" prop="contact_custom_relation">
          <el-input v-model="queryCusForm.contact_custom_relation" placeholder="二者关系"></el-input>
        </el-form-item>
        <el-form-item class="button-right">
          <el-button type="primary" size="medium" @click="queryCusSubmit">查询</el-button>
        </el-form-item>
        <el-form-item class="button-right">
          <el-button size="medium" @click="clearQueryForm">清空</el-button>
        </el-form-item>
      </el-form>
    </el-row>

    <el-row>
      <h3>客户列表</h3>
      <!-- <h3>
        客户列表
        <el-button type="primary" size="medium" @click="queryCusSubmit" class="button-right">查询</el-button>
      </h3> -->
    </el-row>
    <el-row>
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="custom_id"
          label="客户身份证号"
          width="200">
        </el-table-column>
        <el-table-column
          prop="custom_name"
          label="姓名"
          width="100">
        </el-table-column>
        <el-table-column
          prop="custom_phone"
          label="手机号"
          width="130">
        </el-table-column>
        <el-table-column
          prop="custom_address"
          label="家庭住址"
          width="160">
        </el-table-column>
        <el-table-column
          prop="contact_name"
          label="联系人姓名"
          width="100">
        </el-table-column>
        <el-table-column
          prop="contact_phone"
          label="联系人电话"
          width="140">
        </el-table-column>
        <el-table-column
          prop="contact_email"
          label="联系人邮箱"
          width="170">
        </el-table-column>
        <el-table-column
          prop="contact_custom_relation"
          label="二者关系"
          width="100">
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-row>

    <el-row>
      <h3>添加新客户</h3>
    </el-row>
    <el-row>
      <el-form :inline="true" :model="addCusForm" :rules="addCusRules" ref="addCusForm" label-width="100px" class="demo-form-inline">
        <el-form-item label="身份证号" prop="custom_id">
          <el-input v-model="addCusForm.custom_id" placeholder="客户身份证号"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="custom_name">
          <el-input v-model="addCusForm.custom_name" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="custom_phone">
          <el-input v-model="addCusForm.custom_phone" placeholder="手机号"></el-input>
        </el-form-item>
        <el-form-item label="地址" prop="custom_address">
          <el-input v-model="addCusForm.custom_address" placeholder="家庭住址"></el-input>
        </el-form-item>
        <el-form-item label="联系人姓名" prop="contact_name">
          <el-input v-model="addCusForm.contact_name" placeholder="联系人姓名"></el-input>
        </el-form-item>
        <el-form-item label="联系人电话" prop="contact_phone">
          <el-input v-model="addCusForm.contact_phone" placeholder="联系人电话"></el-input>
        </el-form-item>
        <el-form-item label="联系人邮箱" prop="contact_email">
          <el-input v-model="addCusForm.contact_email" placeholder="联系人邮箱"></el-input>
        </el-form-item>
        <el-form-item label="二者关系" prop="contact_custom_relation">
          <el-input v-model="addCusForm.contact_custom_relation" placeholder="二者关系"></el-input>
        </el-form-item>
        <el-form-item class="button-right">
          <el-button type="primary" size="medium" @click="addCusSubmit">添加</el-button>
        </el-form-item>
      </el-form>
    </el-row>

    <!--点击“编辑”按钮弹出的页面-->
    <el-dialog title="修改客户信息" :visible.sync="dialogFormVisible">
      <el-form :inline="true" :model="editCusForm" :rules="addCusRules" label-width="100px" class="demo-form-inline">
        <el-form-item label="身份证号" prop="custom_id">
          <el-input v-model="editCusForm.custom_id" placeholder="客户身份证号"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="custom_name">
          <el-input v-model="editCusForm.custom_name" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="custom_phone">
          <el-input v-model="editCusForm.custom_phone" placeholder="手机号"></el-input>
        </el-form-item>
        <el-form-item label="地址" prop="custom_address">
          <el-input v-model="editCusForm.custom_address" placeholder="家庭住址"></el-input>
        </el-form-item>
        <el-form-item label="联系人姓名" prop="contact_name">
          <el-input v-model="editCusForm.contact_name" placeholder="联系人姓名"></el-input>
        </el-form-item>
        <el-form-item label="联系人电话" prop="contact_phone">
          <el-input v-model="editCusForm.contact_phone" placeholder="联系人电话"></el-input>
        </el-form-item>
        <el-form-item label="联系人邮箱" prop="contact_email">
          <el-input v-model="editCusForm.contact_email" placeholder="联系人邮箱"></el-input>
        </el-form-item>
        <el-form-item label="二者关系" prop="contact_custom_relation">
          <el-input v-model="editCusForm.contact_custom_relation" placeholder="二者关系"></el-input>
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="commitEdit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CyaCustomer',
  data: function () {
    return {
      tableData: [],
      addCusForm: {
        custom_id: '',
        custom_name: '',
        custom_phone: '',
        custom_address: '',
        contact_name: '',
        contact_phone: '',
        contact_email: '',
        contact_custom_relation: ''
      },
      addCusRules: {
        custom_id: [
          { required: true, message: '请输入客户身份证号', trigger: 'change' },
          { min: 18, max: 18, message: '长度为 18 个字符', trigger: 'change' },
          { validator: this.validateCustomId, trigger: 'change' }
        ],
        custom_name: [
          { required: true, message: '请输入客户姓名', trigger: 'change' },
          { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'change' }
        ],
        custom_phone: [
          { required: true, message: '请输入客户电话', trigger: 'change' },
          { pattern: '^[0-9]*$', message: '手机号只允许出现数字', trigger: 'change' },
          { min: 7, max: 11, message: '长度在 7 到 11 个字符', trigger: 'change' }
        ],
        custom_address: [
          { required: true, message: '请输入客户地址', trigger: 'change' },
          { min: 1, max: 100, message: '长度在 1 到 100 个字符', trigger: 'change' }
        ],
        contact_name: [
          { required: true, message: '请输入联系人姓名', trigger: 'change' },
          { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'change' }
        ],
        contact_phone: [
          { required: true, message: '请输入联系人电话', trigger: 'change' },
          { pattern: '^[0-9]*$', message: '手机号只允许出现数字', trigger: 'change' },
          { min: 7, max: 11, message: '长度在 7 到 11 个字符', trigger: 'change' }
        ],
        contact_email: [
          { required: true, message: '请输入联系人邮箱', trigger: 'change' },
          { min: 1, max: 30, message: '长度在 1 到 30 个字符', trigger: 'change' }
        ],
        contact_custom_relation: [
          { required: true, message: '请输入二者关系', trigger: 'change' },
          { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'change' }
        ]
      },
      queryCusForm: {
        custom_id: '',
        custom_name: '',
        custom_phone: '',
        custom_address: '',
        contact_name: '',
        contact_phone: '',
        contact_email: '',
        contact_custom_relation: ''
      },
      queryCusRules: {
        custom_id: [
          { min: 0, max: 18, message: '长度最多为 18 个字符', trigger: 'change' },
          { validator: this.validateCustomId, trigger: 'change' }
        ],
        custom_name: [
          { min: 0, max: 10, message: '长度最多 10 个字符', trigger: 'change' }
        ],
        custom_phone: [
          { pattern: '^[0-9]*$', message: '手机号只允许出现数字', trigger: 'change' },
          { min: 0, max: 11, message: '长度最多 11 个字符', trigger: 'change' }
        ],
        custom_address: [
          { min: 0, max: 100, message: '长度最多 100 个字符', trigger: 'change' }
        ],
        contact_name: [
          { min: 0, max: 10, message: '长度最多 10 个字符', trigger: 'change' }
        ],
        contact_phone: [
          { pattern: '^[0-9]*$', message: '手机号只允许出现数字', trigger: 'change' },
          { min: 0, max: 11, message: '长度最多 11 个字符', trigger: 'change' }
        ],
        contact_email: [
          { min: 0, max: 30, message: '长度最多 30 个字符', trigger: 'change' }
        ],
        contact_custom_relation: [
          { min: 0, max: 10, message: '长度最多 10 个字符', trigger: 'change' }
        ]
      },
      dialogFormVisible: false,
      editCusForm: {
        custom_id: '',
        custom_name: '',
        custom_phone: '',
        custom_address: '',
        contact_name: '',
        contact_phone: '',
        contact_email: '',
        contact_custom_relation: ''
      },
      formLabelWidth: '120px'
    }
  },
  mounted: function () {
    let _this = this
    axios.request({
      url: 'http://localhost:8000/api/customer/',
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(function (response) {
      console.log(response.data)
      console.log('type:', typeof (response.data))
      _this.tableData = response.data
    }).catch(function (error) {
      console.log('get customer info error')
      _this.$alert(error, '获取账户信息出错')
    })
  },
  methods: {
    updateCusTable: function (_this) { // 更新客户列表，在添加、删除、修改之后
      axios.get('http://localhost:8000/api/customer/', {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(function (response) {
        console.log('update table:')
        console.log(response.data)
        _this.tableData = response.data
      }).catch(function (error) {
        console.log('get customer info error')
        _this.$alert(error, '获取账户信息出错')
      })
    },
    addCusSubmit: function () {
      let _this = this
      this.$refs.addCusForm.validate((valid) => {
        if (valid) { // 只有信息检查正确的时候才可以提交
          console.log('addCusSubmit valid')
          console.log('submit new customer')
          axios.request({
            url: 'http://localhost:8000/api/customer/',
            method: 'POST',
            data: this.addCusForm
          }).then(function (response) { // 添加新的客户后更新表格
            console.log('post then:')
            if (response.data.errmsg !== undefined) {
              console.log(response.data.errmsg)
              _this.$alert(response.data.errmsg, '添加出错')
            }
            _this.updateCusTable(_this)
          }).catch(function (error) {
            console.log('catch error when add customer')
            _this.$alert(error, '添加出错')
          })
        } else {
          console.log('addCusSubmit error')
          this.$alert('请按照提示输入正确的信息', '添加新客户出错')
          return false
        }
      })
    },
    queryCusSubmit: function () {
      console.log('query customer')
      let _this = this
      this.$refs.queryCusForm.validate((valid) => {
        if (valid) {
          console.log('query info is valid, perform the query')
          axios.get('http://localhost:8000/api/customer/', {
            headers: {
              'Content-Type': 'application/json'
            },
            params: this.queryCusForm
          }).then(function (response) {
            console.log('query customers according to the filter info:')
            console.log(response.data)
            _this.tableData = response.data
            console.log('_this.tableData = ', _this.tableData)
          }).catch(function (error) {
            console.log('query customer info error')
            _this.$alert(error, '查询客户信息出错')
          })
        } else {
          console.log('queryCusSubmit error')
          this.$alert('请按照提示输入正确的信息', '按条件查询客户出错')
          return false
        }
      })
    },
    handleEdit: function (index, row) {
      console.log('edit: ', index, row)
      this.editCusForm = Object.assign({}, this.tableData[index]) // 深度复制
      this.dialogFormVisible = true
    },
    commitEdit: function () { // TODO
      let _this = this
      console.log('commit edit')
      axios.put('http://localhost:8000/api/customer/', this.editCusForm, {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(function (response) {
        console.log('response after edit customer info')
        console.log(response)
        _this.updateCusTable(_this)
      }).catch(function (error) {
        console.log('edit customer info error:')
        console.log(error)
        _this.$alert(error, '修改出错')
      })
      this.dialogFormVisible = false
    },
    handleDelete: function (index, row) {
      let _this = this
      console.log(index, row)
      console.log('typeof index: ' + typeof (index))
      console.log('typeof row: ' + typeof (row))
      axios.delete('http://localhost:8000/api/customer/', {
        headers: {
          'Content-Type': 'application/json'
        },
        data: this.tableData[index]
      }).then(function (response) {
        console.log('received info for delete method: ', response)
        if (response.data.errmsg !== undefined) {
          _this.$alert(response.data.errmsg, '删除出错')
        } else { // 只有成功删除时才需要更新表格
          _this.updateCusTable(_this)
        }
      }).catch(function (error) {
        console.log('error: ' + error)
      })
    },
    validateCustomId: function (rule, value, callback) {
      // 检查客户身份证号，只允许出现数字，最后一位还允许出现 X
      let valid = true
      for (let i = 0; i < value.length; i++) {
        if (i !== 17) { // 除了第 18 位其他必须是数字
          if (isNaN(value[i]) === true) {
            valid = false
          }
        }
        if (i === 17) {
          if ((isNaN(value[i]) === true) && (value[i] !== 'X')) {
            valid = false
          }
        }
      }
      if (!valid) {
        callback(new Error('不允许输入除数字和 X 以外的字符'))
      } else {
        callback()
      }
    },
    clearQueryForm: function () {
      this.queryCusForm = {
        custom_id: '',
        custom_name: '',
        custom_phone: '',
        custom_address: '',
        contact_name: '',
        contact_phone: '',
        contact_email: '',
        contact_custom_relation: ''
      }
    }
  }
}
</script>

<style scoped>
.button-right {
  float: right;
}
</style>
