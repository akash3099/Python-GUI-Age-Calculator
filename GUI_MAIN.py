from tkinter import *
from tkinter import ttk
from age import *

root=Tk()
root.title("AGE calculator")
root.configure(background="#1e9182")
root.geometry("340x620")
root.resizable(False,False)

a1=Label(root,text="AGE CALCUATOR",fg="White",bg="#1e9182",font="Times 24 bold",bd=15)
a1.grid(row=0,column=0,pady=30)

a2=Label(root,text="DATE OF BIRTH",fg="White",bg="#1e9182",font="Times 14 bold",bd=15)
a2.grid(row=1,column=0,pady=30)

def getdata():
    date1=date.get()
    date1=int(date1)
    month1=month.get()
    year1=year.get()
    year1=int(year1)
    return age(date1,month1,year1)

def out12():
    day,month,year=getdata()
    out.set("you are {} years,{} months and {} days old".format(year,month,day))



date=StringVar()
month=StringVar()
year=StringVar()


l6=Label(root,text="Day",font="times 14 ",bd=8,bg="#1e9182",fg="white")
l6.grid(row=2,column=0,sticky=W,pady=15)

l6=Label(root,text="Month",font="times 14 ",bd=8,bg="#1e9182",fg="white")
l6.grid(row=3,column=0,sticky=W,pady=15)

l6=Label(root,text="Year",font="times 14 ",bd=8,bg="#1e9182",fg="white")
l6.grid(row=4,column=0,sticky=W,pady=15)

combobox1=ttk.Combobox(root,textvariable=date)
combobox1.grid(row=2,column=0,pady=30)
combobox1.config(values=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'))


combobox2=ttk.Combobox(root,textvariable=month)
combobox2.grid(row=3,column=0,pady=30)
combobox2.config(values=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))


spinbox=Spinbox(root,from_=1985, to=2018,textvariable=year )
spinbox.grid(row=4,column=0)

out=StringVar()
c1=Label(root,textvariable=out,height=2,width=35,fg="Black",bg="#1e9182",font="Times 12 bold")
c1.grid(row=5,column=0)


b1=Button(root,text="Calculate", width=16,bg="#134e85",fg="white",bd=4,command=out12)
b1.grid(row=7,column=0,pady=15,rowspan=5)



root.mainloop()
