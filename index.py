import tkinter as tk
from tkinter.filedialog import asksaveasfilename

def save():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = Editor.get(1.0, tk.END)
        output_file.write(text)
    root.title(f"Text Editor - {filepath}")

root = tk.Tk()
root.geometry('600x600')
root.title('Text Editor by Rushi')

# Scrollbar
sc = tk.Scrollbar(root)
sc.pack(side=tk.RIGHT, fill=tk.Y)

# Text Editor
Editor = tk.Text(root, width=550, height=500, yscrollcommand=sc.set)
Editor.pack(fill=tk.BOTH)
sc.config(command=Editor.yview)

# Save Button
btn = tk.Button(root, text='Save', font=('normal', 10), command=save, bg='green')
btn.place(x=600, y=600)  # Adjusted position to fit within the window

root.mainloop()
