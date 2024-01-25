import tkinter
from tkinter import ttk

from ttkbootstrap import Style
from tkinter import *
from tkinter import messagebox, filedialog

import cx_Oracle

import report_gen as rg

cx_Oracle.init_oracle_client(r'D:\instantclient\instantclient_19_8\inst32')
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="right", fill="both", expand=True)
        scrollbar.pack(side="left", fill="y")



class Application(tkinter.Tk):


    def __init__(self):
        super().__init__()
        self.title('Armed Forces Personnel Viewer')
        #self.attributes('-fullscreen',True)
        self.geometry('1360x768')
        self.style = Style('solar')
        self.search = EntryForm(self, padding=10)
        self.search.pack(fill='both', expand='yes')



class EntryForm(ttk.Frame, Application):


    p_attributes = ['military_id' , 'ssn', 'full_name',  'rank_id', 'branch_id', 'formation_id', 'leader_id', 'batch_no', 'physical_status', 'blood_type' , 'address', 'phone_no', 'birth_date', 'marital_status','guarantor_id'] 


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(padding=(20, 10))
        self.columnconfigure(2, weight=1)

        # form variables
        self.military_id = tkinter.StringVar(value='',name='military_id')
        self.physical_status = tkinter.StringVar(value='', name='physical_status')
        self.batch_no = tkinter.StringVar(value='',name='batch_no')
        self.blood_type = tkinter.StringVar(value='', name='blood_type')
        self.phone_no = tkinter.StringVar(value='', name='phone_no')
        self.formation_id = tkinter.StringVar(value='', name='formation_id')
        self.branch_id = tkinter.StringVar(value='', name='branch_id')
        self.rank_id = tkinter.StringVar(value='', name='rank_id')
        self.leader_id = tkinter.StringVar(value='', name='leader_id')
        self.guarantor_id = tkinter.StringVar(value='', name='guarantor_id')
        self.ssn = tkinter.StringVar(value='',name='ssn')
        self.full_name = tkinter.StringVar(value='', name='full_name')
        self.address = tkinter.StringVar(value='', name='address')
        self.birth_date = tkinter.StringVar(value='', name='birth_date')
        self.marital_status = tkinter.StringVar(value='', name='marital_status')

        self.selectedTheme = tkinter.StringVar()
        

        

        Data_farme=ScrollableFrame(self)
        Data_farme.place(x=0,y=65,width=400,height=530)
        
        
        ttk.Entry(Data_farme.scrollable_frame, width=30).grid(row=1, column=1)


        


        # form headers
        Label(self, text='Armed Forces Personnel Viewer',fg='#EAC537',font=('Time New Roman', 16, 'bold')).place(x=0, y=0)

        
        # create label/entry rows
        for i, label in enumerate(self.p_attributes):
            
            ttk.Label(Data_farme.scrollable_frame, text=label.title().replace('_', ' ')).grid(row=i + 1, column=0, sticky='ew', pady=20, padx=(0, 10))
            
            
        

        self.military_id_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.military_id).grid(row=0 + 1, column=1, columnspan=2, sticky='ew')
        self.ssn_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.ssn).grid(row=1 + 1, column=1, columnspan=2, sticky='ew')
        self.full_name_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.full_name).grid(row=2 + 1, column=1, columnspan=2, sticky='ew')    
        self.rank_id_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.rank_id).grid(row=3 + 1, column=1, columnspan=2, sticky='ew')
        self.brnach_id_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.branch_id).grid(row=4 + 1, column=1, columnspan=2, sticky='ew')
        self.formation_id_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.formation_id).grid(row=5 + 1, column=1, columnspan=2, sticky='ew')
        self.leader_id_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.leader_id).grid(row=6 + 1, column=1, columnspan=2, sticky='ew')
        self.batch_no_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.batch_no).grid(row=7 + 1, column=1, columnspan=2, sticky='ew')
        self.physical_status_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.physical_status).grid(row=8 + 1, column=1, columnspan=2, sticky='ew')
        self.blood_type_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.blood_type).grid(row=9 + 1, column=1, columnspan=2, sticky='ew')
        self.address_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.address).grid(row=10 + 1, column=1, columnspan=2, sticky='ew')
        self.phone_no_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.phone_no).grid(row=11 + 1, column=1, columnspan=2, sticky='ew')
        self.birth_date_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.birth_date).grid(row=12 + 1, column=1, columnspan=2, sticky='ew')
        self.marital_status_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.marital_status).grid(row=13 + 1, column=1, columnspan=2, sticky='ew')
        self.guarantor_id_entry = ttk.Entry(Data_farme.scrollable_frame, textvariable=self.guarantor_id).grid(row=14 + 1, column=1, columnspan=2, sticky='ew')

        
        

        
        self.add = ttk.Button(self, text='Add', style='success.TButton', command=self.add_record)
        self.add.place(x=0, y=620, width=70)
        
    
        
        self.update = ttk.Button(self, text='Update', style='info.TButton', command=self.update_record)
        self.update.place(x=100, y=620, width=70)
        




        self.delete = ttk.Button(self, text='Delete', style='danger.TButton', command=self.delete_record)
        self.delete.place(x=200, y=620, width=70)

        
        self.clear = ttk.Button(self, text='Clear', style='warning.TButton', command=self.clearFields)
        self.clear.place(x=290, y=620, width=70)


        self.reportButton = ttk.Button(self, text='Generate Report', style='secondary.TButton', command=self.genReport)
        self.reportButton.place(x=1190, y=650, width=120)

        #Samna Zone
        
        self.shreeta = ttk.Label(self, text='', style='TLabel')
        self.shreeta.place(x=351, y=65, width=19, height=535)

        #samna mn t7t
        self.samna = ttk.Label(self, text='', style='TLabel')
        self.samna.place(x=20, y=593, width=331, height=2)

        #samna mn fo2
        self.samna2 = ttk.Label(self, text='', style='TLabel')
        self.samna2.place(x=20, y=65, width=331, height=2)

        #samna sideway
        self.shreeta = ttk.Label(self, text='', style='TLabel')
        self.shreeta.place(x=20, y=65, width=2, height=535)

        #Samna Zone   

        Table_frame = Frame(self,bg='white')
        Table_frame.place(x=370, y=65, height=575, width=950)
        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.personnel = ttk.Treeview(Table_frame, columns=('NO.','military_id' , 'ssn', 'full_name',  'rank_id', 'branch_id', 'formation_id', 'leader_id', 'batch_no', 'physical_status', 'blood_type' , 'address', 'phone_no', 'birth_date', 'marital_status','guarantor_id'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.personnel.xview)
        scroll_y.config(command=self.personnel.yview)

        self.personnel.heading('NO.', text='No.')
        for name in self.p_attributes:
            self.personnel.heading(name, text=name.upper())
        self.personnel['show'] = 'headings'

        self.personnel.column('NO.',width=30)
        self.personnel.column('military_id',width=95)
        self.personnel.column('ssn',width=140)
        self.personnel.column('full_name',width=200)
        self.personnel.column('rank_id',width=85)
        self.personnel.column('branch_id',width=95)
        self.personnel.column('formation_id',width=115)
        self.personnel.column('leader_id',width=95)
        self.personnel.column('batch_no',width=95)
        self.personnel.column('physical_status',width=134)
        self.personnel.column('blood_type',width=118)
        self.personnel.column('address',width=260)
        self.personnel.column('phone_no',width=160)
        self.personnel.column('birth_date',width=110)
        self.personnel.column('marital_status',width=130)
        self.personnel.column('guarantor_id',width=120)
        
        self.personnel.pack(fill=BOTH, expand=1)
        self.personnel.bind("<ButtonRelease-1>", self.get_record)

        search_by_label = Label(self, text='Search By', font=('time new roman', 15), fg='white').place(x=450, y=17)
        self.search_by = ttk.Combobox(self, font=('time new roman', 13))
        self.search_by['values'] = ('Military Id', 'Formation Id')
        self.search_by.place(x=620, y=20, width=130, height=25)

        self.txt_search = ttk.Entry(self, font=('time new roman', 13))
        self.txt_search.place(x=800, y=20, width=157, height=25)
        search_b = ttk.Button(self, text='Search', command=self.searchFunc).place(x=1000, y=18)
        show_b = ttk.Button(self, text='Show All', command=self.fetch_data).place(x=1100, y=18)
        
        self.themeToggle = ttk.Checkbutton(self, text='Theme',variable=self.selectedTheme,command=self.themeChanger,style='primary.Roundtoggle.Toolbutton').place(x=1200, y=20)

        self.fetch_data()


    def get_record(self,event):
        record=self.personnel.focus()
        content=self.personnel.item(record)
        rows=content['values']

        self.military_id.set(rows[1])
        self.ssn.set(rows[2])
        self.full_name.set(rows[3])
        self.rank_id.set(rows[4])
        self.branch_id.set(rows[5])
        self.formation_id.set(rows[6])
        self.leader_id.set(rows[7])
        self.batch_no.set(rows[8])
        self.physical_status.set(rows[9])
        self.blood_type.set(rows[10])
        self.address.set(rows[11])
        self.phone_no.set('0' + str(rows[12]))
        self.birth_date.set(rows[13])
        self.marital_status.set(rows[14])
        self.guarantor_id.set(rows[15])


    def themeChanger(self):
        #dark theme
        if self.selectedTheme.get() == '1':
            self.style = Style('minty') #change the theme
            Label(self, text='Search By', font=('time new roman', 15), bg='White',fg='black').place(x=450, y=17)
            Label(self, text='Armed Forces Personnel Viewer',fg='#EAC537',bg='White',font=('Time New Roman', 16, 'bold')).place(x=0, y=0) 
        else:
            self.style = Style('solar') #change the theme
            Label(self, text='Search By', font=('time new roman', 15),fg='White', bg='#002b36').place(x=450, y=17)
            Label(self, text='Armed Forces Personnel Viewer',fg='#EAC537',bg='#002b36',font=('Time New Roman', 16, 'bold')).place(x=0, y=0)

    def print_form_data(self):
        #print(self.name.get(), self.address.get(), self.phone.get(), self.age.get())
        
        print(type(self.military_id.get()))
        print(self.military_id.get())



    def fetch_data(self):
        conn = cx_Oracle.connect("ARMEDFORCES", "ARMEDFORCES", "yousef1")
        cur = conn.cursor()
        cur.execute("select p.military_id, pc.ssn, pc.f_name || ' ' || pc.m_name || ' ' || pc.l_name, p.rank_id, p.branch_id, p.formation_id, p.leader_id, p.batch_no, p.physical_status, p.blood_type, pc.street_name || ', ' || pc.city || ', ' || pc.governrate, p.phone_no, to_char(pc.birth_date, 'DD-MM-YYYY'), pc.marital_status, p.guarantor_id  from personnel p, personnel_civilian_data pc where p.military_id = pc.military_id")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.personnel.delete(*self.personnel.get_children())
            for i, row in enumerate(rows):
                listed_query = list(row)
                listed_query.insert(0, i + 1)
                self.personnel.insert('',END,values=listed_query)
                

            conn.commit()
        conn.close()

    def get_values(self):

        if all([self.military_id.get(), self.ssn.get(), self.full_name.get(), self.rank_id.get(), self.branch_id.get(), self.formation_id.get(), self.leader_id.get(), self.batch_no.get(), self.physical_status.get(), self.blood_type.get(), self.address.get(), self.phone_no.get(), self.birth_date.get(), self.marital_status.get(), self.guarantor_id.get()]) == False:
                

            messagebox.showerror("Data Entry Error", "All Fields are Required", parent=self)
        
                

                
        else:
            self.get_full_name = self.full_name.get().split()
            self.get_rank_id = self.rank_id.get()
            self.get_branch_id = self.branch_id.get()
            self.get_formation_id = self.formation_id.get()
            self.get_batch_no = self.batch_no.get()
            self.get_physical_status = self.physical_status.get()
            self.get_blood_type = self.blood_type.get()
            self.get_address = self.address.get().split(', ')
            self.get_phone_no = self.phone_no.get()
            self.get_birth_date = self.birth_date.get()
            self.get_marital_status = self.marital_status.get()
            self.get_guarantor_id = self.guarantor_id.get()

            if len(str(self.military_id.get())) < 6 or len(str(self.military_id.get())) > 6:
                messagebox.showerror("Data Entry Error", "Military ID must be 6 numbers", parent=self)
                self.military_id.set('')
            else:
                self.get_military_id = self.military_id.get()


            if len(str(self.ssn.get())) < 14 or len(str(self.ssn.get())) > 14:
                messagebox.showerror("Data Entry Error", "SSN must be 14 numbers", parent=self)
                self.ssn.set('')
            else:
                self.get_ssn = self.ssn.get()


            if len(str(self.leader_id.get())) < 6 or len(str(self.leader_id.get())) > 6:
                messagebox.showerror("Data Entry Error", "Leader ID must be 6 numbers", parent=self)
                self.leader_id.set('')
            else:
                self.get_leader_id = self.leader_id.get()

    
    def add_record(self):
        self.get_values()
        conn = cx_Oracle.connect("ARMEDFORCES", "ARMEDFORCES", "yousef1")
        cur = conn.cursor()
        if all([self.military_id.get(), self.ssn.get(), self.full_name.get(), self.rank_id.get(), self.branch_id.get(), self.formation_id.get(), self.leader_id.get(), self.batch_no.get(), self.physical_status.get(), self.blood_type.get(), self.address.get(), self.phone_no.get(), self.birth_date.get(), self.marital_status.get(), self.guarantor_id.get()]) == True:
            cur.execute(f"select pc.f_name || ' ' || pc.m_name || ' ' || pc.l_name, p.rank_id, p.branch_id, p.formation_id, p.leader_id, p.batch_no, p.physical_status, p.blood_type, pc.street_name || ', ' || pc.city || ', ' || pc.governrate, p.phone_no, to_char(pc.birth_date, 'DD-MM-YYYY'), pc.marital_status, p.guarantor_id  from personnel p, personnel_civilian_data pc where p.military_id = pc.military_id and p.military_id = {int(self.get_military_id)} or pc.ssn = {int(self.get_ssn)}")
            checkrow = cur.fetchall()
            if checkrow != []:
                messagebox.showwarning('Warning','Data is already Added',parent=self)
            else:
                cur.execute("insert into personnel values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)",(int(self.get_military_id), self.get_physical_status, self.get_batch_no, self.get_blood_type, self.get_phone_no, self.get_formation_id, self.get_branch_id, self.get_rank_id, int(self.get_leader_id), int(self.get_guarantor_id)))
                cur.execute("insert into personnel_civilian_data values(:1,:2,:3,:4,:5,:6,:7,:8,:9,to_date(:10, 'DD-MM-YYYY'))",(int(self.get_ssn), int(self.get_military_id), self.get_full_name[0], self.get_full_name[1], self.get_full_name[2], self.get_address[0], self.get_address[1], self.get_address[2], self.get_marital_status, self.get_birth_date))
                conn.commit()
                messagebox.showinfo("Operation status", "Data Added Successfully", parent=self)
                self.fetch_data()
                conn.close()

    def delete_record(self):
        self.get_values()
        conn = cx_Oracle.connect("ARMEDFORCES", "ARMEDFORCES", "yousef1")
        cur = conn.cursor()
        if all([self.military_id.get(), self.ssn.get(), self.full_name.get(), self.rank_id.get(), self.branch_id.get(), self.formation_id.get(), self.leader_id.get(), self.batch_no.get(), self.physical_status.get(), self.blood_type.get(), self.address.get(), self.phone_no.get(), self.birth_date.get(), self.marital_status.get(), self.guarantor_id.get()]) == True:
            cur.execute(f"select pc.f_name || ' ' || pc.m_name || ' ' || pc.l_name, p.rank_id, p.branch_id, p.formation_id, p.leader_id, p.batch_no, p.physical_status, p.blood_type, pc.street_name || ', ' || pc.city || ', ' || pc.governrate, p.phone_no, to_char(pc.birth_date, 'DD-MM-YYYY'), pc.marital_status, p.guarantor_id  from personnel p, personnel_civilian_data pc where p.military_id = pc.military_id and p.military_id = {int(self.get_military_id)}")
            checkrow = cur.fetchall()
            if checkrow != []:
                cur.execute(f"delete from personnel_civilian_data where military_id ={self.get_military_id}")
                conn.commit()
                cur.execute(f"delete from personnel where military_id ={self.get_military_id}")
                conn.commit()
                messagebox.showinfo("Operation status", "Data Deleted Successfully", parent=self)
                self.fetch_data()
                self.clearFields()
                conn.close()    	            
            else:
                messagebox.showwarning('Warning','Personnel doesn\'t exist',parent=self)

    def update_record(self):
    	self.get_values()
    	conn = cx_Oracle.connect("ARMEDFORCES", "ARMEDFORCES", "yousef1")
    	cur = conn.cursor()
    	if all([self.military_id.get(), self.ssn.get(), self.full_name.get(), self.rank_id.get(), self.branch_id.get(), self.formation_id.get(), self.leader_id.get(), self.batch_no.get(), self.physical_status.get(), self.blood_type.get(), self.address.get(), self.phone_no.get(), self.birth_date.get(), self.marital_status.get(), self.guarantor_id.get()]) == True:            
            cur.execute(f"select p.military_id, pc.ssn, pc.f_name || ' ' || pc.m_name || ' ' || pc.l_name, p.rank_id, p.branch_id, p.formation_id, p.leader_id, p.batch_no, p.physical_status, p.blood_type, pc.street_name || ', ' || pc.city || ', ' || pc.governrate, p.phone_no, to_char(pc.birth_date, 'DD-MM-YYYY'), pc.marital_status, p.guarantor_id  from personnel p, personnel_civilian_data pc where p.military_id = pc.military_id and (p.military_id = {int(self.military_id.get())} and pc.ssn= {int(self.ssn.get())})")
            checkrow1 = cur.fetchall()
 
            if ([(int(self.military_id.get()), int(self.ssn.get()), self.full_name.get(), self.rank_id.get(), self.branch_id.get(),
                 self.formation_id.get(), int(self.leader_id.get()), self.batch_no.get(), self.physical_status.get(),
                 self.blood_type.get(), self.address.get(), self.phone_no.get(), self.birth_date.get(),
                 self.marital_status.get(), int(self.guarantor_id.get()))] == checkrow1):
            	messagebox.showinfo("Warning", "Data has not been modified", parent=self)
            elif checkrow1 == []:
            	messagebox.showinfo("Error", "SSN and military ID cannot be updated", parent=self)
            else:
            	cur.execute(f"update personnel set physical_status=:1, batch_no=:2, blood_type=:3, phone_no=:4, formation_id=:5, branch_id=:6, rank_id=:7, leader_id=:8, guarantor_id=:9 where military_id={int(self.get_military_id)}", (self.get_physical_status, self.get_batch_no, self.get_blood_type, self.get_phone_no, self.get_formation_id, self.get_branch_id, self.get_rank_id, int(self.get_leader_id), int(self.get_guarantor_id)))
            	conn.commit()
            	cur.execute(f"update personnel_civilian_data set f_name=:1, m_name=:2, l_name=:3, street_name=:4, city=:5, governrate=:6, marital_status=:7, birth_date=to_date(:8, 'DD-MM-YYYY') where ssn={int(self.get_ssn)}", (self.get_full_name[0], self.get_full_name[1], self.get_full_name[2], self.get_address[0], self.get_address[1], self.get_address[2], self.get_marital_status, self.get_birth_date))
            	conn.commit()
            	self.fetch_data()
            	self.clearFields()
            	messagebox.showinfo("Operation Status", "Data Has Been Updated", parent=self)
            	conn.close()
                    	            

    def searchFunc(self):
        conn = cx_Oracle.connect("ARMEDFORCES", "ARMEDFORCES", "yousef1")
        cur = conn.cursor()
        if self.search_by.get()=='':
            messagebox.showwarning('Warning','Select the search roll',parent=self)
        elif self.txt_search.get()=='':
            messagebox.showwarning('Warning', 'Enter some thing to search', parent=self)
        else:
        	if self.txt_search.get().isdigit():
        		cur.execute(f"select p.military_id, pc.ssn, pc.f_name || ' ' || pc.m_name || ' ' || pc.l_name, p.rank_id, p.branch_id, p.formation_id, p.leader_id, p.batch_no, p.physical_status, p.blood_type, pc.street_name || ', ' || pc.city || ', ' || pc.governrate, p.phone_no, to_char(pc.birth_date, 'DD-MM-YYYY'), pc.marital_status, p.guarantor_id  from personnel p, personnel_civilian_data pc where p.military_id = pc.military_id and {'p.' + self.search_by.get().replace(' ', '_').lower()} = '{int(self.txt_search.get())}'")
        	else:
        		cur.execute(f"select p.military_id, pc.ssn, pc.f_name || ' ' || pc.m_name || ' ' || pc.l_name, p.rank_id, p.branch_id, p.formation_id, p.leader_id, p.batch_no, p.physical_status, p.blood_type, pc.street_name || ', ' || pc.city || ', ' || pc.governrate, p.phone_no, to_char(pc.birth_date, 'DD-MM-YYYY'), pc.marital_status, p.guarantor_id  from personnel p, personnel_civilian_data pc where p.military_id = pc.military_id and {'p.' + self.search_by.get().replace(' ', '_').lower()} = '{self.txt_search.get()}'")
        	rows = cur.fetchall()
        	if len(rows)!=0:
        		self.personnel.delete(*self.personnel.get_children())
        	for i, row in enumerate(rows):
        		listed_query = list(row)
        		listed_query.insert(0, i + 1)
        		self.personnel.insert('',END,values=listed_query)

        if self.search_by.get() == 'Formation Id' and self.txt_search.get() != '':
            user_in = messagebox.askyesno('report', f'Would you like to generate a report for {self.txt_search.get()}',parent=self)
            if user_in:
                file_path = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=(("PDF file", "*.pdf"), ("All Files", "*.pdf")))
                cur.execute(f"select p.military_id, pc.f_name || ' ' || pc.m_name || ' ' || pc.l_name, p.rank_id, p.branch_id, p.leader_id, p.blood_type from personnel p, personnel_civilian_data pc where p.military_id = pc.military_id and p.formation_id='{self.txt_search.get()}'")
                self.formation_rows = cur.fetchall()
                if file_path:
                    rg.genFormationReport(self.formation_rows, self.txt_search.get(), file_path)
                    messagebox.showinfo("Operation Status", "Report Has Been Generated", parent=self)

        conn.commit()
        conn.close()


    def genReport(self):
        record=self.personnel.focus()
        content=self.personnel.item(record)
        rows=content['values']

        if rows:
        	file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=(("PDF file", ".pdf"),("All Files", ".pdf") ))
        	if file_path:
        		rg.report(rows, file_path)
        		messagebox.showinfo("Operation Status", "Report Has Been Generated", parent=self)
        	else:
        		pass
        else:
        	messagebox.showwarning('Warning', 'Highlight a Personnel to Generate His Report', parent=self)	

    

    def clearFields(self):
        for att in self.p_attributes:
            eval('self.' + att + '.set("")')






        
if __name__ == '__main__':
    Application().mainloop()



 #search(query)    