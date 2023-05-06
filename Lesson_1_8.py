USERS = []

User_1 = {
    "id":1,
    "firs_name": "Axmatov",
    "last_name": "Kamoljon",
    "card_number": 1234567891357903,
    "card_password": 7777,
    "card_tel": 981116172,
    "card_balans": 3000,
    "block": False
    }

User_2 = {
    "id":2,
    "firs_name": "sharopov",
    "last_name": "Durbek",
    "card_number": 1204767890357903,
    "card_password": 9999,
    "card_tel": 988101018,
    "card_balans": 9000,
    "block": False
    }

User_3 = {
    "id":3,
    "firs_name": "Normurudov",
    "last_name": "Dilshod",
    "card_number": 1232507851056903,
    "card_password": 0000,
    "card_tel": 992342145,
    "card_balans": 10000,
    "block": False
    }

USERS.append(User_1)
USERS.append(User_2)
USERS.append(User_3)

card_number_global = 0
card_password_global = 0

def LOGIN ():

    while True:
        print("=====>>> Sis LOGIN bo'limiga xush kelibsiz <<<=====")
        card_number_global = int(input("Siz karta raqamingizni kiriting: "))
        card_password_global = int(input("Siz karta parolingizni kiriting: "))

        if len(str(card_number_global)) == 16 and len(str(card_password_global)) == 4:
            break
        else:
            print("Siz kiritgan karta raqam yoki parol xato")

    for i in USERS:

        if i['card_number'] == card_number_global and i['card_password'] == card_password_global:
            MENU(i)
        else:
            continue

def GIVEMONEY (i):
    print("=====>>> Siz GIVERMONY bo'limiga xush kelibsiz <<<=====")
    
    while True:
        input__give__money = int(input("\n Siz necha pul yechib olmoqchisiz max(1.000.000)."))

        commison__money = input__give__money * 0.01
        if input__give__money <= 1_000_000 and i['card_balans'] >= (input__give__money) + (commison__money):
            i['card_balans'] = i['card_balans'] - (input__give__money + commison__money)
            print(f"\n Sizning hisobingizda {i['card_balans']} \n")
            print(f"\n Sizning hisobingizdan {commison__money} commison olib qoindi \n")
            MENU(i)
        else:
            print("\n Siz juda ko'p summa kiritdingiz.Sizda buncha summa yo'q.")

def ADDMONEY (i):
    print("=====>>> Siz ADDVERMONY bo'limiga xush kelibsiz <<<=====")
    
    while True:
        input__add__meney = int(input("Siz o'tkazmoqchi bo'lgan summangizni kiriting max(1.000.000): "))

        if input__add__meney <= 1_000_000 and (i['card_balans'] + input__add__meney) <= 1_000_000:
            i['card_balans'] = i['card_balans'] + input__add__meney
            print(f"\n sizning hisobingizdagi pul {i['card_balans']} \n")
            MENU(i)
        else:
            print("\n Sizning hisobingizda 1.000.000 dan oshib ketdi. \n")

def BALANS (i):
    print("=====>>> Siz BALANS bo'limiga xush kelibsiz <<<=====")
    print(f"\n Sizning hisobingizda {i['card_balans']} bor. \n")
    MENU(i)

def TRANSEFERMONEY (i):
    input__card__number = 0
    input__card__balans = 0

    print("=====>>> Siz LIVERFERMONY bo'limiga xush kelibsiz <<<=====")
    
    while True:
        input__card__number = int(input("O'tkazmoqchi bo'lgan karta raqamingizni kiriting: "))
        input__card__balans = int(input("Summani kiriting max(1.000.000): "))

        if len(str(input__card__number)) == 16 and input__card__balans <= 1_000_000:
            i['card_balans'] = i['card_balans'] - input__card__balans
            break
        else:
            print("\n Siz ma'lumotlarni noto'g'ri kiritdingiz.Sizning kartangizda buncha mablag' yo'q \n")

    for j in USERS:   
        if j['card_balans'] - input__card__number:
            j['card_balans'] += input__card__balans
            MENU(i)
        else:
            continue

def UPDATE (i):
    
    while True:
        print("=====>>> Siz UPDATE bo'limiga xush kelibsiz <<<=====")
        input__new__password = int(input("\n Siz karta parolingizni o'zgartirmoqchimisiz \n"))
        if i['card_password'] != input__new__password and len(str(input__new__password)) == 4:
            i["card_password"] = input__new__password
            MAIN()
            break
        else:
            print("\n Sizning parolingiz o'zgarmadi \n >>> ")

def LOGOUT ():
    print("=====>>> Siz LOGOUT bo'limiga xush kelibsiz <<<=====")
    print("\n Siz bu kartadan boshqa kartaga o'tmoqchimisiz >>> ")
    MAIN()

def MENU (i):
    print("=====>>> Siz MENU bo'limiga xush kelibsiz <<<=====")
    print("""
    \n 1) Kartaga pul yechish 
    \n 2) Kartaga pul qo'shish
    \n 3) Kartani balansini ko'rish
    \n 4) Kartaga pul o'tkazish
    \n 5) Kartani udate qilish
    \n 6) Log Out
    """)

    input__menu__number = int(input("Menudan birini tanlang: "))

    if input__menu__number == 1: GIVEMONEY(i)
    elif input__menu__number == 2: ADDMONEY(i)
    elif input__menu__number == 3: BALANS(i)
    elif input__menu__number == 4: TRANSEFERMONEY(i)
    elif input__menu__number == 5: UPDATE(i)
    elif input__menu__number == 6: LOGOUT()
    else: print("Menudagi sonlardan birini tanlang: ")

def MAIN():
    LOGIN()
MAIN()





