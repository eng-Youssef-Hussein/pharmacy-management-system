from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import ttk 

def database_query():
    conn = sqlite3.connect('ProductDB.db')

    #create a cursor instance
    c= conn.cursor()
    c.execute("SELECT * FROM Product")
    records = c.fetchall()
    global count
    count = 0

    for record in records:
        if count % 2 ==0 :
            bd_list.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('evenrow'))
        else:
            bd_list.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('oddrow'))
        count +=1


    conn.commit()
    conn.close()


current_id = 51








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


#####################################################################################################################################################
#####################################################################################################################################################
########################################################### THE SECTION TO UPDATE BUTTON ############################################################


button1_img = PhotoImage(file='UPDATE.png')

def select_record(e):
    name_entry.delete(0, END)
    id_entry.delete(0, END)
    production_date_entry.delete(0, END)
    price_entry.delete(0, END)
    quantity_entry.delete(0, END)
    expird_date_entry.delete(0, END)



    selected = bd_list.focus()
    values = bd_list.item(selected, 'values')


    name_entry.insert(0, values[0])
    id_entry.insert(0, values[1])
    production_date_entry.insert(0, values[2])
    price_entry.insert(0, values[3])
    quantity_entry.insert(0, values[4])
    expird_date_entry.insert(0, values[5])


def update_but():
    selected = bd_list.focus()
    bd_list.item(selected, text='', values=(name_entry.get(), id_entry.get(), production_date_entry.get(), price_entry.get(), quantity_entry.get(), expird_date_entry.get()))



    conn = sqlite3.connect('ProductDB.db')

    
    c = conn.cursor()

    
    c.execute("""
        UPDATE Product 
        SET Name = ?, ID = ?, P_Date = ?, Price = ?, Quantity = ?, Ex_DATE = ?
        WHERE ID = ?
    """, (
        name_entry.get(),
        id_entry.get(),
        production_date_entry.get(),
        price_entry.get(),
        quantity_entry.get(),
        expird_date_entry.get(),
        id_entry.get()
    ))

    # حفظ التغييرات
    conn.commit()
    conn.close()





    name_entry.delete(0, END)
    id_entry.delete(0, END)
    production_date_entry.delete(0, END)
    price_entry.delete(0, END)
    quantity_entry.delete(0, END)
    expird_date_entry.delete(0, END)



selection_button = Button(window, command=select_record)
button_submit = Button(window, image=button1_img,text='Submet',border=0, bg='#FFFFFF', command = update_but)
button_submit.place(x=870,y=55)


#################################################################################################################################################################################
#################################################################################################################################################################################
###########################################################    THE SECTION TO ADD BUTTON     ####################################################################################


button2_img = PhotoImage(file='ADD.png')



def add_but():
    global current_id
    bd_list.insert(parent='', index='end', iid=current_id, text='' ,values=(name_entry.get(),id_entry.get(), production_date_entry.get(), price_entry.get(), quantity_entry.get(), expird_date_entry.get()))
    current_id += 1



    add_conn = sqlite3.connect('ProductDB.db')

    
    add_c = add_conn.cursor()

    
    add_c.execute("""
        insert into Product
        values (?,?,?,?,?,?)
    """, (
        name_entry.get(),
        id_entry.get(),
        production_date_entry.get(),
        price_entry.get(),
        quantity_entry.get(),
        expird_date_entry.get()
    ))

    # حفظ التغييرات
    add_conn.commit()
    add_conn.close()



    name_entry.delete(0,END)
    id_entry.delete(0,END)
    production_date_entry.delete(0,END)
    price_entry.delete(0,END)
    quantity_entry.delete(0,END)
    expird_date_entry.delete(0,END)



add_submit = Button(window, image=button2_img,text='Submet',border=0, bg='#FFFFFF' , command=add_but)
add_submit.place(x=870,y=135)



#################################################################################################################################################################################
#################################################################################################################################################################################
###########################################################    THE SECTION TO DELETE BUTTON     #################################################################################

button3_img = PhotoImage(file='DELETE.png')


def delete_but():


    add_conn = sqlite3.connect('ProductDB.db')

    
    add_c = add_conn.cursor()

    
    add_c.execute("""
        delete from Product
        where ID = ?
    """, (
        id_entry.get(),
    ))

    # حفظ التغييرات
    add_conn.commit()
    add_conn.close()


    x = bd_list.selection()
    for selected in x :
        bd_list.delete(selected)

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
tree_frame.place(height=590,width=1920,y=350)


#########################################    CREATE TREEVIEW SCROLLBAR
scroll_bar = Scrollbar(tree_frame)
scroll_bar.pack(side=RIGHT, fill=Y)

################################################THIS SECTION TO MAKE A LIST FOR DATABASES


bd_list = ttk.Treeview(tree_frame, yscrollcommand=scroll_bar.set, selectmode="extended")
bd_list.place(height=590,width=1900)

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




bd_list.tag_configure("oddrow", background="#FFFFFF")
bd_list.tag_configure("evenrow", background="#ABABAB")





#########################################################################################################################         FUNCTION FOR SEARCHING TO DATABASE ROWS

def search_records(event=None):
    #       THE FOR LOOP TO DELETE EVERYTHING IN THE LIST TO SHOW YOU WHAT YOU SEARCHING ABOUT
    for record in bd_list.get_children():
        bd_list.delete(record)
    
    searching = search_entry_box.get()

    #           THIS IS THE SQLITE CONNECTION TO DO DATABASE CODES LIKE SHOW WHAT YOU SEARCHED FOR
    src_conn = sqlite3.connect('ProductDB.db')

    #create a cursor instance
    src_c= src_conn.cursor()
    src_c.execute("SELECT * FROM Product where Name like ?", (f'%{searching.strip()}%',))
    records = src_c.fetchall()
    global count
    count = 0

    for record in records:
        if count % 2 ==0 :
            bd_list.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('evenrow'))
        else:
            bd_list.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('oddrow'))
        count +=1


    src_conn.commit()
    src_conn.close()
    


    #   THIS CODE TO CHESK THE ENTRY IF EMPTY YOU WILL RESET THE TREEVIEW

    if searching == '':
        for record in records:
            if count % 2 ==0 :
                bd_list.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('evenrow'))
            else:
                bd_list.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=('oddrow'))
            count +=1




###################     SEARCH DATABASE ROW IN TREEVIEW
global search_entry_box

search_label = Label(window, text='Search :', font=('Arial', 13, "bold"), bg="#FFFFFF")
search_label.place(y=960, x=1480)

search_entry_image = Label(window, image=rounded_img, bg="#FFFFFF")
search_entry_image.place(y=950,x=1565)


search_entry_box = Entry(window,bg="#5E5E5E", bd=0,font=("Arial", 16), fg="#FFFFFF")
search_entry_box.place(y=957,x=1575,width= 320 ,height=35)

search_button = Button(window,  text="cleck",command=search_records)













search_entry_box.bind('<KeyRelease>', lambda event: search_records())

bd_list.bind("<ButtonRelease-1>", select_record)








database_query()
window.mainloop()
