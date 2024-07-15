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
            time_for_finish = view_balance_user(access_token, proxy)

            if time_for_finish > 0 and time_for_finish > max_delay:
                max_delay = time_for_finish

            print(f"{Fore.CYAN}{'=' * 40}\n\n")

        if access_is_changed:
            with open(DATA_FILE, mode='w', encoding='utf-8', newline='') as file:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()
                writer.writerows(data)
                print(f"{Fore.LIGHTYELLOW_EX}{'=' * 40}")
                print(f"{Fore.LIGHTYELLOW_EX}Токены записаны.")
        else:
            print(f"{Fore.LIGHTYELLOW_EX}{'=' * 40}")
        print(f"{Fore.LIGHTYELLOW_EX}Спим: {max_delay}\n{'=' * 40}")
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
