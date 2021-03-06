head = """
<!DOCTYPE html>
<html lang="zh-CN">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	
	<title>登录 - 测试</title>
	<meta name="keywords" content="" />
	<meta name="description" content="" /> 

	<link rel="stylesheet" type="text/css" href="static/vendor/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="static/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="static/fonts/iconic/css/material-design-iconic-font.min.css">
	<link rel="stylesheet" type="text/css" href="static/css/util.css">
	<link rel="stylesheet" type="text/css" href="static/css/main.css">
</head>

<body>
"""

index = """
<div class="limiter">
    <div class="container-login100" style="background-image: url('/static/images/bg-01.jpg');">
        <div class="wrap-login100 p-l-55 p-r-55 p-t-65 p-b-54">
            <form class="login100-form validate-form" method="POST" action="login.php">
                <span class="login100-form-title p-b-49">登录</span>

                <div class="wrap-input100 validate-input m-b-23" data-validate="请输入用户名">
                    <span class="label-input100">用户名</span>
                    <input class="input100" type="text" name="username" placeholder="请输入用户名" autocomplete="off">
                    <span class="focus-input100" data-symbol="&#xf206;"></span>
                </div>

                <div class="wrap-input100 validate-input" data-validate="请输入密码">
                    <span class="label-input100">密码</span>
                    <input class="input100" type="password" name="password" placeholder="请输入密码">
                    <span class="focus-input100" data-symbol="&#xf190;"></span>
                </div>

                <div class="text-right p-t-8 p-b-31">
                </div>

                <div class="container-login100-form-btn">
                    <div class="wrap-login100-form-btn">
                        <div class="login100-form-bgbtn"></div>
                        <button class="login100-form-btn">登 录</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
"""

login = """
<div class="limiter">
    <div class="container-login100" style="background-image: url('/static/images/bg-01.jpg');">
        <div class="wrap-login100 p-l-55 p-r-55 p-t-65 p-b-54">
            <div class="login100-form validate-form">
                <span class="label-input100 p-b-49">
                %s
                </span>
            </div>
        </div>
    </div>
</div>
"""

foot = """
</body>
<!--hint.php-->
</html>
"""