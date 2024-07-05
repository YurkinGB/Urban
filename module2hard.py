def password_selection(num):
    result = []
    number_list = list(range(num))

    for i in number_list[1: len(number_list) // 2 + 1]:
        for j in number_list[i + 1:]:
            if num % (i + j) == 0:
                result.append(str(i) + str(j))
    return result


def checking_results():
    s = ''
    right_answer = {3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645,
                    10: 141923283746,
                    11: 11029384756,
                    12: 12131511124210394857,
                    13: 112211310495867,
                    14: 1611325212343114105968,
                    15: 1214114232133124115106978,
                    16: 1317115262143531341251161079,
                    17: 11621531441351261171089,
                    18: 12151811724272163631545414513612711810,
                    19: 118217316415514613712811910,
                    20: 13141911923282183731746416515614713812911}

    print('Результат проверки.')
    print('_______________________________________________________________')
    for i in list(right_answer.keys()):
        s = ''.join(password_selection(i))
        print(i, '-', ''.join(password_selection(i)) == str(right_answer[i]))


number = int(input("Ввидите число: "))
print(number, " - ", *password_selection(number), sep='', end='\n\n')

checking_results()
