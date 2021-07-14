from tkinter import *
import http.client
import json
import tkinter as tk

root = Tk()
root.title("Статистика Коронавірусу в Азії")
root.geometry('650x650')
root['bg'] = 'blue'
n = 15  # Кількість держав
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "ab6d7b3e1fmsh8cc4e1f5849a3d1p133ffdjsn8cf7f2a139df",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
}
conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
All_Info = data.decode("utf-8")
json = json.loads(All_Info)
frametop = Frame(root)
framebot = Frame(root)
frametop.pack()
framebot.pack()


def Search():
    j = 0
    for i in range(n):
        InputedCountry = EntryCountry.get()
        GetCountry = json[i].get('Country')
        if InputedCountry == GetCountry:
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', json[i].get('TotalRecovered'))
            TextBox.insert('1.0', 'TotalRecovered : ')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', json[i].get('TotalDeaths'))
            TextBox.insert('1.0', 'TotalDeaths : ')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', json[i].get('TotalCases'))
            TextBox.insert('1.0', 'TotalCases : ')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', json[i].get('Continent'))
            TextBox.insert('1.0', 'Continent : ')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', json[i].get('Country'))
            TextBox.insert('1.0', 'Country : ')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '         We found!')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '=' * 30)
        else:
            j += 1
        if j == 20:
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '          We didnt found')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)


def Refresh():
    import json
    TextBox.delete(1.0, END)
    conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
    res = conn.getresponse()
    data = res.read()
    All_Info = data.decode("utf-8")
    json = json.loads(All_Info)
    TextBox.insert('1.0', '\n')
    TextBox.insert('1.0', '=' * 30)
    for i in range(n):
        TextBox.insert('2.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[14])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[12])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[10])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[3])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[2])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', '=' * 30)


Refreshbutton = Button(frametop, text="ОНОВИТИ", command=Refresh)
Refreshbutton['bg'] = 'black'
Refreshbutton['fg'] = 'white'
Refreshbutton.pack(side=LEFT)
EntryCountry = Entry(frametop, width=50, borderwidth=5)
EntryCountry['bg'] = 'black'
EntryCountry['fg'] = 'white'
EntryCountry.pack(side=LEFT)
Searchbutton = Button(frametop, text="ПОШУК", command=Search)
Searchbutton.pack(side=LEFT)
Searchbutton['bg'] = 'black'
Searchbutton['fg'] = 'white'
TextBox = Text(framebot, width=500, height=500)
TextBox['bg'] = 'yellow'
TextBox['fg'] = 'black'
TextBox.pack()
Refresh()
root.mainloop()