correct_username = "Username"
correct_password = "Password"

while True:
    username = input("请输入账户名：")
    password = input("请输入密码：")

    if username == correct_username and password == correct_password:
        print("登录成功！")
        break
    else:
        print("账户名或密码错误。")
