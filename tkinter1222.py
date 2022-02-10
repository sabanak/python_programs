#1:Tkinter Label
# from tkinter import *
# root=Tk()
# Label(root,text="hello world",bg="cyan").pack()
# Label(root,text="how are you avodha",fg="red").pack()
# root.mainloop()

#2:Tkinter Button
# from tkinter import *
# root=Tk()
# Button(root,text="login",bg="red").pack()
# Button(root,text="cancel",bg="cyan").pack()
# root.mainloop()

#by using frame with function
# from tkinter import *
# root=Tk()
# f=Frame(root)
# f.pack()
# def fun():
#     print("hi avodha")
# def cancel():
#     print("it's cancelled")
# Button(f,text="login",bg="red",command=fun).pack()
# Button(f,text="cancel",bg="cyan",command=cancel).pack()
# root.mainloop()

#3.Tkinter Grid
# from tkinter import *
# root=Tk()
# Label(root,text="username").grid(row=0,column=0)
# Label(root,text="password").grid(row=1,column=0)
# Entry(root).grid(row=0,column=1)
# Entry(root).grid(row=1,column=1)
# root.mainloop()

#4.Tkinter self adjacent widget
# from tkinter import *
# root=Tk()
# Label(root,text="x direction",bg="red").pack(fill=X)
# Label(root,text="y direction",bg="cyan").pack(side=LEFT,fill=Y)
# root.mainloop()

#5.Tkinter class
# from tkinter import *
# root=Tk()
# class demo:
#     def __init__(self,roottone):
#         frame=Frame(roottone)
#         frame.pack()
#         self.p=Button(frame,text="hello avodha",command=self.printmsg)
#         self.p.pack()
#         Button(frame,text="exit",command=frame.quit).pack()
#     def printmsg(self):
#         print("hello avodha")
# obj=demo(root)
# root.mainloop()

#6.Tkinter messagebox
# from tkinter import *
# import tkinter.messagebox
# root=Tk()
#tkinter.messagebox.showinfo("title","this is information")
#tkinter.messagebox.showwarning("title","this is information")
#tkinter.messagebox.showerror("title","this is error")
#tkinter.messagebox.askquestion("title","how are you")
#tkinter.messagebox.askokcancel("title","this is information")
#tkinter.messagebox.askyesno("title","this is information")
#tkinter.messagebox.askretrycancel("title","this is information")
# root.mainloop()

#7.Tkinter  dropdown #like a notepad
# from tkinter import *
# root=Tk()
# def fun():
#     print("am function")
# mymenu=Menu(root)
# root.config(menu=mymenu)
# submenu=Menu(mymenu)
# mymenu.add_cascade(label="file",menu=submenu)
# submenu.add_command(label="save",command=fun)
# submenu.add_separator()
# submenu.add_command(label="exit",command=root.quit)
# newmenu=Menu(mymenu)
# mymenu.add_cascade(label="edit",menu=newmenu)
# newmenu.add_command(label="undo",command=fun)
# newmenu.add_command(label="redo",command=fun)
# root.mainloop()


#1.tkinter label
# from tkinter import *
# root=Tk()
# Label(root,text="hi",bg="cyan").pack()
# Label(root,text="how are you",bg="black",fg="pink").pack()
# root.mainloop()

#2.tkinter button
# from tkinter import *
# root=Tk()
# Button(root,text="Login",bg="skyblue").pack()
# Button(root,text="exit",fg="red").pack()
# root.mainloop()

#3.tkinter button with frame and function
# from tkinter import *
# root=Tk()
# frame=Frame(root)
# frame.pack()
# def hi():
#     print("hello")
# def hey():
#     print("cancelled")
# Button(frame,text="Login",bg="skyblue",command=hi).pack()
# Button(frame,text="cancel",fg="red",command=hey).pack()
# root.mainloop()

#4.tkinter grid
# from tkinter import *
# root=Tk()
# Label(root,text="username",bg="skyblue").grid(row=0,column=0)
# Entry(root).grid(row=0,column=1)
# Label(root,text="password",bg="cyan").grid(row=1,column=0)
# Entry(root).grid(row=1,column=1)
# Button(root,text="Login",bg="pink").grid(row=2,column=1)
# root.mainloop()

#5.tkinter self adjacent widget
# from tkinter import *
# root=Tk()
# Label(root,text="x direction",bg="skyblue").pack(fill=X)
# Label(root,text="y direction",bg="red").pack(side=LEFT,fill=Y)
# root.mainloop()

#6.tkinter class
# from tkinter import *
# root=Tk()
# class demo:
#     def __init__(self,roottone):
#         #frame=Frame(root)
#         #frame.pack()
#         self.p=Button(root,text="hi avodha",bg="pink",command=self.printmsg)
#         self.p.pack()
#         self.p=Button(root,text="exit",command=root.quit).pack()
#     def printmsg(self):
#         print("it's me avodha")
# obj=demo(root)
# root.mainloop()

#7.tkinter message box
#1.showinfo('title',message)
# from tkinter import *
# import tkinter.messagebox
# root=Tk()
# tkinter.messagebox.showinfo('title','this is info')
# root.mainloop()

#2.showwarning('title,message)
# from tkinter import *
# import tkinter.messagebox
# root=Tk()
# tkinter.messagebox.showwarning('title','this is warning')
# root.mainloop()

#3.showerror('title','this is error')
# from tkinter import *
# import tkinter.messagebox
# root=Tk()
# tkinter.messagebox.showerror('title','this is error')
# root.mainloop()

#4.askquestion('title',message,options)
# from tkinter import *
# import tkinter.messagebox
# root=Tk()
# tkinter.messagebox.askquestion('question','this is question')
# root.mainloop()

#5.askokcancel('title',message,options)
# from tkinter import *
# import tkinter.messagebox
# root=Tk()
# tkinter.messagebox.askokcancel('ask','ask ok cancel')
# root.mainloop()

#6.askyesno('title',message,options)
# from tkinter import *
# import tkinter.messagebox
# root=Tk()
# tkinter.messagebox.askyesno('askyesno','YES OR NO')
# root.mainloop()

#7.askretrycancel('title',message,options)
# from tkinter import *
# import tkinter.messagebox
# root=Tk()
# tkinter.messagebox.askretrycancel('retry','ask retry cancel')
# root.mainloop()

#8.tkinter dropdown
# from tkinter import *
# root=Tk()
# def fun():
#     print("opening file")
# def func():
#     print("saved")
#
# mymenu=Menu(root)
# root.config(menu=mymenu)
#
# submenu=Menu(mymenu)
#
# mymenu.add_cascade(label="File",menu=submenu)
# submenu.add_command(label="Open",command=fun)
# submenu.add_separator()
# submenu.add_command(label="Save",command=func)
# submenu.add_separator()
# submenu.add_command(label="Save As",command=func)
# submenu.add_separator()
# submenu.add_command(label="Exit",command=root.quit)
#
# newmenu=Menu(mymenu)
# mymenu.add_cascade(label="Edit",menu=newmenu)
# newmenu.add_command(label="Undo")
# newmenu.add_separator()
# newmenu.add_command(label="Redo")
# newmenu.add_separator()
# newmenu.add_command(label="Copy")
#
#
# smenu=Menu(mymenu)
#
# mymenu.add_cascade(label="Tools",menu=smenu)
# smenu.add_command(label="Debugger")
# smenu.add_separator()
# smenu.add_command(label="Space")
#
#
# mmenu=Menu(mymenu)
#
# mymenu.add_cascade(label="View",menu=mmenu)
# mmenu.add_command(label="Appearance")
# mmenu.add_separator()
# mmenu.add_command(label="Recent File")
# root.mainloop()

from tkinter import *
root=Tk()
Label(root,text="TKINTER DROPDOWN",bg="cyan").pack()
def f():
    print("File is saved")


mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)

mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="save",command=f)
submenu.add_separator()
submenu.add_command(label="Exit",command=root.quit)
root.mainloop()