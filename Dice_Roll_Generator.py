#Author: 3OOYOON

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

def roll_and_display(dice_roll):
    result = roll_die(get_die_options(dice_roll))
    result_text = f'You rolled a {dice_roll}-sided die and got: {result}'
    result_label.config(text=result_text, fg='#FFCCE5', font=my_font)
    history_listbox.insert(0, result_text)

def resize_event(event):
    outer_frame.configure(width=event.width, height=event.height)

#Create the main window
window = tk.Tk()
window.title("Dice Roll Generator")
window.configure(bg='#660033')  

# Set the window icon
window.iconbitmap("icon.ico")

#Custom font
my_font = font.Font(family='Courier', size=12, weight='bold')

#Create and configure an outer frame (border)
outer_frame = tk.Frame(window, bg='#CC0066', bd=2, relief='flat')  
outer_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
outer_frame.bind('<Configure>', resize_event)

# Create and configure an inner frame (content area)
inner_frame = tk.Frame(outer_frame, bg='#CC0066')  
inner_frame.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

# Set the column weights for centering the buttons
for col in range(12):
    inner_frame.grid_columnconfigure(col, weight=1)

# Set the row weights for centering the buttons vertically
inner_frame.grid_rowconfigure(1, weight=1)

#Create and configure widgets within the frame
instruction_label = tk.Label(inner_frame, text='You can roll 4, 6, 8, 10, 12, and 20-sided dice.', bg='#CC0066', fg='#FFCCE5', font=my_font)
instruction_label.grid(row=0, column=0, columnspan=11, pady=10, sticky='nsew')  # Set columnspan to 11

button_4 = tk.Button(inner_frame, text='4', command=lambda: roll_and_display(4), bg='#660033', fg='#FFCCE5', relief='flat', font=my_font, width=3, padx=5)
button_4.grid(row=1, column=3, pady=1)

button_6 = tk.Button(inner_frame, text='6', command=lambda: roll_and_display(6), bg='#660033', fg='#FFCCE5', relief='flat', font=my_font, width=3, padx=5)
button_6.grid(row=1, column=4, pady=1)

button_8 = tk.Button(inner_frame, text='8', command=lambda: roll_and_display(8), bg='#660033', fg='#FFCCE5', relief='flat', font=my_font, width=3, padx=5)
button_8.grid(row=1, column=5, pady=1)

button_10 = tk.Button(inner_frame, text='10', command=lambda: roll_and_display(10), bg='#660033', fg='#FFCCE5', relief='flat', font=my_font, width=3, padx=5)
button_10.grid(row=1, column=6, pady=1)

button_12 = tk.Button(inner_frame, text='12', command=lambda: roll_and_display(12), bg='#660033', fg='#FFCCE5', relief='flat', font=my_font, width=3, padx=5)
button_12.grid(row=1, column=7, pady=1)

button_20 = tk.Button(inner_frame, text='20', command=lambda: roll_and_display(20), bg='#660033', fg='#FFCCE5', relief='flat', font=my_font, width=3, padx=5)
button_20.grid(row=1, column=8, pady=1)

# Result label
result_label = tk.Label(inner_frame, text='', bg='#CC0066', fg='#FFCCE5', font=my_font)
result_label.grid(row=2, column=0, columnspan=11, pady=10, sticky='nsew')

# History Section
history_label = tk.Label(inner_frame, text='Roll History:', bg='#CC0066', fg='#FFCCE5', font=my_font)
history_label.grid(row=4, column=0, columnspan=11, pady=10, sticky='nsew')

history_listbox = tk.Listbox(inner_frame, bg='#660033', fg='#FFCCE5', font=my_font, selectbackground='#CC0066')
history_listbox.grid(row=4, column=0, columnspan=11, pady=5, padx=5, sticky='nsew')

# Scrollbar for history_listbox
history_scrollbar = tk.Scrollbar(inner_frame, command=history_listbox.yview, bg='#CC0066', troughcolor='#660033')
history_scrollbar.grid(row=4, column=11, pady=5, sticky='nsew')
history_listbox.config(yscrollcommand=history_scrollbar.set)

# Use grid_rowconfigure and grid_columnconfigure to make the Listbox expand with the window
inner_frame.grid_rowconfigure(4, weight=1)  # Expand vertically
inner_frame.grid_columnconfigure(0, weight=1)  # Center horizontally

# Start the main event loop
window.mainloop()