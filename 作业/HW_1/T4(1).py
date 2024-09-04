correct_username = "Username"
correct_password = "Password"

attempt_count = 0

while attempt_count < 5:
    username = input("请输入账户名：")
    password = input("请输入密码：")

    if username == correct_username and password == correct_password:
        print("登录成功！")
        break
    else:
        print("账户名或密码错误。")

    attempt_count += 1

    if attempt_count == 5:
        print("对不起，账户已锁定。")
        break