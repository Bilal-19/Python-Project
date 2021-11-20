import tkinter
from tkinter import*
from tkinter import ttk,messagebox

root = Tk()

root.title("Ababeel Airline Ticket Reservation")    # Creating the title of the window
root.geometry("1200x600+100+50")      #Setting window size
root.resizable(False,False)

# Placing Image
# photo_image = PhotoImage(file="airline.png")
photo_image = PhotoImage(file="airline.png")
image_label = Label(root, image = photo_image).place(x=0,y=0,relwidth=1,relheight=1)

# Set Font
SetFont = ("Times New Roman",13)
SetMainHeading = ("Times New Roman",30,"italic","bold")

# Creating Label
title = Label(root, text = "Welcome to Ababeel Airline Ticket Reservation",font= SetMainHeading,fg="blue",bg="white").place(x=220,y=40)
tkinter.Label(root,text="Developed By: Bilal Muhammad Yousuf",font=("Times New Roman",14,"italic"),fg="blue").place(x = 800,y =560)
PassengerName = tkinter.Label(root,text="Passenger Name:",font=SetFont).place(x = 90, y=230)
CNIC = tkinter.Label(root,text="CNIC: ",font=SetFont).place(x=90, y=270)
PhoneNumber = tkinter.Label(root,text="Phone No:",font=SetFont).place(x=90, y=310)
DepartureAirport = tkinter.Label(root,text = "Departure Airport: ",font=SetFont).place(x=90,y=350)
ArrivalAirport = tkinter.Label(root,text="Arrival Airport: ",font=SetFont).place(x=620,y=350)
AirlineClass = tkinter.Label(root,text = "Class: ",font=SetFont).place(x=90,y=390)
PaymentMethod = tkinter.Label(root,text= "Payment Method: ",font=SetFont).place(x=620,y=390)

# Creating Entrybox
PassengerVar = tkinter.StringVar()
PassengerNameEntry = tkinter.Entry(root,width = 25,textvariable = PassengerVar,font=SetFont).place(x = 250, y =230)

CnicVar = tkinter.StringVar()
CnicEntry = tkinter.Entry(root,width = 15,textvariable = CnicVar,font=SetFont).place(x = 250, y=270)

ContactVar = tkinter.StringVar()
ContactEntry = tkinter.Entry(root,width=15,textvariable = ContactVar,font=SetFont).place(x = 250, y=310)

DepartureVar = tkinter.StringVar()
DepartureAirportList = ttk.Combobox(root, width = 35,textvariable = DepartureVar, state="readonly",font=SetFont)
DepartureAirportList['values'] = ('Jinnah International Airport Karachi, Pakistan',
                                  'Islamabad International Airport, Pakistan',
                                  'Dubai International Airport, UAE',
                                  'Al Maktoum International Airport, UAE',
                                  'Hamad International Airport, Doha, Qatar',
                                  'King Abdulaziz International Airport, Jeddah, Saudi Arabia',
                                  'Toronto Pearson International Airport, Canada',
                                  'Muscat International Airport, Oman',
                                  )

DepartureAirportList.current(0)
DepartureAirportList.place(x = 250, y =350)

ArrivalVar = tkinter.StringVar()
ArrivalAirportList = ttk.Combobox(root,width = 35,textvariable = ArrivalVar,state="readonly",font=SetFont)
ArrivalAirportList['values'] = ('Al Maktoum International Airport, UAE',
                                'Jinnah International Airport Karachi, Pakistan',
                                'Islamabad International Airport, Pakistan',
                                'Dubai International Airport, UAE',
                                'Hamad International Airport, Doha, Qatar',
                                'King Abdulaziz International Airport, Jeddah, Saudi Arabia',
                                'Toronto Pearson International Airport, Canada',
                                'Muscat International Airport, Oman',
                                )

ArrivalAirportList.current(0)
ArrivalAirportList.place(x = 780, y = 350)
AirlineClassList = ttk.Combobox(root,width=10,state="readonly",font=SetFont)
AirlineClassList['values'] = ('First Class','Business','Economy','Premium Economy')
AirlineClassList.current(0)
AirlineClassList.place(x = 250,y = 390)

PaymentVar = tkinter.StringVar()
PaymentMethodList = ttk.Combobox(root,width=15,textvariable = PaymentVar,state="readonly",font=SetFont)
PaymentMethodList['values'] = ('Boleto Bancario','Arabica NBD','PayPal','Visa Checkuot')
PaymentMethodList.current(0)
PaymentMethodList.place(x = 780, y = 390)

def confirm():
    '''This function store the user input into csv file'''
    passenger = PassengerVar.get()
    cnic = CnicVar.get()
    contact = ContactVar.get()
    departure = DepartureVar.get()
    arrival = ArrivalVar.get()
    payment = PaymentVar.get()

    from csv import writer
    with open("Passenger Record.csv", "w", newline="") as Record:
        csv_writer = writer(Record)
        csv_writer.writerow(["Passenger Name",
                             "CNIC",
                             "Phone No",
                             "Departure Airport",
                             "Arrival Airport",
                             "PaymentMethod"])

        csv_writer.writerow([passenger, cnic, contact, departure, arrival, payment])
    if departure == arrival:
        messagebox.showerror("Error","Departure and Arrival Location shouldn't same!!")
    elif passenger != "" and cnic != "" and contact != "" and departure != "" and arrival != "" and payment != "":
        messagebox.showinfo("Ticket Reservation","Congratulations, Your booking has been confirmed!!!")
    else:
        messagebox.showerror("Invalid Input","One of the field is empty!")

ConfirmBooking = tkinter.Button(root, text="Confirm Booking",command = confirm, font=("Times New Roman",12,"bold")).place(x = 510, y = 510)


root.mainloop()