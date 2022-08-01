
def check_answer(answer_entered, correct_answer):
    print('Верно') if answer_entered == correct_answer else print('Неверно')
    return answer_entered == correct_answer


def ask_smth(question):
    answer = input(f'{question}')
    return answer


pshkn = {'В каком году родился Пушкин': '1799', 'В какой день родился Пушкин': '6.06'}

def victory(questions_dict):
    for key in questions_dict.keys():
        answer = ask_smth(key)
        while not check_answer(answer, questions_dict[key]):
            answer = ask_smth(key)

if __name__ == '__main__':
    victory(pshkn)