from tkinter import*


# function for any number or operator we click
def btnclick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)

#function for clear button
def btnclear():
    global operator
    operator=" "
    text_Input.set("")

#function for equal button
def btnequal():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""    


cal=Tk()
cal.title("calculator")
operator=""
text_Input=StringVar()


#for firt row of calculator
txtDisplay = Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="white",justify='right').grid(columnspan=4)



#for second row
################################################################################################
btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="gray",command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="gray",command=lambda:btnclick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="gray",command=lambda:btnclick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="gray",command=lambda:btnclick("+")).grid(row=1,column=3)

#for third row
################################################################################################
btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="gray",command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="gray",command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="gray",command=lambda:btnclick(6)).grid(row=2,column=2)
Subtraction=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="gray",command=lambda:btnclick("-")).grid(row=2,column=3)

#for 4th row
################################################################################################
btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="gray",command=lambda:btnclick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="gray",command=lambda:btnclick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="gray",command=lambda:btnclick(3)).grid(row=3,column=2)
Multiply=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="gray",command=lambda:btnclick("*")).grid(row=3,column=3)


################################################################################################
btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="gray",command=lambda:btnclick(0)).grid(row=4,column=0)
btnclear=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="c",bg="gray",command=btnclear).grid(row=4,column=1)
btnequal=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="gray",command=btnequal).grid(row=4,column=2)
Divide=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="gray",command=lambda:btnclick("/")).grid(row=4,column=3)


cal.mainloop()
