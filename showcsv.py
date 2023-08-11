import pandas as pd
import tkinter as tk
from tkinter import ttk


def display(file,title):
    root = tk.Tk()
    root.title(title)
    root.geometry("1200x1000")
    def display_csv(file_path):
        df = pd.read_csv(file_path)
        columns = list(df.columns)
        rows = df.values.tolist()
        
        treeview = ttk.Treeview(root, columns=columns, show="headings",height=len(rows)+1)
        for col in columns:
            treeview.heading(col, text=col)
        for row in rows:
            treeview.insert("", "end", values=row)
        treeview.pack()

    file_path = file
    display_csv(file_path)

    root.mainloop()
    




