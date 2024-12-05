from tkinter import *



def submition():
    email = entry_email.get()
    password = entry_password.get()
    



#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
window = Tk()
window.geometry('500x500')
window.title("pharmacy")
icon = PhotoImage(file='icon.png')
window.iconphoto(True,icon)
window.config(background='#E3E8A3')
#------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------

rounded_img = PhotoImage(file="entry_2.png")  # Ensure the image is rounded and matches your design



pass_label  = Label(window,text='Enter Your Email', font=('Arial', 15),fg='black', bg='#E3E8A3')
pass_label.place(x=180,y=170)
# Display the image as a label
photo_label_email = Label(window, image=rounded_img, bg="#E3E8A3")
photo_label_email.place(x=150, y=200)  # Adjust placement as needed

# Add the entry widget on top of the image
entry_email = Entry(window, bd=0, bg= '#D9D9D9',font=("Arial", 30))  # bd=0 removes border
entry_email.place(x=175, y=215, width=670, height=50)  # Adjust position and size as per the image dimensions


pass_label  = Label(window,text='Enter Your password', font=('Arial', 15),fg='black', bg='#E3E8A3')
pass_label.place(x=180,y=370)
# Display the image as a label
photo_label_password = Label(window, image=rounded_img, bg="#E3E8A3")
photo_label_password.place(x=150, y=400)  # Adjust placement as needed

# Add the entry widget on top of the image
entry_password = Entry(window, bd=0, bg= '#D9D9D9',font=("Arial", 30), show='*')  # bd=0 removes border
entry_password.place(x=175, y=415, width=670, height=50)  # Adjust position and size as per the image dimensions




#add pharmacy photo in the right of window

pharmacy_img = PhotoImage(file = 'phar_pj.png')

phar_img_label = Label(window,image=pharmacy_img, bg='#E3E8A3')
phar_img_label.place(x=1180 )





#button photo img

button_img = PhotoImage(file='button.png')

button_submit = Button(window, image=button_img,text='Submet',border=0, bg='#E3E8A3', command=submition)
button_submit.place(x=650,y=800)





window.mainloop()  #place window on computer screen, listen for events