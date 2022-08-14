import tkinter as tk
import requests
from PIL import ImageTk,Image


# user defined functions to bring the information back from the dictionary
def visibility(responses):
    try:
        visibility = ((responses['list'][0]['visibility'])/1000)
        round4 = int(round(visibility,1))
        st7 = 'visibility = '
        st8 = 'Km '
    except:
        st7 = " "
        round4 = " "
        st8 = " "
    return str(st7) + str(round4) + str(st8)
        
        
def temp_min(responses):
    try:
        temp_min = ((responses['list'][0]['main']['temp_min'])-273.15)
        round2 = int(round(temp_min,1))
        st3 = 'min temperature = '
        st4 = '°C'
    except:
        st3 = " "
        round2 = ' '
        st4 = " "
    return str(st3) + str(round2) + str(st4)

def temp_max(responses):
    try:
        temp_max = ((responses['list'][0]['main']['temp_max'])-273.15)
        round3 = int(round(temp_max,1))
        st5 = 'max temp'
        st6 = '°C'
    except:
        st5 = " "
        round3 = ' '
        st6 = " "
    return str(st5) + str(round3) + str(st6)

def feels_like(responses):
    try:
        feels_like = ((responses['list'][0]['main']['feels_like'])-273.15)
        round1 = int(round(feels_like,1))
        st = 'feels like = '
        st2 = '°C'
    except:
        st = " "
        round1 = ' '
        st2 = " "
    return str(st) + str(round1) + str(st2) 
        

def temp_response(responses):
    try:
        temperature = ((responses['list'][0]['main']['temp'])-273.15)
        rounded_temp = round(temperature,1)
        string = '°C'
        returned_string3 = int(rounded_temp)
    except:
        returned_string3 = "Please enter a valid city name"
        string = " "
    return str(returned_string3) + str(string)
    

def desc_response(responses):
    try:
        description = (responses['list'][0]['weather'][0]['description'])
        returned_string2 = str(description)
    except:
        returned_string2 = " "
    return returned_string2

def name_response(responses):
    try:
        name = responses['city']['name']
        returned_string = str(name)
    except:
        returned_string = " "
    return returned_string

#Changing the background using PIL library
def background(icon):
    size1 = int(root.winfo_height()*1)
    size2 = int(root.winfo_width()*1)
    img1 = ImageTk.PhotoImage(Image.open(icon+ '.png').resize((size2, size1)))
    background_image.delete("all")
    background_image.create_image(0,0, anchor='nw', image=img1)
    background_image.image = img1
                             


def get_weather(city):
    API_key = '76eee7f12e62c7d11b5f04a1d27c3e1d'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    details = {'APPID' : API_key, 'q': city, 'temperature': 'Metric'}
    response = requests.get(url, params=details)
    responses = response.json()
    print(responses)
    
    label1['text'] = name_response(responses)
    label2['text'] = temp_response(responses)
    label3['text'] = desc_response(responses)
    label4['text'] = temp_min(responses)
    label5['text'] = feels_like(responses)
    label6['text'] = visibility(responses)
    label7['text'] = temp_max(responses)


    try:
        background_name = responses['list'][0]['weather'][0]['icon']
        background(background_name)
    except:
        background('error')


HEIGHT = 799
WIDTH =7000

root = tk.Tk()



canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


background_image = tk.Canvas(root, width=WIDTH, height=HEIGHT)
background_image.place(relx=0,rely=0,relwidth=2,relheight=1)





frame = tk.Frame(root, bg='#5e5e5e')
frame.place(relx=0,rely=0.002,relwidth=2,relheight=0.07)

frame2 = tk.Frame(root, bg='#ff9900')
frame2.place(relx=0.445,rely=0.14,relwidth=0.11,relheight=0.2)

frame3 = tk.Frame(root, bg='#ff9900')
frame3.place(relx=0.395,rely=0.31,relwidth=0.21,relheight=0.07)

entry= tk.Entry(root, bg='white')
entry.place(relx=0.76,rely=0.003,relwidth=0.2,relheight=0.05)

button = tk.Button(root, text='🍭',bg='#11d42e',fg='#ffffff',command = lambda: get_weather(entry.get()),font='times 20')
button.place(relx=0.96,rely=0.003,relwidth=0.04,relheight=0.05)


label = tk.Label(root,text="FORECAST",fg='black',bg= '#5e5e5e',font='Helvetica 10 bold italic')
label.place(relx=-0.27,rely=0.01,relwidth=0.6,relheight=0.05)

label1 = tk.Label(root, bg='white',fg='black')
label1.place(relx=0.45,rely=0.15,relwidth=0.1,relheight=0.03)

label2 = tk.Label(root, bg='white',fg='black',font='100')
label2.place(relx=0.45,rely=0.185,relwidth=0.1,relheight=0.09)

label3 = tk.Label(root, bg='white',fg='black')
label3.place(relx=0.45,rely=0.280,relwidth=0.1,relheight=0.03)

label4 = tk.Label(root, bg='white',fg='black')
label4.place(relx=0.4,rely=0.315,relwidth=0.1,relheight=0.03)

label5 = tk.Label(root, bg='white',fg='black')
label5.place(relx=0.5,rely=0.315,relwidth=0.1,relheight=0.03)

label6 = tk.Label(root, bg='white',fg='black')
label6.place(relx=0.5,rely=0.3451,relwidth=0.1,relheight=0.03)

label7 = tk.Label(root,bg='white',fg='black')
label7.place(relx=0.4,rely=0.3451,relwidth=0.1,relheight=0.03)





root.mainloop()
