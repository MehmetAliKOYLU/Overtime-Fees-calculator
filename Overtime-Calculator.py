import tkinter as tk
from tkinter import *


class OvertimeFeeCalculator(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,)
        self.master = master
        self.pack()
        self.create_widgets()



    def create_widgets(self):
        # Create a radio button group for selecting the overtime rate
        self.overtime_rate_var = tk.StringVar(value="2x")
        self.overtime_rate_frame = tk.Frame(self)
        self.overtime_rate_frame.pack(side="top",pady=10)
        tk.Label(self.overtime_rate_frame, text="Overtime Fee",font='Verdana 12 bold').pack(side="top")
        tk.Radiobutton(self.overtime_rate_frame, text="2x   ", variable=self.overtime_rate_var,indicatoron=2,borderwidth=2,selectcolor="white",width="10",fg="black",font=12, value="2x").pack(side="left")
        tk.Radiobutton(self.overtime_rate_frame, text=" 1.5x", variable=self.overtime_rate_var,indicatoron=2,borderwidth=2,selectcolor="white",fg="black",font=12, value="1.5x").pack(side="left",padx=20)

        # Create a label for the instructions
        label = tk.Label(self, text="How Many Hours Worked",font='Verdana 12 bold',width=40,height=4,)
        label.pack()

        # Create an entry box for the hours worked
        self.hours_entry = tk.Entry(self,bg=('#b5b5b5'),font='bold')
        self.hours_entry.pack()

        # Create a label for the instructions
        label = tk.Label(self, text="Salary Value",font='Verdana 12 bold',height=4,)
        label.pack()

        # Create an entry box for the overtime rate
        self.rate_entry = tk.Entry(self,bg=('#b5b5b5'),font='bold')
        self.rate_entry.pack()

        # Create a button to calculate the overtime fees
        button = tk.Button(self, text="Calculate", command=self.calculate,bg=('#000000'),fg=('#ffffff'))
        button.pack(pady=17)

        # Create a label to display the overtime fees
        self.result_label = tk.Label(self)
        self.result_label.pack()
        self.result_label2 = tk.Label(self)
        self.result_label2.pack()

    def calculate(self):
        # Get the number of hours worked from the entry box
        hours_worked = float(self.hours_entry.get())

        # Get the overtime rate from the entry box and the selected option
        overtime_rate = float(self.rate_entry.get())
        maas=overtime_rate
        overtime_rate = overtime_rate/30
        overtime_rate = (overtime_rate/8)
        if self.overtime_rate_var.get() == "2x":
            overtime_rate *= 2
        elif self.overtime_rate_var.get() == "1.5x":
            overtime_rate *= 1.5

        # Calculate the overtime fee
        if hours_worked > 45:
            overtime_hours = hours_worked - 45
            overtime_fee = overtime_hours * overtime_rate
        else:
            overtime_fee = 0
        total = overtime_fee + (maas)
        
        
        # Display the overtime fee
        #ekrana yazdırılması
        self.result_label.config(text=" Overtime Pay: €{:.2f}".format(overtime_fee),font='Tahoma 14 bold')
        self.result_label.pack(pady=21)
        self.result_label2.config(text=" The Total Fee He will Receive: €{:.2f}".format(total),font='Tahoma 14 bold')
        self.result_label2.pack(pady=25)

# Example usage
root = tk.Tk()
calculator_frame = OvertimeFeeCalculator(root)
calculator_frame.mainloop()

