import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from Supermarket_Dicit_3 import *
import random
import datetime

date_now_2 = datetime.datetime.now()


class Super:
    date_d = date_now_2.date()
    time_h = date_now_2.hour
    time_m = date_now_2.minute
    time_s = date_now_2.second

    def __init__(self, root, vendor_name):
        self.root = root
        self.vendor_name = vendor_name
        self.root.geometry('1366x768')
        self.root.title('Main Supermarket | version 1.0.1')
        self.root.iconbitmap("C:\\Users\\abdul\\Downloads\My-Github\\Python_project\\Supermarket_project_3\\icons\\food.ico")
        self.root.config(bg='black')
        print(self.vendor_name)
        self.numbers_0_to_10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        # |---------------------------------------------------------------------------------|
        # -------- Frame [ 1 ] This Place Right - Top
        frame_1 = Frame(self.root, width=315, height=190, bg='#117864')
        frame_1.place(x=1063, y=25)

        # -------- Frame [ 2 ] This Place Right - Bottom
        frame_2 = Frame(self.root, width=696, height=190, bg='#117864')
        frame_2.place(x=360, y=540)

        # -------- Frame [ 3 ] This Place Right
        frame_3 = Frame(self.root, width=335, height=508, bg='#117864')
        frame_3.place(x=720, y=25)

        # -------- Frame [ 4 ] This Place Center
        frame_4 = Frame(self.root, width=350, height=508, bg='#117864')
        frame_4.place(x=360, y=25)

        # -------- Frame [ 5 ] This Place Left
        frame_5 = Frame(self.root, width=351, height=508, bg='#117864')
        frame_5.place(x=0, y=25)

        # -------- Frame [ 6 ] This Place Bill Background
        frame_6 = Frame(self.root, width=353, height=495, bg='#46839E')
        frame_6.place(x=1063, y=225)

        # -------- Frame [ 7 ] This Place Search Area
        frame_7 = Frame(self.root, width=352, height=190, bg='#46839E')
        frame_7.place(x=0, y=540)

        # |---------------------------------------------------------------------------------|
        #       In Frame [ 1 ]
        # -------- Create variables ---------
        self.vendor_name_var = StringVar()
        self.bill_var = StringVar()
        random_bill = random.randint(100, 9999)
        self.bill_var.set(str(random_bill))

        label_vendor_name = Label(frame_1, text=':اسم البائع', font=('Tajawal-Medium', 11, 'bold'),
                                  bg='#117864', fg='white')
        label_vendor_name.place(x=202, y=20)

        label_bill = Label(frame_1, text=':رقم الفاتورة', font=('Tajawal-Medium', 11, 'bold'),
                                  bg='#117864', fg='white')
        label_bill.place(x=198, y=60)

        label_get_vendor_name = Label(frame_1, text=self.vendor_name, font=('Tajawal-Medium', 10, 'bold'),
                                  bg='#117864', fg='white')
        label_get_vendor_name.place(x=8, y=20)

        entry_get_and_search_bill = Entry(frame_1, font=('Tajawal-Medium', 10),
                            bg='white', justify='center', width=12, border='3', textvariable=self.bill_var)
        entry_get_and_search_bill.place(x=100, y=65)

        label_bill_set = Label(frame_1, text="[ الفاتورة ]", font=('Tajawal-Medium', 10, 'bold'),
                                  bg='#117864', fg='white')
        label_bill_set.place(x=130, y=160)

        button_create_bill = Button(frame_1, text='..فاتورة جديدة', fg='black', bg='#F9E79F',
                                    font=('Tajawal-Medium', 9), border='3', width=12,
                                    activebackground='orange', activeforeground='blue', command=self.new_bill_create)
        button_create_bill.place(x=206, y=100)

        button_search_number_bill = Button(frame_1, text='بحث', fg='black', bg='#F9E79F',
                                    font=('Tajawal-Medium', 9), border='3', width=12, activebackground='orange',
                                           activeforeground='blue', command=self.Search_for_bill)
        button_search_number_bill.place(x=10, y=63)
        # |---------------------------------------------------------------------------------|

        # |---------------------------------------------------------------------------------|
        #       In Frame [ 2 ]
        # -------- Create variables ---------
        self.fruits_vegetables_c = StringVar()
        self.pulses_c = StringVar()
        self.general_foodstuffs_c = StringVar()
        self.total_all_item_show = StringVar()

        self.total_all_item = DoubleVar()

        self.fruits_vegetables_c.set('0.0' + " ريال ")
        self.pulses_c.set('0.0' + " ريال ")
        self.general_foodstuffs_c.set('0.0' + " ريال ")
        self.total_all_item_show.set('0.0' + " ريال ")
        global button_2

        button_1 = Button(frame_2, text='الحساب',fg='black',bg='#F9E79F',font=('Tajawal-Medium', 11),
                          border='3', width=16, activebackground='orange',
                          activeforeground='blue', command=self.Total_all)
        button_2 = Button(frame_2, text='تصدير الفاتورة', fg='black', bg='#F9E79F', font=('Tajawal-Medium', 11),
                          border='3', width=16, activebackground='orange',
                          activeforeground='blue', command=self.Export_bill, state='disable')
        button_3 = Button(frame_2, text='افراغ الحقول', fg='black', bg='#F9E79F', font=('Tajawal-Medium', 11), border='3'
                          , width=16, activebackground='orange', activeforeground='blue', command=self.clear_all_entry)
        button_4 = Button(frame_2, text='خروج', fg='black', bg='#F9E79F', font=('Tajawal-Medium', 11),
                          border='3', width=16, activebackground='orange', activeforeground='blue', command=self.out)

        button_1.place(x=540, y=17)
        button_2.place(x=540, y=72)
        button_3.place(x=393, y=17)
        button_4.place(x=393, y=72)

        label_fruits_vegetables_caluclat = Label(frame_2, text='حساب الفواكه و الخضروات',font=('Tajawal-Medium', 12),
                                                 bg='#117864', fg='white')
        label_pulses_caluclat = Label(frame_2, text='حساب البقوليات', font=('Tajawal-Medium', 12),
                                                 bg='#117864', fg='white')
        label_general_foodstuffs = Label(frame_2, text='حساب المواد الغذائية الاخرى', font=('Tajawal-Medium', 12),
                                                 bg='#117864', fg='white')

        label_fruits_vegetables_caluclat.place(x=186, y=19)
        label_pulses_caluclat.place(x=253, y=58)
        label_general_foodstuffs.place(x=186, y=98)

        entry_fruits_vegetables_caluclat = Entry(frame_2, textvariable=self.fruits_vegetables_c, font=('Tajawal-Medium', 12),
                                                 bg='white', justify='center', width=10, border='3', state='readonly')

        entry_pulses_caluclat = Entry(frame_2, textvariable=self.pulses_c, font=('Tajawal-Medium', 12),
                                                 bg='white', justify='center', width=10, border='3', state='readonly')

        entry_general_foodstuffs_caluclat = Entry(frame_2, textvariable=self.general_foodstuffs_c, font=('Tajawal-Medium', 12),
                                                 bg='white', justify='center', width=10, border='3', state='readonly')

        entry_fruits_vegetables_caluclat.place(x=50, y=21)
        entry_pulses_caluclat.place(x=50, y=63)
        entry_general_foodstuffs_caluclat.place(x=50, y=104)
        # |---------------------------------------------------------------------------------|

        # |---------------------------------------------------------------------------------|
        #       In Frame [ 7 ]
        # ----------------- Create variables
        self.search_var_one = StringVar()
        self.search_var_tow = StringVar()

        label_total_all_items = Label(frame_7, text='الحساب الاجمالي', font=('Tajawal-Medium', 12),
                                                 bg='#46839E', fg='white')

        label_search_for_item = Label(frame_7, text='بحث عن سعر منتج', font=('Tajawal-Medium', 12),
                                      bg='#46839E', fg='white')

        label_search_for_item_result = Label(frame_7, text='السعر', font=('Tajawal-Medium', 12),
                                      bg='#46839E', fg='white')

        label_total_all_items.place(x=223, y=10)
        label_search_for_item.place(x=210, y=57)
        label_search_for_item_result.place(x=215, y=115)

        entry_total_all_items = Entry(frame_7, font=('Tajawal-Medium', 13),bg='white', justify='center', width=15,
                                      border='7', textvariable=self.total_all_item_show, state='readonly')

        entry_search_for_item = Entry(frame_7, font=('Tajawal-Medium', 11),bg='white', justify='center', width=13,
                                      border='3', textvariable=self.search_var_one)

        entry_search_for_item_result = Entry(frame_7, font=('Tajawal-Medium', 13), bg='white', justify='center',
                                             width=10, border='3', state='readonly', textvariable=self.search_var_tow)

        entry_total_all_items.place(x=10, y=11)
        entry_search_for_item.place(x=99, y=57)
        entry_search_for_item_result.place(x=99, y=115)

        button_search_for_item = Button(frame_7, text='بحث', fg='black', bg='#F9E79F', font=('Tajawal-Medium', 9),
                                        border='3', width=12, command=self.Search_for_price_item)
        button_search_for_item.place(x=5, y=57)
        # |---------------------------------------------------------------------------------|

        # |---------------------------------------------------------------------------------|
        #       In Frame [ 3 ]
        s1 = """
        شيبس صغير
        
        شيبس كبير
        
        بيبسي صغير
        
        بيبسي كبير
        
        لبن صغير
        
        لبن كبير
        
        حليب صغير
        
        حليب كبير
        
        زبادي
        
        جبن
        
        لبنة
        
        """

        s2 = """
        عصير صغير
        
        عصير كبير
        
        ماء كرتون 24 حبة
        
        """

        # -------- Create variables ---------
        self.general_foodstuffs_var_1 = DoubleVar()
        self.general_foodstuffs_var_2 = DoubleVar()
        self.general_foodstuffs_var_3 = DoubleVar()
        self.general_foodstuffs_var_4 = DoubleVar()
        self.general_foodstuffs_var_5 = DoubleVar()
        self.general_foodstuffs_var_6 = DoubleVar()
        self.general_foodstuffs_var_7 = DoubleVar()
        self.general_foodstuffs_var_8 = DoubleVar()
        self.general_foodstuffs_var_9 = DoubleVar()
        self.general_foodstuffs_var_10 = DoubleVar()
        self.general_foodstuffs_var_11 = DoubleVar()
        self.general_foodstuffs_var_12 = DoubleVar()
        self.general_foodstuffs_var_13 = DoubleVar()
        self.general_foodstuffs_var_14 = DoubleVar()

        label_line_in_frame_3 = Frame(frame_3, bg='black', width=3, height=455)
        label_line_in_frame_3.place(x=178, y=48)
        label_general_foodstuffs_title = Label(frame_3, text="المواد الغذائية", font=('Tajawal-Medium', 13, 'bold', 'italic'),
                                           bg='#117864', justify='right', fg='white')
        label_general_foodstuffs_title.place(x=137, y=1)

        label_general_foodstuffs_1 = Label(frame_3, text=s1, font=('Tajawal-Medium', 11),
                                           bg='#117864', justify='right', fg='white')
        label_general_foodstuffs_1.place(x=217, y=25)

        label_general_foodstuffs_2 = Label(frame_3, text=s2, font=('Tajawal-Medium', 11),
                                           bg='#117864', justify='right', fg='white')
        label_general_foodstuffs_2.place(x=42, y=25)

        spin_box_1 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_1, justify='center', width=6, wrap=False)
        spin_box_2 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_2, justify='center', width=6, wrap=False)
        spin_box_3 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_3, justify='center', width=6, wrap=False)
        spin_box_4 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_4, justify='center', width=6, wrap=False)
        spin_box_5 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_5, justify='center', width=6, wrap=False)
        spin_box_6 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_6, justify='center', width=6, wrap=False)
        spin_box_7 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_7, justify='center', width=6, wrap=False)
        spin_box_8 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_8, justify='center', width=6, wrap=False)
        spin_box_9 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_9, justify='center', width=6, wrap=False)
        spin_box_10 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_10, justify='center', width=6, wrap=False)
        spin_box_11 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_11, justify='center', width=6, wrap=False)
        spin_box_12 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_12, justify='center', width=6, wrap=False)
        spin_box_13 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_13, justify='center', width=6, wrap=False)
        spin_box_14 = ttk.Spinbox(frame_3, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.general_foodstuffs_var_14, justify='center', width=6, wrap=False)

        spin_box_1.place(x=185, y=51)
        spin_box_2.place(x=185, y=91)
        spin_box_3.place(x=185, y=131)
        spin_box_4.place(x=185, y=175)
        spin_box_5.place(x=185, y=215)
        spin_box_6.place(x=185, y=259)
        spin_box_7.place(x=185, y=301)
        spin_box_8.place(x=185, y=340)
        spin_box_9.place(x=185, y=380)
        spin_box_10.place(x=185, y=420)
        spin_box_11.place(x=185, y=470)
        spin_box_12.place(x=8, y=51)
        spin_box_13.place(x=8, y=91)
        spin_box_14.place(x=8, y=131)
        # |---------------------------------------------------------------------------------|

        # |---------------------------------------------------------------------------------|
        #       In Frame [ 4 ]

        s3 = """
        قمح
        
        شعير
        
        رز
        
        طحين
        
        بر
        
        سكر
        
        ملح
        
        ذرة
        
        فول
        
        عدس
        
        دقيق
        """

        s4 = """
        قهوة
        
        هيل
        
        
        """

        # -------- Create variables ---------

        self.pulses_1 = DoubleVar()
        self.pulses_2 = DoubleVar()
        self.pulses_3 = DoubleVar()
        self.pulses_4 = DoubleVar()
        self.pulses_5 = DoubleVar()
        self.pulses_6 = DoubleVar()
        self.pulses_7 = DoubleVar()
        self.pulses_8 = DoubleVar()
        self.pulses_9 = DoubleVar()
        self.pulses_10 = DoubleVar()
        self.pulses_11 = DoubleVar()
        self.pulses_12 = DoubleVar()
        self.pulses_13 = DoubleVar()

        label_line_in_frame_4 = Frame(frame_4, bg='black', width=3, height=455)
        label_line_in_frame_4.place(x=225, y=48)

        label_pulses_title = Label(frame_4, text="البقوليات",
                                               font=('Tajawal-Medium', 13, 'bold', 'italic'),
                                               bg='#117864', justify='right', fg='white')
        label_pulses_title.place(x=137, y=1)

        label_pulses_1 = Label(frame_4, text=s3, font=('Tajawal-Medium', 11),
                                           bg='#117864', justify='right', fg='white')
        label_pulses_1.place(x=275, y=25)

        label_pulses_2 = Label(frame_4, text=s4, font=('Tajawal-Medium', 11),
                                           bg='#117864', justify='right', fg='white')
        label_pulses_2.place(x=122, y=25)

        spin_box_15 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.pulses_1, justify='center', width=6, wrap=False)
        spin_box_16 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.pulses_2, justify='center', width=6, wrap=False)
        spin_box_17 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.pulses_3, justify='center', width=6, wrap=False)
        spin_box_18 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.pulses_4, justify='center', width=6, wrap=False)
        spin_box_19 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.pulses_5, justify='center', width=6, wrap=False)
        spin_box_20 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.pulses_6, justify='center', width=6, wrap=False)
        spin_box_21 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.pulses_7, justify='center', width=6, wrap=False)
        spin_box_22 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.pulses_8, justify='center', width=6, wrap=False)
        spin_box_23 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                 textvariable=self.pulses_9, justify='center', width=6, wrap=False)
        spin_box_24 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.pulses_10, justify='center', width=6, wrap=False)
        spin_box_25 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.pulses_11, justify='center', width=6, wrap=False)
        spin_box_26 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.pulses_12, justify='center', width=6, wrap=False)
        spin_box_27 = ttk.Spinbox(frame_4, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.pulses_13, justify='center', width=6, wrap=False)

        spin_box_15.place(x=240, y=51)
        spin_box_16.place(x=240, y=91)
        spin_box_17.place(x=240, y=131)
        spin_box_18.place(x=240, y=175)
        spin_box_19.place(x=240, y=215)
        spin_box_20.place(x=240, y=259)
        spin_box_21.place(x=240, y=301)
        spin_box_22.place(x=240, y=340)
        spin_box_23.place(x=240, y=380)
        spin_box_24.place(x=240, y=426)
        spin_box_25.place(x=240, y=470)
        spin_box_26.place(x=80, y=51)
        spin_box_27.place(x=80, y=91)
        # |---------------------------------------------------------------------------------|

        # |---------------------------------------------------------------------------------|
        #       In Frame [ 5 ]
        s5 = """
        برتقال
        
        تفاح
        
        عنب
        
        موز
        
        خوخ
        
        مشمش
        
        فراولة
        
        كمثرى
        
        أناناس
        
        توت
        
        تين
        
        رمان
        """

        s6 = """
        خيار
        
        جزر
        
        خس
        
        ملفوف
        
        نعناع
        
        حبق
        
        طماطم
        
        بصل
        """
        # -------- Create variables ---------
        self.F_V_var_1 = DoubleVar()
        self.F_V_var_2 = DoubleVar()
        self.F_V_var_3 = DoubleVar()
        self.F_V_var_4 = DoubleVar()
        self.F_V_var_5 = DoubleVar()
        self.F_V_var_6 = DoubleVar()
        self.F_V_var_7 = DoubleVar()
        self.F_V_var_8 = DoubleVar()
        self.F_V_var_9 = DoubleVar()
        self.F_V_var_10 = DoubleVar()
        self.F_V_var_11 = DoubleVar()
        self.F_V_var_12 = DoubleVar()
        self.F_V_var_13 = DoubleVar()
        self.F_V_var_14 = DoubleVar()
        self.F_V_var_15 = DoubleVar()
        self.F_V_var_16 = DoubleVar()
        self.F_V_var_17 = DoubleVar()
        self.F_V_var_18 = DoubleVar()
        self.F_V_var_19 = DoubleVar()
        self.F_V_var_20 = DoubleVar()

        label_line_in_frame_4 = Frame(frame_5, bg='black', width=3, height=455)
        label_line_in_frame_4.place(x=225, y=48)

        label_F_V_title = Label(frame_5, text="فواكه و خضروات",
                                   font=('Tajawal-Medium', 13, 'bold', 'italic'),
                                   bg='#117864', justify='right', fg='white')
        label_F_V_title.place(x=137, y=1)

        label_F_V_1 = Label(frame_5, text=s5, font=('Tajawal-Medium', 10),
                               bg='#117864', justify='right', fg='white')
        label_F_V_1.place(x=265, y=25)

        label_F_V_2 = Label(frame_5, text=s6, font=('Tajawal-Medium', 10),
                               bg='#117864', justify='right', fg='white')
        label_F_V_2.place(x=122, y=25)

        spin_box_28 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_1, justify='center', width=6, wrap=False)
        spin_box_29 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_2, justify='center', width=6, wrap=False)
        spin_box_30 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_3, justify='center', width=6, wrap=False)
        spin_box_31 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_4, justify='center', width=6, wrap=False)
        spin_box_32 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_5, justify='center', width=6, wrap=False)
        spin_box_33 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_6, justify='center', width=6, wrap=False)
        spin_box_34 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_7, justify='center', width=6, wrap=False)
        spin_box_35 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_8, justify='center', width=6, wrap=False)
        spin_box_36 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_9, justify='center', width=6, wrap=False)
        spin_box_37 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_10, justify='center', width=6, wrap=False)
        spin_box_38 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_11, justify='center', width=6, wrap=False)
        spin_box_39 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_12, justify='center', width=6, wrap=False)
        spin_box_40 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_13, justify='center', width=6, wrap=False)
        spin_box_41 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_14, justify='center', width=6, wrap=False)
        spin_box_42 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_15, justify='center', width=6, wrap=False)
        spin_box_43 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_16, justify='center', width=6, wrap=False)
        spin_box_44 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_17, justify='center', width=6, wrap=False)
        spin_box_45 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_18, justify='center', width=6, wrap=False)
        spin_box_46 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_19, justify='center', width=6, wrap=False)
        spin_box_47 = ttk.Spinbox(frame_5, from_=0, to=10, values=self.numbers_0_to_10,
                                  textvariable=self.F_V_var_20, justify='center', width=6, wrap=False)

        spin_box_28.place(x=234, y=49) # 1
        spin_box_29.place(x=234, y=86) # 2
        spin_box_30.place(x=234, y=120)# 3
        spin_box_31.place(x=234, y=155)# 4
        spin_box_32.place(x=234, y=193)# 5
        spin_box_33.place(x=234, y=227) # 6
        spin_box_34.place(x=234, y=261)# 7
        spin_box_35.place(x=234, y=296) # 8
        spin_box_36.place(x=234, y=330) # 9
        spin_box_37.place(x=234, y=366) # 10
        spin_box_38.place(x=234, y=404) # 11
        spin_box_39.place(x=234, y=439)# 12
        spin_box_40.place(x=90, y=49)
        spin_box_41.place(x=90, y=86)
        spin_box_42.place(x=90, y=120)
        spin_box_43.place(x=90, y=155)
        spin_box_44.place(x=90, y=193)
        spin_box_45.place(x=90, y=227)
        spin_box_46.place(x=90, y=261)
        spin_box_47.place(x=90, y=296)

    # -----------------  The Bill -----------
    # Start
        scroll_one = Scrollbar(frame_6, orient=VERTICAL)
        self.text_area = Text(frame_6, yscrollcommand=scroll_one.set, width=34, height=29, state='normal')
        scroll_one.pack(side=LEFT, fill=Y)
        scroll_one.config(command=self.text_area.yview)
        self.text_area.pack(fill=BOTH, expand=1)
        self.print_bill(Super.date_d, Super.time_h, Super.time_m, Super.time_s)
    # End

    def Total_all(self):


        # general_foodstuffs
        self.general_foodstuffs_var_total_1 = self.general_foodstuffs_var_1.get() * 1
        self.general_foodstuffs_var_total_2 = self.general_foodstuffs_var_2.get() * 7
        self.general_foodstuffs_var_total_3 = self.general_foodstuffs_var_3.get() * 2.5
        self.general_foodstuffs_var_total_4 = self.general_foodstuffs_var_4.get() * 9
        self.general_foodstuffs_var_total_5 = self.general_foodstuffs_var_5.get() * 1.5
        self.general_foodstuffs_var_total_6 = self.general_foodstuffs_var_6.get() * 8
        self.general_foodstuffs_var_total_7 = self.general_foodstuffs_var_7.get() * 1.5
        self.general_foodstuffs_var_total_8 = self.general_foodstuffs_var_8.get() * 8
        self.general_foodstuffs_var_total_9 = self.general_foodstuffs_var_9.get() * 1
        self.general_foodstuffs_var_total_10 = self.general_foodstuffs_var_10.get() * 7
        self.general_foodstuffs_var_total_11 = self.general_foodstuffs_var_11.get() * 5.5
        self.general_foodstuffs_var_total_12 = self.general_foodstuffs_var_12.get() * 1.5
        self.general_foodstuffs_var_total_13 = self.general_foodstuffs_var_13.get() * 4
        self.general_foodstuffs_var_total_14 = self.general_foodstuffs_var_14.get() * 11
        self.total_one = float(
            self.general_foodstuffs_var_total_1 +
            self.general_foodstuffs_var_total_2 +
            self.general_foodstuffs_var_total_3 +
            self.general_foodstuffs_var_total_4 +
            self.general_foodstuffs_var_total_5 +
            self.general_foodstuffs_var_total_6 +
            self.general_foodstuffs_var_total_7 +
            self.general_foodstuffs_var_total_8 +
            self.general_foodstuffs_var_total_9 +
            self.general_foodstuffs_var_total_10 +
            self.general_foodstuffs_var_total_11 +
            self.general_foodstuffs_var_total_12 +
            self.general_foodstuffs_var_total_13 +
            self.general_foodstuffs_var_total_14
        )
        self.general_foodstuffs_c.set(str(self.total_one) + " ريال ")
        # __________________________________________________________

        #  Pulses
        self.pulses_var_total_1 = self.pulses_1.get() * 20
        self.pulses_var_total_2 = self.pulses_2.get() * 25
        self.pulses_var_total_3 = self.pulses_3.get() * 45
        self.pulses_var_total_4 = self.pulses_4.get() * 30
        self.pulses_var_total_5 = self.pulses_5.get() * 20
        self.pulses_var_total_6 = self.pulses_6.get() * 25
        self.pulses_var_total_7 = self.pulses_7.get() * 15
        self.pulses_var_total_8 = self.pulses_8.get() * 15
        self.pulses_var_total_9 = self.pulses_9.get() * 12
        self.pulses_var_total_10 = self.pulses_10.get() * 12
        self.pulses_var_total_11 = self.pulses_11.get() * 25
        self.pulses_var_total_12 = self.pulses_12.get() * 25
        self.pulses_var_total_13 = self.pulses_13.get() * 20
        self.total_tow = float(
            self.pulses_var_total_1 +
            self.pulses_var_total_2 +
            self.pulses_var_total_3 +
            self.pulses_var_total_4 +
            self.pulses_var_total_5 +
            self.pulses_var_total_6 +
            self.pulses_var_total_7 +
            self.pulses_var_total_8 +
            self.pulses_var_total_9 +
            self.pulses_var_total_10 +
            self.pulses_var_total_11 +
            self.pulses_var_total_12 +
            self.pulses_var_total_13
        )
        self.pulses_c.set(str(self.total_tow) + " ريال ")

        # __________________________________________________________

        #
        self.F_V_var_total_1 = self.F_V_var_1.get() * 15
        self.F_V_var_total_2 = self.F_V_var_2.get() * 15
        self.F_V_var_total_3 = self.F_V_var_3.get() * 10
        self.F_V_var_total_4 = self.F_V_var_4.get() * 18
        self.F_V_var_total_5 = self.F_V_var_5.get() * 18
        self.F_V_var_total_6 = self.F_V_var_6.get() * 18
        self.F_V_var_total_7 = self.F_V_var_7.get() * 10
        self.F_V_var_total_8 = self.F_V_var_8.get() * 15
        self.F_V_var_total_9 = self.F_V_var_9.get() * 15
        self.F_V_var_total_10 = self.F_V_var_10.get() * 12
        self.F_V_var_total_11 = self.F_V_var_11.get() * 20
        self.F_V_var_total_12 = self.F_V_var_12.get() * 20
        self.F_V_var_total_13 = self.F_V_var_13.get() * 10
        self.F_V_var_total_14 = self.F_V_var_14.get() * 10
        self.F_V_var_total_15 = self.F_V_var_15.get() * 5
        self.F_V_var_total_16 = self.F_V_var_16.get() * 5
        self.F_V_var_total_17 = self.F_V_var_17.get() * 1
        self.F_V_var_total_18 = self.F_V_var_18.get() * 1
        self.F_V_var_total_19 = self.F_V_var_19.get() * 20
        self.F_V_var_total_20 = self.F_V_var_20.get() * 12
        self.total_three = float(
            self.F_V_var_total_1 +
            self.F_V_var_total_2 +
            self.F_V_var_total_3 +
            self.F_V_var_total_4 +
            self.F_V_var_total_5 +
            self.F_V_var_total_6 +
            self.F_V_var_total_7 +
            self.F_V_var_total_8 +
            self.F_V_var_total_9 +
            self.F_V_var_total_10 +
            self.F_V_var_total_11 +
            self.F_V_var_total_12 +
            self.F_V_var_total_13 +
            self.F_V_var_total_14 +
            self.F_V_var_total_15 +
            self.F_V_var_total_16 +
            self.F_V_var_total_17 +
            self.F_V_var_total_18 +
            self.F_V_var_total_19 +
            self.F_V_var_total_20
        )
        self.fruits_vegetables_c.set(str(self.total_three) + " ريال ")
        self.total_all_item.set(self.total_one + self.total_tow + self.total_three)
        self.total_all_item_show.set(str(self.total_one + self.total_tow + self.total_three) + "ريـال ")
        if self.total_all_item.get() > 0:
            button_2.config(state='normal')
        elif self.total_all_item.get() == 0:
            tkinter.messagebox.showerror('Error', ' !!لا توجد مشتريات')
        else:
            pass

    def clear_all_entry(self):
        self.fruits_vegetables_c.set('0.0' + " ريال ")
        self.pulses_c.set('0.0' + " ريال ")
        self.general_foodstuffs_c.set('0.0' + " ريال ")
        self.total_all_item.set(0.0)
        self.total_all_item_show.set('0.0' + " ريال ")

        button_2.config(state='disable')

        self.general_foodstuffs_var_1.set(0.0)
        self.general_foodstuffs_var_2.set(0.0)
        self.general_foodstuffs_var_3.set(0.0)
        self.general_foodstuffs_var_4.set(0.0)
        self.general_foodstuffs_var_5.set(0.0)
        self.general_foodstuffs_var_6.set(0.0)
        self.general_foodstuffs_var_7.set(0.0)
        self.general_foodstuffs_var_8.set(0.0)
        self.general_foodstuffs_var_9.set(0.0)
        self.general_foodstuffs_var_10.set(0.0)
        self.general_foodstuffs_var_11.set(0.0)
        self.general_foodstuffs_var_12.set(0.0)
        self.general_foodstuffs_var_13.set(0.0)
        self.general_foodstuffs_var_14.set(0.0)

        self.pulses_1.set(0.0)
        self.pulses_2.set(0.0)
        self.pulses_3.set(0.0)
        self.pulses_4.set(0.0)
        self.pulses_5.set(0.0)
        self.pulses_6.set(0.0)
        self.pulses_7.set(0.0)
        self.pulses_8.set(0.0)
        self.pulses_9.set(0.0)
        self.pulses_10.set(0.0)
        self.pulses_11.set(0.0)
        self.pulses_12.set(0.0)
        self.pulses_13.set(0.0)

        self.F_V_var_1.set(0.0)
        self.F_V_var_2.set(0.0)
        self.F_V_var_3.set(0.0)
        self.F_V_var_4.set(0.0)
        self.F_V_var_5.set(0.0)
        self.F_V_var_6.set(0.0)
        self.F_V_var_7.set(0.0)
        self.F_V_var_8.set(0.0)
        self.F_V_var_9.set(0.0)
        self.F_V_var_10.set(0.0)
        self.F_V_var_11.set(0.0)
        self.F_V_var_12.set(0.0)
        self.F_V_var_13.set(0.0)
        self.F_V_var_14.set(0.0)
        self.F_V_var_15.set(0.0)
        self.F_V_var_16.set(0.0)
        self.F_V_var_17.set(0.0)
        self.F_V_var_18.set(0.0)
        self.F_V_var_19.set(0.0)
        self.F_V_var_20.set(0.0)
        # self.new_bill_create()

        self.search_var_one.set('')
        self.search_var_tow.set('')

    def out(self):
        ask1 = tkinter.messagebox.askquestion(title='خروج', message='هل تريد الخروج؟')
        if ask1 == 'yes':
            self.root.destroy()
        else:
            pass

    def print_bill(self, date, hour, minute, second):

        date_now_3 = datetime.datetime.now()
        # date_date_3 = date_now_3.date()
        # time_h = date_now_3.hour
        # time_m = date_now_3.minute
        # time_s = date_now_3.second

        self.text_area.config(state='normal')
        self.text_area.delete('1.0', END)
        self.text_area.insert(END, "\t Weclome  ")
        self.text_area.insert(END, "\n==================================")
        self.text_area.insert(END, f"\n \tName: {self.vendor_name}   ")
        self.text_area.insert(END, f"\n \tNumber Bill: {self.bill_var.get()}   ")
        self.text_area.insert(END, f"\n    Date: {date} | {hour}:{minute}:{second}")
        self.text_area.insert(END, "\n==================================")
        self.text_area.insert(END, "\nالسعر\t    العدد\t       المشتريات")
        self.text_area.insert(END, "\n==================================\n")

    def Export_bill(self):
        date_now_3 = datetime.datetime.now()
        date_date_3 = date_now_3.date()
        time_h = date_now_3.hour
        time_m = date_now_3.minute
        time_s = date_now_3.second

        if self.total_all_item.get() == 0.0:
            tkinter.messagebox.showerror('Error', 'لا توجد مشتريات لكي يتم الحفظ')
        else:
            self.print_bill(date_date_3, time_h, time_m, time_s)

            # ------------- [ 1 ]
            if self.general_foodstuffs_var_1.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_1}\t\t{self.general_foodstuffs_var_1.get()}\tشيبس صغير ")
            if self.general_foodstuffs_var_2.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_2}\t\t{self.general_foodstuffs_var_2.get()}\tشيبس كبير ")
            if self.general_foodstuffs_var_3.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_3}\t\t{self.general_foodstuffs_var_3.get()}\tبيبسي صغير ")
            if self.general_foodstuffs_var_4.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_4}\t\t{self.general_foodstuffs_var_4.get()}\tبيبسي كبير ")
            if self.general_foodstuffs_var_5.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_5}\t\t{self.general_foodstuffs_var_5.get()}\tلبن صغير ")
            if self.general_foodstuffs_var_6.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_6}\t\t{self.general_foodstuffs_var_6.get()}\tلبن كبير ")
            if self.general_foodstuffs_var_7.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_7}\t\t{self.general_foodstuffs_var_7.get()}\tحليب صغير ")
            if self.general_foodstuffs_var_8.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_8}\t\t{self.general_foodstuffs_var_8.get()}\tحليب كبير ")
            if self.general_foodstuffs_var_9.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_9}\t\t{self.general_foodstuffs_var_9.get()}\tزبادي ")
            if self.general_foodstuffs_var_10.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_10}\t\t{self.general_foodstuffs_var_10.get()}\tجبن ")
            if self.general_foodstuffs_var_11.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_11}\t\t{self.general_foodstuffs_var_11.get()}\tلبنة ")
            if self.general_foodstuffs_var_12.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_12}\t\t{self.general_foodstuffs_var_12.get()}\tعصير صغير ")
            if self.general_foodstuffs_var_13.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_13}\t\t{self.general_foodstuffs_var_13.get()}\tعصير كبير ")
            if self.general_foodstuffs_var_14.get() != 0:
                self.text_area.insert(END, f"\n{self.general_foodstuffs_var_total_14}\t\t{self.general_foodstuffs_var_14.get()}\tماء كرتون ")
            # ------------- [ 2 ]
            if self.pulses_1.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_1}\t\t{self.pulses_1.get()}\tقمح  ")
            if self.pulses_2.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_2}\t\t{self.pulses_2.get()}\tشعير ")
            if self.pulses_3.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_3}\t\t{self.pulses_3.get()}\tرز ")
            if self.pulses_4.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_4}\t\t{self.pulses_4.get()}\tطحين ")
            if self.pulses_5.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_5}\t\t{self.pulses_5.get()}\tبر ")
            if self.pulses_6.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_6}\t\t{self.pulses_6.get()}\tسكر ")
            if self.pulses_7.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_7}\t\t{self.pulses_7.get()}\tملح ")
            if self.pulses_8.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_8}\t\t{self.pulses_8.get()}\tذرة ")
            if self.pulses_9.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_9}\t\t{self.pulses_9.get()}\tفول ")
            if self.pulses_10.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_10}\t\t{self.pulses_10.get()}\tعدس ")
            if self.pulses_11.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_11}\t\t{self.pulses_11.get()}\tدقيق ")
            if self.pulses_12.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_12}\t\t{self.pulses_12.get()}\tقهوة ")
            if self.pulses_13.get() != 0:
                self.text_area.insert(END,f"\n{self.pulses_var_total_13}\t\t{self.pulses_13.get()}\tهيل ")

            # ------------- [ 3 ]
            if self.F_V_var_1.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_1}\t\t{self.F_V_var_1.get()}\tبرتقال ")
            if self.F_V_var_2.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_2}\t\t{self.F_V_var_2.get()}\tتفاح ")
            if self.F_V_var_3.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_3}\t\t{self.F_V_var_3.get()}\tعنب ")
            if self.F_V_var_4.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_4}\t\t{self.F_V_var_4.get()}\tموز ")
            if self.F_V_var_5.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_5}\t\t{self.F_V_var_5.get()}\tخوخ ")
            if self.F_V_var_6.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_6}\t\t{self.F_V_var_6.get()}\tمشمش ")
            if self.F_V_var_7.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_7}\t\t{self.F_V_var_7.get()}\tفراولة ")
            if self.F_V_var_8.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_8}\t\t{self.F_V_var_8.get()}\tكمثرى ")
            if self.F_V_var_9.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_9}\t\t{self.F_V_var_9.get()}\tأناناس ")
            if self.F_V_var_10.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_10}\t\t{self.F_V_var_10.get()}\tتوت ")
            if self.F_V_var_11.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_11}\t\t{self.F_V_var_11.get()}\tتين ")
            if self.F_V_var_12.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_12}\t\t{self.F_V_var_12.get()}\tرمان ")
            if self.F_V_var_13.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_13}\t\t{self.F_V_var_13.get()}\tخيار ")
            if self.F_V_var_14.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_13}\t\t{self.F_V_var_13.get()}\tجزر ")
            if self.F_V_var_15.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_15}\t\t{self.F_V_var_15.get()}\tخس ")
            if self.F_V_var_16.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_16}\t\t{self.F_V_var_16.get()}\tملقوف ")
            if self.F_V_var_17.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_17}\t\t{self.F_V_var_17.get()}\tنعناع ")
            if self.F_V_var_18.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_18}\t\t{self.F_V_var_18.get()}\tحبق ")
            if self.F_V_var_19.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_19}\t\t{self.F_V_var_19.get()}\tطماطم ")
            if self.F_V_var_20.get() != 0:
                self.text_area.insert(END, f"\n{self.F_V_var_total_20}\t\t{self.F_V_var_20.get()}\tبصل ")

            self.text_area.insert(END, "\n==================================\n")
            self.text_area.insert(END, f'\t{self.total_all_item_show.get()} المجموع الكلي')
            self.Save()
            self.clear_all_entry()

    def Search_for_bill(self):
        bill = self.bill_var.get()

        try:
            self.text_area.delete('1.0', END)
            search_file = open( f"C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Supermarket_project_3\\Bill_saved\\{str(bill)}.text",
                "r", encoding='utf-8')
            self.text_area.config(state='normal')
            self.text_area.insert('1.0', END)
            self.text_area.insert(END, search_file.read())
            search_file.close()
            self.text_area.config(state='disable')

        except FileNotFoundError:
            tkinter.messagebox.showerror(
                title='عذرا',
                message='هذا الفاتورة غير متوفرة'
            )

    def Search_for_price_item(self):
        name_item = self.search_var_one.get()

        if name_item in Dici_general_foodstuffs or name_item in Dici_pluses or name_item in Dici_fruits_vegetables:
            if name_item in Dici_general_foodstuffs:
                self.search_var_tow.set(Dici_general_foodstuffs[name_item] + 'ريـال')

            elif name_item in Dici_pluses:
                self.search_var_tow.set(Dici_pluses[name_item] + 'ريـال')

            elif name_item in Dici_fruits_vegetables:
                self.search_var_tow.set(Dici_fruits_vegetables[name_item] + 'ريـال')

        else:
            tkinter.messagebox.showerror('عفوا', '!! لا يتوفر هذا المنتج بهذا الاسم')
            self.search_var_one.set('')

    def new_bill_create(self):

        date_now_3 = datetime.datetime.now()
        date_date_3 = date_now_3.date()
        time_h = date_now_3.hour
        time_m = date_now_3.minute
        time_s = date_now_3.second

        if self.total_all_item.get() > 0:
            ask_3 = tkinter.messagebox.askquestion('', 'توجد عملية شراء لم يتم حفظ فاتورة لها, هل تريد حفظ الفاتورة؟')
            self.Export_bill()

        else:
            random_bill = random.randint(100, 9999)
            self.bill_var.set(str(random_bill))
            self.print_bill(date_date_3, time_h, time_m, time_s)
            tkinter.messagebox.showinfo(title=':فاتورة', message='..تم إنشاء فاتورة جديدة')

    def Save(self):
        self.bill_date = self.text_area.get('1.0', END)
        file_1 = open(
            f"C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\Supermarket_project_3\\Bill_saved\\" + str(
                self.bill_var.get()) + ".text", "w", encoding='utf-8')
        file_1.write(self.bill_date)
        tkinter.messagebox.showinfo(title='Done', message='..تم حفظ الفاتورة')



# if __name__ == '__main__':
#     run = Tk()
#     Super(run, 'Ahmed')
#     run.mainloop()