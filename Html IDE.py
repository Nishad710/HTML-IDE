# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 07:34:22 2021

@author: Rajeev Ranjan Sinha
"""
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import os
import webbrowser

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
run_img = ImageTk.PhotoImage(Image.open ("run.png"))

label_file_name = Label(root,text = "File Name")
label_file_name.place(relx = 0.28,rely = 0.03,anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.48,rely = 0.03,anchor = CENTER)

my_html = Text(root,height = 35,width = 80)
my_html.place(relx = 0.5,rely = 0.55,anchor = CENTER)

name = ""
def openFile() :
    global name
    my_html.delete(1.0,END)
    input_file_name.delete(0,END)
    text_html = filedialog.askopenfilename(title = "Open Html File",filetypes = (("Html Files","*.html"),))
    print(text_html)
    name = os.path.basename(text_html)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_html = open(name,'r')
    paragarph = text_html.read()
    my_html.insert(END,paragarph)
    text_html.close()
    
def save() :
    input_name = input_file_name.get()
    file = open(input_name+".html","w")
    data = my_html.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_html.delete(1.0,END)
    messagebox.showinfo("Update","Success")

def run() :
    global name
    webbrowser.open(name)
    
open_button = Button(root,image = open_img,text = "Open File",command = openFile)
open_button.place(relx = 0.05,rely = 0.03,anchor = CENTER)
save_button = Button(root,image = save_img,text = "Save File",command = save)
save_button.place(relx = 0.11,rely = 0.03,anchor = CENTER)
run_button = Button(root,image = run_img,text = "Run File",command = run)
run_button.place(relx = 0.17,rely = 0.03,anchor = CENTER)

root.mainloop()