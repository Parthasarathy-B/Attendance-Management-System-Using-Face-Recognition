import tkinter as tk
from tkinter import Image, messagebox
from PIL import Image, ImageTk

def login():
    # Get the values entered in email and password fields
    email = email_entry.get()
    password = password_entry.get()

    # Check if email and password match a valid login credentials
    if email == 'admin@gmail.com' and password == '12345':
        # Show a success message
        messagebox.showinfo('Login Successful', 'Welcome to the Application!')

        root.destroy()
        # Call a function to create the authorized access window
        import main
        main.login()
    else:
        # Show an error message for invalid credentials
        messagebox.showerror('Login Failed', 'Invalid email or password. Please try again.')

# Create the tkinter window for login
root = tk.Tk()
root.title('Login')

# Set background color
root.config(bg='gray') 

# Load and display logo image
logo_image = Image.open('/home/parthasarathy/Downloads/face_recognition/assets/logo.png')  
logo_image = logo_image.resize((150, 150))  # Resize the logo image as needed
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo)
logo_label.grid(row=0, columnspan=2, padx=10, pady=10)  # Place the logo label on top of the window



email_label = tk.Label(root, text='Email:', font=('Helvetica', 16))
email_label.grid(row=1, column=0, padx=10, pady=30, sticky='e')
email_entry = tk.Entry(root, font=('Helvetica', 16)) 
email_entry.grid(row=1, column=1, padx=10, pady=30, sticky='w')

# Create password label and entry field
password_label = tk.Label(root, text='Password:', font=('Helvetica', 16)) 
password_label.grid(row=2, column=0, padx=10, pady=30, sticky='e')
password_entry = tk.Entry(root, show='*', font=('Helvetica', 16))
password_entry.grid(row=2, column=1, padx=10, pady=30, sticky='w')

# Create login button
login_button = tk.Button(root, text='Login', command=login, font=('Helvetica', 16),height=2,width=8,background='deepskyblue') 
login_button.grid(row=3, columnspan=2, padx=10, pady=30)

root.mainloop()

