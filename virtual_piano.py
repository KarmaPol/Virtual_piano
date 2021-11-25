from tkinter import*
import time
import datetime
import pygame

pygame.init()

root=Tk()

root.title('Virtual Piano')
root.geometry('1600x800+0+0')
root.configure(background='white')

ABC = Frame(root, bg="#6B3922")
ABC.grid()

ABC1 = Frame(ABC, bg="#6B3922")
ABC1.grid()

ABC2 = Frame(ABC, bg="#6B3922")
ABC2.grid()

ABC3 = Frame(ABC, bg="#6B3922")
ABC3.grid()

#===================라벨========================

Label(ABC1, text="Virtual Piano", 
font=('Segoe Script', 70, 'bold', 'italic'),
padx=8,pady=8, bd=4,bg="#6B3922",
fg="white", justify=CENTER).grid(row=0,column=0,columnspan=11)

#===================흑건========================

btnSpace0=Button(ABC2, state=DISABLED, width=20,height=6, bg="#6B3922", relief=FLAT)
btnSpace0.grid( row=0, column=0, padx=0,pady=0)
btnSpace2=Button(ABC2, state=DISABLED, width=15,height=6, bg="#6B3922", relief=FLAT)
btnSpace2.grid( row=0, column=3, padx=0,pady=0)
btnSpace5=Button(ABC2, state=DISABLED, width=15,height=6, bg="#6B3922", relief=FLAT)
btnSpace5.grid( row=0, column=9, padx=0,pady=0)
btnSpace7=Button(ABC2, state=DISABLED, width=20,height=6, bg="#6B3922", relief=FLAT)
btnSpace7.grid( row=0, column=14, padx=0,pady=0)

btnCs=Button(ABC2, height=7,width=6,bd=6,text="C#",bg="black",fg="white",font=('arial',18,'bold'), relief=RAISED, command=value_Cs)
btnCs.grid(row=0,column=1,padx=5,pady=5)

btnDs=Button(ABC2, height=7,width=6,bd=6,text="D#",bg="black",fg="white",font=('arial',18,'bold'), relief=RAISED, command=value_Ds)
btnDs.grid(row=0,column=2,padx=5,pady=5)

btnFs=Button(ABC2, height=7,width=6,bd=6,text="F#", font=('arial',18,'bold'), relief=RAISED, command=value_Fs,bg="black",fg="white")
btnFs.grid(row=0,column=4,padx=5,pady=5)

btnGs=Button(ABC2, height=7,width=6,bd=6,text="G#", font=('arial',18,'bold'), relief=RAISED, command=value_Gs,bg="black",fg="white")
btnGs.grid(row=0,column=6, padx=5,pady=5)

btnAs=Button(ABC2, height=7,width=6,bd=6,text="A#", font=('arial',18,'bold'), relief=RAISED, command=value_As,bg="black",fg="white")
btnAs.grid(row=0,column=8, padx=5,pady=5)

btnCs1=Button(ABC2, height=7,width=6,bd=6,text="C#1",bg="black",fg="white",font=('arial',18,'bold'), relief=RAISED, command=value_Cs1)
btnCs1.grid(row=0,column=10,padx=5,pady=5)

btnDs1=Button(ABC2, height=7,width=6,bd=6,text="D#1",bg="black",fg="white",font=('arial',18,'bold'), relief=RAISED, command=value_Ds1)
btnDs1.grid(row=0,column=12,padx=5,pady=5)

#===================백건========================

btnC=Button(ABC3, height=9,width=6,bd=6,text="C", font=('arial',18,'bold'), relief=RAISED, command=value_C, bg="white",fg="black")
btnC.grid(row=0,column=0,padx=5,pady=5)

btnD=Button(ABC3, height=9,width=6,bd=6,text="D", font=('arial',18,'bold'), relief=RAISED, command=value_D, bg="white",fg="black")
btnD.grid(row=0,column=1,padx=5,pady=5)

btnE=Button(ABC3, height=9,width=6,bd=6,text="E", font=('arial',18,'bold'), relief=RAISED, command=value_E, bg="white",fg="black")
btnE.grid(row=0,column=2,padx=5,pady=5)

btnF=Button(ABC3, height=9,width=6,bd=6,text="F", font=('arial',18,'bold'), relief=RAISED, command=value_F, bg="white",fg="black")
btnF.grid(row=0,column=3,padx=5,pady=5)

btnG=Button(ABC3, height=9,width=6,bd=6,text="G", font=('arial',18,'bold'), relief=RAISED, command=value_G, bg="white",fg="black")
btnG.grid(row=0,column=8,padx=5,pady=5)

btnA=Button(ABC3, height=9,width=6,bd=6,text="A", font=('arial',18,'bold'), relief=RAISED, command=value_A, bg="white",fg="black")
btnA.grid(row=0,column=5,padx=5,pady=5)

btnB=Button(ABC3, height=9,width=6,bd=6,text="B", font=('arial',18,'bold'), relief=RAISED, command=value_B, bg="white",fg="black")
btnB.grid(row=0,column=6,padx=5,pady=5)

btnC1=Button(ABC3, height=9,width=6,bd=6,text="C1", font=('arial',18,'bold'), relief=RAISED, command=value_C1, bg="white",fg="black")
btnC1.grid(row=0,column=7,padx=5,pady=5)

btnD1=Button(ABC3, height=9,width=6,bd=6,text="D1", font=('arial',18,'bold'), relief=RAISED, command=value_D1, bg="white",fg="black")
btnD1.grid(row=0,column=8,padx=5,pady=5)

btnE1=Button(ABC3, height=9,width=6,bd=6,text="E1", font=('arial',18,'bold'), relief=RAISED, command=value_E1, bg="white",fg="black")
btnE1.grid(row=0,column=9,padx=5,pady=5)

btnF1=Button(ABC3, height=9,width=6,bd=6,text="F1", font=('arial',18,'bold'), relief=RAISED, command=value_F1, bg="white",fg="black")
btnF1.grid(row=0,column=10,padx=5,pady=5)

root.mainloop()