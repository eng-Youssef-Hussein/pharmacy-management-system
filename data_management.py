from tkinter import *





window  =Tk()
window.geometry('500x500')
window.title("pharmacy")
icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)
window.config(background='#FFFFFF')

rounded_img = PhotoImage(file="manage_entry.png")


###########################################################the section to name entry################################################################



name_text = Label(window, text = "Madicine Name" , font=("Arial", 15 , "bold"), bg = "#FFFFFF")
name_text.place(x = 45 , y = 34)


name_label = Label(window , image= rounded_img , bg = "#FFFFFF")
name_label.place(x = 35 , y = 60)

name_entry = Entry(window, bg="#5E5E5E", fg="#FFFFFF", bd=0, font=("Arial", 13))
name_entry.place(x = 43 , y = 66 , width= 320 ,height=35)


###########################################################the section to id entry##################################################################


id_text = Label(window, text = "Madicine ID" , font=("Arial", 15 , "bold"), bg = "#FFFFFF")
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


date = Label(window, text = "Production Date" , font=("Arial", 15 , "bold"), bg='#FFFFFF')
date.place(x = 417 , y = 195)


expird_date = Label(window , image= rounded_img, bg = "#FFFFFF")
expird_date.place(x = 405 , y = 220)

expird_date_entry = Entry(window, bg="#5E5E5E", fg="#FFFFFF", bd=0, font=("Arial", 13))
expird_date_entry.place(x = 415 , y = 226 , width= 320 ,height=35)



###########################################################THE SECTION TO UPDATE BUTTON ############################################################
button1_img = PhotoImage(file='UPDATE.png')

button_submit = Button(window, image=button1_img,text='Submet',border=0, bg='#FFFFFF')
button_submit.place(x=870,y=55)



###########################################################THE SECTION TO ADD BUTTON ###############################################################
button2_img = PhotoImage(file='ADD.png')

button_submit = Button(window, image=button2_img,text='Submet',border=0, bg='#FFFFFF')
button_submit.place(x=870,y=135)




###########################################################THE SECTION TO DELETE BUTTON 

button3_img = PhotoImage(file='DELETE.png')

button_submit = Button(window, image=button3_img,text='Submet',border=0, bg='#FFFFFF')
button_submit.place(x=870,y=215)






#################################THIS SECTION TO ADD A PHOTO
pharmacy_img = PhotoImage(file = 'medical-5459630_1280 1.png')

phar_img_label = Label(window,image=pharmacy_img, bg='#FFFFFF')
phar_img_label.place(x=1400)




################################################THIS SECTION TO MAKE A LIST FOR DATABASES


bd_list = Listbox(window, width= 320 , height= 41, bg='#A1A1A1', font=("Arial" , 20))
bd_list.place(y =351)

bd_list.insert(1 ,"koshary")
bd_list.insert(2 ,"mombar")
bd_list.insert(3 ,"kersha")
bd_list.insert(4 ,"ma7shy")
bd_list.insert(5 ,"kofta")
bd_list.insert(6 ,"7alaweyat")





window.mainloop()