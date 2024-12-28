from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox





current_id = 8


def database_query():
    conn = sqlite3.connect('supplierDB.db')

    #create a cursor instance
    c= conn.cursor()
    c.execute("SELECT * FROM supplier")
    records = c.fetchall()
    global count
    count = 1

    for record in records:
        if count % 2 ==0 :
            data_list.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('evenrow'))
        else:
            data_list.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('oddrow'))
        count +=1


    conn.commit()
    conn.close()





window = Tk()

rounded_entry = PhotoImage(file="manage_entry.png")
##########################################                  SUPPLIER NAME ENTRY
supplier_name_text = Label(window, text="Enter The Name Of Supplier :",font=("Arial", 10,"bold")).place(x=30,y=30)
supplier_name_entry_img = Label(window, image=rounded_entry).place(x=20,y=50)
supplier_name_entrybox = Entry(window, fg='#FFFFFF',bg='#5E5E5E',bd=0,font=("Arial",13))
supplier_name_entrybox.place(x=30,y=57,width=320,height=35)

#########################################                   SUPPLIER PHONE NUMBER ENTRY

supplier_phonenumber_text = Label(window,text="Enter The PhoneNumber :", font=("Arial", 10, "bold")).place(x=30,y=150)
supplier_phonenumbername_entry_img = Label(window, image=rounded_entry).place(x=20,y=170)
supplier_phonenumber_entrybox = Entry(window, fg='#FFFFFF',bg='#5E5E5E',bd=0,font=("Arial",13))
supplier_phonenumber_entrybox.place(x=30,y=177,width=320,height=35)

#########################################                   COMPANY NAME ENTRY

companyname_text = Label(window, text="Enter The CompanyName :", font=("Arial", 10, "bold")).place(x=30,y=260)
companyname_entry_img = Label(window,image=rounded_entry).place(x=20,y=280)
companyname_entybox = Entry(window, fg='#FFFFFF',bg='#5E5E5E',bd=0,font=("Arial",13))
companyname_entybox.place(x=30,y=286,width=320,height=35)

#########################################                   SUPPORT EMAIL TO COMPANY ENTRY

support_email_text = Label(window, text="Enter The SupportEmail :", font=("Arial", 10, "bold")).place(x=30,y=380)
support_email_entry_img = Label(window,image=rounded_entry).place(x=20,y=400)
support_email_entrybox = Entry(window, fg='#FFFFFF',bg='#5E5E5E',bd=0,font=("Arial",13))
support_email_entrybox.place(x=30,y=406,width=320,height=35)


########################################                    HOT LINE ENTRY

hot_line_text = Label(window, text="Enter The HOTLINE :", font=("Arial", 10, "bold")).place(x=30,y=500)
hot_line_entry_img = Label(window,image=rounded_entry).place(x=20,y=520)
hot_line_entrybox = Entry(window, fg='#FFFFFF',bg='#5E5E5E',bd=0,font=("Arial",13))
hot_line_entrybox.place(x=30,y=526,width=320,height=35)


########################################                    RECEIPT DATE ENTRY

receipt_date_text = Label(window, text="Enter The Receipt Date :", font=("Arial", 10, "bold")).place(x=30,y=620)
receipt_date_entry_img = Label(window,image=rounded_entry).place(x=20,y=640)
receipt_date_entrybox = Entry(window, fg='#FFFFFF',bg='#5E5E5E',bd=0,font=("Arial",13))
receipt_date_entrybox.place(x=30,y=646,width=320,height=35)



########################################                    CREATE BUTTON FOR ADDING
def add_but():

    name=supplier_name_entrybox.get()
    number=supplier_phonenumber_entrybox.get()
    cname=companyname_entybox.get()
    email=support_email_entrybox.get()
    hotline=hot_line_entrybox.get()
    date=receipt_date_entrybox.get()
    

    if not name and not number and not cname and not email and not hotline and not date:
        messagebox.showerror(title="ERROR!!!", message="All input are required..!")



    else:
        messagebox.showinfo(title="Succesfully", message="Added Successfully 😁")
        global current_id
        data_list.insert(parent='', index='end', iid=current_id, text='' ,values=(supplier_name_entrybox.get(),supplier_phonenumber_entrybox.get(), companyname_entybox.get(), support_email_entrybox.get(), hot_line_entrybox.get(), receipt_date_entrybox.get()))
        current_id += 1



        add_conn = sqlite3.connect('supplierDB.db')

        
        add_c = add_conn.cursor()

        
        add_c.execute("""
            insert into supplier
            values (?,?,?,?,?,?)
        """, (
            supplier_name_entrybox.get(),
            supplier_phonenumber_entrybox.get(),
            companyname_entybox.get(),
            support_email_entrybox.get(),
            hot_line_entrybox.get(),
            receipt_date_entrybox.get()
        ))

        # حفظ التغييرات
        add_conn.commit()
        add_conn.close()

        



        



        supplier_name_entrybox.delete(0,END)
        supplier_phonenumber_entrybox.delete(0,END)
        companyname_entybox.delete(0,END)
        support_email_entrybox.delete(0,END)
        hot_line_entrybox.delete(0,END)
        receipt_date_entrybox.delete(0,END)



ADD_subimtion = PhotoImage(file="ADD.png")
submition_button = Button(window,image=ADD_subimtion,bd=0,command=add_but).place(x=120,y=800)



########################################                    CREATE BUTTON FOR DELETING THE ROW

button3_img = PhotoImage(file='DELETE.png')


def select_record(e):
    

    supplier_name_entrybox.delete(0, END)
    supplier_phonenumber_entrybox.delete(0, END)
    companyname_entybox.delete(0, END)
    support_email_entrybox.delete(0, END)
    hot_line_entrybox.delete(0, END)
    receipt_date_entrybox.delete(0, END)



    selected = data_list.focus()
    values = data_list.item(selected, 'values')


    supplier_name_entrybox.insert(0, values[0])
    supplier_phonenumber_entrybox.insert(0, values[1])
    companyname_entybox.insert(0, values[2])
    support_email_entrybox.insert(0, values[3])
    hot_line_entrybox.insert(0, values[4])
    receipt_date_entrybox.insert(0, values[5])


def delete_but():

    if(messagebox.askokcancel(title="DELETE ITEM", message="Are you sure ?! ")):
        messagebox.showinfo("Successfully", message="Deleted Successfully...")

        add_conn = sqlite3.connect('supplierDB.db')

        
        add_c = add_conn.cursor()

        
        add_c.execute("""
            delete from supplier
            where phone = ?
        """, (
            supplier_phonenumber_entrybox.get(),
        ))

        # حفظ التغييرات
        add_conn.commit()
        add_conn.close()


        x = data_list.selection()
        for selected in x :
            data_list.delete(selected)
    else:
        messagebox.showerror(title="DENIED", message="Deleted denied...")

button_submit = Button(window, image=button3_img,text='Submet',border=0, bg='#FFFFFF', command = delete_but)
button_submit.place(x=105,y=900)







#########################################################################################################################################################################
#########################################################################################################################################################################
##############################################          CREATE THE DATABASE AND SHOW IT IN TREEVIEW         #############################################################

############################################      CREATE STYLE TO TREEVIEW
#ADD STYLE
style = ttk.Style()
#CONFIGURE THE TREEVIEW COLOR
style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight =40 ,font = ("Arial", 10, "bold"))
style.map("Treeview", background = [("selected" , "#347083")])



############################################   CREATE FRAME TO TREEVIEW
tree_frame = Frame(window)
tree_frame.place(height=1008,width=1420,x=500)


#########################################    CREATE TREEVIEW SCROLLBAR
scroll_bar = Scrollbar(tree_frame)
scroll_bar.pack(side=RIGHT, fill=Y)


################################################THIS SECTION TO MAKE A LIST FOR DATABASES


data_list = ttk.Treeview(tree_frame, yscrollcommand=scroll_bar.set, selectmode="extended")
data_list.place(height=1008,width=1400)

scroll_bar.config(command=data_list.yview)

data_list["columns"]=("Supplier_name","Supplier_PhoneNumber","Company_name","Support_Email","HOTLINE","RECEPT_DATE")

data_list.column('#0', width=0 , stretch=NO)
data_list.column('Supplier_name', width="80" , anchor=W)
data_list.column("Supplier_PhoneNumber",width="80", anchor="center")
data_list.column("Company_name",width="80", anchor="center")
data_list.column("Support_Email",width="80", anchor="center")
data_list.column("HOTLINE",width="80", anchor="center")
data_list.column("RECEPT_DATE",width="80", anchor="center")

data_list.column('#0', anchor=W)
data_list.heading('Supplier_name', text="Supplier_name",anchor='w')
data_list.heading("Supplier_PhoneNumber", text="Supplier_PhoneNumber", anchor="center")
data_list.heading("Company_name", text="Company_name", anchor='center')
data_list.heading("Support_Email", text="Support_Email",anchor='center')
data_list.heading("HOTLINE",text="HOTLINE", anchor="center")
data_list.heading("RECEPT_DATE", text="RECEPT_DATE",anchor="center")








data_list.tag_configure("oddrow", background="#FFFFFF")
data_list.tag_configure("evenrow", background="#ABABAB")







data_list.bind("<ButtonRelease-1>", select_record)

database_query()
window.mainloop()