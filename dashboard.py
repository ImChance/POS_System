from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass 
from category import categoryClass
from product import productClass
from sales import salesClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Inventory Management System | CS-1")
        self.root.config(bg="white")



        # --------------------------Title----------------------------------------
        self.icon_title=PhotoImage(file="images/logo1.png")
        
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="purple",fg="white",anchor='w',padx=20).place(x=0,y=0,relwidth=1,height=70)
        

        # ---------------------------Button---------------------------------------
        btn_logout=Button(self.root,text="Logout",font=("times new roman",20,"bold"),bg="pink",fg="black",cursor="hand2").place(x=1350,y=10,height=50,width=130)



        # -------------------------Clock------------------------------------------------

        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="grey",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)


        # ------------------Left Menu-----------------------------
        self.menulogo=Image.open("images/menu.jpg")
        self.menulogo=self.menulogo.resize((200,200),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=100,width=200,height=638)

        lbl_menulogo=Label(leftmenu,image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/arrow.png")
        lbl_menu=Label(leftmenu,text="Menu",font=("times new roman",30),bg="lightgreen").pack(side=TOP,fill=X)
        btn_employee=Button(leftmenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",23,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(leftmenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",23,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(leftmenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",23,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(leftmenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",23,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(leftmenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",23,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(leftmenu,text="Exit",image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",23,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


        # -----------------------content-------------------

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="light blue",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="grey",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="light green",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="navy blue",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)


        # ----------------footer--------------------
        lbl_footer=Label(self.root,text="IMS Engineering College\nPython Project | By Chance Gupta | Gaurav Kumar Patel | Atresh Dixit",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

# ------------------------------------------------------------------------------------------------
    def employee(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=salesClass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()


