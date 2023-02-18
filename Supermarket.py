from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Main_Supermarket import *
import webbrowser
import random
import sqlite3
import datetime

date_now = datetime.datetime.now()


def Create_user():
    user_window = Toplevel()
    user_window.title("Register New User")
    user_window.config(bg='#46839E')
    user_window.geometry('570x350+280+170')

    text_1 = """
    هذا النافذة تعمل على تسجيل بائعين 
    . جدد في النظام
    
     . يجب تسجيل الاسمين الاول و الثاني
     
     يجب إدخال اسم مستخدم ويتكون
      . من حروف و ارقام
      
     . يجب إدخال كلمة المرور بـ حرف و ارقام
    """

    label_1 = Label(user_window, text=text_1, justify='right', font=('Tajawal-Medium', 9),
                    fg='black', bg='#46839E')
    label_1.place(x=360, y=14)

    # ------- variables
    create_user_full_name_var = StringVar()
    create_user_user_name_var = StringVar()
    create_user_password_name_var = StringVar()

    def clear_all_entrys():
        create_user_full_name_var.set('')
        create_user_user_name_var.set('')
        create_user_password_name_var.set('')

    def add_user_in_database():
        if len(create_user_full_name_var.get()) <= 2:
            messagebox.showerror('Error', 'يجب وضع أسم كاملا')

        elif len(create_user_user_name_var.get()) <= 2:
            messagebox.showerror('Error', 'يجب وضع أسم مستخدم صالحا')

        elif len(create_user_password_name_var.get()) <= 2:
            messagebox.showerror('Error', 'يجب الايكون كلمة المرور قصيرة')

        else:
            db = sqlite3.connect(
                "C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Supermarket_project_3\\Database\\Supermarket_Users.db")

            my_cursor = db.cursor()
            full_name = create_user_full_name_var.get()
            user_name = create_user_user_name_var.get()
            password = create_user_password_name_var.get()
            id_random = random.randint(100, 250)
            my_cursor.execute(f"INSERT INTO Users (ID, Full_name, User_name, Password)"
                              f" VALUES('{id_random}','{full_name}', '{user_name}', '{password}')")
            messagebox.showinfo(
                title='تم',
                message='..تم إنشاء مستخدم جديد بنجاح',
            )
            db.commit()
            db.close()
            user_window.destroy()

    # ----- Buttons All
    # ------ Start
    buttons_create_user_top_level = Button(user_window, text='.. إنشاء', width=13, fg='black', bg='#F7DC6F',
                                           font=('Tajawal-Medium', 9), command=add_user_in_database)
    buttons_create_user_top_level_2 = Button(user_window, text='إلغاء', width=13, fg='black', bg='#F7DC6F',
                                             font=('Tajawal-Medium', 9), command=user_window.destroy)
    buttons_create_user_top_level_3 = Button(user_window, text='افراغ الحقول', width=13, fg='black', bg='#F7DC6F',
                                             font=('Tajawal-Medium', 9), command=clear_all_entrys)
    buttons_create_user_top_level.place(x=470, y=270)
    buttons_create_user_top_level_2.place(x=225, y=270)
    buttons_create_user_top_level_3.place(x=350, y=270)
    # ------ End

    # ------ Labels All
    # ------ Start
    label_create_user_full_name = Label(user_window, text='Full Name:', font=('Tajawal-Medium', 13, 'bold'),
                                        fg='black', bg='#46839E')
    label_create_user_name = Label(user_window, text='User Name:', font=('Tajawal-Medium', 13, 'bold'),
                                   fg='black', bg='#46839E')

    label_create_user_password = Label(user_window, text='Password:', font=('Tajawal-Medium', 13, 'bold'),
                                       fg='black', bg='#46839E')

    label_create_user_full_name.place(x=235, y=30)
    label_create_user_name.place(x=235, y=110)
    label_create_user_password.place(x=235, y=190)

    # ------ End

    # ------ Entry's All
    # ------ Start
    entry_create_user_Full_name = Entry(user_window, font=('Tajawal-Medium', 11), fg='black', bg='#7F8C8D',
                                        justify='center', textvariable=create_user_full_name_var)
    entry_create_user_Full_name.place(x=195, y=60)

    entry_create_user_name = Entry(user_window, font=('Tajawal-Medium', 11), fg='black', bg='#7F8C8D',
                                   justify='center', textvariable=create_user_user_name_var)
    entry_create_user_name.place(x=195, y=140)

    entry_create_user_password = Entry(user_window, font=('Tajawal-Medium', 11), fg='black', bg='#7F8C8D',
                                       justify='center', textvariable=create_user_password_name_var)
    entry_create_user_password.place(x=195, y=220)
    # ------ End

    user_window.mainloop()


def get_user_and_password():
    db = sqlite3.connect(
        "C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Supermarket_project_3\\Database\\Supermarket_Users.db")

    my_cursor = db.cursor()
    get_name = user_name_ver.get()
    get_password = user_password_var.get()

    if len(get_name) == 0 or len(get_password) == 0:
        messagebox.showerror('Error', ' !!يجب ملئ كل الحقول')
        user_name_ver.set('')
        user_password_var.set('')

    else:

        my_cursor.execute(f"SELECT * FROM Users WHERE User_name = '{get_name}'")

        check_data = my_cursor.fetchone()

        if check_data is not None:

            if get_name == check_data[2] and get_password == check_data[3]:
                messagebox.showinfo(title='Done',
                                    message=f'Welcome {check_data[1]}')
                user_name_ver.set('')
                user_password_var.set('')
                root = Toplevel()
                Super(root, check_data[1])
                root.mainloop()

            else:
                messagebox.showerror(title='Sorry',
                                     message='User Name or Password is Not Correct!!')
                user_password_var.set('')
                user_name_ver.set('')

        else:
            messagebox.showerror("خطأ", "!!!هذا البيانات غير مسجلة أو غير صالحة")
            user_password_var.set('')
            user_name_ver.set('')


window = Tk()
window.geometry('800x450+250+50')
window.resizable(False, False)
window.title('Supermarket: 1.0.1')
window.config(bg='#7F8C8D')
window.iconbitmap('C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Supermarket_project_3\\icons\\icon_1.ico')
title_1 = Label(window, text='Supermarket System', fg='#FDFEFE', bg='black', font=('Tajawal-Medium', 16, 'bold'))
title_1.pack(fill=X)

# --------- Frame [ 1 ] Right
frame_1 = Frame(window, width=230, height=418, bg='#46839E')
frame_1.place(x=590, y=35)

# --------- Links
url_1 = 'https://twitter.com/explore'
url_2 = 'https://www.instagram.com/'
url_3 = 'https://youtube.com'


def link_one():
    webbrowser.open(url_1)


def link_tow():
    webbrowser.open(url_2)


def link_three():
    webbrowser.open(url_3)


def about():
    messagebox.showinfo('حول التطبيق', 'هذا التطبيق خاص بـ أسعار المنتجات في السوبر ماركت')


# --------- Frame [ 2 ] Bottom
frame_2 = Frame(window, width=586, height=141, bg='#46839E')
frame_2.place(x=0, y=310)

# -------- Images [ 1 | 2 | 3]
# ------- Start --------
image_1 = PhotoImage(
    file="C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Supermarket_project_3\\icons\\photo_1.png"
)

image_2 = PhotoImage(
    file="C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Supermarket_project_3\\icons\\photo_2.png"
)

image_3 = PhotoImage(
    file="C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Supermarket_project_3\\icons\\photo_4.png"
)

image_label_1 = Label(window, image=image_1, bg='#7F8C8D')
image_label_2 = Label(window, image=image_2, bg='#7F8C8D')
image_label_3 = Label(window, image=image_3, bg='#46839E')

image_label_1.place(x=290, y=50, width=257, height=257)
image_label_2.place(x=8, y=50, width=257, height=257)
image_label_3.place(x=485, y=320, width=95, height=95)
# ------- End --------

# ------- ( Buttons Area)
# ------- Start --------
button_1 = Button(frame_1, text='حسابنا على تويتر', width=22, fg='black', bg='#F7DC6F',
                  font=('Tajawal-Medium', 10, 'bold'), command=link_one)
button_2 = Button(frame_1, text='حسابنا على انستقرام', width=22, fg='black', bg='#F7DC6F',
                  font=('Tajawal-Medium', 10, 'bold'), command=link_tow)
button_3 = Button(frame_1, text='من نحن', width=22, fg='black', bg='#F7DC6F',
                  font=('Tajawal-Medium', 10, 'bold'), command=about)
button_4 = Button(frame_1, text='اغلاق البرنامج', width=22, fg='black', bg='#F7DC6F'
                  , font=('Tajawal-Medium', 10, 'bold'), command=window.quit)

button_1.place(x=15, y=90)
button_2.place(x=15, y=137)
button_3.place(x=15, y=185)
button_4.place(x=15, y=245)
# ------- End --------

# ----------  ( Login Area)
# ---------Start

# ------- variables
user_name_ver = StringVar()
user_password_var = StringVar()

label_user_name = Label(frame_2, text=':اسم المستخدم', font=('Tajawal-Medium', 10, 'bold'), fg='black', bg='#46839E')
label_user_password = Label(frame_2, text=':كلمة المرور', font=('Tajawal-Medium', 10, 'bold'), fg='black', bg='#46839E')

label_user_name.place(x=380, y=33)
label_user_password.place(x=398, y=75)

entry_user_name = Entry(frame_2, font=('Tajawal-Medium', 10),
                        bg='#7F8C8D', justify='center', textvariable=user_name_ver)

entry_user_password = Entry(frame_2, font=('Tajawal-Medium', 10),
                            bg='#7F8C8D', justify='center', textvariable=user_password_var)

entry_user_name.place(x=245, y=35, width=125, height=25)
entry_user_password.place(x=245, y=75, width=125, height=25)

buttons_login = Button(frame_2, text='دخول', width=16, height=1, fg='black', bg='#F7DC6F',
                       font=('Tajawal-Medium', 8, 'bold'), command=get_user_and_password)
buttons_create_user = Button(frame_2, text='انشاء مستخدم جديد', width=19, height=1, fg='black', bg='#F7DC6F',
                             font=('Tajawal-Medium', 8), command=Create_user)

buttons_login.place(x=90, y=41)
buttons_create_user.place(x=90, y=81)
# ---------End

# Data and Time
list_d = [date_now.day, "/", date_now.month, "/", date_now.year]

label_day_month_data = Label(frame_1, text=list_d[0:], bg='#46839E', font=('Tajawal-Medium', 12), fg='white')
label_data = Label(frame_1, text=':تاريخ اليوم', bg='#46839E', font=('Tajawal-Medium', 12), fg='white')
label_show_day = Label(frame_1, text=date_now.strftime("%A"), bg='#46839E', font=('Tajawal-Medium', 12), fg='white')
label_day = Label(frame_1, text=':اليوم', bg='#46839E', font=('Tajawal-Medium', 12), fg='white')

label_day_month_data.place(x=10, y=290)
label_data.place(x=120, y=290)
label_show_day.place(x=10, y=320)
label_day.place(x=157, y=320)

window.mainloop()
