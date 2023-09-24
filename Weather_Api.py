import requests
from tkinter import *
from api_keys import weather_api
from pprint import pprint as pp
from tkinter import messagebox
from requests.exceptions import ConnectionError

root = Tk()
root.title("Weather Report")

class EmptyError(Exception):
    pass

class CityNotFoundError(Exception):
    pass


def delete_box_values():
    country_box.delete(0, END)
    temp_c_box.delete(0, END)
    temp_f_box.delete(0, END)
    humidity_box.delete(0, END)
    wind_speed_box.delete(0, END)
    precip_box.delete(0, END)
    current_state_box.delete(0, END)
    date_box.delete(0, END)
    time_box.delete(0, END)


def show_values(r):
    # Getting values
    country = r.json()["location"]["country"]
    temp_c = r.json()["current"]["temp_c"]
    temp_f = r.json()["current"]["temp_f"]
    humidity = r.json()["current"]["humidity"]
    weather_state = r.json()["current"]["condition"]["text"]
    wind_speed = r.json()["current"]["wind_kph"]
    precipitation = r.json()["current"]["precip_mm"]

    date_time = r.json()["location"]["localtime"]
    date_time_lst = date_time.split()
    date = date_time_lst[0]
    time = date_time_lst[1]
    
    # Showing on screen
    country_box.insert(0, country)
    temp_c_box.insert(0, str(temp_c) + u"\u00B0" + "C")
    temp_f_box.insert(0, str(temp_f) + u"\u00B0" + "F")
    humidity_box.insert(0, str(humidity) + " %")
    current_state_box.insert(0, weather_state)
    wind_speed_box.insert(0, str(wind_speed) + " kph")
    precip_box.insert(0, str(precipitation) + " mm")
    date_box.insert(0, date)
    time_box.insert(0, time)
    


def api_status(status_code):
    if status_code == 400:
        raise CityNotFoundError
    elif status_code == "":
        pass

def show_report():
    try:
        city_box_check = city_box.get()
        if city_box_check == "":
            raise EmptyError
        
        url = f"https://api.weatherapi.com/v1/current.json?key={weather_api}&q={city_box.get()}&aqi=yes"
        # Hypertext Transfer Protocol Secure(https) is an extension of Hypertext Transfer Protocol(http)
        # aqi = Air Quality Data and is optional
        r = requests.get(url=url)

        api_status(r.status_code)

    except EmptyError:
        icon = messagebox.showerror("City Error", "Please enter a city!!!")
    except CityNotFoundError:
        icon = messagebox.showerror("City Not Found", "No such city exists!!! Please enter a valid city!!!")
    except ConnectionError:
        icon = messagebox.showerror("Connection Error", "Could not connect to the internet!!! Please try again!!!")

    else:
        delete_box_values()
        show_values(r)
        


# GUI Labels

city_label = Label(root, text="CITY: ")
city_label.grid(row=0, column=0)

submit = Button(root, text="SUBMIT", command=show_report, width=30)
submit.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

date = Label(root, text="DATE: ")
date.grid(row=2, column=0)

time = Label(root, text="TIME: ")
time.grid(row=3, column=0)

country_label = Label(root, text="COUNTRY: ")
country_label.grid(row=4, column=0)

temp_c_label = Label(root, text="TEMPERATURE (" + u"\u00B0" + "C): ")
temp_c_label.grid(row=5, column=0)

temp_f_label = Label(root, text="TEMPERATURE (" + u"\u00B0" + "F): ")
temp_f_label.grid(row=6, column=0)

humidity_label = Label(root, text="HUMIDITY (%): ")
humidity_label.grid(row=7, column=0)

wind_speed = Label(root, text="WIND SPEED (kph)")
wind_speed.grid(row=8, column=0)

precip_label = Label(root, text="PRECIPITATION (mm)")
precip_label.grid(row=9, column=0)

current_state_label = Label(root, text="CURRENT STATE: ")
current_state_label.grid(row=10, column=0)


# Entry boxes of respective Labels

city_box = Entry(root, width=30,)
city_box.grid(row=0, column=1, padx=20)

date_box = Entry(root, width=30,)
date_box.grid(row=2, column=1, padx=20)

time_box = Entry(root, width=30,)
time_box.grid(row=3, column=1, padx=20)

country_box = Entry(root, width=30)
country_box.grid(row=4, column=1, pady=5)

temp_c_box = Entry(root, width=30,)
temp_c_box.grid(row=5, column=1, pady=5)

temp_f_box = Entry(root, width=30,)
temp_f_box.grid(row=6, column=1, pady=5)

humidity_box = Entry(root, width=30,)
humidity_box.grid(row=7, column=1, pady=5)

wind_speed_box = Entry(root, width=30)
wind_speed_box.grid(row=8, column=1, pady=5)

precip_box = Entry(root, width=30)  # Precipitation
precip_box.grid(row=9, column=1, pady=5)

current_state_box = Entry(root, width=30,)
current_state_box.grid(row=10, column=1, pady=5)

root.mainloop()




