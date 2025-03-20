import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow for resizing images

def on_enter(e, button):
    button.config(bg='#d9d9d9', relief='raised')  # Lighten the button and add raised effect

def on_leave(e, button):
    button.config(bg='#c3c3c3', relief='flat')  # Restore original color and flat style

# Load and Resize Image
image_path = r"C:\Users\amaan\Desktop\Coding\doggy.jpg"  # Ensure this is the correct path

root = tk.Tk()
root.geometry('700x500')
root.title('CyberSecurity Audit Application')

def home_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame, text='CyberSecurity Audit Application\n\nPage: 1', font=('Bold', 30))
    lb.pack()
    home_frame.pack(pady=20)

def automateservices_page():
    automateservices_frame = tk.Frame(main_frame)
    lb = tk.Label(automateservices_frame, text='automateservices Audit Application\n\nPage: 2', font=('Bold', 30))
    lb.pack()
    automateservices_frame.pack(pady=20)

def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    automateservices_indicate.config(bg='#c3c3c3')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()

options_frame = tk.Frame(root, bg='#c3c3c3')

# Load and Resize Logo
try:
    original_image = Image.open(image_path)
    resized_image = original_image.resize((95, 95), Image.LANCZOS)  # Resize to fit the sidebar
    logo_img = ImageTk.PhotoImage(resized_image)  # Convert to Tkinter-compatible format

    logo_label = tk.Label(root, image=logo_img, bg='#c3c3c3')
    logo_label.place(x=20, y=10)  # Adjust position as needed
except Exception as e:
    print(f"Error loading logo: {e}")

# Create indicators first before buttons to avoid NameError
home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=20, y=140, width=5, height=40)

automateservices_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
automateservices_indicate.place(x=20, y=200, width=5, height=40)

# Home Button
home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', relief='flat', command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=35, y=140)
home_btn.bind('<Enter>', lambda e: on_enter(e, home_btn))
home_btn.bind('<Leave>', lambda e: on_leave(e, home_btn))

# AutomateServices Button
automateservices_btn = tk.Button(options_frame, text='AUTOMATE\nSERVICES', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', relief='flat', command=lambda: indicate(automateservices_indicate, automateservices_page))
automateservices_btn.place(x=35, y=200)
automateservices_btn.bind('<Enter>', lambda e: on_enter(e, automateservices_btn))
automateservices_btn.bind('<Leave>', lambda e: on_leave(e, automateservices_btn))

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=140, height=600)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=500, width=600)

root.mainloop()
