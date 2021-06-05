from tkinter import *
from tkinter import ttk,messagebox
import csv
from datetime import datetime


GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย By NKD')
GUI.geometry('700x700+500+300')



#------------img-----------------------------------------------
img1 = PhotoImage(file='C:/Users/nkd/Desktop/python/diskette.png')
img2 = PhotoImage(file='C:/Users/nkd/Desktop/python/expenses.png')
img3 = PhotoImage(file='C:/Users/nkd/Desktop/python/add.png')
img4 = PhotoImage(file='C:/Users/nkd/Desktop/python/wallet.png')
img5 = PhotoImage(file='C:/Users/nkd/Desktop/python/to-do-list.png')
#--------------------------------------------------------------

#--------------------สร้าง TAB------------------------------------
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill='both',expand =True) #
Tab.add(T1,text=f'{"Add Expense" : ^{20}}',image=img3,compound='top')
Tab.add(T2,text=f'{"Expense List" : ^{20}}',image=img4,compound='top')
#text=f'{"Add Expense" : ^{20}}' ทำให้ช่องแท้บมีขนาดเท่ากัน
#.subsample(2) = ย่อรูป(วงเล็บ2คือ2เท่า)
#-----------------------------------------------------------------
###############MENU#########################################

menubar = Menu(GUI)
GUI.config(menu=menubar)

# # file menu

filemenu = Menu(menubar)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export file')
# # help menu

def About():
    messagebox.showinfo('About','สวัสดีฮะ บริจาคเราเป่า')
helpmenu = Menu(menubar)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)
# # donate menu

donatemenu = Menu(menubar)
menubar.add_cascade(label='Donate',menu=donatemenu)
##############################################################


#สร้าง Frame ให้แต่ละ Tab
F1 = Frame(T1)
F2 = Frame(T2)
F1.place(x=200,y=10)
F2.place(x=100,y=10)
#--------------ใส่รูปด้านบน-----------------
bg_label = ttk.Label(F1,image=img2)
bg_label.pack()


days = {'Mon' : 'จันทร์',
        'Tue' : 'อังคาร',
        'Wed' : 'พุธ',
        'Thu' : 'พฤหัสบดี',
        'Fri' : 'ศุกร์' ,
        'Sat' : 'เสาร์',
        'Sun' : 'อาทิตย์'}

    

def Save(event=None):
	expense = v_expense.get()
	price = v_price.get()
	quantity = v_quantity.get()

	if expense == '':
		print('No Data')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
		return
	elif price == '':
		messagebox.showwarning('Error','กรุณากรอกราคา')
		return
	elif quantity == '':
		quantity = 1

	total = float(price) * float(quantity)
	try:
		total = float(price) * float(quantity)
		# .get() คือดึงค่ามาจาก v_expense = StringVar()
		print('รายการ: {} ราคา: {}'.format(expense,price))
		print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
		text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
		text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total)
		v_result.set(text)
		# clear ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')

		# บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
		today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
		print(today)
		dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		dt = days[today] + '-' + dt
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
			# with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			# 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
			# newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
			data = [dt,expense,price,quantity,total]
			fw.writerow(data)

		# ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
		E1.focus()
		resulttable.delete(*resulttable.get_children())
		update_table()
	except:
		print('ERROR')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		#messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		#messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        

GUI.bind('<Return>',Save) # ต้องเพิ่ม def Save(event=None)

FONT1 = (None,20) #None เปลี่ยนเป็นชื่อฟ้อน ส่วน 20 คือ ขนาดตัวอักษร

#---pack 1 ----
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar() # StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)#ช่องรับข้อมูล
E1.pack()
#----------------

#---pack 2 ----
L = ttk.Label(F1,text='ราคา(บาท)',font=FONT1).pack()
v_price = StringVar() # StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)#ช่องกรอกข้อมูล
E2.pack()
#----------------

#---pack 3 ----
L = ttk.Label(F1,text='จำนวน(ชิ้น)',font=FONT1).pack()
v_quantity = StringVar() # StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)#ช่องกรอกข้อมูล
E3.pack()
#----------------

B2 = ttk.Button(F1,image=img1,text=f'{"Save" : ^{20}}',command=Save,compound='left')
B2.pack(ipadx=50,ipady=20,pady=20)

v_result = StringVar()
v_result.set('----ผลลัพธ์------')
result = ttk.Label(F1,textvariable =v_result,font=FONT1,foreground='blue' )
#result = ttk.Label(F1,textvariable =v_result,font=FONT1 )
result.pack(pady=20)
GUI.bind('<Tab>',lambda x: E2.focus())
##------------------Tab 2---------------#
#----------read CSV------------------
def read_csv():
    with open('savedata.csv',newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
        return data
        # print(data)
        # print('------------')
        # print(data[0][0])
        # for d in data:
        #      print(d)
        #fr = file reader
        #data = list(fr)คือการแปลงข้อมูลให้เราอ่านออก ลองโดยการprint
#table
LT = ttk.Label(T2,text='ตารางค่าใช้จ่าย',font=FONT1).pack(pady=20)
header = ['วัน-เวลา', 'รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10)
resulttable.pack()
# for i in range(len(header)):
#     resulttable.heading(header[i],text=header[i])

for h in header:
    resulttable.heading(h,text=h)

#####################ความกว้างของแต่ละcolumn###########################3
headerwidth = [180,150,80,80,80]
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)

# resulttable.insert('', 'end',value=['จันทร','น้ำดื่ม','200','2','400'])

def update_table():
    resulttable.delete(*resulttable.get_children())
    data = read_csv()
    for d in data: 
        resulttable.insert('','end',value=d)

update_table() 


GUI.mainloop()
