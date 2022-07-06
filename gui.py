from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root 
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="Red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # data frame making
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400,)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Prescriptions")
        DataFrameRight.place(x=990,y=5,width=500,height=350)

        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=520,width=1530,height=70)

        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=595,width=1530,height=180)

        #Data Frame Left Info
        

        lblName=Label(DataFrameLeft,text="Patient Name:",font=("times new roman",14,"bold"),padx=3,pady=8)
        lblName.grid(row=0,column=0)
        nametext=Entry(DataFrameLeft,font=("arial",11),width=40)
        nametext.grid(row=0,column=1)

        lblAddress=Label(DataFrameLeft,text="Patient Address:",font=("times new roman",14,"bold"),padx=3,pady=8)
        lblAddress.grid(row=1,column=0)
        addresstext=Entry(DataFrameLeft,font=("arial",11),width=40)
        addresstext.grid(row=1,column=1)

        lbldob=Label(DataFrameLeft,text="Date of birth:",font=("times new roman",14,"bold"),padx=3,pady=8)
        lbldob.grid(row=2,column=0)
        dobtext=Entry(DataFrameLeft,font=("arial",11),width=40)
        dobtext.grid(row=2,column=1)

        lblpatientid=Label(DataFrameLeft,text="Patient ID:",font=("times new roman",14,"bold"),padx=3,pady=8)
        lblpatientid.grid(row=3,column=0)
        patientidtext=Entry(DataFrameLeft,font=("arial",11),width=40)
        patientidtext.grid(row=3,column=1)

        





        

root=Tk()
ob=Hospital(root)
root.mainloop()