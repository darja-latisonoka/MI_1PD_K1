# Source - https://stackoverflow.com/a/63781176
# Posted by OysterShucker, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-03, License - CC BY-SA 4.0

import time
import tkinter as tk

root = tk.Tk()
root.geometry('150x100')

def countdown_clock(s, t):
    if not s:
        t.configure(text='time!')
        return
    
    t.configure(text=s)
    root.after(1000, countdown_clock, s-1, t)
    


time_lbl     = tk.Label(root, text='00', font=20)
time_lbl.grid()

start_btn    = tk.Button(root, text='start', command=lambda: countdown_clock(int(seconds_ent.get()), time_lbl))
start_btn.grid()

seconds_ent  = tk.Entry(root)
seconds_ent.grid()

root.mainloop()
