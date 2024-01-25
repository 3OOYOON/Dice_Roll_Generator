#Author : 3OOYOON

import tkinter as tk
from tkinter import messagebox
from tkinter import font

import random

def roll_die(die_options):
    return random.choice(die_options)

def get_die_options(dice_roll):
    return {
        4: ['1', '2', '3', '4'],
        6: ['1', '2', '3', '4', '5', '6'],
        8: ['1', '2', '3', '4', '5', '6', '7', '8'],
        10: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        12: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
        20: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    }[dice_roll]

def roll_and_display():
    result = roll_die(get_die_options(dice_var.get()))
    result_text = f'You rolled a {dice_var.get()}-sided die and got: {result}'
    result_label.config(text=result_text, fg='#FFCCE5', font=my_font)
    history_listbox.insert(0, result_text)  # Add the result to the history

def resize_event(event):
    outer_frame.configure(width=event.width, height=event.height)

#Create the main window
window = tk.Tk()
window.title("Dice Roll Generator")
window.configure(bg='#660033')  

#Custom font
my_font = font.Font(family='Courier', size=12, weight='bold')

#Create and configure an outer frame (border)
outer_frame = tk.Frame(window, bg='#CC0066', bd=2, relief='flat')  
outer_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
outer_frame.bind('<Configure>', resize_event)

#Create and configure an inner frame (content area)
inner_frame = tk.Frame(outer_frame, bg='#CC0066')  
inner_frame.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

#Create and configure widgets within the frame
instruction_label = tk.Label(inner_frame, text='You can roll 4, 6, 8, 10, 12, and 20-sided dice.', bg='#CC0066', fg='#FFCCE5', font=my_font)
instruction_label.grid(row=0, column=0, pady=10)

dice_var = tk.IntVar()
dice_var.set(6)  # Default to 6-sided die
dice_entry = tk.Entry(inner_frame, textvariable=dice_var, width=5)
dice_entry.grid(row=1, column=0, pady=5)

roll_button = tk.Button(inner_frame, text="Roll", command=roll_and_display, bg='#660033', fg='#FFCCE5', relief='flat', font=my_font)
roll_button.grid(row=2, column=0, pady=10)

result_label = tk.Label(inner_frame, text='', bg='#CC0066', fg='#FFCCE5', font=my_font)
result_label.grid(row=3, column=0, pady=10)

#History Section
history_label = tk.Label(inner_frame, text='Roll History:', bg='#CC0066', fg='#FFCCE5', font=my_font)
history_label.grid(row=4, column=0, pady=10)

history_listbox = tk.Listbox(inner_frame, bg='#660033', fg='#FFCCE5', font=my_font, selectbackground='#CC0066')
history_listbox.grid(row=5, column=0, pady=5, padx=5, sticky='nsew')

#Scrollbar for history_listbox
history_scrollbar = tk.Scrollbar(inner_frame, command=history_listbox.yview, bg='#CC0066', troughcolor='#660033')
history_scrollbar.grid(row=5, column=1, pady=5, sticky='nsew')
history_listbox.config(yscrollcommand=history_scrollbar.set)

#Use grid_rowconfigure and grid_columnconfigure to make the Listbox expand with the window
inner_frame.grid_rowconfigure(5, weight=1)
inner_frame.grid_columnconfigure(0, weight=1)

#Start the main event loop
window.mainloop()