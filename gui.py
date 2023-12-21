from tkinter import Tk, ttk, StringVar, Label, Entry, HORIZONTAL, filedialog, messagebox, IntVar, TclError
from tkinter.ttk import Progressbar
import os
import threading

from flags import make_flags

gui = Tk()
gui.title('HoI4 Flag Maker')

gui.iconbitmap('flag.ico')
gui.resizable(False, False)


def make_many_flags_gui(input_dir_: str, output_dir_: str, large_width: int, large_height: int, medium_width: int,
                        medium_height: int, small_width: int, small_height: int) -> None:
    make_btn.config(state='disabled')
    files = os.listdir(input_dir_)
    count = 0
    length = len(files)
    for file in files:
        if '.png' in file:
            tag_ = file.split('.')[0]
            make_flags(f'{input_dir_}/{file}', tag_, output_dir_, large_width, large_height, medium_width,
                       medium_height, small_width, small_height)
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


def clean_integer_input(integer_input: int) -> int:
    absolute = abs(integer_input)
    if absolute >= 1:
        return absolute
    else:
        return 1


def make_flags_btn():
    input_folder = input_dir.get()
    output_folder = output_dir.get()

    try:
        large_width = clean_integer_input(large_wid.get())
        large_height = clean_integer_input(large_hei.get())
        medium_width = clean_integer_input(medium_wid.get())
        medium_height = clean_integer_input(medium_hei.get())
        small_width = clean_integer_input(small_wid.get())
        small_height = clean_integer_input(small_hei.get())
    except TclError as e:
        messagebox.showerror("Error", str(e))
        return

    large_wid.set(large_width)
    large_hei.set(large_height)
    medium_wid.set(medium_width)
    medium_hei.set(medium_height)
    small_wid.set(small_width)
    small_hei.set(small_height)

    if not os.path.isdir(input_folder):
        messagebox.showerror("Error", "Input directory is not a valid directory")
        return
    if not os.path.isdir(output_folder):
        messagebox.showerror("Error", "Output directory is not a valid directory")
        return
    if not input_folder != output_folder:
        messagebox.showerror("Error", "Input directory and Output directory can not be the same directory")
        return
    x = threading.Thread(target=make_many_flags_gui, args=(input_folder, output_folder, large_width, large_height,
                                                           medium_width, medium_height, small_width, small_height))
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

large_wid = IntVar(value=82)
large_width_label = Label(gui, text="Large width")
large_width_label.grid(row=2, column=0)
large_width_entryE = Entry(gui, textvariable=large_wid)
large_width_entryE.grid(row=2, column=1)

large_hei = IntVar(value=52)
large_height_label = Label(gui, text="Large height")
large_height_label.grid(row=3, column=0)
large_height_entryE = Entry(gui, textvariable=large_hei)
large_height_entryE.grid(row=3, column=1)

medium_wid = IntVar(value=41)
medium_width_label = Label(gui, text="Medium width")
medium_width_label.grid(row=4, column=0)
medium_width_entryE = Entry(gui, textvariable=medium_wid)
medium_width_entryE.grid(row=4, column=1)

medium_hei = IntVar(value=26)
medium_height_label = Label(gui, text="Medium height")
medium_height_label.grid(row=5, column=0)
medium_height_entryE = Entry(gui, textvariable=medium_hei)
medium_height_entryE.grid(row=5, column=1)

small_wid = IntVar(value=10)
small_width_label = Label(gui, text="Small width")
small_width_label.grid(row=6, column=0)
small_width_entryE = Entry(gui, textvariable=small_wid)
small_width_entryE.grid(row=6, column=1)

small_hei = IntVar(value=7)
small_height_label = Label(gui, text="Small height")
small_height_label.grid(row=7, column=0)
small_height_entryE = Entry(gui, textvariable=small_hei)
small_height_entryE.grid(row=7, column=1)

make_btn = ttk.Button(gui, text="Make Flags", command=make_flags_btn)
make_btn.grid(row=8, column=0)

progress = Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
progress.grid(row=8, column=1)

gui.mainloop()
