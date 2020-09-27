import sys

    try:
        import Tkinter as tk
    except ImportError:
        import tkinter as tk

    try:
        import ttk
        py3 = False
    except ImportError:
        import tkinter.ttk as ttk
        py3 = True

    import medicine_support

    def vp_start_gui():
        '''Starting point when module is the main routine.'''
        global val, w, root
        root = tk.Tk()
        top = Toplevel1 (root)
        medicine_support.init(root, top)
        root.mainloop()

    w = None
    def create_Toplevel1(rt, *args, **kwargs):
        global w, w_win, root
        #rt = root
        root = rt
        w = tk.Toplevel (root)
        top = Toplevel1 (w)
        medicine_support.init(w, top, *args, **kwargs)
        return (w, top)

    def destroy_Toplevel1():
        global w
        w.destroy()
        w = None

    class Toplevel1:
        def __init__(self, top=None):
            #populates top level window
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana1color = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'

            top.geometry("675x741+650+119")
            top.minsize(148, 1)
            top.maxsize(1924, 1055)
            top.resizable(1, 1)
            top.title("Medicine data")
            top.configure(background="#d9d9d9")

            self.Frame1 = tk.Frame(top)
            self.Frame1.place(relx=0.044, rely=0.027, relheight=0.476
                    , relwidth=0.923)
            self.Frame1.configure(relief='groove')
            self.Frame1.configure(borderwidth="2")
            self.Frame1.configure(relief="groove")
            self.Frame1.configure(background="#d9d9d9")

            self.Label1 = tk.Label(self.Frame1)
            self.Label1.place(relx=0.075, rely=0.091, height=39, width=130)
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(text='''Brand''')

            self.Label2 = tk.Label(self.Frame1)
            self.Label2.place(relx=0.093, rely=0.275, height=29, width=108)
            self.Label2.configure(background="#d9d9d9")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(foreground="#000000")
            self.Label2.configure(text='''Product''')

            self.Label3 = tk.Label(self.Frame1)
            self.Label3.place(relx=0.112, rely=0.428, height=29, width=84)
            self.Label3.configure(background="#d9d9d9")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(text='''quantity''')

            self.Label4 = tk.Label(self.Frame1)
            self.Label4.place(relx=0.112, rely=0.584, height=28, width=85)
            self.Label4.configure(background="#d9d9d9")
            self.Label4.configure(disabledforeground="#a3a3a3")
            self.Label4.configure(foreground="#000000")
            self.Label4.configure(text='''Status''')

            self.Label5 = tk.Label(self.Frame1)
            self.Label5.place(relx=0.112, rely=0.737, height=28, width=84)
            self.Label5.configure(background="#d9d9d9")
            self.Label5.configure(disabledforeground="#a3a3a3")
            self.Label5.configure(foreground="#000000")
            self.Label5.configure(text='''Price''')

            self.txtname = tk.Text(self.Frame1)
            self.txtname.place(relx=0.318, rely=0.122, relheight=0.076
                   , relwidth=0.475)
            self.txtname.configure(background="white")
            self.txtname.configure(font="TkTextFont")
            self.txtname.configure(foreground="black")
            self.txtname.configure(highlightbackground="#d9d9d9")
            self.txtname.configure(highlightcolor="black")
            self.txtname.configure(insertbackground="black")
            self.txtname.configure(selectbackground="blue")
            self.txtname.configure(selectforeground="white")
            self.txtname.configure(wrap="word")

            self.txtpr = tk.Text(self.Frame1)
            self.txtpr.place(relx=0.318, rely=0.275, relheight=0.076, relwidth=0.475)

            self.txtpr.configure(background="white")
            self.txtpr.configure(font="TkTextFont")
            self.txtpr.configure(foreground="black")
            self.txtpr.configure(highlightbackground="#d9d9d9")
            self.txtpr.configure(highlightcolor="black")
            self.txtpr.configure(insertbackground="black")
            self.txtpr.configure(selectbackground="blue")
            self.txtpr.configure(selectforeground="white")
            self.txtpr.configure(wrap="word")

            self.txtqt = tk.Text(self.Frame1)
            self.txtqt.place(relx=0.318, rely=0.428, relheight=0.076, relwidth=0.475)

            self.txtqt.configure(background="white")
            self.txtqt.configure(font="TkTextFont")
            self.txtqt.configure(foreground="black")
            self.txtqt.configure(highlightbackground="#d9d9d9")
            self.txtqt.configure(highlightcolor="black")
            self.txtqt.configure(insertbackground="black")
            self.txtqt.configure(selectbackground="blue")
            self.txtqt.configure(selectforeground="white")
            self.txtqt.configure(wrap="word")

            self.txtst = tk.Text(self.Frame1)
            self.txtst.place(relx=0.318, rely=0.584, relheight=0.074, relwidth=0.475)

            self.txtst.configure(background="white")
            self.txtst.configure(font="TkTextFont")
            self.txtst.configure(foreground="black")
            self.txtst.configure(highlightbackground="#d9d9d9")
            self.txtst.configure(highlightcolor="black")
            self.txtst.configure(insertbackground="black")
            self.txtst.configure(selectbackground="blue")
            self.txtst.configure(selectforeground="white")
            self.txtst.configure(wrap="word")

            self.txtpri = tk.Text(self.Frame1)
            self.txtpri.place(relx=0.318, rely=0.737, relheight=0.074
                    , relwidth=0.475)
            self.txtpri.configure(background="white")
            self.txtpri.configure(font="TkTextFont")
            self.txtpri.configure(foreground="black")
            self.txtpri.configure(highlightbackground="#d9d9d9")
            self.txtpri.configure(highlightcolor="black")
            self.txtpri.configure(insertbackground="black")
            self.txtpri.configure(selectbackground="blue")
            self.txtpri.configure(selectforeground="white")
            self.txtpri.configure(wrap="word")

            self.btsh = tk.Button(top)
            self.btsh.place(relx=0.207, rely=0.553, height=33, width=66)
            self.btsh.configure(activebackground="#ececec")
            self.btsh.configure(activeforeground="#000000")
            self.btsh.configure(background="#d9d9d9")
            self.btsh.configure(disabledforeground="#a3a3a3")
            self.btsh.configure(foreground="#000000")
            self.btsh.configure(highlightbackground="#d9d9d9")
            self.btsh.configure(highlightcolor="black")
            self.btsh.configure(pady="0")
            self.btsh.configure(text='''show''')

            self.btadd = tk.Button(top)
            self.btadd.place(relx=0.385, rely=0.553, height=33, width=58)
            self.btadd.configure(activebackground="#ececec")
            self.btadd.configure(activeforeground="#000000")
            self.btadd.configure(background="#d9d9d9")
            self.btadd.configure(disabledforeground="#a3a3a3")
            self.btadd.configure(foreground="#000000")
            self.btadd.configure(highlightbackground="#d9d9d9")
            self.btadd.configure(highlightcolor="black")
            self.btadd.configure(pady="0")
            self.btadd.configure(text='''add''')

            self.btup = tk.Button(top)
            self.btup.place(relx=0.548, rely=0.553, height=33, width=56)
            self.btup.configure(activebackground="#ececec")
            self.btup.configure(activeforeground="#000000")
            self.btup.configure(background="#d9d9d9")
            self.btup.configure(cursor="fleur")
            self.btup.configure(disabledforeground="#a3a3a3")
            self.btup.configure(foreground="#000000")
            self.btup.configure(highlightbackground="#d9d9d9")
            self.btup.configure(highlightcolor="black")
            self.btup.configure(pady="0")
            self.btup.configure(text='''update''')

            self.btdl = tk.Button(top)
            self.btdl.place(relx=0.711, rely=0.553, height=33, width=62)
            self.btdl.configure(activebackground="#ececec")
            self.btdl.configure(activeforeground="#000000")
            self.btdl.configure(background="#d9d9d9")
            self.btdl.configure(disabledforeground="#a3a3a3")
            self.btdl.configure(foreground="#000000")
            self.btdl.configure(highlightbackground="#d9d9d9")
            self.btdl.configure(highlightcolor="black")
            self.btdl.configure(pady="0")
            self.btdl.configure(text='''remove''')

            self.Listbox1 = tk.Listbox(top)
            self.Listbox1.place(relx=0.05, rely=0.679, relheight=0.286
                   , relwidth=0.907)
            self.Listbox1.configure(background="white")
            self.Listbox1.configure(disabledforeground="#a3a3a3")
            self.Listbox1.configure(font="TkFixedFont")
            self.Listbox1.configure(foreground="#000000")

   if __name__ == '__main__':
       vp_start_gui()
