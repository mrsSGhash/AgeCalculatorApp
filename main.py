''' AGE Calculator
Source: https://www.askpython.com/python-modules/tkinter/age-calculator
Date: 22/01/2022
 '''
# Creating a custom window
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title('Age Calculator!')

# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")
 
# Labels for date, month and year
lb_date = tk.Label(window,text = "Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_month = tk.Label(window,text = "Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_year = tk.Label(window,text = "Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")

# Entry boxes for date, month and year
e_date = tk.Entry(window,width=5)
e_month = tk.Entry(window,width=5)
e_year = tk.Entry(window,width=5)

# Button to calculate age 
btn_calculate_age = tk.Button(window,text="Calculate Age!",font=("Arial",13), command='get_age')
 
# Label for text box that will display the calculated age
lb_calculated_age = tk.Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
tbox_age=tk.Text(window,width=5,height=0,state="disabled")

# Button to exit application


# Placing the elements on the screen
