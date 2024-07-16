import random
import time
import urllib
import json
from colorama import Fore, init
from data_worker import *
from proxy_checker import checkout_list_proxy
from requests_data import *
from response_view import *

init(autoreset=True)
proxy_for_test = {
    'http': 'http://yrdcniql:w1ardyejj2ul@104.222.185.235:5798',
    'https': 'http://yrdcniql:w1ardyejj2ul@104.222.185.235:5798'
}


def main():
    say_hello()

    data = reader_data_validate()
    print(f"{Fore.WHITE} Проверка прокси..")
    checkout_list_proxy(data)

    max_delay = 0

    while True:
        access_is_changed = False
        for i, acc in enumerate(data, 1):
            user_data = acc['query'].split('&')[1].split('=')[1]
            user_info = urllib.parse.unquote(user_data)
            user_info = json.loads(user_info)

            username = user_info.get('username', '')
            firstname = user_info.get('first_name', 'Unknown')

            proxy = None if acc['proxy'] == '' else {'http': acc['proxy'], 'https': acc['proxy']}
            query = acc['query']

            access_token = None if acc['access_token'] == '' else acc['access_token']
            if access_token is None:
                new_token = get_new_token(query, proxy)
                if new_token is not None:
                    access_token = new_token['token']['refresh']
                    print(f"{Fore.CYAN}Получен новый токен")
                    access_is_changed = True
                    acc['access_token'] = access_token
                else:
                    print(f"{Fore.RED}Не удалось получить новый токен")
                    exit()
            print(
                Fore.CYAN + f"\n\n===== [ {username} ({firstname}) ] =====             ",
                flush=True)

            blum_codes(proxy)

            time.sleep(1)
            time_now(access_token, proxy)

            time.sleep(1)
            user_me(access_token, proxy)

            time.sleep(1)
            view_balance_friends(access_token, proxy)

            time.sleep(1)
            view_daily_reward(access_token, proxy)

            time.sleep(1)
            response = user_balance(access_token, proxy)
            tickets = None
            if response is not None:
                print(f"{Fore.CYAN}[ BALANCE ] Баланс: {response.get('availableBalance', 'Нет данных')} токенов")
                tickets = response.get('playPasses', -1)
                print(f"{Fore.CYAN}[ BALANCE ] Билеты: {tickets} билетов")
                # если фарминг уже идет, или закончился
                if 'farming' in response:
                    farming_end = datetime.fromtimestamp(response['farming']['endTime'] // 1000)
                    if farming_end < datetime.now():
                        print(f"{Fore.CYAN}[ FARMING ] Фарминг закончился")
                        farming_resp = farming_start(access_token, proxy)
                        if farming_resp is not None:
                            if 'startTime' in farming_resp:
                                print(f"{Fore.CYAN}[ FARMING ] Фарминг начался.")
                                farming_end = datetime.fromtimestamp(farming_resp['endTime'] // 1000)
                                time_second_end = (farming_end - datetime.now()).total_seconds()
                                if time_second_end > max_delay:
                                    max_delay = time_second_end
                        else:
                            print(f"{Fore.CYAN}[ FARMING ] Не удалось начать фарминг.")
                    else:
                        print(f"{Fore.CYAN}[ FARMING ] Фарминг еще не закончился. Конец: {farming_end}")
                        time_second_end = (farming_end - datetime.now()).total_seconds()
                        if time_second_end > max_delay:
                            max_delay = time_second_end
                # если фарминг еще не начат
                else:
                    farming_resp = farming_start(access_token, proxy)
                    if farming_resp is not None:
                        if 'startTime' in farming_resp:
                            print(f"{Fore.CYAN}[ FARMING ] Фарминг начался.")
                            farming_end = datetime.fromtimestamp(farming_resp['endTime'] // 1000)
                            time_second_end = (farming_end - datetime.now()).total_seconds()
                            if time_second_end > max_delay:
                                max_delay = time_second_end

            if tickets is not None:
                while tickets > 0:
                    print(f"{Fore.CYAN}[ GAME ] Начинаем игру...")
                    game_start = play_game(access_token, proxy)
                    print(f"{Fore.CYAN}[ GAME ] Проверяем ответ от сервера..")
                    if game_start is not None and 'gameId' in game_start:
                        game_id = game_start['gameId']
                        print(f"{Fore.CYAN}[ GAME ] Игра началась")
                        time.sleep(random.randint(30, 35))
                        points = random.randint(180, 300)

                        game_claim = claim_game(access_token, proxy, game_id, points)
                        if game_claim is not None:
                            if game_claim == "OK":
                                print(f"{Fore.CYAN}[ GAME ] Получено {points} токенов")
                                tickets -= 1
                    else:
                        print(f"{Fore.CYAN}[ ERROR ] Не удалось получить ответ от сервера.")
                        break
                else:
                    print(f"{Fore.CYAN}[ GAME ] Тикеты закончились")

            print(f"{Fore.CYAN}{'=' * 40}\n\n")

        if access_is_changed:
            with open(DATA_FILE, mode='w', encoding='utf-8', newline='') as file:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()
                writer.writerows(data)
                print(f"{Fore.LIGHTYELLOW_EX}{'=' * 30}")
                print(f"{Fore.LIGHTYELLOW_EX}Токены записаны.")
        else:
            print(f"{Fore.LIGHTYELLOW_EX}{'=' * 30}")
        print(f"{Fore.LIGHTYELLOW_EX}Спим: {max_delay}\n{'=' * 300}")
        time.sleep(max_delay)
        max_delay = 0


def say_hello():
    print(Fore.BLUE + r"""  _____                  
 |  __ \                 
 | |__) |_ _ _ __  _   _ 
 |  ___/ _` | '_ \| | | |
 | |  | (_| | | | | |_| |
 |_|   \__,_|_| |_|\__,_|                             
""")
    print(Fore.CYAN + "Questions - https://t.me/Panunchik")
    print(Fore.CYAN + "GitHub - https://github.com/VrotNaoborot")


if __name__ == '__main__':
    main()
