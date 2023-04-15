import tkinter as tk
from tkinter import NW, W, Canvas, filedialog
import csv
from PIL import Image, ImageTk

def register():  
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()


        def create_widgets(self):
            self.heading_label = tk.Label(canvas, text="Student Registration", font=("Helvetica", 24), bg='lime')
            self.heading_label.grid(row=0, column=0, columnspan=5, padx=10, pady=5)

            # Create labels and Entry widgets for the student details   
            self.reg_no_label = tk.Label(canvas, text="Register Number:",bg='white', font=('Helvetica', 15) )
            self.reg_no_label.grid(row=1, column=0, padx=10, pady=15, sticky=W)
            self.reg_no_entry = tk.Entry(canvas,bg='white', font=('Helvetica', 15))
            self.reg_no_entry.grid(row=1, column=1, padx=10, pady=15)

            self.name_label = tk.Label(canvas, text="Name:",bg='white', font=('Helvetica', 15))
            self.name_label.grid(row=2, column=0, padx=10, pady=15, sticky=W)
            self.name_entry = tk.Entry(canvas,bg='white', font=('Helvetica', 15))
            self.name_entry.grid(row=2, column=1, padx=10, pady=15)

            self.dep_label = tk.Label(canvas, text="Department:",bg='white', font=('Helvetica', 15))
            self.dep_label.grid(row=3, column=0, padx=10, pady=15, sticky=W)
            self.dep_entry = tk.Entry(canvas,bg='white', font=('Helvetica', 15))
            self.dep_entry.grid(row=3, column=1, padx=10, pady=15)
            
            self.year_label = tk.Label(canvas, text="Year:",bg='white', font=('Helvetica', 15))
            self.year_label.grid(row=4, column=0, padx=10, pady=15, sticky=W)
            self.year_entry = tk.Entry(canvas,bg='white', font=('Helvetica', 15))
            self.year_entry.grid(row=4, column=1, padx=10, pady=15)

            self.section_label = tk.Label(canvas, text="Section:",bg='white', font=('Helvetica', 15))
            self.section_label.grid(row=5, column=0, padx=10, pady=15, sticky=W)
            self.section_entry = tk.Entry(canvas,bg='white', font=('Helvetica', 15))
            self.section_entry.grid(row=5, column=1, padx=10, pady=5)


            # Create a button to browse for the image file
            self.browse_button = tk.Button(canvas, text="Select Image", command=self.browse_image,bg='#0047d4')
            self.browse_button.grid(row=6, column=0, padx=10, pady=10)
            
            # Create a label to display the selected image
            self.image_label = tk.Label(canvas)
            self.image_label.grid(row=6, column=1, columnspan=2, padx=10, pady=5)
            
            # Create a button to submit the form
            self.submit_button = tk.Button(canvas, text="Add", command=self.submit_form,bg='#00d451', height=2, width=10)
            self.submit_button.grid(row=8, column=0, columnspan=2, padx=10, pady=20)
            
        def browse_image(self):
            global filepath
            # Browse for an image file and display it in the image_label widget
            initialdir = "/home/parthasarathy/Downloads/face_recognition/temp/"
            filetypes = [("Image files", "*.*")]
            filepath = filedialog.askopenfilename(initialdir=initialdir,filetypes=filetypes)
            if filepath:
                image = Image.open(filepath)
                image = image.resize((180, 220), Image.ANTIALIAS)
                self.photo = ImageTk.PhotoImage(image)
                self.image_label.configure(image=self.photo)
            
        def submit_form(self):
            global filepath
            # Get the student details and image file path
            reg_no = self.reg_no_entry.get()
            name = self.name_entry.get()
            dep_name = self.dep_entry.get()
            year_name = self.year_entry.get()
            section = self.section_entry.get()

            # Save the student details to a CSV file
            with open("Database.csv", mode="a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([reg_no, name, dep_name, year_name, section, "/home/parthasarathy/Downloads/face_recognition/images/"+f"{reg_no}_{name}.jpg"])

            # Save the image file to a specific directory with a specific file name
            if filepath:
                image = Image.open(filepath)
                filename = f"{reg_no}_{name}.jpg"
                filepath = f"/home/parthasarathy/Downloads/face_recognition/images/{filename}"
                image.save(filepath)
                encode_flag = True

            # Display the student details and image
            image = Image.open(filepath)
            root.destroy()
            tk.Tk.destroy()
                
    root = tk.Toplevel()
    root.title('Student Registration')
    
    canvas = Canvas(root, width=400, height=600)
    canvas.pack()

    app = Application(master=root)
    root.configure(bg="black")
    canvas.configure(bg="gray")

    app.mainloop()


