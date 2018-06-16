import tkinter
from tkinter import filedialog, ttk, scrolledtext
from pathlib import Path
import customnotebook
import time
import _thread
import os

MASTER_TITLE = 'Real Time File Logger'

class rtfilelogger:
    def __init__(self, master):
        master.minsize(width=1000, height=666)
        master.title(MASTER_TITLE)
        self.master = master
        self.mainframe = tkinter.Frame(self.master)
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)
        self.build_grid()
        self.build_buttons()
        self.create_notebook()
        self.monitoredfiles = []
        self.pause = {}
        self.selected_index = tkinter.IntVar()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_buttons(self):
        self.add_filebtn = tkinter.Button(
            self.mainframe,
            text='Add New File',
            command=self.add_file
        )
        self.add_filebtn.grid(row=0, column=0,padx=(10, 10), pady=(10, 0), sticky="nsew")
        #self.add_filebtn.config(highlightbackground='blue',highlightthickness=10)
        self.play_resumebtn = tkinter.Button(
            self.mainframe,
            text='Play/Pause',
            command=self.play_resume
        )
        #self.play_resumebtn.config(highlightbackground='blue',highlightthickness=10)
        self.play_resumebtn.grid(row=2, column=0,padx=(10, 10), pady=(0, 10), sticky="nsew")

    def create_notebook(self):
        self.nb = customnotebook.CustomNotebook(self.mainframe)
        self.nb.grid(row=1, column=0, sticky='nsew',
                     padx=(10, 10), pady=(5, 5))
        self.nb.set_close_action(self.close_tab)
        self.nb.set_select_action(self.select_tab)

    def add_file(self):
        key = filedialog.askopenfilename()
        page = ttk.Frame(self.nb)
        page.columnconfigure(0, weight=1)
        page.rowconfigure(0, weight=1)
        text = scrolledtext.ScrolledText(page)
        text.config(state=tkinter.DISABLED)
        if key == '':
            return
        f = open(key, 'r+')
        self.pause[len(self.monitoredfiles)] = tkinter.IntVar()
        _thread.start_new_thread(tail,(text,f,key,self.pause[len(self.monitoredfiles)]))   
        text.grid(column=0,row=0,sticky="nsew")
        keyname = key[key.rfind('/')+1:]
        self.nb.add(page,text=keyname)
        self.nb.select(page)
        self.monitoredfiles.append(f)
        self.select_tab(len(self.monitoredfiles)-1)


    def close_tab(self,element):
        f = self.monitoredfiles[element]
        f.close()
        del self.monitoredfiles[element]

    def select_tab(self,element):
        self.selected_index.set(element)

    def play_resume(self):
        p = self.pause[self.selected_index.get()]
        if p.get():
            p.set(False)
        else:
            p.set(True)


def tail(text,f,name,pause):
    content = f.read()
    add_line(text,content)
    initial_size = os.path.getsize(name)
    while not f.closed:
        if pause.get():
            time.sleep(2)
            continue
        line = f.readline()
        if not line:
            time.sleep(1)    # Sleep briefly for 1sec
            if os.path.getsize(name) < initial_size:
                f.seek(0)
                initial_size = os.path.getsize(name) 
            continue
        add_line(text,line)


def add_line(text,data):
    text.config(state=tkinter.NORMAL)
    text.insert(tkinter.INSERT,data)
    text.see(tkinter.END)
    text.config(state=tkinter.DISABLED)


if __name__ == '__main__':
    root = tkinter.Tk()
    logger = rtfilelogger(root)
    root.mainloop()
    for file in logger.monitoredfiles:
        file.close()
    print('Closing The Program')
