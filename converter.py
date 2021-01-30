from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('400x235')
root.resizable(0,0)
root.title('Temperature Converter')
root.config(bg='#000')
temperatures = ('Celcius', 'Fahrenheit', 'Kelvin')

class Converter():
    def __init__(self):
        Label(text='Select temperature units',fg='teal',bg='#000',
            font='poppins 18').pack(pady=5)
        Label(text='Enter units:',font='poppins 12',fg='teal',bg='#000').place(x=120,y=55)
        self.entry = Entry(font='calibri 14',relief='flat',width=5,
            bg='light gray',fg='teal')
        self.entry.place(x=220,y=55)

        self.f_temp = ttk.Combobox(width=9,font='calibri 14')
        self.f_temp['values'] = temperatures
        self.f_temp.current(0)
        self.f_temp.place(x=60,y=100)

        Label(text='TO',font='poppins 14',fg='teal',bg='#000').pack(pady=(40,0))

        self.s_temp = ttk.Combobox(width=9,font='calibri 14')
        self.s_temp['values'] = temperatures
        self.s_temp.current(1)
        self.s_temp.place(x=230,y=100)

        Button(text='Convert',font='candara 14',bd=0,fg='white',
            width=8,bg='teal',command=self.convert).pack(pady=5)
        self.output = Label(font='poppins 16',bg='#000')

    def convert(self):
        self.output.pack()
        first, second = self.f_temp.get(), self.s_temp.get()

        # Check if user did not select given temperatures
        if first not in temperatures or second not in temperatures:
            self.output.config(text='Invalid Temperature',fg='red')
        # Check if user selected the same temperatures
        if first == second:
            self.output.config(text='Choose different temperatures',fg='orange red')

        try:
            entry = int(self.entry.get())
            # Convert them and output the result
            if first == 'Celcius' and second == 'Fahrenheit':
                self.output.config(text='Output: ' + str(round((entry * 9/5) + 32, 2)),fg='green')
            if first == 'Celcius' and second == 'Kelvin':
                self.output.config(text='Output: ' + str(round(entry + 273.15, 2)),fg='green')

            if first == 'Fahrenheit' and second == 'Celcius':
                self.output.config(text='Output: ' + str(round((entry - 32) * 5/9, 2)),fg='green')
            if first == 'Fahrenheit' and second == 'Kelvin':
                self.output.config(text='Output: ' + str(round((entry - 32) * 5/9 + 273.15, 2)),fg='green')

            if first == 'Kelvin' and second == 'Celcius':
                self.output.config(text='Output: ' + str(round(entry - 273.15, 2)),fg='green')
            if first == 'Kelvin' and second == 'Fahrenheit':
                self.output.config(text='Output: ' + str(round((entry - 273.15) * 9/5 + 32, 2)),fg='green')
        except:
            self.output.config(text='Enter a unit',fg='red')
        


if __name__ == '__main__':
    app = Converter()
    mainloop()