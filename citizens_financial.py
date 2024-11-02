import time
import random as r
import copy

print('''
________________________________________________________________________________________________________________
| Citizens' Financial Inc.  x |_+_____________________________________________________________________  -  ◻  X
 ← → ↻ (🔒 citizensfinancialinc.com/#134e3/login                                                    ⭐) 🧩 Ⓜ ⋮
⋮⋮⋮ Apps  📧 Gmail  [▶] YouTube  📌 Maps  ∆ Drive
----------------------------------------------------------------------------------------------------------------
''')
print('\n\n')
print('''
________________________________________________________________________________________________________________
Advertisement_______________________________________________________________________________________________i_X_                                           
  __                   ___                                                               __        ___
 |""|  ___    _   __  |"""|  __                 !!!100 AMENITIES!!!                     |""|____  |"""| __
 |""| |"""|  |"| |""| |"""| |""|           2 & 3BHK Electronic City Ph-1                |""|""""| |"""||""|
 |""| |"""|  |"| |""| |"""| |""|       Buy now get EMI Holiday for 12 Months -          |""|" ""| |"""||""|
 |""| |"""|  |"| |""| |"""| |""|   Starts ₹ 55 Lac* at the heart of Electronic City     |""|""" | |"""||""|
________________________________________________________________________________________________________________
''')
print('\n\n')
print('''                                   welcome to citizens\' financial inc.'''.title())
print('\n\n\n\n')
sentence1 = 'User... You can use any of the first ten names in the original database to continue this program\n' \
            'or create a new account for the same'
time.sleep(3)

for i in sentence1:
    time.sleep(0.1)
    print(i + '', end='')
time.sleep(1)

data_base = {
    'Aditya Shekhar': {
        'Name': 'Aditya Shekhar',
        'Username': 'aditya123@email.com',
        'Card_Number': '123-4567-890',
        'PIN_number': 2544,
        'Balance': 2200000
    },
    'Mohan Reddy': {
        'Name': 'Mohan Reddy',
        'Username': 'mohanreddy@email.com',
        'Card_Number': '443-4507-560',
        'PIN_number': 6678,
        'Balance': 2400000
    },
    'Ramesh Ramanujan': {
        'Name': 'Ramesh Ramanujan',
        'Username': 'ramesh.ram3@email.com',
        'Card_Number': '166-0747-110',
        'PIN_number': 7890,
        'Balance': 2100000
    },
    'Anne Sudeep': {
        'Name': 'Anne Sudeep',
        'Username': 'annes.1983@email.com',
        'Card_Number': '996-9341-254',
        'PIN_number': 8822,
        'Balance': 3000000
    },
    'David Dobrik': {
        'Name': 'David Dobrik',
        'Username': 'david.dobrik_12@gmail.com',
        'Card_Number': '145-0892-445',
        'PIN_number': 5545,
        'Balance': 1900000
    },
    'Siraj Sharma': {
        'Name': 'Siraj Sharma',
        'Username': 'siraj_sharma@email.com',
        'Card_Number': '577-8907-345',
        'PIN_number': 7450,
        'Balance': 2700000
    },
    'Henry Roberts': {
        'Name': 'Henry Roberts',
        'Username': 'henryr08@email.com',
        'Card_Number': '876-9367-211',
        'PIN_number': 5452,
        'Balance': 2000000
    },
    'Zoya Akhtar': {
        'Name': 'Zoya Akhtar',
        'Username': 'zoyaa89@email.com',
        'Card_Number': '600-9910-254',
        'PIN_number': 9900,
        'Balance': 1800000
    },
    'Tommy Cruise': {
        'Name': 'Tommy Cruise',
        'Username': 'heyitstommy@email.com',
        'Card_Number': '601-9331-236',
        'PIN_number': 1265,
        'Balance': 3400000
    },
    'Jack Mamba': {
        'Name': 'Jack Mamba',
        'Username': 'jackmamba34@email.com',
        'Card_Number': '644-4234-456',
        'PIN_number': 6764,
        'Balance': 3700000
    }

}
print()
print('\n')
print('predefined names are: '.capitalize())
time.sleep(2)

print('analysing data, please wait'.capitalize(), end='')
for i in range(3):
    time.sleep(1)
    print('.', end='')
print()
time.sleep(1)
print('''


''')
main_data_base = copy.deepcopy(data_base)

print(data_base)
print('''


''')
time.sleep(0.25)
print('{0:6}{1:40}{2:40}{3:21}{4:12}{5:11}'.format('S.No.', 'NAME', 'EMAIL', 'CARD', 'PIN', 'BALANCE'))

c = 0
for key in main_data_base:
    c = c + 1
    print('{0:6}{1:40}{2:40}{3:15}{4:10}{5:15}'.format(str(c) + ' ', data_base[key]['Name'], data_base[key]['Username'],
                                                       data_base[key]['Card_Number'], data_base[key]['PIN_number'],
                                                       data_base[key]['Balance']))

print('''

''')

print(
    '=================================================================================================================')
print(
    '=================================================================================================================')
print('''


''')

print('''                                   welcome to citizens\' financial inc.'''.title())
print('''

''')
blocked_cards = []
pending_loans = []

while True:
    print('''

    ''')
    data_base = data_base
    blocked_cards = blocked_cards

    pending_loans = pending_loans


    print(data_base)
    time.sleep(1)

    print()
    print('this is only for user reference'.capitalize())
    print('{0:6}{1:40}{2:40}{3:21}{4:12}{5:11}'.format('S.No.', 'NAME', 'EMAIL', 'CARD', 'PIN', 'BALANCE'))

    c = 0
    for key in data_base:
        c = c + 1
        print('{0:6}{1:40}{2:40}{3:15}{4:10}{5:15}'.format(str(c) + ' ', data_base[key]['Name'],
                                                           data_base[key]['Username'], data_base[key]['Card_Number'],
                                                           data_base[key]['PIN_number'], data_base[key]['Balance']))
    print('''

    ''')
    time.sleep(1)
    choice = input(
        "Do you want to Log in or Sign Up?\nType Log in or Sign up below\n\n OR PRESS \n\n 1. Log In \n 2. Sign Up\n\n"
        " ADDITIONAL OPTIONS \n\n 3. Account Recovery\n 4. PIN Change\n 5. Email Change \n 6. Blocking a Card "
        "\n 7. Unblocking a Card\n\n" " OTHER BANKING OPTIONS \n\n 8. Money Transfer \n 9. Loan\n\n"'EXTRAS \n\n 10. About the Bank'
        '\n 11. About the Makers \n').lstrip().rstrip()
    # we need to work on these: pin number change, email id change, displaying the makers of this program, blocking the card
    print()

    if choice.upper().lstrip().rstrip() == 'LOG IN' or choice.lstrip().rstrip() == '1':
        print()
        print('log in'.upper())
        print()

        while True:
            card = input('enter your card number : '.capitalize()).lstrip().rstrip()
            card_spl = list(card)
            if card_spl[3] == '-' and card_spl[8] == '-':
                card = ''.join(card_spl)
                break
            elif '-' not in card_spl:
                card_spl.insert(3, '-')
                card_spl.insert(8, '-')
                card = ''.join(card_spl)
                break
            else:
                print('please enter the card number in the correct format'.capitalize())

        card = card
        if card in blocked_cards:
            print()
            time.sleep(2)
            print('this card is blocked'.upper())
            time.sleep(1)
            print()
        else:
            pin = int(input('enter your pin : '))
            for __name__ in data_base:
                if data_base[__name__]['Card_Number'] == card and data_base[__name__]['PIN_number'] == pin:
                    NAME = data_base[__name__]['Name']
                    EMAIL = data_base[__name__]['Username']
                    CARD_NUM = data_base[__name__]['Card_Number']
                    PIN_NUM = data_base[__name__]['PIN_number']
                    BALANCE = data_base[__name__]['Balance']
                    print('''

                    ''')
                    reCaptca_numerals = r.randrange(0, 9999)
                    alpha_1 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                    alpha_2 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                    alpha_3 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                    reCaptcha = str(reCaptca_numerals) + alpha_1.upper() + alpha_2.upper() + alpha_3.upper()
                    print('''

                    ''')
                    print('your code is: '.capitalize())
                    print('''

                    ''')
                    print('_______________')
                    print(reCaptcha)
                    print('_______________')
                    print('''

                    ''')
                    chance = 3
                    while chance > 0:
                        print('chance left: '.capitalize(), chance)
                        print('please let us know that you are not a robot'.capitalize())
                        reCaptcha_input = input('enter the code you see above: '.capitalize()).lstrip().rstrip()
                        if reCaptcha_input == reCaptcha:
                            print('task finished successfully!'.capitalize())
                            break
                        else:
                            print('''

                            ''')
                            print('entered code is not correct'.capitalize())
                            print('retrying'.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')

                            print()
                            chance = chance - 1
                            print('''

                            ''')
                    else:
                        time.sleep(2)
                        print('we have lost the connection to the server'.capitalize())
                        time.sleep(1)
                        print('reCaptcha verification failed!'.capitalize())
                        time.sleep(2)
                        print('redirecting you the login screen again'.capitalize(), end='')
                        for i in range(3):
                            time.sleep(1)
                            print('.', end='')
                        time.sleep(1)
                        print('''

                        ''')
                        break
                    print('''


                    ''')
                    print('hello'.capitalize(), __name__.title())
                    print()
                    print('your balance is ₹'.capitalize(), data_base[__name__]['Balance'])
                    print()
                    chance = 4
                    while chance > 0:
                        print('chances left'.capitalize(), chance)
                        print('''
                                                1. Withdraw
                                                2. Deposit
                                                3. Exit''')
                        input_val = int(input('enter your choice number here: '.capitalize()))
                        if input_val == 1:
                            pin_repeat = int(input("Enter PIN for confirmation :\n"))
                            if pin_repeat == pin:
                                print('your balance is: ₹ '.capitalize(), data_base[__name__]['Balance'])
                                print('''Withdrawal for :
                                        ₹ 20
                                        ₹ 50
                                        ₹ 100
                                        ₹ 200
                                        ₹ 500
                                        ₹ 2000
                                         ''')
                                withdrawal = int(
                                    input('enter the denomination of note to withdraw your cash: '.capitalize()))
                                if withdrawal in (20, 50, 100, 200, 500, 2000):
                                    user_balance = int(data_base[__name__]['Balance'])

                                    user_balance = user_balance - withdrawal
                                    user_balance = user_balance

                                    data_base[__name__] = {
                                        'Name': NAME,
                                        'Username': EMAIL,
                                        'Card_Number': CARD_NUM,
                                        'PIN_number': PIN_NUM,
                                        'Balance': user_balance
                                    }
                                    print('''
                                    ''')

                                    print('₹', data_base[__name__]['Balance'], 'left')
                                    print('''
                                    ''')

                                    print('₹', withdrawal, 'has been withdrawn from your account from your account')
                                    print('''

                                    ''')
                                    print('____________________________________')
                                    print('your remaining balance is: ₹ '.capitalize(), user_balance)
                                    print('____________________________________')
                                    print('''

                                    ''')
                                    print('do you want to continue with other banking procedures?'.capitalize())
                                    print()
                                    print('enter 1 for yes or 2 for no', '\nor'.upper(), '\nenter a', ' yes '.upper(),
                                          'or a ', 'no: \n'.upper())
                                    input_val_2 = input().lstrip().rstrip()
                                    if input_val_2 in ('y', 'yes', 'Yes', 'YES', 'Y') or input_val_2 == '1':
                                        continue
                                    else:
                                        print('''
                                        ''')
                                        print('''thank you for visiting citizens\' financial inc.'''.upper())
                                        print()
                                        time.sleep(1)
                                        print('have a pleasant day!'.capitalize())
                                        time.sleep(1)
                                        print()
                                        print('''
                                                                           :)
                                        ''')
                                        print('''

                                        ''')
                                        print()
                                        time.sleep(2)
                                        print('redirecting you the login screen again'.capitalize(), end='')
                                        for i in range(3):
                                            time.sleep(1)
                                            print('.', end='')
                                        time.sleep(1)
                                        print('''

                                        ''')
                                        break
                            else:
                                print('Incorrect PIN entered .\nExiting', end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')
                                time.sleep(1)
                                print('''

                                ''')
                                break

                        elif input_val == 2:
                            pin_repeat = int(input("Enter PIN for confirmation :\n"))
                            if pin_repeat == pin:
                                print('your balance is: ₹ '.capitalize(), data_base[__name__]['Balance'])
                                print('''Deposit for :
                                                ₹ 100
                                                ₹ 200
                                                ₹ 500
                                                ₹ 2000
                                                ₹ 5000 
                                                ₹ 10000
                                                ₹ 20000
                                                ₹ 50000
                                                ₹ 100000
                                                ₹ 200000
                                                ₹ 500000
                                                ''')
                                deposit = int(input('enter the amount you want to deposit: '.capitalize()))
                                if deposit in (100, 200, 500, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000):
                                    user_balance = int(data_base[__name__]['Balance'])
                                    user_balance = user_balance + deposit
                                    user_balance = user_balance

                                    data_base[__name__] = {
                                        'Name': NAME,
                                        'Username': EMAIL,
                                        'Card_Number': CARD_NUM,
                                        'PIN_number': PIN_NUM,
                                        'Balance': user_balance
                                    }
                                    print('''
                                    ''')

                                    print('₹', data_base[__name__]['Balance'], 'left')
                                    print('''
                                    ''')
                                    print('₹', deposit, 'has been deposited to your account.')
                                    print('''
                                    ''')
                                    print('____________________________________')
                                    print('your new balance is: ₹ '.capitalize(), user_balance)
                                    print('____________________________________')
                                    print('''

                                    ''')

                                    print('do you want to continue with other banking procedures?'.capitalize())
                                    print()
                                    print('enter 1 for yes or 2 for no', '\nor'.upper(), '\nenter a', ' yes '.upper(),
                                          'or a ', 'no: \n'.upper())
                                    input_val_3 = input().lstrip().rstrip()

                                    if input_val_3 in ('y', 'yes', 'Yes', 'YES', 'Y') or input_val_3 == '1':
                                        continue
                                    else:
                                        print('''
                                        ''')
                                        print('''thank you for visiting citizens\' financial inc.'''.upper())
                                        print()
                                        print('have a pleasant day!'.capitalize())
                                        print()
                                        print('''
                                                                           :)
                                        ''')
                                        print('''

                                        ''')
                                        print()
                                        time.sleep(2)
                                        print('redirecting you the login screen again'.capitalize(), end='')
                                        for i in range(3):
                                            time.sleep(1)
                                            print('.', end='')
                                        time.sleep(1)
                                        print('''

                                        ''')
                                        break

                            else:
                                print('Incorrect PIN entered .\nExiting', end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')
                                time.sleep(1)
                                print('''

                                        ''')
                                break
                        elif input_val == 3:
                            print('''
                            ''')
                            print('''thank you for visiting citizens\' financial inc.'''.upper())
                            print()
                            time.sleep(1)
                            print('have a pleasant day!'.capitalize())
                            time.sleep(1)
                            print()
                            print('''
                                   :)
                            ''')
                            print('''

                            ''')

                            time.sleep(2)
                            print('redirecting to the login screen '.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')
                            time.sleep(1)
                            print('''

                            ''')
                            break

                        else:
                            print('please enter valid option'.capitalize())
                        chance = chance - 1
                    else:
                        print('you have been locked out.'.capitalize())
                        print()
                        time.sleep(2)
                        print('redirecting you the login screen again'.capitalize(), end='')
                        for i in range(3):
                            time.sleep(1)
                            print('.', end='')
                        time.sleep(1)
                        print('''

                        ''')
                        break
            else:
                print('data not found!'.capitalize())

    elif choice.upper().lstrip().rstrip() == 'SIGN UP' or choice.lstrip().rstrip() == '2':
        print()
        print('sign up'.upper())
        print()
        name = input('enter your name: '.capitalize()).lstrip().rstrip()

        chance = 3
        while chance >= 0:
            turns = 3
            while turns > 0:
                print('chance left :'.capitalize(), turns)
                email_id = input('enter your email id: '.capitalize()).lstrip().rstrip()
                if '@' in email_id:
                    if 'gmail' in email_id or 'yahoo' in email_id or 'outlook' in email_id or 'hotmail' in email_id or 'email' in email_id:
                        for user in data_base:
                            if data_base[user]['Username'] == email_id:
                                print()
                                print('this email id already exists'.capitalize())
                                print()
                                break
                        else:
                            email_id = email_id
                            break

                turns = turns - 1

            else:
                print()
                time.sleep(2)
                print('redirecting you the login screen again'.capitalize(), end='')
                for i in range(3):
                    time.sleep(1)
                    print('.', end='')
                time.sleep(1)
                print('''

                ''')
                break

            email_id = email_id
            print()
            print('your email id: ', email_id)
            print('''

            ''')
            email = input('confirm your email id: '.capitalize()).lstrip().rstrip()
            if email == email_id:
                if '@' in email:
                    if 'gmail' in email or 'yahoo' in email or 'outlook' in email or 'hotmail' in email or 'email' in email:

                        reCaptca_numerals = r.randrange(0, 9999)
                        alpha_1 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                        alpha_2 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                        alpha_3 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                        reCaptcha = str(reCaptca_numerals) + alpha_1.upper() + alpha_2.upper() + alpha_3.upper()
                        print('''

                        ''')
                        print('your code is: '.capitalize())
                        print('''

                        ''')
                        print('_______________')
                        print(reCaptcha)
                        print('_______________')
                        print('''

                        ''')
                        chance = 3
                        while chance > 0:
                            print('chance left: '.capitalize(), chance)
                            print('please let us know that you are not a robot'.capitalize())
                            reCaptcha_input = input('enter the code you see above: '.capitalize()).lstrip().rstrip()
                            if reCaptcha_input == reCaptcha:
                                print('task finished successfully!'.capitalize())
                                break
                            else:
                                print('''

                                ''')
                                print('entered code is not correct'.capitalize())
                                print('retrying'.capitalize(), end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')

                                print()
                                chance = chance - 1
                                print('''

                                ''')
                        else:
                            time.sleep(2)
                            print('we have lost the connection to the server'.capitalize())
                            time.sleep(1)
                            print('reCaptcha verification failed!'.capitalize())
                            time.sleep(2)
                            print('redirecting you the login screen again'.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')
                            time.sleep(1)
                            print('''

                            ''')
                            break

                        n1 = r.choice('1234567890')
                        n2 = r.choice('1234567890')
                        n3 = r.choice('1234567890')
                        n4 = r.choice('1234567890')
                        n5 = r.choice('1234567890')
                        n6 = r.choice('1234567890')
                        n7 = r.choice('1234567890')
                        n8 = r.choice('1234567890')
                        n9 = r.choice('1234567890')
                        n10 = r.choice('1234567890')
                        card_num = n1 + n2 + n3 + '-' + n4 + n5 + n6 + n7 + '-' + n8 + n9 + n10
                        pin_num = r.randrange(1000, 9999)
                        balance = 0
                        data_base[name.title()] = {'Name': name.title(),
                                                   'Username': email,
                                                   'Card_Number': card_num,
                                                   'PIN_number': pin_num,
                                                   'Balance': balance
                                                   }
                        print('''

                        ''')
                        print('Your name :', name.title())
                        print('Email ID :', email)
                        print('''

                        ''')
                        print('_________________________________________')
                        print('Assigned Card Number :', card_num)
                        print('Assigned PIN Number :', pin_num)
                        print('_________________________________________')
                        print('''

                        ''')
                        print('Current Balance : ₹', balance)
                        print()
                        print('Mr./Mrs.'.upper(), name.upper(),
                              'please keep your card details extremely confidential'.upper())
                        print()
                        print('you are signed up!'.capitalize())
                        print()
                        print('redirecting you to the login page'.capitalize(), end='')
                        for i in range(3):
                            time.sleep(1)
                            print('.', end='')
                        time.sleep(1)
                        print()
                        print('''

                        ''')
                        break
                    else:
                        print('you have not entered the email address correctly'.capitalize(),
                              '\n Attempts left: ',
                              chance)
                else:
                    print('you have not entered the email address correctly'.capitalize(), '\n Attempts left: ',
                          chance)
            else:
                print('email id doesnt match'.capitalize())
                print('''


                ''')

            chance = chance - 1
        else:
            print()
            print('you have been logged out!'.upper())
            print()

    elif choice.upper().lstrip().rstrip() == 'ACCOUNT RECOVERY' or choice.lstrip().rstrip() == '3':
        print()
        print('account recovery'.upper())
        print()

        print('''

        ''')
        print('account recovery initialising'.capitalize(), end='')
        for i in range(3):
            time.sleep(1)
            print('.', end='')
        time.sleep(1)
        print('''

        ''')

        rev_email = input('enter your email id: '.capitalize()).lstrip().rstrip()
        print('''
        ''')

        while True:
            card = input('enter your card number: '.capitalize()).lstrip().rstrip()
            print()
            card_spl = list(card)
            if card_spl[3] == '-' and card_spl[8] == '-':
                card = ''.join(card_spl)
                break
            elif '-' not in card_spl:
                card_spl.insert(3, '-')
                card_spl.insert(8, '-')
                card = ''.join(card_spl)
                break
            else:
                print('please enter the card number in the correct format'.capitalize())

        card = card
        for __name__ in data_base:
            if data_base[__name__]['Card_Number'] == card and data_base[__name__]['Username'] == rev_email:
                print('''

                ''')
                reCaptca_numerals = r.randrange(0, 9999)
                alpha_1 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                alpha_2 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                alpha_3 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                reCaptcha = str(reCaptca_numerals) + alpha_1.upper() + alpha_2.upper() + alpha_3.upper()
                print('''

                ''')
                print('your code is: '.capitalize())
                print('''

                ''')
                print('_______________')
                print(reCaptcha)
                print('_______________')
                print('''

                ''')
                chance = 3
                while chance > 0:
                    print('chance left: '.capitalize(), chance)
                    print('please let us know that you are not a robot'.capitalize())
                    reCaptcha_input = input('enter the code you see above: '.capitalize()).lstrip().rstrip()
                    if reCaptcha_input == reCaptcha:
                        print('task finished successfully!'.capitalize())
                        break
                    else:
                        print('''

                        ''')
                        print('entered code is not correct'.capitalize())
                        print('retrying'.capitalize(), end='')
                        for i in range(3):
                            time.sleep(1)
                            print('.', end='')

                        print()
                        chance = chance - 1
                        print('''

                        ''')
                else:
                    time.sleep(2)
                    print('we have lost the connection to the server'.capitalize())
                    time.sleep(1)
                    print('reCaptcha verification failed!'.capitalize())
                    time.sleep(2)
                    print('redirecting you to the login screen again'.capitalize(), end='')
                    for i in range(3):
                        time.sleep(1)
                        print('.', end='')
                    time.sleep(1)
                    print('''

                    ''')
                    break

                print('''


                ''')

                print('your name:'.capitalize(), data_base[__name__]['Name'])
                print('your email id: '.capitalize(), data_base[__name__]['Username'])
                print('your card number: '.capitalize(), data_base[__name__]['Card_Number'])
                print('your pin number: '.capitalize(), data_base[__name__]['PIN_number'])
                print('''

                ''')
                print('Mr./ Mrs.'.upper(), data_base[__name__]['Name'].upper(),
                      'please keep your card details extremely confidential'.upper())

                print('''

                ''')

                print('account recovery successful!'.upper())
                print()

                time.sleep(2)
                print('redirecting you to the login screen again'.capitalize(), end='')
                for i in range(3):
                    time.sleep(1)
                    print('.', end='')
                time.sleep(1)
                print('''

                ''')

                break
        else:
            print('data not found!'.capitalize())
            print('redirecting you to the login screen again'.capitalize(), end='')
            for i in range(3):
                time.sleep(1)
                print('.', end='')
            time.sleep(1)
            print('''

            ''')

    elif choice.upper().lstrip().rstrip() == 'PIN CHANGE' or choice.lstrip().rstrip() == '4':
        print()
        print('pin change'.upper())
        print()
        time.sleep(1)

        while True:
            card_num = input('enter your card number: '.capitalize()).lstrip().rstrip()
            card_spl = list(card_num)
            if card_spl[3] == '-' and card_spl[8] == '-':
                card = ''.join(card_spl)
                break
            elif '-' not in card_spl:
                card_spl.insert(3, '-')
                card_spl.insert(8, '-')
                card = ''.join(card_spl)
                break
            else:
                print('please enter the card number in the correct format'.capitalize())
        card = card
        time.sleep(1)
        pin_num = int(input('enter your pin number: '.capitalize()))
        print('''
        ''')

        for __name__ in data_base:
            if data_base[__name__]['Card_Number'] == card and data_base[__name__]['PIN_number'] == pin_num:
                NAME = data_base[__name__]['Name']
                EMAIL = data_base[__name__]['Username']
                CARD_NUM = data_base[__name__]['Card_Number']
                PIN_NUM = data_base[__name__]['PIN_number']
                BALANCE = data_base[__name__]['Balance']
                print('''
                ''')
                print('hello'.capitalize(), NAME)
                print()

                time.sleep(1)

                new_pin = int(input('enter your new pin: '.capitalize()))
                if len(str(new_pin)) == 4:
                    time.sleep(1)
                    print('''
                                    ''')

                    new_pin_confirm = int(input('confirm your new pin: '.capitalize()))
                    print('''
                                    ''')

                    if new_pin == new_pin_confirm:
                        reCaptca_numerals = r.randrange(0, 9999)
                        alpha_1 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                        alpha_2 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                        alpha_3 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                        reCaptcha = str(reCaptca_numerals) + alpha_1.upper() + alpha_2.upper() + alpha_3.upper()
                        print('''

                                        ''')
                        print('your code is: '.capitalize())
                        print('''

                                        ''')
                        print('_______________')
                        print(reCaptcha)
                        print('_______________')
                        print('''

                                        ''')
                        chance = 3
                        while chance > 0:
                            print('chance left: '.capitalize(), chance)
                            print('please let us know that you are not a robot'.capitalize())
                            reCaptcha_input = input('enter the code you see above: '.capitalize()).lstrip().rstrip()
                            if reCaptcha_input == reCaptcha:
                                print('task finished successfully!'.capitalize())
                                break
                            else:
                                print('''

                                                ''')
                                print('entered code is not correct'.capitalize())
                                print('retrying'.capitalize(), end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')

                                print()
                                chance = chance - 1
                                print('''

                                                ''')
                        else:
                            time.sleep(2)
                            print('we have lost the connection to the server'.capitalize())
                            time.sleep(1)
                            print('reCaptcha verification failed!'.capitalize())
                            time.sleep(2)
                            print('redirecting you to the login screen again'.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')
                            time.sleep(1)
                            print('''

                                            ''')
                            break
                        print('''

                                        ''')

                        print('changing password.'.capitalize())
                        print('please wait'.capitalize(), end='')
                        for i in range(3):
                            time.sleep(1)
                            print('.', end='')
                        print('''

                                        ''')
                        data_base[__name__] = {
                            'Name': NAME,
                            'Username': EMAIL,
                            'Card_Number': CARD_NUM,
                            'PIN_number': new_pin_confirm,
                            'Balance': BALANCE

                        }
                        print()
                        print('pin changed!'.upper())
                        print('''

                                        ''')

                        print('redirecting you to the login screen again'.capitalize(), end='')
                        for i in range(3):
                            time.sleep(1)
                            print('.', end='')
                        time.sleep(1)
                        print('''

                                        ''')
                        break
                    else:
                        print('pin numbers don\'t match'.capitalize())
                else:
                    print('enter the pin number with four digits'.capitalize())

        else:
            print('data not found!'.capitalize())
            print('redirecting you to the login screen again'.capitalize(), end='')
            for i in range(3):
                time.sleep(1)
                print('.', end='')
            time.sleep(1)
            print('''

            ''')

    elif choice.upper().lstrip().rstrip() == 'EMAIL CHANGE' or choice.lstrip().rstrip() == '5':
        print()
        print('email change'.upper())
        print()
        time.sleep(1)

        while True:
            card_num = input('enter your card number: '.capitalize()).lstrip().rstrip()
            card_spl = list(card_num)
            if card_spl[3] == '-' and card_spl[8] == '-':
                card = ''.join(card_spl)
                break
            elif '-' not in card_spl:
                card_spl.insert(3, '-')
                card_spl.insert(8, '-')
                card = ''.join(card_spl)
                break
            else:
                print('please enter the card number in the correct format'.capitalize())
        card = card
        time.sleep(1)
        pin_num = int(input('enter your pin number: '.capitalize()))
        print('''
        ''')

        user_email = input('enter your registered email id: '.capitalize()).lstrip().rstrip()

        for __name__ in data_base:
            if data_base[__name__]['Card_Number'] == card and data_base[__name__]['PIN_number'] == pin_num and \
                    data_base[__name__]['Username'] == user_email:
                NAME = data_base[__name__]['Name']
                EMAIL = data_base[__name__]['Username']
                CARD_NUM = data_base[__name__]['Card_Number']
                PIN_NUM = data_base[__name__]['PIN_number']
                BALANCE = data_base[__name__]['Balance']
                print('''
                ''')
                print('hello'.capitalize(), NAME)
                print()

                time.sleep(1)

                turns = 3
                while turns > 0:
                    print('chance left :'.capitalize(), turns)
                    new_email = input('enter your new email address: '.capitalize()).lstrip().rstrip()
                    print()

                    if '@' in new_email:
                        if 'gmail' in new_email or 'yahoo' in new_email or 'outlook' in new_email or 'hotmail' in new_email or 'email' in new_email:
                            for user in data_base:
                                if data_base[user]['Username'] == new_email:
                                    print()
                                    print('this email id already exists'.capitalize())
                                    print()
                                    break
                            else:
                                new_email = new_email
                                break
                    turns = turns - 1
                else:
                    time.sleep(2)
                    print('we have lost the connection to the server'.capitalize())
                    time.sleep(1)
                    print('redirecting you to the login screen again'.capitalize(), end='')
                    for i in range(3):
                        time.sleep(1)
                        print('.', end='')
                    time.sleep(1)
                    print('''

                    ''')
                    break

                new_email_confirm = input('confirm your new email address: '.capitalize()).lstrip().rstrip()

                if new_email == new_email_confirm:
                    reCaptca_numerals = r.randrange(0, 9999)
                    alpha_1 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                    alpha_2 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                    alpha_3 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                    reCaptcha = str(reCaptca_numerals) + alpha_1.upper() + alpha_2.upper() + alpha_3.upper()
                    print('''

                    ''')
                    print('your code is: '.capitalize())
                    print('''

                    ''')
                    print('_______________')
                    print(reCaptcha)
                    print('_______________')
                    print('''

                    ''')
                    chance = 3
                    while chance > 0:
                        print('chance left: '.capitalize(), chance)
                        print('please let us know that you are not a robot'.capitalize())
                        reCaptcha_input = input('enter the code you see above: '.capitalize()).lstrip().rstrip()
                        if reCaptcha_input == reCaptcha:
                            print('task finished successfully!'.capitalize())
                            break
                        else:
                            print('''

                            ''')
                            print('entered code is not correct'.capitalize())
                            print('retrying'.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')

                            print()
                            chance = chance - 1
                            print('''

                            ''')
                    else:
                        time.sleep(2)
                        print('we have lost the connection to the server'.capitalize())
                        time.sleep(1)
                        print('reCaptcha verification failed!'.capitalize())
                        time.sleep(2)
                        print('redirecting you to the login screen again'.capitalize(), end='')
                        for i in range(3):
                            time.sleep(1)
                            print('.', end='')
                        time.sleep(1)
                        print('''

                        ''')
                        break
                    print('''

                    ''')

                    print('changing email address.'.capitalize())
                    print('please wait'.capitalize(), end='')
                    for i in range(3):
                        time.sleep(1)
                        print('.', end='')
                    print('''

                    ''')
                    data_base[__name__] = {
                        'Name': NAME,
                        'Username': new_email_confirm,
                        'Card_Number': CARD_NUM,
                        'PIN_number': PIN_NUM,
                        'Balance': BALANCE

                    }
                    print()
                    print('email address changed!'.upper())
                    print('''

                    ''')

                    print('redirecting you to the login screen again'.capitalize(), end='')
                    for i in range(3):
                        time.sleep(1)
                        print('.', end='')
                    time.sleep(1)
                    print('''

                    ''')
                    break
                else:
                    print('Email addresses don\'t match'.capitalize())

        else:
            print('data not found!'.capitalize())
            print('redirecting you to the login screen again'.capitalize(), end='')
            for i in range(3):
                time.sleep(1)
                print('.', end='')
            time.sleep(1)
            print('''

            ''')

    elif choice.upper() == 'BLOCK' or choice.lstrip().rstrip() == '6':
        print()
        print('blocking card'.upper())
        print()

        while True:
            card_num = input('enter your card number: '.capitalize()).lstrip().rstrip()
            card_spl = list(card_num)
            if card_spl[3] == '-' and card_spl[8] == '-':
                card = ''.join(card_spl)
                break
            elif '-' not in card_spl:
                card_spl.insert(3, '-')
                card_spl.insert(8, '-')
                card = ''.join(card_spl)
                break
            else:
                print('please enter the card number in the correct format'.capitalize())
        card = card
        print()
        pin = int(input('enter your pin number: '))
        print('''

        ''')

        for __name__ in data_base:
            if data_base[__name__]['Card_Number'] == card and data_base[__name__]['PIN_number'] == pin:
                print()
                print('hello'.capitalize(), __name__.title())
                print()
                while True:
                    while True:
                        rec_card = input('confirm your card number: '.capitalize()).lstrip().rstrip()
                        card_spl = list(rec_card)
                        if card_spl[3] == '-' and card_spl[8] == '-':
                            rec_card = ''.join(card_spl)
                            break
                        elif '-' not in card_spl:
                            card_spl.insert(3, '-')
                            card_spl.insert(8, '-')
                            rec_card = ''.join(card_spl)
                            break
                        else:
                            print('please enter the card number in the correct format'.capitalize())
                    rec_card = rec_card

                    if card == rec_card:
                        print()
                        card_spl = list(rec_card)
                        if card_spl[3] == '-' and card_spl[8] == '-':
                            rec_card = ''.join(card_spl)
                            blocked_cards.append(rec_card)
                            card_spl.pop(3)
                            card_spl.pop(7)
                            rec_card = ''.join(card_spl)
                            blocked_cards.append(rec_card)

                            print('blocking your card'.capitalize())
                            print('please wait'.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')
                                time.sleep(1)
                            print()
                            print('card blocked'.upper())
                            print('''



                            ''')

                            print('redirecting you to the login screen again'.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')
                            time.sleep(1)
                            print('''

                            ''')

                            break
                        elif '-' not in card_spl:
                            blocked_cards.append(rec_card)
                            card_spl.insert(3, '-')
                            card_spl.insert(8, '-')
                            rec_card = ''.join(card_spl)
                            blocked_cards.append(rec_card)
                            print('blocking your card'.capitalize())
                            print('please wait'.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')
                            time.sleep(1)
                            print()
                            print('card blocked'.upper())
                            print('''

                            ''')
                            print('redirecting you to the login screen again'.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')
                            time.sleep(1)

                            break
                        else:
                            print('please enter the card number in the correct format'.capitalize())
                    else:
                        print('card numbers don\'t match'.capitalize())

    elif choice.upper().lstrip().rstrip() == 'UNBLOCK' or choice.lstrip().rstrip() == '7':
        print()
        print('unblocking card'.upper())
        print()

        while True:
            card_num = input('enter your card number: '.capitalize()).lstrip().rstrip()
            card_spl = list(card_num)
            if card_spl[3] == '-' and card_spl[8] == '-':
                card = ''.join(card_spl)
                break
            elif '-' not in card_spl:
                card_spl.insert(3, '-')
                card_spl.insert(8, '-')
                card = ''.join(card_spl)
                break
            else:
                print('please enter the card number in the correct format'.capitalize())
        card = card
        print()
        pin = int(input('enter your pin number: '))
        print('''

        ''')

        for __name__ in data_base:
            if data_base[__name__]['Card_Number'] == card and data_base[__name__]['PIN_number'] == pin:
                print()
                print('hello'.capitalize(), __name__.title())
                print()
                while True:
                    while True:
                        rec_card = input('confirm your card number: '.capitalize()).lstrip().rstrip()
                        card_spl = list(rec_card)
                        if card_spl[3] == '-' and card_spl[8] == '-':
                            rec_card = ''.join(card_spl)
                            break
                        elif '-' not in card_spl:
                            card_spl.insert(3, '-')
                            card_spl.insert(8, '-')
                            rec_card = ''.join(card_spl)
                            break
                        else:
                            print('please enter the card number in the correct format'.capitalize())
                    rec_card = rec_card

                    if card == rec_card:
                        if card in blocked_cards:

                            card_spl = list(rec_card)
                            if card_spl[3] == '-' and card_spl[8] == '-':
                                rec_card = ''.join(card_spl)
                                blocked_cards.remove(rec_card)
                                card_spl.pop(3)
                                card_spl.pop(7)
                                rec_card = ''.join(card_spl)
                                blocked_cards.remove(rec_card)

                                print('unblocking your card'.capitalize())
                                print('please wait'.capitalize(), end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')
                                    time.sleep(1)
                                print()
                                print('card unblocked'.upper())
                                print('''

                                ''')
                                print('''

                                ''')
                                print('redirecting you to the login screen again'.capitalize(), end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')
                                time.sleep(1)
                                print('''

                                ''')

                                break
                            elif '-' not in card_spl:
                                blocked_cards.remove(rec_card)
                                card_spl.insert(3, '-')
                                card_spl.insert(8, '-')
                                rec_card = ''.join(card_spl)
                                blocked_cards.remove(rec_card)

                                print('unblocking your card'.capitalize())
                                print('please wait'.capitalize(), end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')
                                    time.sleep(1)
                                print()
                                print('card unblocked'.upper())
                                print('''

                                ''')

                                print('redirecting you to the login screen again'.capitalize(), end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')
                                time.sleep(1)
                                print('''

                                ''')

                                break

                            else:
                                print('please enter the card number in the correct format'.capitalize())
                        else:
                            print('this card is not blocked'.capitalize())
                            break
                    else:
                        print('card numbers don\'t match'.capitalize())

    elif choice.upper().lstrip().rstrip() == 'MONEY TRANSFER' or choice.lstrip().rstrip() == '8':

        print()
        print()
        print('welcome to citizens\' financial inc money transfer'.upper())
        print('''

        ''')
        while True:
            card_num = input('enter your card number: '.capitalize()).lstrip().rstrip()
            card_spl = list(card_num)
            if card_spl[3] == '-' and card_spl[8] == '-':
                card = ''.join(card_spl)
                break
            elif '-' not in card_spl:
                card_spl.insert(3, '-')
                card_spl.insert(8, '-')
                card = ''.join(card_spl)
                break
            else:
                print('please enter the card number in the correct format'.capitalize())
        card = card

        if card in blocked_cards:
            print()
            print('this card is blocked'.upper())
            print()
        else:
            pin = int(input('enter your pin number: '.capitalize()))
            print('''
                           ''')

            for __name__ in data_base:
                if data_base[__name__]['Card_Number'] == card and data_base[__name__]['PIN_number'] == pin:
                    NAME = data_base[__name__]['Name']
                    EMAIL = data_base[__name__]['Username']
                    CARD_NUM = data_base[__name__]['Card_Number']
                    PIN_NUM = data_base[__name__]['PIN_number']
                    BALANCE = data_base[__name__]['Balance']
                    print()
                    print('hello'.capitalize(), __name__)
                    print()
                    print('your current balance is: '.capitalize(), BALANCE)

                    print('\n\n')

                    while True:
                        rec_card = input('enter the receiver\'s card number: '.capitalize()).lstrip().rstrip()
                        card_spl = list(rec_card)
                        if card_spl[3] == '-' and card_spl[8] == '-':
                            rec_card = ''.join(card_spl)
                            break
                        elif '-' not in card_spl:
                            card_spl.insert(3, '-')
                            card_spl.insert(8, '-')
                            rec_card = ''.join(card_spl)
                            break
                        else:
                            print('please enter the card number in the correct format'.capitalize())
                    card = rec_card

                    for receiver in data_base:
                        if data_base[receiver]['Card_Number'] == card:

                            rNAME = data_base[receiver]['Name']
                            rEMAIL = data_base[receiver]['Username']
                            rCARD_NUM = data_base[receiver]['Card_Number']
                            rPIN_NUM = data_base[receiver]['PIN_number']
                            rBALANCE = data_base[receiver]['Balance']
                            print('''

                            ''')

                            print('you are transferring money to '.capitalize(), rNAME.upper())
                            print()

                            amount = int(input('enter the amount you want to transfer: '.capitalize()))
                            print('''

                            ''')

                            pin_repeat = int(input('confirm your pin again: '.capitalize()))
                            print()

                            if pin_repeat == pin:
                                reCaptca_numerals = r.randrange(0, 9999)
                                alpha_1 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                                alpha_2 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                                alpha_3 = r.choice('qwertyuiopasdfghjklzxcvbnm')
                                reCaptcha = str(reCaptca_numerals) + alpha_1.upper() + alpha_2.upper() + alpha_3.upper()
                                print('''

                                ''')
                                print('your code is: '.capitalize())
                                print('''

                                ''')
                                print('_______________')
                                print(reCaptcha)
                                print('_______________')
                                print('''

                                ''')
                                chance = 3
                                while chance > 0:
                                    print('chance left: '.capitalize(), chance)
                                    print('please let us know that you are not a robot'.capitalize())
                                    reCaptcha_input = input(
                                        'enter the code you see above: '.capitalize()).lstrip().rstrip()
                                    if reCaptcha_input == reCaptcha:
                                        print()
                                        print('task finished successfully!'.capitalize())
                                        break
                                    else:
                                        print('''

                                        ''')
                                        print('entered code is not correct'.capitalize())
                                        print('retrying'.capitalize(), end='')
                                        for i in range(3):
                                            time.sleep(1)
                                            print('.', end='')

                                        print()
                                        chance = chance - 1
                                        print('''

                                        ''')
                                else:
                                    time.sleep(2)
                                    print('we have lost the connection to the server'.capitalize())
                                    time.sleep(1)
                                    print('reCaptcha verification failed!'.capitalize())
                                    time.sleep(2)
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print('''

                                    ''')
                                    break

                                print()
                                print('transaction in progress'.capitalize(), end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')
                                time.sleep(1)

                                data_base[__name__] = {
                                    'Name': NAME,
                                    'Username': EMAIL,
                                    'Card_Number': CARD_NUM,
                                    'PIN_number': PIN_NUM,
                                    'Balance': BALANCE - amount

                                }

                                data_base[receiver] = {
                                    'Name': rNAME,
                                    'Username': rEMAIL,
                                    'Card_Number': rCARD_NUM,
                                    'PIN_number': rPIN_NUM,
                                    'Balance': rBALANCE + amount

                                }
                                print()
                                print()

                                print('Transaction successful!'.upper())
                                print()

                                print('____________________________________')
                                print('your new balance is:   ₹  '.capitalize(), BALANCE - amount)
                                print('amount transferred:    ₹  '.capitalize(), amount)
                                print('____________________________________')
                                print('''



                                ''')
                                print('''
                                ''')
                                print('''thank you for visiting citizens\' financial inc.'''.upper())
                                print()
                                time.sleep(1)
                                print('have a pleasant day!'.capitalize())
                                time.sleep(1)
                                print()
                                print('''
                                                                           :)

                                ''')
                                print('''

                                ''')
                                time.sleep(1)

                                print('redirecting to the login screen again'.capitalize(), end='')
                                for i in range(3):
                                    time.sleep(1)
                                    print('.', end='')
                                time.sleep(1)
                                print('''

                                ''')
                                break

                            else:
                                print('pin numbers don\'t match!'.capitalize())

                    else:
                        print('data not found!'.capitalize())

    elif choice.upper().lstrip().rstrip() == 'LOAN' or choice.lstrip().rstrip() == '9':

        print()
        print()
        print('welcome to citizens\' financial inc loan acquisition '.upper())
        print('''

        ''')

        while True:
            card_num = input('enter your card number: '.capitalize()).lstrip().rstrip()
            card_spl = list(card_num)
            if card_spl[3] == '-' and card_spl[8] == '-':
                card = ''.join(card_spl)
                break
            elif '-' not in card_spl:
                card_spl.insert(3, '-')
                card_spl.insert(8, '-')
                card = ''.join(card_spl)
                break
            else:
                print('please enter the card number in the correct format'.capitalize())
        card = card

        if card in blocked_cards:
            print()
            time.sleep(1)
            print('this card is blocked'.upper())
            print()
            print('redirecting to the login screen again'.capitalize(), end='')
            for i in range(3):
                time.sleep(1)
                print('.', end='')
            time.sleep(1)
            print('''

            ''')

        else:
            if card in pending_loans:
                print()
                time.sleep(1)
                print('clear your loans first!'.capitalize())
                time.sleep(1)
                print()
                print('redirecting to the login screen again'.capitalize(), end='')
                for i in range(3):
                    time.sleep(1)
                    print('.', end='')
                time.sleep(1)
                print('''

            ''')

            else:

                pin = int(input('enter your pin number: '.capitalize()))
                print('''
                ''')

                for __name__ in data_base:
                    if data_base[__name__]['Card_Number'] == card and data_base[__name__]['PIN_number'] == pin:
                        print('hello'.capitalize(), __name__)

                        NAME = data_base[__name__]['Name']

                        name = input('enter your name again for proceeding further: '.capitalize()).lstrip().rstrip()
                        if __name__ == name:
                            profession = input('enter your profession: '.capitalize()).lstrip().rstrip()
                            salary = float(input('enter your monthly income (in numbers) : '.capitalize()))
                            loan_for = input('''Enter the reason for the loan: 
                                                    1.Educational
                                                    2.Medical
                                                    3.Business
                                                    4.Home & Auto
                                                    5.Personal
                                                        ''').lstrip().rstrip()
                            if loan_for.upper() == 'EDUCATIONAL' or int(loan_for) == 1:
                                amount_req = int(input('enter the required amount: '.capitalize()))
                                collateral = input('''Enter the collateral that you are providing to the bank
                                1. Jewellery
                                2. House
                                3. Gold
                                4. Land
                                5. Car\n''')

                                print('the rate of interest for Educational loan is 10%'.capitalize())
                                return_amount = 1.1 * amount_req
                                print()

                                print('This signing is to confirm and guarantee the repayment of the loan that\n ',
                                      'has been taken by applicant', NAME.upper(), '. This is an EDUCATIONAL loan for \n',
                                      'Rs.', amount_req, 'on 10% ROI for 18 months. The collateral provided by the user is', collateral.upper(),
                                      'Your monthly income is', salary, 'and your profession is', profession.upper())

                                print()
                                print('I', NAME.upper(), 'agree to repay the EDUCATIONAL loan of Rs.', amount_req, '\n'
                                                                                                                   'along with 10% ROI amounting totally to Rs.',
                                      return_amount, 'within the \n time period of 18 months',
                                      'I leave my ', collateral.upper(), 'as a guarantee that I will repay the loan I have taken')
                                print('''

                                ''')

                                card_spl = list(card)

                                if card_spl[3] == '-' and card_spl[8] == '-':
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    card_spl.pop(3)
                                    card_spl.pop(7)
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)

                                    print('Processing your loans'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                        time.sleep(1)
                                    print()
                                    print('loan approved!'.upper())
                                    print('''



                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print('''

                                    ''')

                                    break
                                elif '-' not in card_spl:
                                    pending_loans.append(card)
                                    card_spl.insert(3, '-')
                                    card_spl.insert(8, '-')
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    print('processing your loan'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print()
                                    print('loan approved'.upper())
                                    print('''

                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)

                                    break
                                else:
                                    print('please enter the card number in the correct format'.capitalize())

                            elif loan_for.upper() == 'MEDICAL' or int(loan_for) == 2:

                                amount_req = int(input('enter the required amount: '.capitalize()))

                                collateral = input('''Enter the collateral that you are providing to the bank
                                1. Jewellery
                                2. House
                                3. Gold
                                4. Land
                                5. Car \n''')

                                print('the rate of interest for Medical loan is 12%'.capitalize())
                                return_amount = 1.12 * amount_req

                                print()

                                print('This signing is to confirm and guarantee the repayment of the loan that\n ',
                                      'has been taken by applicant', NAME.upper(),
                                      '. This is a MEDICAL loan for \n',
                                      'Rs.', amount_req,
                                      'on 12% ROI for 18 months. The collateral provided by the user is',
                                      collateral.upper(),
                                      'Your monthly income is', salary, 'and your profession is', profession.upper())

                                print()
                                print('I', NAME.upper(), 'agree to repay the MEDICAL loan of Rs.', amount_req, '\n'
                                                                                                               'along with 12% ROI amounting totally to Rs.',
                                      return_amount, 'within the \n time period of 18 months',
                                      'I leave my ', collateral.upper(), 'as a guarantee that I will repay the loan I have taken')
                                print('''

                                ''')

                                card_spl = list(card)

                                if card_spl[3] == '-' and card_spl[8] == '-':
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    card_spl.pop(3)
                                    card_spl.pop(7)
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)

                                    print('Processing your loans'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                        time.sleep(1)
                                    print()
                                    print('loan approved!'.upper())
                                    print('''

                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print('''

                                    ''')

                                    break
                                elif '-' not in card_spl:
                                    pending_loans.append(card)
                                    card_spl.insert(3, '-')
                                    card_spl.insert(8, '-')
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    print('processing your loan'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print()
                                    print('loan approved'.upper())
                                    print('''

                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)

                                    break
                                else:
                                    print('please enter the card number in the correct format'.capitalize())

                            elif loan_for.upper() == 'Business' or int(loan_for) == 3:

                                amount_req = int(input('enter the required amount: '.capitalize()))
                                collateral = input('''Enter the collateral that you are providing to the bank
                                                                1. Jewellery
                                                                2. House
                                                                3. Gold
                                                                4. Land
                                                                5. Car \n''')
                                print('the rate of interest for Business loan is 10%'.capitalize())
                                return_amount = 1.1 * amount_req

                                print()

                                print('This signing is to confirm and guarantee the repayment of the loan that\n ',
                                      'has been taken by applicant', NAME.upper(),
                                      '. This is a BUSINESS loan for \n',
                                      'Rs.', amount_req,
                                      'on 10% ROI for 18 months. The collateral provided by the user is',
                                      collateral.upper(),
                                      'Your monthly income is', salary, 'and your profession is', profession.upper())

                                print()
                                print('I', NAME.upper(), 'agree to repay the BUSINESS loan of Rs.', amount_req, '\n'
                                                                                                                'along with 10% ROI amounting totally to Rs.',
                                      return_amount, 'within the \n time period of 18 months',
                                      'I leave my ', collateral.upper(),
                                      'as a guarantee that I will repay the loan I have taken')
                                print('''

                                ''')

                                card_spl = list(card)

                                if card_spl[3] == '-' and card_spl[8] == '-':
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    card_spl.pop(3)
                                    card_spl.pop(7)
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)

                                    print('Processing your loans'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                        time.sleep(1)
                                    print()
                                    print('loan approved!'.upper())
                                    print('''



                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print('''

                                    ''')

                                    break
                                elif '-' not in card_spl:
                                    pending_loans.append(card)
                                    card_spl.insert(3, '-')
                                    card_spl.insert(8, '-')
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    print('processing your loan'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print()
                                    print('loan approved'.upper())
                                    print('''

                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)

                                    break
                                else:
                                    print('please enter the card number in the correct format'.capitalize())

                            elif loan_for.upper() == 'Home & Auto' or int(loan_for) == 4:

                                amount_req = int(input('enter the required amount: '.capitalize()))
                                collateral = input('''Enter the collateral that you are providing to the bank
                                                                1. Jewellery
                                                                2. House
                                                                3. Gold
                                                                4. Land
                                                                5. Car \n''')
                                print('the rate of interest for Home & Auto loan is 6.75%'.capitalize())
                                return_amount = 1.0675 * amount_req

                                print()

                                print('This signing is to confirm and guarantee the repayment of the loan that\n ',
                                      'has been taken by applicant', NAME.upper(),
                                      '. This is a HOME & AUTO loan for \n',
                                      'Rs.', amount_req,
                                      'on 6.75% ROI for 18 months. The collateral provided by the user is',
                                      collateral.upper(),
                                      'Your monthly income is', salary, 'and your profession is', profession.upper())

                                print()
                                print('I', NAME.upper(), 'agree to repay the HOME & AUTO loan of Rs.', amount_req, '\n'
                                                                                                                   'along with 6.75% ROI amounting totally to Rs.',
                                      return_amount, 'within the \n time period of 18 months',
                                      'I leave my ', collateral.upper(),
                                      'as a guarantee that I will repay the loan I have taken')
                                print('''

                                ''')

                                card_spl = list(card)

                                if card_spl[3] == '-' and card_spl[8] == '-':
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    card_spl.pop(3)
                                    card_spl.pop(7)
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)

                                    print('Processing your loans'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                        time.sleep(1)
                                    print()
                                    print('loan approved!'.upper())
                                    print('''



                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print('''

                                    ''')

                                    break
                                elif '-' not in card_spl:
                                    pending_loans.append(card)
                                    card_spl.insert(3, '-')
                                    card_spl.insert(8, '-')
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    print('processing your loan'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print()
                                    print('loan approved'.upper())
                                    print('''

                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)

                                    break
                                else:
                                    print('please enter the card number in the correct format'.capitalize())

                            elif loan_for.upper() == 'Personal' or int(loan_for) == 5:

                                amount_req = int(input('enter the required amount: '.capitalize()))
                                collateral = input('''Enter the collateral that you are providing to the bank
                                1. Jewellery
                                2. House
                                3. Gold
                                4. Land
                                5. Car \n''')
                                print('the rate of interest for Personal loan is 11%'.capitalize())
                                return_amount = 1.11 * amount_req

                                print()

                                print('This signing is to confirm and guarantee the repayment of the loan that\n ',
                                      'has been taken by applicant', NAME.upper(),
                                      '. This is a PERSONAL loan for \n',
                                      'Rs.', amount_req,
                                      'on 11% ROI for 18 months. The collateral provided by the user is',
                                      collateral.upper(),
                                      'Your monthly income is', salary, 'and your profession is', profession.upper())

                                print()
                                print('I', NAME.upper(), 'agree to repay the PERSONAL loan of Rs.', amount_req, '\n'
                                                                                                                'along with 11% ROI amounting totally to Rs.',
                                      return_amount, 'within the \n time period of 18 months',
                                      'I leave my ', collateral.upper(),
                                      'as a guarantee that I will repay the loan I have taken')
                                print('''

                                ''')

                                card_spl = list(card)

                                if card_spl[3] == '-' and card_spl[8] == '-':
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    card_spl.pop(3)
                                    card_spl.pop(7)
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)

                                    print('Processing your loans'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                        time.sleep(1)
                                    print()
                                    print('loan approved!'.upper())
                                    print('''



                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print('''

                                    ''')

                                    break
                                elif '-' not in card_spl:
                                    pending_loans.append(card)
                                    card_spl.insert(3, '-')
                                    card_spl.insert(8, '-')
                                    rec_card = ''.join(card_spl)
                                    pending_loans.append(rec_card)
                                    print('processing your loan'.capitalize())
                                    print('please wait'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)
                                    print()
                                    print('loan approved'.upper())
                                    print('''

                                    ''')
                                    print('redirecting you to the login screen again'.capitalize(), end='')
                                    for i in range(3):
                                        time.sleep(1)
                                        print('.', end='')
                                    time.sleep(1)

                                    break
                                else:
                                    print('please enter the card number in the correct format'.capitalize())

                            else:
                                print('enter a valid choice: '.capitalize())
                        else:
                            print('entered name doesn\'t match'.capitalize())
                            print()
                            time.sleep(1)
                            print('redirecting you to the login screen again'.capitalize(), end='')
                            for i in range(3):
                                time.sleep(1)
                                print('.', end='')
                            time.sleep(1)
                            print('''                         

                            ''')
                            break
                else:
                    print('data not found!'.upper())
                    print('\n\n')
                    time.sleep(1)
                    print('server connection lost!'.capitalize())
                    print()
                    time.sleep(1)
                    print('redirecting you to the login screen again'.capitalize(), end='')
                    for i in range(3):
                        time.sleep(1)
                        print('.', end='')
                    time.sleep(1)
                    print('''

                    ''')

    elif choice.upper().lstrip().rstrip() == 'BANK' or choice.lstrip().rstrip() == '10':
        print('\n')
        print('System Details')
        print('\n\n')
        time.sleep(2)
        print('citizens\' financial inc \n\n'.upper())
        print('Established on       : January 1, 2021')
        print('\n\n')
        time.sleep(2)

        print('System Security Pack : CFI-12KU-779S ')
        print('System Type          : 64-bit Operating System')
        print()
        time.sleep(2)

        print('security patch       : 1-01-2021--16-41-48'.title())
        print('Bank ID              : 126P-75GH-78D')
        time.sleep(2)

        print()
        print('main head-office     : New Delhi, Central Vista, 110-032'.title())
        print('main city branch     : Bangalore North'.title())
        print('\n\n')
        time.sleep(4)

    elif choice.upper().lstrip().rstrip() == 'MAKERS' or choice.lstrip().rstrip() == '11':
        print()
        print('the founders'.title())
        print('\n\n')
        time.sleep(2)
        print('citizens\' financial inc \n\n'.upper())
        print('Founded on January 1ˢᵗ 2021')
        print()
        time.sleep(2)

        print('founders'.capitalize())
        print('''
        Abhijeet Rajhans      : 11A
        Armaan Shaikh         : 11A
        Zaid Khan Md.         : 11A 
        ''')
        time.sleep(2)
        print()
        print('this bank is the overall result of the extreme dedication and determination of all the heads, \n'
              'managers and especially the employees'.upper())
        print()
        print('the coding part took a while but it was worth the wait'.upper())
        print('''

        ''')
        time.sleep(4)

        print('''
        ________________________________________________________________________________________________________________
        Advertisement_______________________________________________________________________________________________i_X_

             .-="""""""""""=-.                                                                           _______
             | . . . . . . . |                    Free Delivery & Installation                          |_o_|_o_|
             | .'.'.'.'.'.'. |       Use Coupon Code: OFF50 & Get Flat 50% Off for first 3 months       |___o___|
            ()_______________()                    Applicable on all tenures*                           |___o___|
            ||_______________||               +Custom made furniture of your choice                     |___o___|
             W               W                                                                           ||   ||
        _________________________________________________________________________________________________________________
        ''')

    else:
        print('please enter a valid option'.capitalize())
