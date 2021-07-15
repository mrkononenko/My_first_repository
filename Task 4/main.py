import http.client
import json
import telebot
from telebot import types

bot = telebot.TeleBot('1812172202:AAEtvRMBCfya2T_tWBWjiksH2ZyZCDJ4yIY')
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "ab6d7b3e1fmsh8cc4e1f5849a3d1p133ffdjsn8cf7f2a139df",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
}


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.row('/file')
    keyboard.row('/search')
    bot.send_message(message.chat.id, "Привіт!\nЯ MaxKonononeko_bot\nЗробіть свій вибір, щоб продовжити",
                     reply_markup=keyboard)


@bot.message_handler(commands=['search'])
def textforsearch(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    send = bot.send_message(message.chat.id, 'Country', reply_markup=keyboard)
    bot.register_next_step_handler(send, search)


@bot.message_handler(commands=['file'])
def file(message):
    import http.client
    import json
    conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
    res = conn.getresponse()
    data = res.read()
    All_Info = data.decode("utf-8")
    json = json.loads(All_Info)

    f = open('CovidAsia.txt', 'w')
    f.write('=' * 30)
    f.write('\n')
    for i in range(30):
        f.write('Country : ')
        f.write(str(json[i].get('Country')))
        f.write('\n')
        f.write('Continent : ')
        f.write(str(json[i].get('Continent')))
        f.write('\n')
        f.write('Total Cases : ')
        f.write(str(json[i].get('TotalCases')))
        f.write('\n')
        f.write('Total Deaths : ')
        f.write(str(json[i].get('TotalDeaths')))
        f.write('\n')
        f.write('Total Recovered : ')
        f.write(str(json[i].get('TotalRecovered')))
        f.write('\n')
        f.write('=' * 30)
        f.write('\n')
    f.close()
    f = open('CovidAsia.txt', 'rb')
    bot.send_document(message.chat.id, f)


def search(message):
    import json
    j = 0
    conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
    res = conn.getresponse()
    data = res.read()
    All_Info = data.decode("utf-8")
    json = json.loads(All_Info)
    for i in range(30):
        GetCountry = json[i].get('Country')
        if message.text == GetCountry:
            bot.send_message(message.chat.id, 'Country : ' + str(json[i].get('Country')) + '\n' + 'Continent : ' + str(
                json[i].get('Continent')) + '\n' + 'Total Cases : ' + str(
                json[i].get('TotalCases')) + '\n' + 'Total Deaths : ' + str(
                json[i].get('TotalDeaths')) + '\n' + 'Total Recovered : ' + str(json[i].get('TotalRecovered')))
        else:
            j += 1
        if j == 30:
            bot.send_message(message.chat.id, 'Я не знайшов цю країну у своїй програмі')


bot.polling(none_stop=True)