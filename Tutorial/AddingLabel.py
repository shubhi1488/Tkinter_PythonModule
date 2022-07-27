from tkinter import *
#it will load all the basic components of GUI
var_root=Tk()
#it will set the size of the window that will appear
var_root.geometry("444x234")
#this method allows u to minimise the window upto a mentioned width and height
var_root.minsize(200,100)
#this method allows u to maximise the window upto a mentioned width and height
var_root.maxsize(1200,988)
#we can create a label through this we need to pass the parameter as text="text" and to add it on frame we need to pack it using pack()
variable=Label(text="this is a label")
variable.pack()
#mainloop() will make the window respinsive and store all the work done .
var_root.mainloop()
