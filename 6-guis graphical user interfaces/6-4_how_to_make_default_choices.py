import easygui

# 默认输入
flavor = easygui.enterbox("What is your favorite ice cream flavor?", default = 'Vanilla') # 这是默认选项
easygui.msgbox("You entered " + flavor)