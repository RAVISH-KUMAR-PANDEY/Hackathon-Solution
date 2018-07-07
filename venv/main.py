import matplotlib

from matplotlib import style
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")


class Fb_Trends(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Fb_Trends")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Graph_Page,Graph_Page2):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""According to a Pew Research Center survey this year, 51 percent of US teens ages
         13 to 17 use Facebook, compared with 72 percent for Instagram and 69 percent who are on Snapchat.
         The survey found 85 percent used the Google video sharing service YouTube.The landscape has shifted since a 2014-15 
         Pew survey which found Facebook leading other social networks with 71 percent of the teen segment.
         The social media environment among teens is quite different from what it was just three years ago,” said Pew 
         researcher Monica Anderson.Backthen, teens’ social media use mostly revolved around Facebook. Today, their habits 
         revolve less around a single platform.” The breakup of teens and Facebook was occurring before the latest scandals 
         which have hit Facebook over hijacked user data and propagation of misinformation.According to a Forrester Research survey 
         34 percent of US online youth view Facebook as a website for 'old people and parents'A forecast by data and analysis 
         firm eMarketer suggests that in 2018, the number of Facebook users in the US younger than 11 will decline by 9.3%
         and the number of users in the age ranges of 12 to 17 and 18 to 24 will decrease by 5.6% and 5.8%, respectively.."""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Show Graph As Proof",
                             command=lambda: controller.show_frame(Graph_Page))
        button1.pack()

        button2 = ttk.Button(self, text="Quit",
                             command=quit)
        button2.pack()
        self.snap = tk.PhotoImage(file="fb_logo.png")
        self.snap = self.snap.subsample(10,10)
        self.lbl = tk.Label(self, image=self.snap)
        self.lbl.pack(pady=10, padx=10)


class Graph_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.snap = tk.PhotoImage(file="impdecline.png")
        self.lbl = tk.Label(self, image=self.snap)
        self.lbl.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Graph 2",
                             command=lambda: controller.show_frame(Graph_Page2))
        button1.pack()
        button2 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack()
class Graph_Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page 2", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        df = pd.DataFrame(
               {
                    "Facebook": [13,15,13,11,9,8]
                }
            )
        f = Figure()
        a = f.add_subplot(111)
        bin_edge=[2013,2014,2015,2016,2017,2018]
        a.bar(bin_edge,df["Facebook"],label="Facebook Trends In Teens",color='blue')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        button1 = ttk.Button(self, text="Graph 1",
                             command=lambda: controller.show_frame(Graph_Page))
        button1.pack()
        button2 = ttk.Button(self, text="Back To Home",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack()
        lbl = tk.Label(self, text="Facebook Trends In Teenagers In US In Percentage", font=LARGE_FONT)
        lbl.pack(pady=10, padx=10)


app = Fb_Trends()
app.geometry("1100x800")
app.mainloop()

# Made By Ravish Kumar Pandey And Sourabh Saini

