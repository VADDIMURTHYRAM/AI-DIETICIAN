from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox  
from random import randint
import os
 
# Registraion Window
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("850x720")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    label_0 = Label(register_screen, text="Registration form",width=30,font=("bold", 20),fg='steel blue')
    label_0.place(x=150,y=53)

    name = StringVar()
    phone = IntVar()
    registrationid = IntVar()
    Label(register_screen, text="Please enter details below",fg="steel blue",font=( 'Bradley Hand ITC' ,20, 'bold' )).place(x=200,y=0)

    label_1 = Label(register_screen, text="Full Name",width=20,font=("bold", 10))
    label_1.place(x=250,y=130)

    entry_1 = Entry(register_screen,textvariable=name)
    entry_1.place(x=440,y=130)

    label_2 = Label(register_screen, text="Phone no.",width=20,font=("bold", 10))
    label_2.place(x=250,y=180)

    entry_2 = Entry(register_screen,textvariable=phone)
    entry_2.place(x=440,y=180)
    
    label_3 = Label(register_screen, text="Registration Id",width=20,font=("bold", 10))
    label_3.place(x=250,y=230)

    entry_3 = Entry(register_screen,textvariable=registrationid)
    entry_3.place(x=440,y=230)

    label_4 = Label(register_screen, text="Gender",width=20,font=("bold", 10))
    label_4.place(x=250,y=280)
    var = IntVar()
    Radiobutton(register_screen, text="Male",padx = 5, variable=var, value=1).place(x=445,y=280)
    Radiobutton(register_screen, text="Female",padx = 20, variable=var, value=2).place(x=500,y=280)
    label_5 = Label(register_screen, text="Email",width=20,font=("bold", 10))
    label_5.place(x=250,y=330)
    email=StringVar()
    entry_5 = Entry(register_screen,textvariable=email,width=40)
    entry_5.place(x=440,y=330)

    username_lable = Label(register_screen, text="Username",font=( 'Times New Roman' ,17, 'italic' ),)
    username_lable.place(x=250,y=380)
    username_entry = Entry(register_screen, font=( 15 ),bd=2,textvariable=username)
    username_entry.place(x=440,y=380)
    password_lable = Label(register_screen, text="Password",font=( 'Times New Roman' ,17, 'italic' ))
    password_lable.place(x=250,y=420)
    password_entry = Entry(register_screen,font=( 15),bd=2, textvariable=password, show='*')
    password_entry.place(x=440,y=420)
    Label(register_screen, text="").place(x=500,y=750)
    
    Button(register_screen, text="Register", width=10, height=1, bg='brown',fg='white', command = register_user).place(x=380,y=500)
    
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("650x480")
    Label(login_screen, text="Please enter your details below to login",font=( 'Bradley Hand ITC' ,17, 'bold' )).place(x=170,y=0)
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen,font=( 'Bradley Hand ITC' ,17,'bold' ), text="Username").place(x=250,y=50)
    username_login_entry = Entry(login_screen,font=(17) ,textvariable=username_verify)
    username_login_entry.place(x=250,y=100)
    Label(login_screen,font=( 'Bradley Hand ITC' ,17, 'bold' ), text="Password").place(x=250,y=150)
    password_login_entry = Entry(login_screen,font=(17 ), textvariable=password_verify, show= '*')
    password_login_entry.place(x=250,y=200)
    Button(login_screen, text="Login", width=10, height=1,bg='brown',fg='white', command = login_verify).place(x=275,y=250)





# Function on Register Button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    messagebox.showinfo("Registration","Registration Success")

# Funciton on Login Button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            BMR()
        else:
            password_not_recognised()
 
    else:
        user_not_found()
        
        
def BMR():
    global in_screen
    in_screen = Toplevel(login_screen)
    in_screen.title("Dietician")
    in_screen.geometry("650x480")

    l1 = Label(in_screen, text='Weight')
    l2 = Label(in_screen, text='Height(in cms)')
    l3 = Label(in_screen, text='Age  ')
    l4 = Label(in_screen, text = 'Gender', bg = 'white')
    l5 = Label(in_screen, text = 'Activity', bg = 'white')
    l7 = Label(in_screen, text = '')


    v3=DoubleVar()
    v4=DoubleVar()
    v5=IntVar()


    e3 = Entry(in_screen, textvariable=v3, width=30)
    e4 = Entry(in_screen, textvariable=v4, width=30)
    e5 = Entry(in_screen, textvariable=v5, width=30)

    Lb = Listbox(in_screen, height=6, width=30)
    Lb.insert(1, 'Sedentary (little or no exercise)')
    Lb.insert(2, 'Lightly active (1-3 days/week)')
    Lb.insert(3, 'Moderately active (3-5 days/week)')
    Lb.insert(4, 'Very active (6-7 days/week)')
    Lb.insert(5, 'Super active (twice/day)')

    Lb2 = Listbox(in_screen, height=2, width=30)
    Lb2.insert(1, 'Male')
    Lb2.insert(2, 'Female')

    var = Lb.get(ACTIVE)
    print (var)

    l5 = Label(in_screen, text = '')
    l5.grid(row=5,column=0)

    b1 = Button(in_screen, text = 'Submit', width=25, command = CALO)

    l1.grid(row=1,column=0)
    l2.grid(row=2,column=0)
    l3.grid(row=3,column=0)
    l4.grid(row=0,column=0)
    l5.grid(row=4,column=0)
    l7.grid(row=0,column=2)
    e3.grid(row=1, column=1)
    e4.grid(row=2, column=1)
    e5.grid(row=3, column=1)
    Lb.grid(row=4, column = 1)
    Lb2.grid(row=0, column = 1)
    b1.grid(row=6,columns=3)

    w = float(v3.get())
    h = float(v4.get())
    age = float(v5.get())
    act = str(Lb.get(ACTIVE))
    gender = Lb2.get(ACTIVE)
    global cal;
    cal = float()
    if gender == 'Male':
        cal = float()
        cal = 88.362 + (13.397*float(w)) + (4.799*float(h)) - (5.677*float(age))
        print (cal)
    elif gender == 'Female':
        cal = float()
        cal = 447.593 + (9.247*float(w)) + (3.098*float(h)) - (4.330*float(age))


    if act == 'Sedentary (little or no exercise)':
        cal = cal*1.2

    elif act == 'Lightly active (1-3 days/week)':
        cal = cal*1.375

    elif act == 'Moderately active (3-5 days/week)':
        cal = cal*1.55

    elif act == 'Very active (6-7 days/week)':
        cal = cal*1.725

    elif act == 'Super active (twice/day)':
        cal = cal*1.9

    print (cal)

def CALO():
    protein = ['Yogurt(1 cup)','Cooked meat(3 Oz)','Cooked fish(4 Oz)','1 whole egg + 4 egg whites','Tofu(5 Oz)']
    fruit = ['Berries(80 Oz)','Apple','Orange','Banana','Dried Fruits(Handfull)','Fruit Juice(125ml)']
    vegetable = ['Any vegetable(80g)']
    grains = ['Cooked Grain(150g)','Whole Grain Bread(1 slice)','Half Large Potato(75g)','Oats(250g)','2 corn tortillas']
    ps = ['Soy nuts(i Oz)','Low fat milk(250ml)','Hummus(4 Tbsp)','Cottage cheese (125g)','Flavored yogurt(125g)']
    taste_en = ['2 TSP (10 ml) olive oil','2 TBSP (30g) reduced-calorie salad dressin','1/4 medium avocado','Small handful of nuts','1/2 ounce  grated Parmesan cheese','1 TBSP (20g) jam, jelly, honey, syrup, sugar']
    
    if cal<1500:
        fin = StringVar()
        l6 = Label(in_screen, textvariable=fin, relief=RAISED )
        fin.set("Breakfast: "+protein[randint(0, 4)]+" + "+fruit[randint(0, 5)])
        l6.grid(row=0,column=3)


        fin2 = StringVar()
        l8 = Label(in_screen, textvariable=fin2, relief=RAISED )
        fin2.set("Lunch: "+protein[randint(0, 4)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
        l8.grid(row=1,column=3)


        fin3 = StringVar()
        l9 = Label(in_screen, textvariable=fin3, relief=RAISED )
        fin3.set("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
        l9.grid(row=2,column=3)


        fin4 = StringVar()
        l10 = Label(in_screen, textvariable=fin4, relief=RAISED )
        fin4.set("Dinner: "+protein[randint(0, 4)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
        l10.grid(row=3,column=3)


        fin5 = StringVar()
        l11 = Label(in_screen, textvariable=fin5, relief=RAISED )
        fin5.set("Snack: "+fruit[randint(0, 5)])
        l11.grid(row=4,column=3)


    elif cal<1800:
        fin = IntVar()
        l6 = Label(in_screen, textvariable=fin, relief=RAISED )
        fin.set("Breakfast: "+protein[randint(0, 4)]+" + "+fruit[randint(0, 5)])
        l6.grid(row=0,column=3)


        fin2 = StringVar()
        l8 = Label(in_screen, textvariable=fin2, relief=RAISED )
        fin2.set("Lunch: "+protein[randint(0, 4)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])
        l8.grid(row=1,column=3)


        fin3 = StringVar()
        l9 = Label(in_screen, textvariable=fin3, relief=RAISED )
        fin3.set("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
        l9.grid(row=2,column=3)


        fin4 = StringVar()
        l10 = Label(in_screen, textvariable=fin4, relief=RAISED )
        fin4.set("Dinner: 2 "+protein[randint(0, 4)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
        l10.grid(row=3,column=3)


        fin5 = StringVar()
        l11 = Label(in_screen, textvariable=fin5, relief=RAISED )
        fin5.set("Snack: "+fruit[randint(0, 5)])
        l11.grid(row=4,column=3)

    elif cal<2200:
        fin = StringVar()
        l6 = Label(in_screen, textvariable=fin, relief=RAISED )
        fin.set("Breakfast: "+protein[randint(0, 4)]+" + "+fruit[randint(0, 5)])
        l6.grid(row=0,column=3)


        fin2 = StringVar()
        l8 = Label(in_screen, textvariable=fin2, relief=RAISED )
        fin2.set("Lunch: "+protein[randint(0, 4)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])
        l8.grid(row=1,column=3)


        fin3 = StringVar()
        l9 = Label(in_screen, textvariable=fin3, relief=RAISED )
        fin3.set("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
        l9.grid(row=2,column=3)


        fin4 = StringVar()
        l10 = Label(in_screen, textvariable=fin4, relief=RAISED )
        fin4.set("Dinner: 2 "+protein[randint(0, 4)]+" + 2 "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)])
        l10.grid(row=3,column=3)


        fin5 = StringVar()
        l11 = Label(in_screen, textvariable=fin5, relief=RAISED )
        fin5.set("Snack: "+fruit[randint(0, 5)])
        l11.grid(row=4,column=3)


    elif cal>=2200:
        fin = StringVar()
        l6 = Label(in_screen, textvariable=fin, relief=RAISED )
        fin.set("Breakfast: 2 "+protein[randint(0, 4)]+" + "+fruit[randint(0, 5)]+" + "+grains[randint(0,4)])
        l6.grid(row=0,column=3)


        fin2 = StringVar()
        l8 = Label(in_screen, textvariable=fin2, relief=RAISED )
        fin2.set("Lunch: "+protein[randint(0, 4)]+" + "+vegetable[0]+" + Leafy Greens"+grains[randint(0,4)]+" + "+taste_en[randint(0,5)]+" + "+fruit[randint(0, 5)])
        l8.grid(row=1,column=3)


        fin3 = StringVar()
        l9 = Label(in_screen, textvariable=fin3, relief=RAISED )
        fin3.set("Snack: "+ps[randint(0, 4)]+" + "+vegetable[0])
        l9.grid(row=2,column=3)


        fin4 = StringVar()
        l10 = Label(in_screen, textvariable=fin4, relief=RAISED )
        fin4.set("Dinner: 2 "+protein[randint(0, 4)]+" + 2 "+vegetable[0]+" + Leafy Greens + 2 "+grains[randint(0,4)]+" + 2 "+taste_en[randint(0,5)])
        l10.grid(row=3,column=3)


        fin5 = StringVar()
        l11 = Label(in_screen, textvariable=fin5, relief=RAISED )
        fin5.set("Snack: "+fruit[randint(0, 5)])
        l11.grid(row=4,column=3)

    
      
'''
v1 = IntVar()
c1 = Checkbutton(a, text = 'Male', variable = v1)
c1.grid(row=0,column=1)

v2 = IntVar()
c2 = Checkbutton(a, text = 'Female', variable = v2)
c2.grid(row=0,column=2)
'''




def login_sucess():     
    messagebox.showinfo("Login","Login Sucess") 
    delete_login_success()
    
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("100x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()    
    
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("100x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()    
        

    
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
def delete_user_not_found_screen():
    user_not_found_screen.destroy()    
    
        
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1300x800")
    main_screen.title("Account Login")
    #img = ImageTk.PhotoImage(Image.open("diet.png"))
    #panel = Label(main_screen, image = img)
    #panel.place(x=220,y=100)
    lblinfo = Label(font=( 'Times New Roman' ,45, 'bold' ),text="AI DIETICIAN",fg="steel blue",bd=10)
    lblinfo.place(x=435,y=15)
    lb1 = Label(font=( 'Times New Roman' ,15 ),text="Already a user ??",fg="steel blue",bd=10)
    lb1.place(x=550,y=200)
    lb2 = Label(font=( 'Times New Roman' ,15 ),text="A New User ??",fg="steel blue",bd=10)
    lb2.place(x=550,y=300)
    b=Button(text="Login", height="3", width="35", command = login, bg="red",)
    b.place(x=520,y=240)
    c=Button(text="Register", height="3", width="35", command=register, bg="red")
    c.place(x=520,y=340)
    main_screen.mainloop()
main_account_screen()        
