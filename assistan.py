import tkinter as tk
from PIL import ImageTk, Image
from random import randint
import wikipedia


class App:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.mascot = Image.open('bbook.png')
        self.ph = ImageTk.PhotoImage(self.mascot)
        self.label = tk.Label(master, image=self.ph)
        self.label.image = self.ph
        self.entry = tk.Entry(master, width=70)
        self.response = tk.Text(master, width=60, height=5, fg='white', bg ='black')
        self.response.pack(side=tk.BOTTOM)
        self.response.insert('1.0', 'What do you need?')
        self.response.config(state='disabled')
        self.entry.bind('<Return>', self.question)
        self.entry.pack()
        self.label.pack()

    def question(self, master):
        self.changeimg(self.master)
        qtn = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        self.response.config(state='normal')
        self.response.delete('1.0', tk.END)
        if 'wikipedia' in qtn:
            topic = qtn.replace('wikipedia', '')
            try:
                summary = wikipedia.summary(topic, sentences=2)
                self.response.insert('1.0', f'{summary}')
            except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError):
                self.response.insert('1.0', "It's either not there or you need to be more specific.")
        self.response.config(state='disabled')

    def changeimg(self, master):
        image_list = ['bbook.png', 'bbird.png', 'bfood.png', 'bpass.png']
        counter = randint(0, 3)
        self.label.destroy()
        self.mascot = Image.open(image_list[counter])
        self.ph = ImageTk.PhotoImage(self.mascot)
        self.label = tk.Label(master, image=self.ph)
        self.label.image = self.ph
        self.label.pack()







def run_app():
    root = tk.Tk()
    window = App(root)
    root.resizable(False, False)
    root.mainloop()

run_app()







