# 密碼重試程式
# 先在程式碼中設定好密碼 password = 'a123456'
# 讓使用者「最多輸入三次密碼」
# 不對的話,就印出"密碼錯誤！ 還有＿次機會"
# 對的話, 就印出"登入成功"
password = 'a123456'
i = 3 #最多輸入密碼次數

while i > 0:
    user_password = input('請輸入七位數密碼(含中英文): ')
    if user_password == password:
        print('登入成功')
        break
    else:
        print('密碼錯誤!') 
        if i > 1:
            print('還有', i-1, '次機會')
        else:
            print('沒有機會嘗試了,帳號已鎖定！')
        i = i-1
print ('GG 遊戲結束喔！')

