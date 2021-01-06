from tkinter import *
from datetime import *
from random import sample as rnd


#basic tkinter layout
tab = Tk()
tab.title("LOTTO")
tab.geometry("600x400")
tab.configure(background="grey")

#date
date=datetime.now()
date_lb=Label(tab)
date_lb.place(x=400, y=10)
date_lb.config(text="DATE" + date.strftime("%d/%m/%y %H:%M"))


#function
def win():
        numbers.append(int(num_1.get()))
        numbers.append(int(num_2.get()))

        numbers.append(int(num_3.get()))
        numbers.append(int(num_4.get()))
        numbers.append(int(num_5.get()))
        numbers.append(int(num_6.get()))

        num_correct = set(numbers).intersection(rands)

        if numbers==rands:
            output_lb.config(text=" WINNER!!\n"+ " lotto numbers "+ str(rands) + "\n"+"10 000 000.00")
            outputtext=output_lb.cget("text")
            file=open('results.txt', "a")
            file.write("persons results:"+ outputtext)
            file.close()


        elif len(num_correct) == 0:
            output_lb.config(text="0  numbers matched\n"+ "lotto numbers "+ str(rands) + "\n"+"shame")
            outputtext=output_lb.cget("text")
            file=open('data.txt', "a")
            file.write("persons results:"+ outputtext)
            file.close()


        elif len(num_correct) == 1:
            output_lb.config(text="1  number matched!\n" + "lotto numbers " + str(rands) + "\n" + "shame")
            outputtext=output_lb.cget("text")
            file=open('data.txt', "a")
            file.write("persons results:"+ outputtext)
            file.close()


        elif len(num_correct) == 2:
            output_lb.config(text="2 numbers matched!\n" + "lotto numbers " + str(rands) + "\n" + "20")
            outputtext=output_lb.cget("text")
            file=open('data.txt', "a")
            file.write("persons results:"+ outputtext)
            file.close()


        elif len(num_correct) == 3:
            output_lb.config(text="3 numbers matched!\n" + "lotto numbers " + str(rands) + "\n" + "100.50")
            outputtext=output_lb.cget("text")
            file=open('data.txt', "a")
            file.write("persons results:"+ outputtext)
            file.close()


        elif len(num_correct) == 4:
            output_lb.config(text="4 numbers matched!\n" + "lotto numbers " + str(rands) + "\n" + "2,384.00")
            outputtext=output_lb.get()
            file=open('data.txt', "a")
            file.write("persons results:"+ outputtext)
            file.close()


        elif len(num_correct) == 5:
            output_lb.config(text="5 numbers matched!\n" + "lotto numbers " + str(rands) + "\n" + "8,584.00")
            outputtext=output_lb.get()
            file=open('data.txt', "a")
            file.write("persons results:"+ outputtext)
            file.close()

#randomnum
numbers = []
rands = rnd(range (1,49),6)



#layout of ents and lbs
heading_lb=Label(tab, text="LOTTO DRAW", font=50, bg="yellow", fg="black" )
heading_lb.place(x=235, y=10)
subheading_lb= Label(tab, text="ENTER YOUR NUMBERS:")
subheading_lb.place(x=205, y=60)
num_1 = Entry(tab, width=10, justify='center', bd=3, bg="#696969")
num_1.place(x=5, y=120)
num_2 = Entry(tab, width=10, justify='center', bd=3, bg="#696969")
num_2.place(x=105, y=120)
num_3 = Entry(tab,  width=10, justify='center', bd=3, bg="#696969")
num_3.place(x=205, y=120)
num_4 = Entry(tab,  width=10, justify='center', bd=3, bg="#696969")
num_4.place(x=305, y=120)
num_5 = Entry(tab,  width=10, justify='center', bd=3, bg="#696969")
num_5.place(x=405, y=120)
num_6 = Entry(tab,  width=10, justify='center', bd=3, bg="#696969")
num_6.place(x=505, y=120)
output_lb = Label(tab,  justify='center')
output_lb.place(x=170, y=260)

#button

lot_btn = Button(tab, text="submit", command=win).place(x=245, y=180)



tab.mainloop()
