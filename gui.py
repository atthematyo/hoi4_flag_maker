from tkinter import Tk, ttk, StringVar, Label, Entry, HORIZONTAL, filedialog, messagebox
from tkinter.ttk import Progressbar
import os
import threading

from flags import make_flags


gui = Tk()
gui.title('HoI4 Flag Maker')


gui.iconbitmap('flag.ico')
gui.resizable(False, False)


def make_many_flags_gui(input_dir_: str, output_dir_: str) -> None:
    make_btn.config(state='disabled')
    files = os.listdir(input_dir_)
    count = 0
    length = len(files)
    for file in files:
        if '.png' in file:
            tag_ = file.split('.')[0]
            make_flags(f'{input_dir_}/{file}', tag_, output_dir_)
        count += 1
        number = round((count * 100) / length)
        progress['value'] = number
    make_btn.config(state='normal')


def get_dir_path_input():
    dir_selected = filedialog.askdirectory()
    input_dir.set(dir_selected)


def get_dir_path_output():
    dir_selected = filedialog.askdirectory()
    output_dir.set(dir_selected)


def make_flags_btn():
    input_folder = input_dir.get()
    output_folder = output_dir.get()

    if not os.path.isdir(input_folder):
        messagebox.showerror("Error", "Input directory is not a valid directory")
        return
    if not os.path.isdir(output_folder):
        messagebox.showerror("Error", "Output directory is not a valid directory")
        return
    if not input_folder != output_folder:
        messagebox.showerror("Error", "Input directory and Output directory can not be the same directory")
        return
    x = threading.Thread(target=make_many_flags_gui, args=(input_folder, output_folder))
    x.start()


input_dir = StringVar()
input_label = Label(gui, text="Input directory")
input_label.grid(row=0, column=0)
input_dir_entry = Entry(gui, textvariable=input_dir)
input_dir_entry.grid(row=0, column=1)
input_btn_browse = ttk.Button(gui, text="Browse", command=get_dir_path_input)
input_btn_browse.grid(row=0, column=2)

output_dir = StringVar()
output_label = Label(gui, text="Output directory")
output_label.grid(row=1, column=0)
output_dir_entryE = Entry(gui, textvariable=output_dir)
output_dir_entryE.grid(row=1, column=1)
output_btn_browse = ttk.Button(gui, text="Browse", command=get_dir_path_output)
output_btn_browse.grid(row=1, column=2)

make_btn = ttk.Button(gui, text="Make Flags", command=make_flags_btn)
make_btn.grid(row=4, column=0)

progress = Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
progress.grid(row=4, column=1)

gui.mainloop()
