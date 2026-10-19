import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()
def helloCallback():
    msg.showinfo("belajar gui","M DZAKI AL FURQON P")
w1=tk.Button(top,text="klik saya",command=helloCallback)
w1.pack()
top.mainloop()
