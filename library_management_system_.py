from tkinter import*
from tkinter import messagebox
import mysql.connector as mc
from PIL import ImageTk, Image

root = Tk()
root.resizable(0,0)
canvas = Canvas(root)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("library.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)
#========================================add books window==================================================
def addBooks():
    
    def submit():
        con = mc.connect(host="localhost", user="root", password="tiger", database="library", use_pure=True)
        cur = con.cursor()
        query = "insert into books values(%s, %s, %s, %s)"
        val = (f"{ent1.get()}", f"{ent2.get()}", f"{ent3.get()}", f"{ent4.get()}")
        cur.execute(query, val)
        con.commit()
        messagebox.showinfo("Records", "Record Added")
        cur.close()
        con.close()
        
    def cancel():
        window.destroy()
        
    window = Toplevel()
    window.resizable(0, 0)
    canvas1 = Canvas(window)
    canvas1.pack()
    img1 = ImageTk.PhotoImage(Image.open("library.jpg"))
    canvas1.create_image(0, 0, anchor=NW, image=img1)
    lbl1 = Label(canvas1, text="ADD BOOK DETAILS", font=("times 24", 40, "bold"), bg="black", fg="white")
    lbl1.pack()
    lbl2 = Label(canvas1, text="")
    lbl2.pack()
    frame = Frame(canvas1)
    
    lb1 = Label(frame, text="Book ID:   ", font=("verdana", 20), fg="black")
    lb1.grid(row=0, column=0)
    ent1 = Entry(frame, bg="black", fg="white", bd=5)
    ent1.grid(row=0, column=1)
    
    lb2 = Label(frame, text="Title:     ", font=("verdana", 20), fg="black")
    lb2.grid(row=1, column=0)
    ent2 = Entry(frame, bg="black", fg="white", bd=5)
    ent2.grid(row=1, column=1)

    lb3 = Label(frame, text="Author:    ", font=("verdana", 20), fg="black")
    lb3.grid(row=2, column=0)
    ent3 = Entry(frame, bg="black", fg="white", bd=5)
    ent3.grid(row=2, column=1)

    lb4 = Label(frame, text="status:    ", font=("verdana", 20), fg="black")
    lb4.grid(row=3, column=0)
    ent4 = Entry(frame, bg="black", fg="white", bd=5)
    ent4.grid(row=3, column=1)
    
    submitButton = Button(frame, text="Submit", bg="black", fg="white", font=("verdana", 20), command=submit)
    submitButton.grid(row=4, column=0)
    cancelButton = Button(frame, text="Cancel", bg="black", fg="white", font=("verdana", 20), command=cancel)
    cancelButton.grid(row=4, column=1)
    frame.pack(side=BOTTOM)


#=========================================View Data==============================================================

def viewRecord():    
    def viewSpecific():
        def showButton():
            top = Toplevel()
            con = mc.connect(host="localhost", user="root", password="tiger", database="library", use_pure=True)
            cur = con.cursor()
            query = f"select * from books where book_id='{en1.get()}'"
            cur.execute(query)
            limit = 0
            for book in cur:
                for items in range(len(book)):
                    e1 = Entry(top, bg="black", fg="white", width=20)
                    e1.grid(row=limit, column=items)
                    e1.insert(END, book[items])
                limit += 1 
        def cancel__():
            win.destroy()
        
        w = Toplevel()
        w.resizable(0,0)
        frame1 = Frame(w)
        l1 = Label(frame1, text="Book ID:   ", font=("verdana", 20), fg="black")
        l1.grid(row=0, column=0)
        en1 = Entry(frame1, bg="black", fg="white", bd=5)
        en1.grid(row=0, column=1)
        frame1.pack(side=BOTTOM)
        submitButton1 = Button(frame1, text="Submit", bg="black", fg="white", font=("verdana", 20), command=showButton)
        submitButton1.grid(row=1, column=0)
        cancelButton1 = Button(frame1, text="Cancel", bg="black", fg="white", font=("verdana", 20), command=cancel__)
        cancelButton1.grid(row=1, column=1)
    
    def viewIssue():
        top = Toplevel()
        top.resizable(0,0)
        con = mc.connect(host="localhost", user="root", password="tiger", database="library", use_pure=True)
        cur = con.cursor()
        cur.execute("select * from issued_books")
        mu = 0
        for g in cur:
            for xu in range(len(g)):
                eN = Entry(top, bg="black", fg="white", width=20)
                eN.grid(row=mu, column=xu)
                eN.insert(END, g[xu])
            mu = mu + 1
    
    
    def viewAll():
        top = Toplevel()
        top.resizable(0,0)
        con = mc.connect(host="localhost", user="root", password="tiger", database="library", use_pure=True)
        cur = con.cursor()
        cur.execute("select * from books")
        mu = 0
        for g in cur:
            for xu in range(len(g)):
                eN = Entry(top, bg="black", fg="white", width=20)
                eN.grid(row=mu, column=xu)
                eN.insert(END, g[xu])
            mu = mu + 1
        
    

  
    win = Toplevel()
    win.resizable(0,0)
    lbl1 = Label(win, text="Choose To View Record", font=("times 24", 40, "bold"), bg="black", fg="white")
    lbl1.pack()
    lbl2 = Label(win, text="")
    lbl2.pack()
    b1 = Button(win, bg="black", fg="white", text="Issued Books", width=13, font=("verdana", 20), command=viewIssue)
    b1.pack()
    b2 = Button(win, bg="black", fg="white", text="Specific Book", width=13, font=("verdana", 20), command=viewSpecific)
    b2.pack()
    b3 = Button(win, bg="black", fg="white", text="All Books", width=13, font=("verdana", 20), command=viewAll)
    b3.pack()
    
        


#=====================================Delete books window==========================================================    
def deleteBook():
    def submit_():
        con = mc.connect(host="localhost", user="root", password="tiger", database="library", use_pure=True)
        cur = con.cursor()
        query1 = f"delete from books where book_id='{en1.get()}'"
        cur.execute(query1)
        con.commit()
        messagebox.showinfo("Records", "Record Deleted")
        cur.close()
        con.close()
        
    
    def cancel_():
        wind.destroy()
    
    wind = Toplevel()
    wind.resizable(0,0)
    lbl1 = Label(wind, text="Delete Book", font=("times 24", 40, "bold"), bg="black", fg="white")
    lbl1.pack()
    lbl2 = Label(wind, text="")
    lbl2.pack()
    frame1 = Frame(wind)
    l1 = Label(frame1, text="Book ID:   ", font=("verdana", 20), fg="black")
    l1.grid(row=0, column=0)
    en1 = Entry(frame1, bg="black", fg="white", bd=5)
    en1.grid(row=0, column=1)
    frame1.pack(side=BOTTOM)
    submitButton1 = Button(frame1, text="Submit", bg="black", fg="white", font=("verdana", 20), command=submit_)
    submitButton1.grid(row=1, column=0)
    cancelButton1 = Button(frame1, text="Cancel", bg="black", fg="white", font=("verdana", 20), command=cancel_)
    cancelButton1.grid(row=1, column=1)


#===================================Return Books=================================================================
def returnBook():
    def return_():
        con = mc.connect(host="localhost", user="root", password="tiger", database="library", use_pure=True)
        cur = con.cursor()
        que1 = f"delete from issued_books where book_id='{en1.get()}'"
        que2 = f"update books set status='not issued' where book_id='{en1.get()}'"
        cur.execute(que1)
        con.commit()
        cur.execute(que2)
        con.commit()
        messagebox.showinfo("Records", "Update Done")
        cur.close()
        con.close()
        
    def returnCancel():
        tp.destroy()
    
    
    tp = Toplevel()
    tp.resizable(0,0)
    lbl1 = Label(tp, text="Return Book", font=("times 24", 40, "bold"), bg="black", fg="white")
    lbl1.pack()
    lbl2 = Label(tp, text="")
    lbl2.pack()
    frame1 = Frame(tp)
    l1 = Label(frame1, text="Book ID:   ", font=("verdana", 20), fg="black")
    l1.grid(row=0, column=0)
    en1 = Entry(frame1, bg="black", fg="white", bd=5)
    en1.grid(row=0, column=1)
    frame1.pack(side=BOTTOM)
    submitButton1 = Button(frame1, text="Return", bg="black", fg="white", font=("verdana", 20), command=return_)
    submitButton1.grid(row=1, column=0)
    cancelButton1 = Button(frame1, text="Cancel", bg="black", fg="white", font=("verdana", 20), command=returnCancel)
    cancelButton1.grid(row=1, column=1)


#==================================Issue book===========================================================================
def issueBook():
    def issue():
        con = mc.connect(host="localhost", user="root", password="tiger", database="library", use_pure=True)
        cur = con.cursor()
        cur.execute(f"select status from books where book_id='{en1.get()}'")
        for i in cur:
            if "issued" in i:
                messagebox.showerror("DANGER", "Already Issued")
            else:
                query = "insert into issued_books values(%s, %s, %s)"
                value1 = (f"{en1.get()}", f"{en2.get()}", f"{en3.get()}")
                cur.execute(query, value1)
                con.commit()       
                q = f"update books set status='issued' where book_id={en1.get()}"
                cur.execute(q)
                con.commit()
                messagebox.showinfo("Records", "Record Added")
                cur.close()
                con.close()
        
    def _cancel_():
        wi.destroy()
    
    wi = Toplevel()
    wi.resizable(0,0)
    lbl1 = Label(wi, text="Issue Book", font=("times 24", 40, "bold"), bg="black", fg="white")
    lbl1.pack()
    lbl2 = Label(wi, text="")
    lbl2.pack()
    frame1 = Frame(wi)
    l1 = Label(frame1, text="Book ID:    ", font=("verdana", 20), fg="black")
    l1.grid(row=0, column=0)
    en1 = Entry(frame1, bg="black", fg="white", bd=5)
    en1.grid(row=0, column=1)
    l2 = Label(frame1, text="Student name:", font=("verdana", 20), fg="black")
    l2.grid(row=1, column=0)
    en2 = Entry(frame1, bg="black", fg="white", bd=5)
    en2.grid(row=1, column=1)
    l3 = Label(frame1, text="Standard:   ", font=("verdana", 20), fg="black")
    l3.grid(row=2, column=0)
    en3 = Entry(frame1, bg="black", fg="white", bd=5)
    en3.grid(row=2, column=1)
    frame1.pack(side=BOTTOM)
    submitButton1 = Button(frame1, text="Issue", bg="black", fg="white", font=("verdana", 20), command=issue)
    submitButton1.grid(row=3, column=0)
    cancelButton1 = Button(frame1, text="Cancel", bg="black", fg="white", font=("verdana", 20), command=_cancel_)
    cancelButton1.grid(row=3, column=1)

#===================================main WIndow==================================================================

lbl = Label(canvas, text="Panda Enterprises", font=("verdana", 50, "bold"), bg="black", fg="white")
lbl.pack()
l = Label(root, text="")
l.pack()
btn1 = Button(canvas, text="Add Book", width=20, bd=5, bg="black", fg="white", font=("times 24", 30, "bold"), relief='sunken', command=addBooks)
btn1.pack()
btn2 = Button(canvas, text="Delete Book", width=20, bd=5, bg="black", fg="white", font=("times 24", 30, "bold"), relief='sunken', command=deleteBook)
btn2.pack()
btn3 = Button(canvas, text="View Book", width=20, bd=5, bg="black", fg="white", font=("times 24", 30, "bold"), relief='sunken', command=viewRecord)
btn3.pack()
btn4 = Button(canvas, text="Issue Book", width=20, bd=5, bg="black", fg="white", font=("times 24", 30, "bold"), relief='sunken', command=issueBook)
btn4.pack()
btn5 = Button(canvas, text="Return Book", width=20, bd=5, bg="black", fg="white", font=("times 24", 30, "bold"), relief='sunken', command=returnBook)
btn5.pack()

root.mainloop()
