from tkinter import *
from PIL import Image, ImageTk
import os
import webbrowser

def open_url(url):
    webbrowser.open_new(url)

root = Tk()
root.title("ВКонтакте")
root.geometry("1100x650")
root.configure(bg="#f0f0f0")

# ========================= ПУТИ =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

bed_path = os.path.join(BASE_DIR, "bedhead.png")
hul_path = os.path.join(BASE_DIR, "huligan.png")
avatar_path = os.path.join(BASE_DIR, "avatar.png")
bell_path = os.path.join(BASE_DIR, "bell.png")
icon_profile = os.path.join(BASE_DIR, "icon_profile.png")
icon_feed = os.path.join(BASE_DIR, "icon_feed.png")
icon_friends = os.path.join(BASE_DIR, "icon_friends.png")
icon_msg = os.path.join(BASE_DIR, "icon_msg.png")

# ========================= ВЕРХНЯЯ ПАНЕЛЬ =========================
header = Frame(root, bg="#eafff0", height=60)
header.pack(fill="x", side="top")
header.pack_propagate(False)

left = Frame(header, bg="#eafff0")
left.pack(side="left", padx=20)
Label(left, text="вконтакте",
      font=("Arial", 18, "bold"),
      bg="#eafff0", fg="#000000").pack()

center_top = Frame(header, bg="#eafff0")
center_top.pack(side="left", expand=True)

search_frame = Frame(center_top, bg="#f2f3f5", bd=0)
search_frame.pack(fill="x", padx=100)

search_field = Entry(search_frame,
                     font=("Arial", 14),
                     bg="#f2f3f5",
                     fg="#000000",
                     bd=0,
                     relief="flat")
search_field.insert(0, "Поиск")
search_field.pack(ipady=6, fill="x")

right = Frame(header, bg="#f2f3f5")
right.pack(side="right", padx=20)
Label(right, text="Иван Копылов",
      font=("Arial", 14),
      bg="#f2f3f5", fg="#000000").pack(side="left", padx=10)

try:
    avatar_raw = Image.open(avatar_path).resize((32, 32))
    avatar_img = ImageTk.PhotoImage(avatar_raw)
except:
    avatar_img = None

try:
    bell_raw = Image.open(bell_path).resize((26, 26))
    bell_img = ImageTk.PhotoImage(bell_raw)
except:
    bell_img = None

if bell_img:
    bell_label = Label(right, image=bell_img, bg="#f2f3f5", cursor="hand2")
    bell_label.pack(side="left", padx=10)

if avatar_img:
    avatar_label = Label(right, image=avatar_img, bg="#f2f3f5", cursor="hand2")
    avatar_label.pack(side="left", padx=10)

# ========================= ОСНОВНАЯ ОБЛАСТЬ =========================
main = Frame(root, bg="#f0f0f0")
main.pack(fill="both", expand=True)

# ========================= ЛЕВОЕ МЕНЮ (С ДОБАВЛЕННЫМИ ЭЛЕМЕНТАМИ) =========================
nav_frame = Frame(main, bg="#eeeeee", width=200)
nav_frame.pack(side="left", fill="y")
nav_frame.pack_propagate(False)

# --- Основные пункты меню (Профиль, Лента, Друзья, Мессенджер) ---
menu_items = [
    ("ПРОФИЛЬ", icon_profile),
    ("ЛЕНТА", icon_feed),
    ("ДРУЗЬЯ", icon_friends),
    ("МЕССЕНДЖЕР", icon_msg)
]

icons = {}

for title, path in menu_items:
    try:
        img_raw = Image.open(path).resize((22, 22))
        img = ImageTk.PhotoImage(img_raw)
        icons[title] = img
    except:
        icons[title] = None

    item_frame = Frame(nav_frame, bg="#eeeeee")
    item_frame.pack(fill="x", pady=2)

    if icons[title]:
        Label(item_frame, image=icons[title], bg="#eeeeee").pack(side="left", padx=15)

    Button(item_frame,
           text=title,
           font=("Arial", 12),
           bg="#eeeeee",
           fg="#000000",
           bd=0,
           anchor="w",
           activebackground="#34c759",
           activeforeground="#ffffff",
           cursor="hand2").pack(side="left", fill="x", padx=10, pady=10)

# --- Разделитель (визуальный отступ) ---
separator = Frame(nav_frame, bg="#cccccc", height=1, bd=0)
separator.pack(fill="x", padx=15, pady=10)

# --- Дополнительные ссылки (Блог, Разработчикам, Для бизнеса, Авторам, Действия, Ещё) ---
extra_links = ["Блог", "Разработчикам", "Для бизнеса", "Авторам", "Действия", "Ещё"]
for link in extra_links:
    btn = Button(nav_frame,
                 text=link,
                 font=("Arial", 11),
                 bg="#eeeeee",
                 fg="#2a5885",
                 bd=0,
                 anchor="w",
                 padx=25,
                 pady=6,
                 activebackground="#d0d6db",
                 activeforeground="#2a5885",
                 cursor="hand2")
    btn.pack(fill="x")

# --- Пустой расширяемый фрейм, чтобы прижать "рекомендательные технологии" к низу ---
spacer = Frame(nav_frame, bg="#eeeeee")
spacer.pack(fill="both", expand=True)

# --- Текст о рекомендательных технологиях в самом низу ---
tech_frame = Frame(nav_frame, bg="#eeeeee")
tech_frame.pack(side="bottom", fill="x", pady=10)

Label(tech_frame,
      text="Применяются\nрекомендательные технологии",
      font=("Arial", 9),
      bg="#eeeeee",
      fg="#656565",
      justify="center").pack()

# ========================= ЦЕНТР =========================
center = Frame(main, bg="#ffffff")
center.pack(side="left", fill="both", expand=True, padx=20, pady=20)

header_feed = Frame(center, bg="#306eff", height=45)
header_feed.pack(fill="x")
header_feed.pack_propagate(False)

Label(header_feed, text="ЛЕНТА НОВОСТЕЙ",
      font=("Arial", 16, "bold"),
      bg="#306eff", fg="#ffffff").pack(expand=True)

white_box = Frame(center, bg="white", highlightbackground="#dddddd", highlightthickness=1)
white_box.pack(fill="both", expand=True, pady=10)

# ========================= ПРАВАЯ КОЛОНКА (РЕКЛАМА) =========================
right_ads = Frame(main, bg="#f0f0f0", width=260)
right_ads.pack(side="right", fill="y")
right_ads.pack_propagate(False)

try:
    bed_img_raw = Image.open(bed_path).resize((240, 300))
    bed_img = ImageTk.PhotoImage(bed_img_raw)
except:
    bed_img = None

try:
    hul_img_raw = Image.open(hul_path).resize((240, 300))
    hul_img = ImageTk.PhotoImage(hul_img_raw)
except:
    hul_img = None

ad1 = Frame(right_ads, bg="white", highlightbackground="#cccccc", highlightthickness=1)
ad1.pack(fill="x", padx=10, pady=10)

BED_URL = "https://www.bedhead.com/"
HUL_URL = "https://ru.wikipedia.org/wiki/%D0%A5%D1%83%D0%BB%D0%B8%D0%B3%D0%B0%D0%BD_(%D0%B6%D1%83%D1%80%D0%BD%D0%B0%D0%BB)?ysclid=mlgh5wqvjg272145097"

if bed_img:
    bed_label = Label(ad1, image=bed_img, bg="white", cursor="hand2")
    bed_label.pack()
    bed_label.bind("<Button-1>", lambda e: open_url(BED_URL))
    link1 = Label(ad1, text="Перейти на сайт", fg="#306eff", cursor="hand2",
                  bg="white", font=("Arial", 10, "underline"))
    link1.pack(pady=5)
    link1.bind("<Button-1>", lambda e: open_url(BED_URL))

ad2 = Frame(right_ads, bg="white", highlightbackground="#cccccc", highlightthickness=1)
ad2.pack(fill="x", padx=10, pady=10)

if hul_img:
    hul_label = Label(ad2, image=hul_img, bg="white", cursor="hand2")
    hul_label.pack()
    hul_label.bind("<Button-1>", lambda e: open_url(HUL_URL))
    link2 = Label(ad2, text="Купить сейчас", fg="#306eff", cursor="hand2",
                  bg="white", font=("Arial", 10, "underline"))
    link2.pack(pady=5)
    link2.bind("<Button-1>", lambda e: open_url(HUL_URL))

info_label = Label(right_ads,
                   text="Рекламные баннеры кликабельны\nи ведут на сайты рекламодателей",
                   bg="#f0f0f0", fg="#666666", font=("Arial", 9))
info_label.pack(pady=10)

root.mainloop()