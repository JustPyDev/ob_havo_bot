from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS

# get zaproslar
t = requests.get('https://sinoptik.ua/погода-ташкент')
html_t = BS(t.content, 'html.parser')

s = requests.get('https://sinoptik.ua/погода-сырдарья')
html_s = BS(s.content, 'html.parser')

j = requests.get('https://sinoptik.ua/погода-джизак')
html_j = BS(j.content, 'html.parser')

m = requests.get('https://sinoptik.ua/погода-самарканд')
html_m = BS(m.content, 'html.parser')

f = requests.get('https://sinoptik.ua/погода-фергана')
html_f = BS(f.content, 'html.parser')

n = requests.get('https://sinoptik.ua/погода-наманган')
html_n = BS(n.content, 'html.parser')

a = requests.get('https://sinoptik.ua/погода-андижан')
html_a = BS(a.content, 'html.parser')

q = requests.get('https://sinoptik.ua/погода-карши')
html_q = BS(q.content, 'html.parser')

su = requests.get('https://sinoptik.ua/погода-байсун')
html_su = BS(su.content, 'html.parser')

b = requests.get('https://sinoptik.ua/погода-олот')
html_b = BS(b.content, 'html.parser')

na = requests.get('https://sinoptik.ua/погода-навои')
html_na = BS(na.content, 'html.parser')

x = requests.get('https://sinoptik.ua/погода-гурлен')
html_x = BS(x.content, 'html.parser')

qo = requests.get('https://sinoptik.ua/погода-нукус')
html_qo = BS(qo.content, 'html.parser')

# shaharlar
for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    t_min = min[4:]
    t_max = max[5:]

for el in html_s.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    s_min = min[4:]
    s_max = max[5:]

for el in html_j.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    j_min = min[4:]
    j_max = max[5:]

for el in html_m.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    m_min = min[4:]
    m_max = max[5:]

for el in html_f.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    f_min = min[4:]
    f_max = max[5:]

for el in html_n.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    n_min = min[4:]
    n_max = max[5:]

for el in html_a.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    a_min = min[4:]
    a_max = max[5:]

for el in html_q.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    q_min = min[4:]
    q_max = max[5:]

for el in html_su.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    su_min = min[4:]
    su_max = max[5:]

for el in html_b.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    b_min = min[4:]
    b_max = max[5:]

for el in html_na.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    na_min = min[4:]
    na_max = max[5:]

for el in html_x.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    x_min = min[4:]
    x_max = max[5:]

for el in html_qo.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    qo_min = min[4:]
    qo_max = max[5:]


def city():
    return [
        [InlineKeyboardButton("Toshkent", callback_data=f"01"),
         InlineKeyboardButton("Sirdaryo", callback_data=f"20")],
        [InlineKeyboardButton("Jizzax", callback_data=f"25"),
         InlineKeyboardButton("Samarqand", callback_data=f"30")],
        [InlineKeyboardButton("Fargʻona", callback_data=f"40"),
         InlineKeyboardButton("Namangan", callback_data=f"50")],
        [InlineKeyboardButton("Andijon", callback_data=f"60"),
         InlineKeyboardButton("Qashqadaryo", callback_data=f"70")],
        [InlineKeyboardButton("Surxondaryo", callback_data=f"75"),
         InlineKeyboardButton("Buxoro", callback_data=f"80")],
        [InlineKeyboardButton("Navoiy", callback_data=f"85"),
         InlineKeyboardButton("Xorazm", callback_data=f"90")],
        [InlineKeyboardButton("Qoraqalpog`iston", callback_data=f"95")],
    ]


def back():
    return [
        [InlineKeyboardButton("Orqaga ⬅", callback_data=f"back1")]
    ]


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")

    if data[0] == "01":
        query.message.edit_text(f"Bugun Toshkent shaxrida havo o`zgarib turadi min {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "20":
        query.message.edit_text(f"Bugun Sirdaryo viloyatida havo o`zgarib turadi\nmin {s_min}\nmax "
                                f"{s_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "25":
        query.message.edit_text(f"Bugun Jizzax viloyatida havo o`zgarib turadi\nmin {j_min}\nmax "
                                f"{j_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "30":
        query.message.edit_text(f"Bugun Samarqand viloyatida havo o`zgarib turadi\nmin {m_min}\nmax "
                                f"{m_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "40":
        query.message.edit_text(f"Bugun Farg`ona viloyatida havo o`zgarib turadi\nmin {f_min}\nmax "
                                f"{f_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "50":
        query.message.edit_text(f"Bugun Namangan viloyatida havo o`zgarib turadi\nmin {n_min}\nmax "
                                f"{n_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "60":
        query.message.edit_text(f"Bugun Andijon viloyatida havo o`zgarib turadi\nmin {a_min}\nmax "
                                f"{a_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "70":
        query.message.edit_text(f"Bugun Qashqadaryo viloyatida havo o`zgarib turadi\nmin {q_min}\nmax "
                                f"{q_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "75":
        query.message.edit_text(f"Bugun Surxondaryo viloyatida havo o`zgarib turadi\nmin {su_min}\nmax "
                                f"{su_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "80":
        query.message.edit_text(f"Bugun Buxoro viloyatida havo o`zgarib turadi\nmin {b_min}\nmax "
                                f"{b_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "85":
        query.message.edit_text(f"Bugun Navoiy viloyatida havo o`zgarib turadi\nmin {na_min}\nmax "
                                f"{na_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "90":
        query.message.edit_text(f"Bugun Xorazim viloyatida havo o`zgarib turadi\nmin {x_min}\nmax "
                                f"{x_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    if data[0] == "95":
        query.message.edit_text(
            f"Bugun Qoraqalpog`iston Respublikasida havo o`zgarib turadi\nmin {qo_min}\nmax "
            f"{qo_max} \nbo`lishi kutilmoqda ⛅",
            reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == 'back1':
        query.message.edit_text(
            f"Bu yerdan Shahar yoki viloyatni tanla 👇",
            reply_markup=InlineKeyboardMarkup(city()))


def start(update, context):
    user = update.message.from_user
    print('BOTDAN FOYDALANGANLAR>>>', user.first_name)
    update.message.reply_text(
        f"""Salom {user.first_name} 🖐🏼\nBu yerdan Shahar yoki viloyatni tanla 👇""",
        reply_markup=InlineKeyboardMarkup(city()))


def main():
    Token = "5242194976:AAG5t3z8mFm9Jw2pdth_Bm_uZSUmw8YObiY"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
