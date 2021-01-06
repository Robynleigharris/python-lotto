#robyn-leigh harris
# :)

from tkinter import *
from tkinter import messagebox
import datetime

tab = Tk()
tab.title("LOTTO")
tab.geometry("300x200")
tab.configure(background="grey")


#functions for age
def check():
    try:
        if int(age_ent.get())<18:
            messagebox.showwarning("underage")

        if int(age_ent.get())>=18:
            messagebox.showinfo("ok!")
            name_ent_info=name_ent.get()
            age_ent_info=age_ent.get()
            file=open('data.txt', "w")
            file.write("persons name:"+ name_ent_info)
            file.write("persons age:"+ str(age_ent_info))
            file.close()
            tab.withdraw()
            import raw
            raw()


    except ValueError:
            messagebox.showinfo("please enter your age in numbers")


name_lb=Label(tab, text="enter your name:")
name_lb.pack()
name_ent=Entry(tab)
name_ent.pack()
age_lb=Label(tab, text="enter your age:")
age_lb.pack()
age_ent=Entry(tab, textvariable="age")
age_ent.pack()
age_btn=Button(tab, text="submit", width = 10, command=check)
age_btn.pack()



tab.mainloop()
