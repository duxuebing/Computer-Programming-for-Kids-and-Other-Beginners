import easygui

# 文本输入
flavor = easygui.enterbox("What is your favorite ice cream flavor?")
easygui.msgbox("You entered " + flavor)