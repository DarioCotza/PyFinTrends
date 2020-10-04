import tkinter as tk
import src.trends as trends
import src.etc as etc
import src.yahoo_data as yd
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



class MyApp:
    def __init__(self, win):
        #default values
        self.period = '5y'
        self.normalized_prices = []
        self.short_name = ''


        #menubar
        self.menu_bar = tk.Menu(win)


        #period menu
        self.period_menu = tk.Menu(self.menu_bar, tearoff=0)
        for timeframe in trends.timeframes:
            self.period_menu.add_command(label=timeframe, 
            command= lambda timeframe=timeframe: set_period(self, timeframe))
        self.menu_bar.add_cascade(label="Period", menu=self.period_menu)
        win.config(menu = self.menu_bar)


        #symbol 
        self.symbol_label = tk.Label(win, text = 'Symbol') 
        self.symbol_label.place(rely= .0)
        self.symbol_text = tk.Text(win, height=2, width=15)
        self.symbol_text.place(rely = .05)
        #keyword
        self.keyword_label = tk.Label(win, text = 'Keyword')
        self.keyword_label.place(rely= .1)
        self.keyword_text = tk.Text(win, height=2, width=15)
        self.keyword_text.place(rely = .15)
        #nation
        self.nation_label = tk.Label(win, text = 'Nation')
        self.nation_label.place(rely= .2)
        self.nation_text = tk.Text(win, height=2, width=15)
        self.nation_text.place(rely = .25)
        self.nation_text.insert(tk.END, 'ALL')
        #indicator checkbuttons
        self.lr_checkbutton = tk.IntVar()
        self.linear_regression_checkbutton = tk.Checkbutton(win, text="linear regression", variable=self.lr_checkbutton).place(rely = .30)
        #enter button
        self.enter_button = tk.Button(win, text = "Enter",  height=2, width=15,
         command = lambda: enter(self, trends.nations), bg='green2', bd=0)
        self.enter_button.place(rely = 0.4)

        
        #chart
        self.fig = Figure(figsize=(5, 4), dpi=130)
        self.fig.add_subplot(111).plot(self.normalized_prices)
        self.canvas = FigureCanvasTkAgg(self.fig, master=win) 
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx = .15, relheight = 1.0, relwidth = .85)
        self.toolbar = NavigationToolbar2Tk(self.canvas, win)
        self.toolbar.update()
        self.canvas.get_tk_widget().place(relx = .15,)
        
        
        def set_period(self, timeframe):
            self.period = timeframe
            print(self.period)
        

        def enter(self, nations):
            if self.symbol_text.get("1.0", "end-1c") != '':
                symbol = self.symbol_text.get("1.0", "end-1c")
            else:
                symbol = 'btc-usd'
                self.symbol_text.insert("end-1c", symbol)
            if self.keyword_text.get("1.0", "end-1c") != '':
                keyword = self.keyword_text.get("1.0", "end-1c")
            else:
                keyword = ''
            nat = self.nation_text.get("1.0", "end-1c").upper()
            if nat in nations:
                nation = self.nation_text.get("1.0", "end-1c")
            elif nat == 'ALL':
                nation = ''
            else:
                self.nation_text.delete("1.0", "end-1c")
                self.nation_text.insert("end-1c", 'Invalid Value')
                nation = ''


            #yahoo data
            self.y_data = yd.yahoo_data(symbol, self.period)
            self.normalized_prices = self.y_data[0]
            self.short_name = self.y_data[1]


            #trends data
            if keyword == '':
                keyword = self.short_name
                self.trend = trends.trends([keyword], self.period, nation)
                self.keyword_text.insert("end-1c", self.short_name)
            else:
                self.trend = trends.trends([keyword], self.period, nation)
            
            
            # A tk.DrawingArea.
            self.fig.clear()
            sbp = self.fig.add_subplot(111)
            sbp.set_title(self.short_name)
            #plot prices
            x = np.arange(0, len(self.normalized_prices), 1)
            sbp.plot(x, self.normalized_prices, color = "green")
            #plot prices linear regression
            if self.lr_checkbutton.get() == 1:
                lr_normalized_prices = etc.linear_regression(np, x, self.normalized_prices)
                sbp.plot(lr_normalized_prices[0], color = "green", label = f"Price r = {np.round(lr_normalized_prices[1], 4)}")
            #plot trends
            x = np.arange(0, len(self.normalized_prices), len(self.normalized_prices)/len(self.trend))
            try:
                sbp.plot(x, self.trend, color = "blue")
            except ValueError:
                diff = len(x)-len(self.trend)
                for i in range(diff):
                    x = np.delete(x, -1)
                sbp.plot(x, self.trend)
            #plot trends linear regression
            if self.lr_checkbutton.get() == 1:
                lr_trend = etc.linear_regression(np, x, self.trend)
                sbp.plot(x, lr_trend[0], color = "blue", label= f"Trend r = {np.round(lr_trend[1], 4)}")
            #fill in lightgreen if trend > price
            sbp.fill_between(x, self.trend, color = 'lawngreen', alpha = .1)
            sbp.fill_between(np.arange(0, len(self.normalized_prices), 1) ,self.normalized_prices, color = 'white')
            #show legend
            sbp.legend()
            
            self.canvas.draw()


window = tk.Tk()
myapp = MyApp(window)
window.title("PyFinTrends")
window.geometry("900x600")
window.mainloop()