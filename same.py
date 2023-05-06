from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog
import os
from tkinter import messagebox
root=Tk()

root.title("notebook")
root.minsize(650,650)
root.maxsize(650,650)

open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))

label_filename=Label(root,text="File name")
label_filename.place(relx=0.28,rely=0.03,anchor=CENTER)

input_filename=Entry(root)
input_filename.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name=""


def openfile():
    global name
    my_text.delete(1.0,END)
    input_filename.delete(0,END)
    text_file=filedialog.askopenfilename(title="open text file",filetypes=(("Text Files","*.txt"),)) 
    name=os.path.basename(text_file)
    formated_name=name.split(".")[0]
    input_filename.insert(END,formated_name)
    root.title(formated_name)
    text_file=open(name,"r")
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    
open_btn=Button(root,text="Open File",image=open_img,command=openfile)
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)

def savefile():
    input_name=input_filename.get()
    file=open(input_name+".txt","w")
    data=my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_filename.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("update","sucess")
    
    
save_btn=Button(root,text="Save File",image=save_img,command=savefile)
save_btn.place(relx=0.11,rely=0.03,anchor=CENTER)

def exitfile():
    root.destroy()
    
exit_btn=Button(root,text="exit file",image=exit_img,command=exitfile)
exit_btn.place(relx=0.17,rely=0.03,anchor=CENTER)

root.mainloop()






