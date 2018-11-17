from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from ScrolledText import *
import re

class editor:
    def __init__(self,master):
        frame = Frame(master,width=80,height=150)
        frame.pack()

         
        self.var = StringVar()
        
        menu=Menu(root)
        root.config(menu=menu)
        subMenu=Menu(menu)
        menu.add_cascade(label="File",menu=subMenu)
        subMenu.add_command(label="Open...\t\t  Ctrl+O",command=self.open)
        subMenu.add_separator()
        subMenu.add_command(label="Exit\t\t         Ctrl+Q",command=self.close)
  
        editMenu=Menu(menu)
        menu.add_cascade(label="Edit",menu=editMenu)
        editMenu.add_command(label="Find...\t     Ctrl+F",command=self.fin)
        editMenu.add_separator()
        editMenu.add_command(label="Replace\t  Ctrl+H",command=self.rep)
        editMenu.add_separator()
        editMenu.add_command(label="Reset",command=self.res)
        editMenu.add_separator()
        formatMenu=Menu(menu)
        menu.add_cascade(label="Format",menu=formatMenu)
        runMenu=Menu(menu)
        menu.add_cascade(label="Run",menu=runMenu)

        optionsMenu=Menu(menu)
        menu.add_cascade(label="Options",menu=optionsMenu)

        windowsMenu=Menu(menu)
        menu.add_cascade(label="Windows",menu=windowsMenu)

        helpMenu=Menu(menu)
        menu.add_cascade(label="Help",menu=helpMenu)
       
       
        self.text=ScrolledText(frame, width=70, height=25)
        self.text.grid(row=3,columnspan=3)
        self.text.tag_configure('t',background='green',foreground='white')
        
         
    def open(self):
        self.f = askopenfilename()
        self.var.set(self.f)
        self.display()

    def display(self):
        self.fr = open(str(self.f),'r')
        n = self.fr.read()
        self.n=n
        if n!='':
            self.text.insert(END,str(n))
        

   

    def res(self):
        self.e.delete(0,END)
        self.text.delete('1.0',END)
        


    def findword(self):
        
        self.text.tag_remove('t','1.0',END)
        x=0
        r = re.compile(self.e.get())
        self.fr.seek(0)
        z = self.fr.readline()
        count=1
        while z!='':
             y = r.search(z[x:])
             if y:
                 
                 self.text.tag_add('t',str(count)+'.'+str(x+y.start()),str(count)+'.'+str(x+y.end()))
                 x = x+y.end()+1
                 continue
             count+=1
             x=0
             z=self.fr.readline()

    def rep(self):
        window = Toplevel(root)
        self.nw(window)
    def fin(self):
        wind = Toplevel(root)
        self.win_n(wind)
    
    def win_n(self,master):
        frame = Frame(master)
        frame.pack()
        
        
        self.label1 = Label(frame,textvariable=self.var,padx=5,pady=5)
        self.label1.grid(row=0,columnspan=2)

    
        label2 = Label(frame,text='Enter word:-',padx=2,pady=10)
        label2.grid(row=0)
        self.label1 = Label(frame,textvariable=self.var,padx=5,pady=5)
        self.label1.grid(row=0,column=2)

        button1 = Button(frame,text="Find",command=self.findword)
        button1.grid(row=0,column=4)
        self.e = Entry(frame,width=20)
        self.e.grid(row=0,column=2)
    
    def nw(self,master):
        frame = Frame(master)
        frame.pack()
        label1 = Label(frame,text='Find:-')
        label1.grid(row=0)
        self.entry1 = Entry(frame)
        self.entry1.grid(row=0,column=1)
        label1 = Label(frame,text='Replace:-')
        label1.grid(row=1)
        self.entry2 = Entry(frame)
        self.entry2.grid(row=1,column=1)
        button1 = Button(frame,text="Replace",command=self.rep1)
        button1.grid(row=0,column=2)
        button2 = Button(frame,text="Replace all",command=self.rep2)
        button2.grid(row=1,column=2)
        button3 = Button(frame,text="close",command=self.close)
        button3.grid(row=2,column=1)
    def rep1(self):
        w=self.entry1.get()
        r=self.entry2.get()
        

        m=re.sub(w,r,self.n,1)
        
        if m!='':
            self.text.delete(1.0,END)
            self.text.insert(END,str(m))

    def rep2(self):
        
        w=self.entry1.get()
        r=self.entry2.get()
        

        m=re.sub(w,r,self.n)
        
        if m!='':
            self.text.delete(1.0,END)
            self.text.insert(END,str(m))

    def close(self):
        
         
        tkMessageBox.showinfo("Close","Close?")
        answer=tkMessageBox.askquestion("close","Are You Sure?")
        if(answer=="yes"):
            
          print("Done")
         

root = Tk()
obj = editor(root)
root.mainloop()
        
        
