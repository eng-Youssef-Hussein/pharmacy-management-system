from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import ttk


current_id = 51

def update_but():
    ...


def add_but():
    global current_id
    bd_list.insert(parent='', index="end",text=str(current_id) , values=(name_entry.get(), id_entry.get(),production_date_entry.get(), price_entry.get(),quantity_entry.get(),expird_date_entry.get()))
    current_id += 1



def delete_but():
    ...






window  =Tk()
window.geometry('500x500')
window.title("pharmacy")
icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)
window.config(background='#FFFFFF')

rounded_img = PhotoImage(file="manage_entry.png")


###########################################################the section to name entry################################################################



name_text = Label(window, text = "Medicine Name" , font=("Arial", 15 , "bold"), bg = "#FFFFFF")
name_text.place(x = 45 , y = 34)


name_label = Label(window , image= rounded_img , bg = "#FFFFFF")
name_label.place(x = 35 , y = 60)

name_entry = Entry(window, bg="#5E5E5E", fg="#FFFFFF", bd=0, font=("Arial", 13))
name_entry.place(x = 43 , y = 66 , width= 320 ,height=35)


###########################################################the section to id entry##################################################################


id_text = Label(window, text = "Medicine ID" , font=("Arial", 15 , "bold"), bg = "#FFFFFF")
id_text.place(x = 45 , y = 115)



id_label = Label(window , image= rounded_img, bg = "#FFFFFF")
id_label.place(x = 35 , y = 140)

id_entry = Entry(window, bg="#5E5E5E", fg="#FFFFFF", bd=0, font=("Arial", 13))
id_entry.place(x = 43 , y = 146 , width= 320 ,height=35)


###########################################################the section to production date entry#####################################################


date = Label(window, text = "Production Date" , font=("Arial", 15 , "bold"), bg = "#FFFFFF")
date.place(x = 45 , y = 195)


production_date = Label(window , image= rounded_img, bg = "#FFFFFF")
production_date.place(x = 35 , y = 220)

production_date_entry = Entry(window, bg="#5E5E5E", fg="#FFFFFF", bd=0, font=("Arial", 13))
production_date_entry.place(x = 43 , y = 226 , width= 320 ,height=35)


###########################################################THE SECTION TO PRICE ENTRY ##############################################################


price_text = Label(window, text = "Price" , font=("Arial", 15 , "bold"), bg = "#FFFFFF")
price_text.place(x = 417 , y = 34)


price = Label(window , image= rounded_img, bg = "#FFFFFF")
price.place(x = 405 , y = 60)

price_entry = Entry(window, bg="#5E5E5E", fg="#FFFFFF", bd=0, font=("Arial", 13))
price_entry.place(x = 415 , y = 66 , width= 320 ,height=35)



###########################################################THE SECTION TO QUANTITY ENTRY ###########################################################


quantity_text = Label(window, text = "Quantity" , font=("Arial", 15 , "bold"), bg = "#FFFFFF")
quantity_text.place(x = 417 , y = 115)



quantity = Label(window , image= rounded_img, bg = "#FFFFFF")
quantity.place(x = 405 , y = 140)

quantity_entry = Entry(window, bg="#5E5E5E", fg="#FFFFFF", bd=0, font=("Arial", 13))
quantity_entry.place(x = 415 , y = 146 , width= 320 ,height=35)


###########################################################THE SECTION TO EXPIRD ENTRY #############################################################


date = Label(window, text = "Expire Date" , font=("Arial", 15 , "bold"), bg='#FFFFFF')
date.place(x = 417 , y = 195)


expird_date = Label(window , image= rounded_img, bg = "#FFFFFF")
expird_date.place(x = 405 , y = 220)

expird_date_entry = Entry(window, bg="#5E5E5E", fg="#FFFFFF", bd=0, font=("Arial", 13))
expird_date_entry.place(x = 415 , y = 226 , width= 320 ,height=35)



###########################################################THE SECTION TO UPDATE BUTTON ############################################################
button1_img = PhotoImage(file='UPDATE.png')

button_submit = Button(window, image=button1_img,text='Submet',border=0, bg='#FFFFFF', command = update_but)
button_submit.place(x=870,y=55)



###########################################################THE SECTION TO ADD BUTTON ###############################################################
button2_img = PhotoImage(file='ADD.png')

button_submit = Button(window, image=button2_img,text='Submet',border=0, bg='#FFFFFF', command = add_but)
button_submit.place(x=870,y=135)




###########################################################THE SECTION TO DELETE BUTTON 

button3_img = PhotoImage(file='DELETE.png')

button_submit = Button(window, image=button3_img,text='Submet',border=0, bg='#FFFFFF', command = delete_but)
button_submit.place(x=870,y=215)






#################################THIS SECTION TO ADD A PHOTo
pharmacy_img = PhotoImage(file = 'medical-5459630_1280 1.png')

phar_img_label = Label(window,image=pharmacy_img, bg='#FFFFFF' )
phar_img_label.place(x=1400)


############################################      CREATE STYLE TO TREEVIEW
#ADD STYLE
style = ttk.Style()
#CONFIGURE THE TREEVIEW COLOR
style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight =40 ,font = ("Arial", 10, "bold"))
style.map("Treeview", background = [("selected" , "#347083")])



############################################   CREATE FRAME TO TREEVIEW
tree_frame = Frame(window)
tree_frame.place(height=650,width=1920,y=350)


#########################################    CREATE TREEVIEW SCROLLBAR
scroll_bar = Scrollbar(tree_frame)
scroll_bar.pack(side=RIGHT, fill=Y)

################################################THIS SECTION TO MAKE A LIST FOR DATABASES


bd_list = ttk.Treeview(tree_frame, yscrollcommand=scroll_bar.set, selectmode="extended")
bd_list.place(height=650,width=1900)

scroll_bar.config(command=bd_list.yview)

bd_list["columns"]=("Name","ID","Production_Date","Price","Quantity","Expired_Date")

bd_list.column('#0', width=0 , stretch=NO)
bd_list.column('Name', width=120 , anchor=W)
bd_list.column("ID",width="120", anchor="center")
bd_list.column("Production_Date",width="120", anchor="center")
bd_list.column("Price",width="120", anchor="center")
bd_list.column("Quantity",width="120", anchor="center")
bd_list.column("Expired_Date",width="120", anchor="center")

bd_list.column('#0', anchor=W)
bd_list.heading('Name', text="Name",anchor='w')
bd_list.heading("ID", text="ID", anchor="center")
bd_list.heading("Production_Date", text="Production_Date", anchor='center')
bd_list.heading("Price", text="Price",anchor='center')
bd_list.heading("Quantity",text="Quantity", anchor="center")
bd_list.heading("Expired_Date", text="Expired_Date",anchor="center")


data = [
    ["Acetaminophen", "241001731", "22-10-22023", "100 EGP", "30", "21-01-2026"],
    ["Paracetamol", "241046531", "12-11-22023", "55 EGP", "30", "31-12-2067"],
    ["Sildenafil", "241003211", "22-11-22023", "55 EGP", "30", "31-12-2066"],
    ["Ondansetron", "2411326531", "22-11-22023", "45 EGP", "30", "31-12-2064"],
    ["Metoprolol", "24100146", "22-31-22023", "35 EGP", "30", "31-12-2063"],
    ["Bupropion", "24100172132", "22-11-22023", "22 EGP", "30", "31-12-2062"],
    ["Doxycycline", "2410046541", "12-11-22023", "21 EGP", "30", "31-12-2061"],
    ["Valsartan", "2410045678", "12-11-22023", "65 EGP", "30", "31-12-2060"],
    ["Diazepam", "24179512", "31-12-22023", "45 EGP", "30", "31-12-2059"],
    ["Cetirizine", "241786542", "22-11-22023", "9 EGP", "30", "31-12-2058"],
    ["Ranitidine ", "241004561", "31-11-22023", "63 EGP", "30", "31-12-2057"],
    ["Loratadine", "241001236", "22-12-22023", "10 EGP", "30", "31-12-2056"],
    ["Tamsulosin", "241009874", "22-11-22023", "41 EGP", "30", "31-12-2054"],
    ["Furosemide", "241007894", "31-11-22023", "59 EGP", "30", "31-02-2053"],
    ["Hydrochlorothiazide", "241101731", "22-11-22023", "536 EGP", "30", "31-22-2051"],
    ["Duloxetine", "241991731", "31-11-22023", "45 EGP", "30", "31-12-2050"],
    ["Ciprofloxacin", "241881731", "22-12-22023", "89 EGP", "30", "31-12-2049"],
    ["Rosuvastatin", "241771731", "31-11-22023", "82 EGP", "30", "31-12-2048"],
    ["Albuterol", "241661731", "12-11-22023", "46 EGP", "30", "31-12-2047"],
    ["Warfarin", "241551731", "22-11-22023", "96 EGP", "30", "31-12-2046"],
    ["Fluoxetine", "255551731", "22-11-22023", "69 EGP", "30", "31-12-2045"],
    ["Pantoprazole", "441001731", "22-10-22023", "45 EGP", "30", "31-12-2044"],
    ["Zolpidem", "241044444", "31-11-22023", "45 EGP", "30", "05-10-2043"],
    ["Tramadol", "241444731", "05-05-22023", "65 EGP", "30", "05-06-2042"],
    ["Prednisone", "241333331", "22-11-22023", "31 EGP", "30", "20-10-2041"],
    ["Azithromycin", "333001731", "30-10-22023", "46 EGP", "30", "30-02-2040"],
    ["Simvastatin", "233301731", "01-02-22023", "61 EGP", "30", "30-11-2039"],
    ["Montelukast", "223401731", "22-11-22023", "34 EGP", "30", "01-02-2038"],
    ["Clopidogrel", "221001731", "22-02-22023", "46 EGP", "30", "01-02-2037"],
    ["Sertraline", "296311731", "31-11-22023", "63 EGP", "30", "11-05-2033"],
    ["Gabapentin", "269601731", "22-12-22023", "522 EGP", "30", "31-12-2032"],
    ["Losartan", "369001731", "07-02-22023", "650 EGP", "30", "07-02-2032"],
    ["Alprazolam", "241963731", "20-09-22023", "150 EGP", "30", "26-06-2032"],
    ["Omeprazole", "241025731", "22-12-22023", "100 EGP", "30", "25-12-2032"],
    ["Amlodipine", "2410018531", "13-01-22023", "99 EGP", "30", "20-01-2033"],
    ["Levothyroxine", "24285731", "12-11-22023", "19 EGP", "30", "01-12-2032"],
    ["Atorvastatin", "225801731", "11-11-22023", "17 EGP", "30", "02-02-2031"],
    ["Lisinopril", "245681731", "22-03-22023", "16 EGP", "30", "02-03-2030"],
    ["Metformin", "225881731", "22-02-22023", "18 EGP", "30", "20-02-2029"],
    ["Amoxicillin", "228688731", "22-01-22023", "20 EGP", "30", "01-09-2028"],
    ["Ibuprofen", "241071731", "22-05-22023", "13 EGP", "30", "11-01-2027"]

]

bd_list.tag_configure("oddrow", background="#FFFFFF")
bd_list.tag_configure("evenrow", background="#ABABAB")


global count
count = 0
for record in data:
    if count % 2 == 0 :
        bd_list.insert(parent='',index='end', text='',iid=count ,values=(record[0], record[1],record[2],record[3], record[4], record[5]),tags=("evenrow") )
    else:
        bd_list.insert(parent='',index='end', text='',iid=count ,values=(record[0], record[1],record[2],record[3], record[4], record[5]),tags=("oddrow") )
    count+=1





window.mainloop()