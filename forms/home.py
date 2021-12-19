from tkinter import *
from tkinter.ttk import *
from forms.hsn import FormHSN

class FormMenu:
    """This is the main form that shows after user login.
    Contains
    =========
    --> Label shows login Company name.
    --> Three Buttons
        --> HSN:   OnClick Shows FormHSN,
    --> A background Image
    """
    def __init__(self,master):
        self.frame=master
        #self.frame.title="Shop Pro using Python & Tkinter by Suhail"
        self._init_menu()
        self._init_widgets()
        
    def _init_menu(self):
        self.frame.bind("<KeyPress>",self.keypressed)
        
        self.menu = Menu(self.frame)
        self.frame.config(menu=self.menu)
        filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="HSN...", command=self.hsn_click)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.frame.quit)
        helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.about_click)

    def about_click(self):
        w=Toplevel()
        lbl1=Label(w,text="Welcome to medicalshop. version 1.2")
        lbl1.pack(side="top",padx=10,pady=10)
        lbl3=Label(w,text="for help contact me at: suhailvs@gmail.com")
        lbl3.pack(side="top",padx=10,pady=10)
        lbl3=Label(w,text="https://github.com/sta-k/medicalshop")
        lbl3.pack(side="top",padx=10,pady=10)
        
    def _init_widgets(self):
        #initiate toolbar
        self.toolbar = Frame(self.frame)
        imgdir="images/24x24/"
        self.toolbar.imghome=PhotoImage(file=imgdir+"home.gif")
        self.toolbar.imgcalc=PhotoImage(file=imgdir+"calc.gif")
        self.toolbar.imgcalander=PhotoImage(file=imgdir+"date.gif")
        self.toolbar.imgexit=PhotoImage(file=imgdir+"exit.gif")
        self.toolbar.imghelp=PhotoImage(file=imgdir+"help.gif")
        # butcompany=Button(self.toolbar,image=self.toolbar.imghome,command=self.calc_click)
        # butcompany.pack(side=LEFT,padx=2)
        # lbl0=Label(self.toolbar,text='Select Company.').pack(side=LEFT,padx=5)
           
        
        butexit=Button(self.toolbar,image=self.toolbar.imgexit,command=self.frame.quit)
        butexit.pack(side=RIGHT,padx=2)
        buthelp=Button(self.toolbar,image=self.toolbar.imghelp,command=self.about_click)
        buthelp.pack(side=RIGHT,padx=2)
        self.toolbar.pack(side='top',fill='x')
        

        #buttons frame
        #--------------------------------------------
        style = Style()
        style.configure("BW.TLabel", foreground="black", background="#e6fffb")
        self.buttons = Frame(self.frame, style="BW.TLabel")
        #button products
        self.btnproducts = Button(self.buttons,command=self.hsn_click)
        self.imgprdt=PhotoImage(file="images/products.gif")#self.btnproducts['font']=("Helvetica", 16)
        self.btnproducts['image']=self.imgprdt
        self.btnproducts.pack(side='top')#, fill='x')
        lbl1=Label(self.buttons,text="Products...", style="BW.TLabel").pack()
        #button invoices
        self.btninvoices = Button(self.buttons, command=self.hsn_click)
        self.imginv=PhotoImage(file="images/invoices.gif")
        self.btninvoices['image']=self.imginv
        self.btninvoices.pack(side='top')
        lbl2=Label(self.buttons,text="Invoices...", style="BW.TLabel").pack()
        #button customers
        self.btncustomers = Button(self.buttons, command=self.hsn_click)
        self.imgcust=PhotoImage(file="images/customers.gif")
        self.btncustomers['image']=self.imgcust
        self.btncustomers.pack(side='top')
        lbl3=Label(self.buttons,text="Create Invoice...", style="BW.TLabel").pack()
        self.buttons.pack(side='left',padx=10)
        """
        #buttons frame
        #--------------------------------------------
        style = Style()
        style.configure("BW.TLabel", foreground="white", background="#e6fffb")
        self.buttons = Frame(self.frame, style="BW.TLabel")
        #button products
        self.btnproducts = Button(self.buttons,command=self.hsn_click)
        self.imgprdt=PhotoImage(file="images/products.gif")#self.btnproducts['font']=("Helvetica", 16)
        self.btnproducts['image']=self.imgprdt
        self.btnproducts.pack(side='top')#, fill='x')
        lbl1=Label(self.buttons,text="Products...", style="BW.TLabel").pack()
       
        self.buttons.pack(side='left',padx=10)

        """
        #background label
        #-------------------------------------------
        self.imgback=PhotoImage(file="images/back2.gif")
        self.lblbackground= Label(self.frame, style="BW.TLabel",borderwidth=0)
        self.lblbackground.pack(side='top')
        self.lblbackground['image'] = self.imgback

    def calc_click(self):
        import os
        try: os.startfile('calc.exe')
        except: print ('calculator doesnt exist')

    def keypressed(self,e):
        #33 p, 31 i, 54 c
        if e.keycode == 33: self.products_click()
        elif e.keycode == 31: self.invoices_click()
        elif e.keycode == 54: self.addinvoice_click()
        
    def hsn_click(self):
        print ("hsn")
        self.frame.withdraw()
        self.frm_products=FormHSN()
        self.frame.wait_window(self.frm_products.frame)
        self.frame.deiconify()
       