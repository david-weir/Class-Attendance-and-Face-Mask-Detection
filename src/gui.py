import tkinter as tk
from tkinter import ttk, Canvas, PhotoImage
from tkinter.messagebox import showerror, showwarning, showinfo
from ctypes import windll
from PIL import ImageTk, Image
from webcamrecognition import live_attendance
from dataset_generator import generate
from feature_extract import extract

# fix text bluriness on Windows
windll.shcore.SetProcessDpiAwareness(1)

# window title
root = tk.Tk()
root.title('Class Attendance and Face Mask Detectection')

# set window size
window_width = 1200
window_height = 800

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# set window icon
root.iconbitmap('../src/icon/face_mask.ico')

# create canvas
canvas = Canvas(root, width=400, height=400)
canvas.pack(fill="both", expand=True)

# set window background
bg = ImageTk.PhotoImage(Image.open('../src/background/masks.jpg'))  # PIL solution
canvas.create_image(0, 0, anchor="nw", image=bg)

# create header label
heading = tk.Label(root,
                   text="CA326:\n"
                        "Third Year Project: Class Attendance using\n"
                        "Facial Recognition and Mask Detection",
                   font=("Arial", 22),
                   bg="white")

# set the position of label
heading.place(relx=0.5, rely=0.1, anchor='center')

# set welcome intro label
message = tk.Label(root,
                   text="Welcome to the user interface of our 3rd Year Project\n"
                        "Use the available commands below or see the user manual\n"
                        "\n"
                        "Students:\n"
                        "David Weir (19433086)\n"
                        "Cian Mullarkey (19763555)\n",
                   font=("Arial", 12),
                   bg="white")

message.place(relx=0.5, rely=0.4, anchor='center')

# calls feature extract program
def feat_ext():
    print("Extracting Features")
    extract()
    print("Extracted facial features successfully")

# calls webcam recognition program
def attend():
    live_attendance()

# def user_manual():

def data_gen():
    # declaring string variables for storing fname and lname
    first_name_var = tk.StringVar()
    last_name_var = tk.StringVar()

    # defining a function that will get the fname and lname from the user and pass them as
    # parameters through to the dataset generator function
    def submit():
        first_name = first_name_var.get()
        last_name = last_name_var.get()

        if len(first_name) == 0 or len(last_name) == 0:
            showerror(title='Error', message='A first and second name must be entered.')
        else:
            print("The dataset is called : " + first_name + " " + last_name)
            print("Generating dataset")
            generate(first_name, last_name)
            print("Dataset generated")

            first_name_var.set("")
            last_name_var.set("")

    # !!!!! CLICLKING GENERATE BUTTON SHOWS/HIDES TEXT PROMPT !!!!!!!

    # create labels and entries for fname and lname
    first_name_label = tk.Label(root, text='First Name', font=('calibre', 10, 'bold'))
    first_name_label.place(relx=0.4, rely=0.85, anchor='center')

    first_name_entry = tk.Entry(root, textvariable=first_name_var, font=('calibre', 10, 'normal'))
    first_name_entry.place(relx=0.6, rely=0.85, anchor='center')

    last_name_label = tk.Label(root, text='Last Name', font=('calibre', 10, 'bold'))
    last_name_label.place(relx=0.4, rely=0.9, anchor='center')

    last_name_entry = tk.Entry(root, textvariable=last_name_var, font=('calibre', 10, 'normal'))
    last_name_entry.place(relx=0.6, rely=0.9, anchor='center')

    # submit button
    sub_btn = tk.Button(root, text='Submit', command=submit)
    sub_btn.place(relx=0.5, rely=0.95, anchor='center')

attend_button = ttk.Button(root, text='Attendance', command=attend)
attend_button.place(relx=0.5, rely=0.6, anchor='center')

extract_button = ttk.Button(root, text='Extract Features', command=feat_ext)
extract_button.place(relx=0.5, rely=0.7, anchor='center')

data_button = ttk.Button(root, text='Generate Dataset', command=data_gen)
data_button.place(relx=0.5, rely=0.8, anchor='center')

usrman_button = ttk.Button(root, text='User Manual', command=data_gen)
usrman_button.place(relx=1.0, rely=1.0, anchor='se')

root.mainloop()
