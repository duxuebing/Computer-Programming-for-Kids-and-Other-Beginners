import easygui

# 选择框
flavor = easygui.choicebox("What is your favorite ice cream flavor?", choices = ['Vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox("You picked " + flavor)