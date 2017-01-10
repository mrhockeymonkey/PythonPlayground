
import tkinter
from tkinter import ttk
from tkinter import constants

def gui():
#define and configure the window
	ms_window = tkinter.Toplevel()
	ms_window.title("Mine Sweeper - UNFINISHED")
	ms_window.columnconfigure(0, weight = 1, minsize = 600)
	ms_window.rowconfigure(0, weight = 1, minsize = 300)

	#define and configure the frame
	ms_frame = ttk.Frame(ms_window)
	ms_frame.grid(column = 0, row =0, sticky = constants.NSEW)


	#define all the 10x10 tiles
	for row_index in range(10):
		ms_frame.rowconfigure(row_index, weight=1)
		for col_index in range(10):
			ms_frame.columnconfigure(col_index, weight=1)
			ttk.Button(ms_frame).grid(row=row_index, column=col_index, sticky = constants.NSEW)  

if __name__ == '__main__':
	gui()



