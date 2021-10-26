from tkinter import *


window = Tk()
window.geometry('500x500')
window.title("Food Deliveries")
window.configure(background="gray")
frame0 = Frame(window, bg="gray")
frame1 = Frame(window, bg="gray")
frame2 = Frame(window, bg="gray")
frame3 = Frame(window, bg="gray")

#next button
def frame_one():
    frame0.pack_forget()
    frame1.pack(fill=BOTH, expand=True)

def frame_two():
    frame0.pack_forget()
    frame2.pack(fill=BOTH, expand=True)

def frame_three():
    frame0.pack_forget()
    frame3.pack(fill=BOTH, expand=True)

def one_zero():
    frame1.pack_forget()
    frame0.pack(fill=BOTH, expand=True)

def two_zero():
    frame2.pack_forget()
    frame0.pack(fill=BOTH, expand=True)

def three_zero():
    frame3.pack_forget()
    frame0.pack(fill=BOTH, expand=True)

def submit_inventory():
    pass
    #double_check_label = Label(frame1, text)
    #double_check_button = Button(frame1,)

#Food Deliveries label
f0l1 = Label(frame0, text="Windham Community Foodbank", bg="gray", fg="black", font="Helvetica 16 bold", anchor="center")
f0l1.pack(pady=20)

'''Family labels
class family_label: #add dietary restrictions and preferences, and calculate those within class to generate food order
    def __init__(self, name, address, size, produce, groceries):
        self.name = name
        self.address = address
        self.size = size
        self.produce = produce
        self.groceries = groceries

    def name_label(self, window=window, bg="gray", fg="navy", font="Helvetica 12 bold", anchor="left"):
        Label(window, text="{} Family, {}, {} members".format(self.name, self.address, self.size), bg=bg, fg=fg, font=font, anchor=anchor)
    
    def produce_label(self, window=window, bg="gray", fg="navy", font="Helvetica 10", anchor="left"):
        pass
'''
# buttons
f1b = Button(frame0, text="Update Inventory", font="Helvetica 10", width=20, command=frame_one)
f1b.pack(pady=20)

f2b = Button(frame0, text="Create Delivery", font="Helvetica 10", width=20, command=frame_two)
f2b.pack(pady=20)

f3b = Button(frame0, text="Customer Settings", font="Helvetica 10", width=20, command=frame_three)
f3b.pack(pady=20)

#FRAME 1
f1l1 = Label(frame1, text="Update Inventory", bg="gray", fg="black", font="Helvetica 16 bold", anchor="center")
f1l1.pack(pady=20)

#frame 1 questions
food_list = ["apples", "peaches", "peanut butter"]
item=StringVar()
item.set(food_list[0])
count=IntVar()
modifier=StringVar()
modifier.set("add")

def confirm_submit():
    subWindow = Tk()
    if count.get() == 1 and item.get()[-1] == "s":
        item_text = item.get()[:-1]
    else:
        item_text = item.get()
    if modifier.get() == "remove":
        mod_text = "from"
    else:
        mod_text = "to"
    subLabel = Label(subWindow, text="You have chosen to {} {} {} {} inventory.".format(modifier.get(), count.get(), item_text, mod_text), font="Helvetica 10 bold", anchor="center")
    subLabel.pack(pady=20)

    def send_info():
        print("Action: {}\nItem: {}\nCount: {}".format(modifier.get(), item.get(), count.get()))
        subWindow.destroy()
        confWindow = Tk()
        confLabel = Label(confWindow, text="You have successfully updated the inventory!", font="Helvetica 10 bold", anchor="center")
        confLabel.pack(pady=20)

    confirm = Button(subWindow, text="confirm", font="none 10", width=10, command=send_info, anchor="center")
    confirm.pack(pady=20)

f1l2 = Label(frame1, text="Grocery Item:", bg="gray", fg="black", font="Helvetica 10 bold", anchor="center")
f1l2.pack(pady=10)

f1q1 = OptionMenu(frame1, item, *food_list)
f1q1.pack(pady=10)

f1l3 = Label(frame1, text="Quantity:", font="Helvetica 10 bold", bg="gray", fg="black", anchor="center")
f1l3.pack(pady=10)

f1q2 = Spinbox(frame1, textvariable=count, from_=1, to=100)
f1q2.pack(pady=10)

f1q3b1 = Radiobutton(frame1, text="Add", variable=modifier, value="add", bg="gray", font="Helvetica 10 bold")
f1q3b1.pack(pady=10)

f1q3b2 = Radiobutton(frame1, text="Remove", variable=modifier, value="remove", bg="gray", font="Helvetica 10 bold")
f1q3b2.pack(pady=0)

f1_submit = Button(frame1, text="Submit", font="none 10", width=10, command=confirm_submit)
f1_submit.pack(pady=20)

h1b = Button(frame1, text="home", font="none 10", width=10, command=one_zero)
h1b.pack(side=BOTTOM)

#FRAME 2
f2l1 = Label(frame2, text="Create Delivery", bg="gray", fg="black", font="Helvetica 16 bold", anchor="center")
f2l1.pack(pady=20)

h2b = Button(frame2, text="home", font="none 10", width=10, command=two_zero)
h2b.pack(side=BOTTOM)

#frame 3
f3l1 = Label(frame3, text="Customer Settings", bg="gray", fg="black", font="Helvetica 16 bold", anchor="center")
f3l1.pack(pady=20)

h3b = Button(frame3, text="home", font="none 10", width=10, command=three_zero)
h3b.pack(side=BOTTOM)

def close_window():
    window.destroy()
    exit()

frame0.pack(fill=BOTH, expand=True)

#home_button = Button(window, text="home", font="none 10", width=10, command=home)
#home_button.pack(side=LEFT)
#exit_button = Button(window, text="exit", font="none 10", width=10, command=close_window)
#exit_button.pack()
window.mainloop()

