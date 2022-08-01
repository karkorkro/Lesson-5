import os
import json


# проверяет наличие названия покупки в словаре, в случае повтора добавляет звездочку к названию
def key_check(search_dict):
    new_key = input('Введите название:')
    if new_key in search_dict:
        new_key += '*'
    else:
        new_key = new_key
    return new_key


# проверяет наличие средств, вычитает сумму покупки из баланса, выдает False если средств недостаточно
def charging(balance, price):
    balance = float(balance)
    price = float(price)
    if price > balance:
        return False
    else:
        balance -= price
        return balance


# выдает название и стоимость покупки как словарь
def recording_purchase(storing_dict, price):
    purchase_name = key_check(storing_dict)
    amount = price
    return {purchase_name: amount}


# пополняет баланс
def top_up(balance):
    amount = float(input('Для пополнения ведите сумму: '))
    balance = float(balance)
    balance += amount
    return balance


# показывает отформатированный список покупок
def show_purchases(purchases_dictionary):
    for key, value in purchases_dictionary.items():
        print(f'Название: {key} - Сумма: {value}')


# сам код
def accounting():
    if os.path.exists('acc_balance.txt'):
        with open('acc_balance.txt', 'r') as f:
            account_balance = f.read()
    else:
        account_balance = 0
        with open('acc_balance.txt', 'w') as f:
            f.write(f'{account_balance}')

    if os.path.exists('purchases_file.json'):
        with open('purchases_file.json') as f:
            recent_purchases = json.load(f)
    else:
        recent_purchases = {}

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            account_balance = top_up(account_balance)
        elif choice == '2':
            price = float(input('Введите сумму покупки: '))
            if charging(account_balance, price):
                account_balance = charging(account_balance, price)
                new_purchase = recording_purchase(recent_purchases, price)
                recent_purchases.update(new_purchase)
            else:
                print('Недостаточно средств, сначала пополните счет.')
            pass
        elif choice == '3':
            if os.path.exists('purchases_file.json'):
                show_purchases(recent_purchases)
            else:
                print('Покупок не найдено')
            pass
        elif choice == '4':
            with open('acc_balance.txt', 'w') as f:
                f.write(f'{account_balance}')
            with open('purchases_file.json', 'w') as f:
                json.dump(recent_purchases, f)
            break
        else:
            print('Неверный пункт меню')


if __name__ == 'main':
    accounting()
