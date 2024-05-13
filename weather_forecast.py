# Import Module
from tkinter import *
import requests

root = Tk()

root.title("Weather Forecast")
root.geometry('350x200')

lbl1 = Label(root, text = "Enter a city name")
lbl1.grid(column=0,row=2)
lbl2 = Label(root, text = "")
lbl2.grid(column=0,row=3)
# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =0, row =0)


# function to display user text when
# button is clicked
def clicked():
	city = txt.get()
	URL = f"https://api.weatherbit.io/v2.0/current?key=0c3f5e963366446e9ec626cb438c5b8d&city={city}"

	r = requests.get(url=URL)

	# extracting data in json format
	results = r.json()
	temp = results['data'][0]['temp']
	humidity = results['data'][0]['rh']

	temperature_string = "Temperature : " + str(temp)
	lbl1.configure(text = temperature_string)
	humidity_string = "Humidity : "+str(humidity)
	lbl2.configure(text=humidity_string)


btn = Button(root, text = "Click me",fg = "red", command=clicked)
btn.grid(column=0, row=4)

root.mainloop()
