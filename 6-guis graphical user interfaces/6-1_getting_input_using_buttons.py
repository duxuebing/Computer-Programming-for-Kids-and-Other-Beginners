import easygui

# 带有多个按钮的对话框
flavor = easygui.buttonbox("What is your favorite ice cream flavor?", choices = ['Vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox("You picked " + flavor)