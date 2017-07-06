
$(function(){

  // 1.0 设置默认值全为false,只有当验证全部通过了才能提交表单
  var error_name = false;
  var error_password = false;
  var error_check_password = false;
  var error_email = false;
  var error_check = false;


  // 2.0 当用户名失去焦点的时候,执行用户名判断
  $('#user_name').blur(function() {
    check_user_name();
  });

  // 2.1 当密码失去焦点的时候,执行密码判断
  $('#pwd').blur(function() {
    check_pwd();
  });

  // 2.2 当重复密码失去焦点的时候,进行判断 
  $('#cpwd').blur(function() {
    check_cpwd();
  });

  $('#email').blur(function() {
    check_email();
  });

  // 2.3 当选中了同意协议的时候
  $('#allow').click(function() {
    if($(this).is(':checked'))
    {
      error_check = false;
      $(this).siblings('span').hide();
    }
    else
    {
      error_check = true;
      $(this).siblings('span').html('请勾选同意').show();
    }
  });


  // 检查用户名函数.一般的function会产生作用域的问题,需要注意.
  function check_user_name(){
    var len = $('#user_name').val().length;
    if(len<5||len>20)
    {
      $('#user_name').next().html('请输入5-20个字符的用户名')
      $('#user_name').next().show();
      error_name = true;
    }
    else
    { 
      // ajax请求,检查用户名是否已经被注册.注意不能用$(this).
      $.get('/user/register_valid/',{'uname':$('#user_name').val()},function (data) {
        // 如果返回的数据大于1说明已经被注册
        if(data.valid>=1){
          //用户名不可用,显示错误提示
          $('#user_name').next().html('用户名已经存在').show();
          error_name = true;
        }else{
          //用户名可用,隐藏提示
          $('#user_name').next().hide();
          error_name = false;
        }
            });
    }
  }


  function check_pwd(){
    var len = $('#pwd').val().length;
    if(len<8||len>20)
    {
      $('#pwd').next().html('密码最少8位，最长20位')
      $('#pwd').next().show();
      error_password = true;
    }
    else
    {
      $('#pwd').next().hide();
      error_password = false;
    }   
  }


  function check_cpwd(){
    var pass = $('#pwd').val();
    var cpass = $('#cpwd').val();

    if(pass!=cpass)
    {
      $('#cpwd').next().html('两次输入的密码不一致')
      $('#cpwd').next().show();
      error_check_password = true;
    }
    else
    {
      $('#cpwd').next().hide();
      error_check_password = false;
    }   
    
  }


  function check_email(){
    var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

    if(re.test($('#email').val()))
    {
      $('#email').next().hide();
      error_email = false;
    }
    else
    {
      $('#email').next().html('你输入的邮箱格式不正确')
      $('#email').next().show();
      error_email = true;
    }

  }


  // 获取表单并进行判断,符合要求才允许提交表单,否则在input窗口下方显示输入错误提示
  $('#reg_form').submit(function() {
    check_user_name();
    check_pwd();
    check_cpwd();
    check_email();
        
    if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
    {
      return true;
    }
    else
    {
      return false;
    }

  });
})