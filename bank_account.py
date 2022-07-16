account_balance = 0
recent_purchases = {}

# проверяет наличие названия покупки в словаре, в случае повтора добавляет звездочку к названию
def key_check(search_dict):
    newkey = input('Введите название:')
    if newkey in search_dict:
        newkey += '*'
    else:
        newkey = newkey
    return newkey

# проверяет наличие средств и заносит в словарь покупки
def purchase(balance):
    price = float(input('Введите сумму покупки: '))
    if price > balance:
        print('Недостаточно средств, сначала пополните счет.')
        pass
    else:
        balance -= price
        purchase_name = key_check(recent_purchases)
        recent_purchases.update({purchase_name: price})
    return balance

#пополняет баланс
def top_up(balance):
    amount = float(input('Для пополнения ведите сумму: '))
    return amount
# показывает отформатированный список покупок
def show_purchases(purchases_dictionary):
    for key, value in purchases_dictionary.items():
        print(f'Название: {key} - Сумма: {value}')

# сам код
def accounting():
    account_balance = 0
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
            account_balance = purchase(account_balance)
            pass
        elif choice == '3':
            show_purchases(recent_purchases)
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

