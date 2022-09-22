# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:21:54 2022

@author: PC_RC
"""


from tkinter import *
root = Tk()
root.title("Fever Report")
root.geometry("600x600")

question1_radioButton = StringVar(value ="0")
Question1 = Label(root, text="Do you have a headache and a sore throat?")
Question1.pack()
question1_r1 = Radiobutton(root, text = "yes", variable = question1_radioButton, value = "yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "no", variable = question1_radioButton, value = "no")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")
Question2 = Label(root, text = "Is your body temeperature hight?")
Question2.pack()
question2_r1 = Radiobutton(root, text = "yes", variable = question2_radioButton, value = "yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "no", variable = question2_radioButton, value = "no")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")
Question3 = Label(root, text = "Are there any symptoms of eye redness?")
Question3.pack()
question3_r1 = Radiobutton(root, text = "yes", variable = question3_radioButton, value = "yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "no", variable = question3_radioButton, value = "no")
question3_r2.pack()

def fever_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
    if question2_radioButton.get()=="yes":
        score = score+20
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
        
    if score <= 20:
        
        print("You don't need to visit the doctor")
    elif score > 20 and score <= 40:
        
        print("You perhaps might need to visit the doctor")
    else:
        
        print("You must visit the doctor")
        
btn = Button(root, text = "Get Results", command = fever_score)
btn.pack()
root.mainloop()