<!DOCTYPE html>
<!--[if IE 9]><html class="lt-ie10" lang="en" > <![endif]-->
<html class="no-js" lang="en" >

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>熊猫翻滚 Pandafan</title>

  <!-- If you are using CSS version, only link these 2 files, you may add app.css to use for your overrides if you like. -->
  <link rel="stylesheet" href="css/normalize.css">
  <link rel="stylesheet" href="css/foundation.css">
  <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,700italic,400,300,700">
  <link href="http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">

  <!-- If you are using the gem version, you need this only -->
  <link rel="stylesheet" href="css/app.css">

  <script src="js/modernizr.js"></script>

</head>
<body>

  <!-- body content here -->


  <header>


    <div class="row hide-for-small-only">
      <div id="header" class="large-12 columns">
        <h1>熊猫翻滚</h1>
        <h3 class="subheader en">PandaFan</h3>
        <ul class="inline-list">
          <li><a href="#panda-story">熊猫故事</a></li>
          <li><a href="#panda-contact">联系熊猫</a></li>
          <li><a href="#panda-price">资费定价</a></li>
          <li><a href="#panda-faq">常见问题</a></li>
          <li><a href="#">Blog</a></li>
        </ul>
      </div>
    </div>

    <div class="row show-for-small-only">
      <div id="mobile-header" class="large-12 columns">
        <h1>熊猫翻滚</h1>
        <h3 class="subheader en">PandaFan</h3>
        <ul class="inline-list">
          <li><a href="#panda-story">熊猫故事</a></li>
          <li><a href="#panda-contact">联系熊猫</a></li>
          <li><a href="#panda-price">资费定价</a></li>
          <li><a href="#panda-faq">常见问题</a></li>
          <li><a href="#">Blog</a></li>
        </ul>
      </div>
    </div>


  </header>

  <div class="row break-line">
  </div>

    <div class="row">
      <div class="large-12 columns">
        <div class="row-title">{{message}}</div>
        <br>

        <div class="row">
  <div class="large-6 columns">
  <h3 class="row-title">登录</h3>

  <form data-abide>
  <div class="name-field">
    <label>用户名 <small>必填</small></label>
    <input type="text" required pattern="[a-zA-Z]+">
    <small class="error">请输入正确的用户名</small>
  </div>
  <div class="password-field">
    <label>密码 <small>必填</small></label>
    <input type="password" required>
    <small class="error">请输入正确的密码</small>
  </div>
  <button class="small" type="submit">登录</button>
</form>

  </div>
  <div class="large-6 columns">
  <h3 class="row-title green">注册</h3>
  <form data-abide>
  <div class="name-field">
    <label>用户名 <small>必填</small></label>
    <input type="text" required pattern="[a-zA-Z]+">
    <small class="error">请输入正确的用户名</small>
  </div>
  <div class="password-field">
    <label>密码 <small>必填</small></label>
    <input type="password" required>
    <small class="error">请输入正确的密码</small>
  </div>
  <div class="password-field">
    <label>确认密码 <small>必填</small></label>
    <input type="password" required>
    <small class="error">请输入正确的密码</small>
  </div>
  <button class="small success" type="submit">注册</button>
</form>
  </div>
  </div>
        <a href="#">返回</a>
        </div>
      </div>

<div class="row grey-end-line"></div>


<div class="row hide-for-small-only" id="footer">


    <div class="large-12 columns text-left">
    <h4><small><a href="/contact?locale=zh-CN">中文版 </a></small>
   <small><a href="/contact?locale=en"> English</a></small></h4><h4>
   <small>熊猫翻滚.Beta © 2012-2013 <a href="http://www.miibeian.gov.cn/">京ICP备12050215号</a></small></h4><br>



    </div>

    </div>


<div class="row show-for-small-only" id="footer-mobile">


    <div class="large-12 columns text-center">
    <h4><small><a href="/contact?locale=zh-CN">中文版 </a></small>
   <small><a href="/contact?locale=en"> English</a></small></h4><h4>
   <small>熊猫翻滚.Beta © 2012-2013 <a href="http://www.miibeian.gov.cn/">京ICP备12050215号</a></small></h4><br>



    </div>

    </div>

  <script src="js/vendor/jquery.js"></script>
  <script src="js/foundation.min.js"></script>
  <script>
    $(document).foundation();
  </script>
</body>
</html>
