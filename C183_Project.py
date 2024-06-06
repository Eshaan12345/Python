from tkinter import *
import requests
import json

root = Tk()
root.geometry("300x400")

l1 = Label(root, text="City Name", font=('bold', 10))
l2 = Label(root, text="Country: ")
l3 = Label(root, text="Region: ")
l4 = Label(root, text="Language: ")
l5 = Label(root, text="Population: ")
l6 = Label(root, text="Area: ")
e1 = Entry(root)

l1.place(relx=0.5, rely=0.1, anchor=CENTER)
l2.place(relx=0.3, rely=0.4, anchor=CENTER)
l3.place(relx=0.3, rely=0.5, anchor=CENTER)
l4.place(relx=0.3, rely=0.6, anchor=CENTER)
l5.place(relx=0.3, rely=0.7, anchor=CENTER)
l6.place(relx=0.3, rely=0.8, anchor=CENTER)
e1.place(relx=0.5, rely=0.2, anchor=CENTER)

def city_data():
    try:
        city_name = e1.get()
        response = requests.get(f"https://restcountries.com/v3.1/capital/{city_name}")
        api_content = response.json()
        
        if api_content:
            country = api_content[0]['name']['common']
            region = api_content[0]['region']
            languages = ", ".join(api_content[0]['languages'].values())
            population = api_content[0]['population']
            area = api_content[0]['area']
            
            l2.config(text=f"Country: {country}")
            l3.config(text=f"Region: {region}")
            l4.config(text=f"Language: {languages}")
            l5.config(text=f"Population: {population}")
            l6.config(text=f"Area: {area} sq km")
        else:
            l2.config(text="Country: Not found")
            l3.config(text="Region: Not found")
            l4.config(text="Language: Not found")
            l5.config(text="Population: Not found")
            l6.config(text="Area: Not found")
            
    except Exception as e:
        l2.config(text="Error fetching data")
        l3.config(text=str(e))
        l4.config(text="")
        l5.config(text="")
        l6.config(text="")

b1 = Button(root, text='Get Data', command=city_data)
b1.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
