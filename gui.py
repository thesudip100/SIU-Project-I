from tkinter import*
from tkinter import ttk 
from tkinter.ttk import Progressbar
import random 
import datetime
from tkinter import messagebox 
import mysql.connector  


#SPLASH SCREEN

w = Tk()


width_of_window = 427
height_of_window = 250

screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()

x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)

w.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)


s=ttk.Style() 
s.theme_use("clam")
s.configure("red.Horizontal.TProgressbar",fg="red",bg="#4f4f4f")
progress = Progressbar(w,style="white.Horizontal.TProgressbar",orient=HORIZONTAL,length = 427,mode='determinate')

def progress_bar():
    l1 = Label(w,text = "Loading.....", fg = "white", bg = "#249794",font= ("Calibri",10))
    l1.place(x=0,y=210)
    #l1.grid(padx=0,pady=210)
    
    import time
    r = 0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.05)
        r = r+1
    w.destroy()
    
progress.place(x=0,y=235)

#adding frame

Frame(w,width=427,height=241,bg = "#249794").place(x=0,y=0)
btn = Button(w,width=10, height=1,text="Get Started",command = progress_bar ,border=0,fg="#249794")
btn.place(x=170,y=200)

#adding label

l2 = Label(w,text="HOSPITAL",fg="white",bg="#249794",font=("Calibri",20))
l2.place(x=50,y=80)

l3 = Label(w,text="DATABASE",fg="white",bg="#249794",font=("Calibri",20))
l3.place(x=170,y=80)

l4 = Label(w,text="MANAGEMENT",fg="white",bg="#249794",font=("Calibri",20))
l4.place(x=50,y=110)

w.mainloop()


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System") 
        self.root.geometry("1540x800+0+0") 


        self.Patient_Name=StringVar()
        self.Address=StringVar()
        self.DOB=StringVar()
        self.ID=StringVar()
        self.Admission=StringVar()
        self.Symptom=StringVar()
        self.Depart=StringVar()
        self.Doctor=StringVar()
        self.Medical_History=StringVar()
        self.Diagnosis=StringVar()
        self.Allergens=StringVar()
        self.Followup=StringVar()

 
        ########MAKING THE TITLE OF THE HOMESCREEN###############
        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)



        ## Making Dataframe

        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400,)

        ######## Adding hospital in left side of dataframe ##
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Patient hospital")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        ##### Adding in the right side of the dataframe

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Prescriptions")
        DataFrameRight.place(x=990,y=5,width=500,height=350)

        ######## Buttons Frame #######

        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=520,width=1530,height=70)


        ###### Making Details Frame #####

        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=595,width=1530,height=180)



        ######### Adding Values in Dataframe Left ########

        lblName=Label(DataFrameLeft,text="Patient Name:",font=("times new roman",14,"bold"),padx=3,pady=8)
        lblName.grid(row=0,column=0)
        nametext=Entry(DataFrameLeft,font=("arial",11),textvariable=self.Patient_Name,width=40)
        nametext.grid(row=0,column=1)

        lblAddress=Label(DataFrameLeft,text="Patient Address:",font=("times new roman",14,"bold"),padx=3,pady=8)
        lblAddress.grid(row=1,column=0)
        addresstext=Entry(DataFrameLeft,font=("arial",11),textvariable=self.Address,width=40)
        addresstext.grid(row=1,column=1)

        lbldob=Label(DataFrameLeft,text="Date of birth:",font=("times new roman",14,"bold"),padx=3,pady=12)
        lbldob.grid(row=2,column=0)
        dobtext=Entry(DataFrameLeft,font=("arial",11),textvariable=self.DOB,width=40)
        dobtext.grid(row=2,column=1)

        lblpatientid=Label(DataFrameLeft,text="Patient ID:",font=("times new roman",14,"bold"),padx=3,pady=12)
        lblpatientid.grid(row=3,column=0)
        patientidtext=Entry(DataFrameLeft,font=("arial",11),textvariable=self.ID,width=40)
        patientidtext.grid(row=3,column=1)

        lblAdmissionDate=Label(DataFrameLeft,text="Admission Date:",font=("times new roman",14,"bold"),padx=3,pady=12)
        lblAdmissionDate.grid(row=4,column=0)
        admissiondate_text=Entry(DataFrameLeft,font=("arial",11),textvariable=self.Admission,width=40)
        admissiondate_text.grid(row=4,column=1)

        Symptoms_seen=Label(DataFrameLeft,text="Symptoms seen:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Symptoms_seen.grid(row=5,column=0)
        Symptoms_seen_text=Entry(DataFrameLeft,font=("arial",11),textvariable=self.Symptom,width=40)
        Symptoms_seen_text.grid(row=5,column=1)

        Department=Label(DataFrameLeft,text="Department:",font=("times new roman",14,"bold"),padx=6,pady=12)
        Department.grid(row=0,column=2)
        combo_department=ttk.Combobox(DataFrameLeft,state="readonly",font=("times new roman",13,"bold"),textvariable=self.Depart,width=30)
        combo_department['value']=("General OPD","ENT","Internal Medicine","Gynaecology","Opthalmic","Orthopaedic","Pediatrics","Anesthesiology","ICU")
        combo_department.grid(row=0,column=3)

        Doctor=Label(DataFrameLeft,text="Doctor in charge:",font=("times new roman",14,"bold"),padx=6,pady=12)
        Doctor.grid(row=1,column=2)
        combo_doctor=ttk.Combobox(DataFrameLeft,state="readonly",font=("times new roman",13,"bold"),textvariable=self.Doctor,width=30)
        combo_doctor['value']=("Dr.Prasansha","Dr.Subodh","Dr.Sunil","Dr.Rachana","Dr.Bikesh","Dr.Surya","Dr.Ratna","Dr.Neeshma","Dr.Pranil")
        combo_doctor.grid(row=1,column=3)

        Medical_History=Label(DataFrameLeft,text="Medical History:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Medical_History.grid(row=2,column=2)
        Medical_History_text=Entry(DataFrameLeft,font=("arial",11),textvariable=self.Medical_History,width=36)
        Medical_History_text.grid(row=2,column=3)

        Diagnosis=Label(DataFrameLeft,text="Initial Diagnois:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Diagnosis.grid(row=3,column=2)
        Diagnosis_text=Entry(DataFrameLeft,font=("arial",11),textvariable=self.Diagnosis,width=36)
        Diagnosis_text.grid(row=3,column=3)

        Allergic=Label(DataFrameLeft,text="Allergens to Patient:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Allergic.grid(row=4,column=2)
        Allergic_text=Entry(DataFrameLeft,font=("arial",11),textvariable=self.Allergens,width=36)
        Allergic_text.grid(row=4,column=3)

        Followup=Label(DataFrameLeft,text="Followup Date:",font=("times new roman",14,"bold"),padx=3,pady=12)
        Followup.grid(row=5,column=2)
        Followup_text=Entry(DataFrameLeft,font=("arial",11),textvariable=self.Followup,width=36)
        Followup_text.grid(row=5,column=3)
        
        # **------------------------------BUTTONS------------------------------------------------------*

        btnPrescription = Button(ButtonFrame,text = "Prescription",bg="blue",fg ="white", width =23,font = ("Times New Roman",12,"bold" ))
        btnPrescription.grid(row=0,column = 1)

        btnPrescriptionData = Button(ButtonFrame, text = "Record Entry", bg="blue",fg ="white", width =23,font = ("Times New Roman",12,"bold" ) )
        btnPrescriptionData.grid(row=0,column = 2)

        btnUpdate = Button(ButtonFrame, text = "Update",bg="blue",fg ="white", width =23,font = ("Times New Roman",12,"bold" ) )
        btnUpdate.grid(row = 0, column = 3)

        btnDelete = Button(ButtonFrame, text = "Delete",bg="blue",fg ="white", width =23,font = ("Times New Roman",12,"bold" ))
        btnDelete.grid(row = 0, column = 4)
        
        btnReset = Button(ButtonFrame, text = "Reset",bg="blue",fg ="white", width =23,font = ("Times New Roman",12,"bold" ) )
        btnReset.grid(row = 0,column = 5 )

        btnExit = Button(ButtonFrame, text = "Exit",bg="blue",fg ="white", width =23,font = ("Times New Roman",12,"bold" ) )
        btnExit.grid(row = 0,column = 6)


        ####DATA FRAME RIGHT############

        self.Prescription=Text(DataFrameRight,font=("arial",11,"bold"),width=57,height=17,padx=2,pady=2)
        self.Prescription.grid(row=0,column=0)



        ################## Making buttons ############################ 

        btnPrescription = Button(ButtonFrame, command=self.iprescription, font=("arial",13,"bold"),bg="blue",fg="white",text="Presciption",width=24, padx=0,pady=1)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionDate = Button(ButtonFrame, command=self.iPrescriptionData, font=("arial",13,"bold"),bg="blue",fg="white",text="Record Entry", width=24, padx=1,pady=1)
        btnPrescriptionDate.grid(row=0,column=1)

        btnupdate = Button(ButtonFrame, font=("arial",13,"bold"),bg="blue",fg="white",text="Update", width=24, padx=1,pady=1)
        btnupdate.grid(row=0,column=2)

        btndelete = Button(ButtonFrame, font=("arial",13,"bold"),bg="blue",fg="white",text="Delete", width=24, padx=1,pady=1)
        btndelete.grid(row=0,column=3)

        btnclear = Button(ButtonFrame, command=self.iclear, font=("arial",13,"bold"),bg="blue",fg="white",text="Clear", width=24, padx=1,pady=1)
        btnclear.grid(row=0,column=4) 

        btnexit = Button(ButtonFrame, command = self.iexit, font=("arial",13,"bold"),bg="blue",fg="white",text="Exit", width=24, padx=1,pady=1)
        btnexit.grid(row=0,column=5)


        ############## Making Table in the button and scroll bar ############## 

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(DetailsFrame,columns=('Patient_Name','Address','DOB','ID','Admission','Symptom','Depart','Doctor','Medical_History','Diagnosis','Allergens','Followup'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("Patient_Name",text="Name of Patient")
        self.hospital_table.heading("Address",text="Address")
        self.hospital_table.heading("DOB",text="Date of Birth")
        self.hospital_table.heading("ID",text="Patient Id")
        self.hospital_table.heading("Admission",text="Admission Date")
        self.hospital_table.heading("Symptom",text="Symptoms seen")
        self.hospital_table.heading("Depart",text="Department")
        self.hospital_table.heading("Doctor",text="Doctor")
        self.hospital_table.heading("Medical_History",text="Medical History")
        self.hospital_table.heading("Diagnosis",text="Medical Diagnosis")
        self.hospital_table.heading("Allergens",text="Allergens to Patient")
        self.hospital_table.heading("Followup",text="Followup Date")

        self.hospital_table["show"] = "headings"

        self.hospital_table.pack(fill=BOTH,expand=1)

        # Setting Width

        self.hospital_table.column("Patient_Name",width=100)
        self.hospital_table.column("Address",width=100)
        self.hospital_table.column("DOB",width=100)
        self.hospital_table.column("ID",width=100)
        self.hospital_table.column("Admission",width=100)
        self.hospital_table.column("Symptom",width=100)
        self.hospital_table.column("Depart",width=100)
        self.hospital_table.column("Doctor",width=100)
        self.hospital_table.column("Medical_History",width=100)
        self.hospital_table.column("Diagnosis",width=100)
        self.hospital_table.column("Allergens",width=100)
        self.hospital_table.column("Followup",width=100)
        

        self.hospital_table.pack(fil=BOTH,expand=1) 

        ##### While CLicking the data is shown in the table

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
 
        ######### Fetching the Data ########### 
        self.fatch_data() 
        


    ## Connecting the Database ##  

    def iPrescriptionData(self): 
        if self.Patient_Name.get()== "" or self.Address.get()=="": 
            messagebox.showerror("Error","all fields required")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="mydatabase")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                    self.Patient_Name.get(),self.Address.get(),self.DOB.get(),self.ID.get(),self.Admission.get(),
                                    self.Symptom.get(),self.Depart.get(),self.Doctor.get(),self.Medical_History.get(),self.Diagnosis.get(),
                                    self.Allergens.get(),self.Followup.get()))
            
            conn.commit()
            self.fatch_data()
            # self.update_data()
            conn.close()
            messagebox.showinfo("Success","Successfully inserted into database") 




    def fatch_data(self): 
        conn = mysql.connector.connect(host="localhost",username="root",password="",database="mydatabase")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        
        self.Patient_Name.set(row[0])
        self.Address.set(row[1])
        self.DOB.set(row[2])
        self.ID.set(row[3])
        self.Admission.set(row[4])
        self.Symptom.set(row[5])
        self.Depart.set(row[6])
        self.Doctor.set(row[7])
        self.Medical_History.set(row[8])
        self.Diagnosis.set(row[9])
        self.Allergens.set(row[10])
        self.Followup.set(row[11])

    ######### Displaying Data in the side box ########

    def iprescription(self):
            self.Prescription.insert(END, "Patient_Name: \t\t\t" + self.Patient_Name.get() + "\n")
            self.Prescription.insert(END, "Address: \t\t\t" + self.Address.get() + "\n")     
            self.Prescription.insert(END, "DOB: \t\t\t" + self.DOB.get() + "\n")     
            self.Prescription.insert(END, "ID: \t\t\t" + self.ID.get() + "\n")     
            self.Prescription.insert(END, "Admission: \t\t\t" + self.Admission.get() + "\n")     
            self.Prescription.insert(END, "Symptom: \t\t\t" + self.Symptom.get() + "\n")     
            self.Prescription.insert(END, "Depart: \t\t\t" + self.Depart.get() + "\n")     
            self.Prescription.insert(END, "Doctor: \t\t\t" + self.Doctor.get() + "\n")     
            self.Prescription.insert(END, "Medical_History: \t\t\t" + self.Medical_History.get() + "\n")     
            self.Prescription.insert(END, "Diagnosis: \t\t\t" + self.Diagnosis.get() + "\n")     
            self.Prescription.insert(END, "Allergens: \t\t\t" + self.Allergens.get() + "\n")     
            self.Prescription.insert(END, "Followup: \t\t\t" + self.Followup.get() + "\n")       


    
    def iclear(self):
        self.Patient_Name.set("")
        self.Address.set("")
        self.DOB.set("")
        self.ID.set("")
        self.Admission.set("")
        self.Symptom.set("")
        self.Depart.set("")
        self.Doctor.set("")
        self.Medical_History.set("")
        self.Diagnosis.set("")
        self.Allergens.set("")
        self.Followup.set("")

        self.Prescription.delete("1.0",END)


    def iexit(self):
        iex = messagebox.askyesno("Hospital management System", "You want to exit?")
        if iex>0: 
            root.destroy() 
            return


root = Tk()
ob = Hospital(root)
root.mainloop()  
