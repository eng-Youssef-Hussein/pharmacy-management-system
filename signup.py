from tkinter import *
    


#-------------------------------------------#-------------------------------------------#-------------------------------------------#-------------------------------------------
#-------------------------------------------#-------------------------the functions for the button code     ------------------------#-------------------------------------------
#-------------------------------------------#-------------------------------------------#-------------------------------------------#-------------------------------------------

def submition():
    User_name = entry_user.get()
    Email = entry_email.get()
    Password = entry_password.get()
    Con_password = entry_conferm_password.get()

#-------------------------------------------#-------------------------------------------#-------------------------------------------#-------------------------------------------
#-------------------------------------------#-------------------------------------------#-------------------------------------------#-------------------------------------------
#-------------------------------------------#-------------------------------------------#-------------------------------------------#-------------------------------------------




    








#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
window = Tk()
window.geometry('500x500')
window.title("pharmacy")
icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)
window.config(background='#FFFFFF')
#------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------




rounded_img = PhotoImage(file="Rectangle 2.png")  #img for rounded entry


########################################################  User Name Entry ###############################################################


user_label  = Label(window,text='User name', font=('Arial', 15),fg='black', bg='#FFFFFF')
user_label.place(x=180,y=70)
# Display the image as a label
photo_label_user = Label(window, image=rounded_img, bg="#FFFFFF")
photo_label_user.place(x=150, y=100)  

# Add the entry widget on top of the image
entry_user = Entry(window, bd=0, bg= '#414141',font=("Arial", 20),fg="#FFFFFF")  
entry_user.place(x=170, y=107, width=420, height=40) 

#----------------------------------------------------------------------------------------------------------------------------------

########################################################  Email Name Entry ###############################################################

label1  = Label(window,text='Email', font=('Arial', 15),fg='black', bg='#FFFFFF')
label1.place(x=180,y=270)
# Display the image as a label
photo_label_email = Label(window, image=rounded_img, bg="#FFFFFF")
photo_label_email.place(x=150, y=300) 

# Add the entry widget on top of the image
entry_email = Entry(window, bd=0, bg= '#414141',font=("Arial", 20),fg="#FFFFFF")  
entry_email.place(x=170, y=308, width=420, height=40)  
#----------------------------------------------------------------------------------------------------------------------------------
########################################################  Password Name Entry ###############################################################

label2  = Label(window,text='Password', font=('Arial', 15),fg='black', bg='#FFFFFF')
label2.place(x=180,y=470)
# Display the image as a label
photo_label_password = Label(window, image=rounded_img, bg="#FFFFFF")
photo_label_password.place(x=150, y=500)  # Adjust placement as needed

# Add the entry widget on top of the image
entry_password = Entry(window, bd=0, bg= '#414141',font=("Arial", 20), show='*',fg="#FFFFFF")  
entry_password.place(x=170, y=508, width=420, height=40)  

#----------------------------------------------------------------------------------------------------------------------------------

########################################################  Confirm Password Name Entry ###############################################################

label3  = Label(window,text='Confirm Password', font=('Arial', 15),fg='black', bg='#FFFFFF')
label3.place(x=180,y=670)
# Display the image as a label
photo_label_password = Label(window, image=rounded_img, bg="#FFFFFF")
photo_label_password.place(x=150, y=700) 

# Add the entry widget on top of the image
entry_conferm_password = Entry(window, bd=0, bg= '#414141',font=("Arial", 20), show='*',fg="#FFFFFF") 
entry_conferm_password.place(x=170, y=708, width=420, height=40) 

#----------------------------------------------------------------------------------------------------------------------------------




#add photo in the right of window

pharmacy_img = PhotoImage(file = 'medical-5459630_1280.png')

phar_img_label = Label(window,image=pharmacy_img, bg='#FFFFFF')
phar_img_label.place(x=675)
#----------------------------------------------------------------------------------------------------------------------------------





#button photo img

button_img = PhotoImage(file='button.png')

button_submit = Button(window, image=button_img,text='Submet',border=0, bg='#FFFFFF', command = submition)
button_submit.place(x=220,y=900)

#----------------------------------------------------------------------------------------------------------------------------------





window.mainloop()  