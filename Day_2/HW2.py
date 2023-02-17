from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta

GUI = Tk()
GUI.title('โปรแกรมบันทึกเวลาเข้างาน/ออกงาน')
GUI.geometry('500x200')

L1 = Label(GUI,text='Check-in and Check-out time for work', font=('Angsana New', 30),fg='blue')
L1.place(x=30,y=20)

now = datetime.today()


def Button1():
    text = now.strftime('%d/%m/%Y %H:%M:%S')
    messagebox.showinfo('Check-in time',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=100)
B1 = ttk.Button(FB1,text='Check-in',command=Button1)
B1.pack(ipadx=20,ipady=20)


def Button2():
    text = now.strftime("%d/%m/%Y %H:%M:%S")
    messagebox.showinfo('Check-out time',text)

FB2 = Frame(GUI)
FB2.place(x=300,y=100)
B2 = ttk.Button(FB2,text='Check-out',command=Button2)
B2.pack(ipadx=20,ipady=20)


f = open('Work_log.txt', 'a')
f.write('Time Stamp : ' + now.strftime('%d/%m/%Y %H:%M:%S') +'\n') 
f.close()



    
