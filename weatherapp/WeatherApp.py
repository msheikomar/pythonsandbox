import tkinter as tk
import requests
from tkinter import font
from PIL import ImageTk, Image

HEIGHT = 500
WIDTH = 600


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City:  %s \nConditions:    %s  \nTemperature   (F):    %s' % (
            name, desc, temp)
    except:
        final_str = 'There was a problem'
    return final_str


#api.openweathermap.org/data/2.5/weather?q={city name},{country code}
#c7347b0e9978c8b8f6142a0b61100260


def get_weather(city):
    weather_key = 'c7347b0e9978c8b8f6142a0b61100260'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
    label['text'] = format_response(weather)


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('background2.jpeg'))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))  #bg='green'
#entry.pack(side='left', fill='both')
entry.place(relwidth=0.65, relheight=1)  #relx=0.8, rely=0,

button = tk.Button(frame,
                   text="Get Weather",
                   font=('Courier', 12),
                   command=lambda: get_weather(entry.get()))  #bg='gray'
#button.pack(side='left', fill='both', expand=True)
button.place(relx=0.7, relheight=1, relwidth=0.3)  #rely=0,

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5,
                  rely=0.25,
                  relwidth=0.75,
                  relheight=0.6,
                  anchor='n')

label = tk.Label(lower_frame,
                 font=('Courier', 18),
                 anchor='nw',
                 justify='left',
                 bd=4)  # text='This is a label', bg='yellow'
#label.pack(side='left', fill='both')
label.place(relwidth=1, relheight=1)  #relx=0.3, rely=0,

#print(tk.font.families())

root.mainloop()
