from Library import *
from SQL import *
Closed = False
class Manger:
    def window_settings(window):
        window.geometry('1230x700+0+0')
        window.iconbitmap(f'{getcwd()}\\ICON.ico')
        window.resizable(False,False)
        window.title('Staff Management')
        title = Label(window,bg='#525C68',text='Staff Management',font=('bold',20),fg='white')
        title.place(x=35,y=5)
        window.config(background='#525C68')
    
    def freams(widnow):
        global ViewFream
        ViewFream = Frame(widnow,bg='silver')
        ViewFream.place(x=300,y=0,width=1100,height=660)
    def treeviwe(window,freams=freams):
        Scroll_y = Scrollbar(window,orient='vertical')
        global ViewData
        ViewData = ttk.Treeview(ViewFream,yscrollcommand=Scroll_y.set,columns=('id','name','age','job','email','gender','address','Fc','recruitment','pn'))
        ViewData['show']='headings'
        '''
        id,name,age,job,email,gender,address,Fc,recruitment,pn
        '''
        Scroll_y.config(command=ViewData.yview_scroll)
        ViewData.heading('id',text='id',anchor='center')
        ViewData.heading('name',text='Name',anchor='center')
        ViewData.heading('age',text='Age',anchor='center')
        ViewData.heading('job',text='Job',anchor='center')
        ViewData.heading('email',text='Email',anchor='center')
        ViewData.heading('gender',text='Gender',anchor='center')
        ViewData.heading('address',text='Address',anchor='center')
        ViewData.heading('Fc',text='Degree',anchor='center')
        ViewData.heading('recruitment',text='Recruitment',anchor='center')
        ViewData.heading('pn',text='Phone Number',anchor='center')
        '''
        id,name,age,job,email,gender,address,Fc,recruitment,pn
        '''
        ViewData.column('id',width=25)
        ViewData.column('name',width=150)
        ViewData.column('age',width=50)
        ViewData.column('job',width=120)
        ViewData.column('email',width=150)
        ViewData.column('gender',width=55)
        ViewData.column('address',width=100)
        #ViewData.column('address',width=100)
        ViewData.column('Fc',width=60)
        ViewData.column('recruitment',width=100)
        ViewData.column('pn',width=100)
        ViewData.place(x=0,y=0,height=800)
        Scroll_y.pack(side='right',fill=Y)
    
    def Entrys(window):
        global Name_Entry
        global Job_Entry
        global Gender_Entry
        global Age_Entry
        global Email_Entry
        global Mobile_Entry
        global Address_Entry
        global Functional_class
        global Recruitment
        global Id_del
        Name_Entry = Entry(window,font=5,justify='center')
        Id_del = Entry(window,font=5,justify='center',bg='red')
        Job_Entry = Entry(window,font='bold',justify='center')
        Gender_Entry = ttk.Combobox(window,values=('Male','Female'),state='readonly')
        Gender_Entry.set('Male')
        Age_Entry = Entry(window,font='bold',justify='center')
        Email_Entry = Entry(window,font='bold',justify='center')
        Mobile_Entry = Entry(window,font='bold',justify='center')
        Functional_class = Entry(window,font='bold',justify='center')
        Functional_class.insert(0,'7.1')
        now = datetime.now()
        Recruitment = Entry(window,font='bold',justify='center')
        Recruitment.insert(0,f'{now.year}/{now.month}/{now.day}')
        Address_Entry = Text(window,width=30,height=2)
        
        ###########################################
        Name_Entry.place(x=100,y=50)
        Job_Entry.place(x=100,y=100)
        Gender_Entry.place(x=100,y=150,width=185)
        Age_Entry.place(x=100,y=200)
        Email_Entry.place(x=100,y=250)
        Mobile_Entry.place(x=100,y=300)
        Functional_class.place(x=100,y=350)
        Recruitment.place(x=100,y=400)
        Address_Entry.place(x=27,y=450)
        Id_del.place(x=100,y=500)
    def show():
        pass
        '''cursor.execute('select * from data;')
        ViewData.delete(*ViewData.get_children())
        for i in cursor:
            ViewData.insert("",END,values=i)'''
    def commands_mysql(show = show):
        pass
        er = False
        if len(Name_Entry.get()) < 1:
            messagebox.showerror('Sorry','Sorry, but you have to fill in the Name field to complete the process')
            er = True
        elif len(Job_Entry.get()) < 1:
            messagebox.showerror('Sorry','Sorry, but you have to fill in the Job field to complete the process')
            er = True
        elif len(Gender_Entry.get()) < 1:
            messagebox.showerror('Sorry','Sorry, but you have to fill in the Gender field to complete the process')
            er = True
        elif len(Age_Entry.get()) < 1:
            messagebox.showerror('Sorry','Sorry, but you have to fill in the Age field to complete the process')
            er = True
            try:
                Age = int(Age_Entry.get())
            except ValueError:
                messagebox.showerror('Error','Please enter a number in the Age field instead of letters')
                er = True
        elif len(Email_Entry.get()) < 4 or '@' not in Email_Entry.get() or '.com' not in Email_Entry.get():
            messagebox.showerror('Sorry','Please check the email field')
            er = True
        elif len(Mobile_Entry.get()) < 6:
            messagebox.showerror('Sorry','Sorry, but you have to fill in the Phone Number field to complete the process')
            er = True
            try:
                Phone_Number = int(Mobile_Entry.get())
            except ValueError:
                messagebox.showerror('Error','Please enter a number in the Mobile field instead of letters')
                er = True
        elif len(Address_Entry.get(1.0,'end-1c')) < 3:
            messagebox.showerror('Sorry','Sorry, but you have to fill in the Address field to complete the process')
            er = True
        elif len(Recruitment.get()) < 1:
            messagebox.showerror('sorry','Please Check Recruitment field to complete the process')
            er = True
        elif len(Functional_class.get()) < 1:
            messagebox.showerror('sorry','Please Check Recruitment field to complete the process')
        cursor.execute('select * from data;')
        for data in cursor:
            if Email_Entry.get() in data or Mobile_Entry.get() in data:
                messagebox.showerror('خطاء في ادخال المعلومات','Sorry, but we have identical information in the system and in the fields. Please check the number field and the email field and try again.')
                er = True
        try:
            Address = f'{Address_Entry.get(1.0,"end-1c").splitlines()[0]} {Address_Entry.get(1.0,"end-1c").splitlines()[1]}'
        except IndexError:
            messagebox.showerror('خطاء في الأدخال','Excuse me, but you must enter the name of the country and region in which the employee lives to complete the process')
            er = True
        if er == False:
            big_number = 0
            #cursor.execute('select * from data')
            #for i in cursor:
            #    if int(i[0]) >= big_number:
            #        big_number = int(i[0])+1
            time = f"{Recruitment.get().split('/')[0]}/{Recruitment.get().split('/')[1]}/{Recruitment.get().split('/')[2]}"
            values = int(big_number),Name_Entry.get(),int(Age_Entry.get()),Job_Entry.get(),Email_Entry.get(),Gender_Entry.get(),Address,float(Functional_class.get()),Recruitment.get(),int(Mobile_Entry.get())
            #print(values)
            #id name age job email gender address Fc recruitment pn
            #cursor.execute("INSERT INTO data (id,name,age,job,email,gender,address,Fc,recruitment,pn) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",values)
            #                                  1 2     3   4    5      6      7     8     9       10         1   2  3 4   5 6  7   8   9
            #connect.commit()''
            show()
    def clear_entrys(show=show):
        Name_Entry.delete(0,END)
        Age_Entry.delete(0,END)
        Job_Entry.delete(0,END)
        Email_Entry.delete(0,END)
        Gender_Entry.delete(0,END)
        Mobile_Entry.delete(0,END)
        Address_Entry.delete("1.0","end")
        Id_del.delete(0,END)
        show()
    def update_window(treeview=treeviwe,show=show):
        update = Tk()
        update.geometry('300x300+100+100')
        #update.resizable(False,False)
        update.title('Delete Window')
        update.config(background='#525C68')
        hello = Label(update,text='Hello',bg='#525C68',fg='black',font=('bold',25))
        des = Label(update,text='We need id for update the data',font=('bold',12))
        id_text=Label(update,text='ID',bg='#525C68',fg='black',font='bold')
        id_entry = Entry(update,bg='silver',font='bold')
        btdel = Button(update,text='Delete',font=('bold',10),bg='red')
        hello.pack(pady=30)
        des.pack()
        id_text.place(x=40,y=150)
        id_entry.place(x=70,y=150)
        btdel.place(x=100,y=200,width=100,height=30)
        update.mainloop()
        id_text.place(x=40,y=150)
        id_entry.place(x=70,y=150)
        btdel.place(x=100,y=200,width=100,height=30)
        show()
    
    def delete(show=show):
        id_number=int(Id_del.get())
        cursor.execute(f'delete from data where id={id_number}')
        connect.commit()
        cursor.execute('select * from data;')
        ViewData.delete(*ViewData.get_children())
        for i in cursor:
            ViewData.insert("",END,values=i)
        show()
    def Buttons(window,Del=delete,commands_mysql=commands_mysql,update_window=update_window,Clear=clear_entrys):
        Add_values = Button(window,command=commands_mysql,text='Add Details',bg='green',fg='black',height=2,font='bold',activebackground='#9B889D')
        Delete_values = Button(window,command=Del,text='Delete Details',bg='red',fg='black',height=2,font='bold',activebackground='#9B889D')
        Update_values = Button(window,command=update_window,text='Update Details',bg='orange',fg='black',height=2,font='bold',activebackground='#9B889D')
        Clear_values = Button(window,command=Clear,text='Clear Entrys',bg='#4426FF',fg='black',height=2,font='bold',activebackground='#9B889D')
        ###############################################
        Add_values.place(x=15,y=540,width=113)
        Delete_values.place(x=15,y=610)
        Update_values.place(x=150,y=540)
        Clear_values.place(x=150,y=610,width=120)
    def Texts(window):
        Id_delt = Label(window,text='ID',bg='#525C68',border=0,font=('bold',15),fg='red')
        Name_Text = Label(window,text='Name',bg='#525C68',border=0,font=('bold',15),fg='white')
        Job_Text = Label(window,text='Job',bg='#525C68',border=0,font=('bold',15),fg='white')
        Gender_Text = Label(window,text='Gender',bg='#525C68',border=0,font=('bold',15),fg='white')
        Age_Text = Label(window,text='Age',bg='#525C68',border=0,font=('bold',15),fg='white')
        Email_Text = Label(window,text='Email',bg='#525C68',border=0,font=('bold',15),fg='white')
        Mobile_Text = Label(window,text='Mobile',bg='#525C68',border=0,font=('bold',15),fg='white')
        Functional_class = Label(window,text='Degree',bg='#525C68',border=0,font=('bold',15),fg='white')
        Recruitment = Label(window,text='Recruitment',bg='#525C68',border=0,font=(15),fg='white')
        Address_Text = Label(window,text='Address',bg='#525C68',border=0,font=('bold',13),fg='white')
        Zero_Text = Label(window,text='0',bg='#525C68',border=0,font=('bold',13),fg='white')
        #########################################################################################
        Name_Text.place(x=10,y=48)
        Job_Text.place(x=10,y=98)
        Gender_Text.place(x=10,y=148)
        Age_Text.place(x=10,y=198)
        Email_Text.place(x=10,y=248)
        Mobile_Text.place(x=10,y=298)
        Functional_class.place(x=10 , y=348)
        Recruitment.place(x=10,y=400)
        Address_Text.place(x=110,y=424)
        Zero_Text.place(x=86,y=300)
        Id_delt.place(x=20,y=500)
    def __init__(self,show=show,TreeViewData=treeviwe,Texts=Texts,Buttons=Buttons,window_settings=window_settings,freams=freams,Entrys=Entrys):
        self.window = Tk()
        window_settings(self.window)
        freams(self.window)
        Entrys(self.window)
        Buttons(self.window)
        Texts(self.window)
        TreeViewData(self.window)
        show()
        self.window.mainloop()
Manger()
Closed = True