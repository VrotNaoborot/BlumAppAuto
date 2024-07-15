import json
import random
import requests
from colorama import Fore, init
from getuseragent import UserAgent

init(autoreset=True)
ua = UserAgent("android")
useragent = random.choice(ua.list)


def blum_codes(proxy=None):
    headers = {
        'upgrade-insecure-requests': '1',
        'user-agent': useragent,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://telegram.blum.codes/'
    try:
        if proxy is None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, proxies=proxy)

        response.raise_for_status()
        return response
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None


def user_me(token, proxy=None):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': "Bearer " + token,
        'user-agent': useragent,
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://gateway.blum.codes/v1/user/me'
    try:
        if proxy is None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, proxies=proxy)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None


def friends_balance(token, proxy=None):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': "Bearer " + token,
        'user-agent': useragent,
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://gateway.blum.codes/v1/friends/balance'
    try:
        if proxy is None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, proxies=proxy)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None


def time_now(token, proxy=None):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': "Bearer " + token,
        'user-agent': useragent,
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://game-domain.blum.codes/api/v1/time/now'
    try:
        if proxy is None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, proxies=proxy)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None


def user_balance(token, proxy=None):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': "Bearer " + token,
        'user-agent': useragent,
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://game-domain.blum.codes/api/v1/user/balance'
    try:
        if proxy is None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, proxies=proxy)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None


def farming_claim(token, proxy=None):
    headers = {
        'content-length': '0',
        'accept': 'application/json, text/plain, */*',
        'authorization': "Bearer " + token,
        'user-agent': useragent,
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://game-domain.blum.codes/api/v1/farming/claim'
    try:
        if proxy is None:
            response = requests.post(url, headers=headers)
        else:
            response = requests.post(url, headers=headers, proxies=proxy)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None


def farming_start(token, proxy=None):
    headers = {
        'content-length': '0',
        'accept': 'application/json, text/plain, */*',
        'authorization': "Bearer " + token,
        'user-agent': useragent,
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://game-domain.blum.codes/api/v1/farming/start'
    try:
        if proxy is None:
            response = requests.post(url, headers=headers)
        else:
            response = requests.post(url, headers=headers, proxies=proxy)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError as j:
        print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
        return None
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None


def daily_reward(token, proxy=None):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': "Bearer " + token,
        'user-agent': useragent,
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://game-domain.blum.codes/api/v1/daily-reward?offset=-180'
    try:
        if proxy is None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, proxies=proxy)
        return response.json(), response.status_code
    except json.JSONDecodeError as j:
        print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
        return None, -1
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None, -1
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None, -1
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None, -1


def claim_daily_reward(token, proxy=None):
    headers = {
        'content-length': '0',
        'accept': 'application/json, text/plain, */*',
        'authorization': "Bearer " + token,
        'user-agent': useragent,
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://game-domain.blum.codes/api/v1/daily-reward?offset=-180'
    try:
        if proxy is None:
            response = requests.post(url, headers=headers)
        else:
            response = requests.post(url, headers=headers, proxies=proxy)
        return response.text, response.status_code
    except json.JSONDecodeError as j:
        print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
        return None, -1
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None, -1
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None, -1
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None, -1


def friends_claim(token, proxy):
    headers = {
        'content-length': '0',
        'accept': 'application/json, text/plain, */*',
        'authorization': "Bearer " + token,
        'user-agent': useragent,
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    url = 'https://game-domain.blum.codes/api/v1/daily-reward?offset=-180'
    try:
        if proxy is None:
            response = requests.post(url, headers=headers)
        else:
            response = requests.post(url, headers=headers, proxies=proxy)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError as j:
        print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
        return None, -1
    except requests.HTTPError as http_err:
        print(f"{Fore.RED}HTTP ошибка: {http_err}")
        return None, -1
    except requests.RequestException as req_err:
        print(f"{Fore.RED}Ошибка запроса: {req_err}")
        return None, -1
    except Exception as ex:
        print(f"{Fore.RED}Неизвестная ошибка: {ex}")
        return None, -1


def get_new_token(query_id, proxy):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'user-agent': useragent,
        'content-type': 'application/json',
        'origin': 'https://telegram.blum.codes',
        'x-requested-with': 'org.telegram.messenger.web',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    data = json.dumps({"query": query_id})
    url = "https://gateway.blum.codes/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
    for i in range(3):
        try:
            if proxy is None:
                response = requests.post(url, headers=headers, data=data)
            else:
                response = requests.post(url, headers=headers, data=data, proxies=proxy)
            response.raise_for_status()
            return response.json()
        except json.JSONDecodeError as j:
            print(f"{Fore.RED}Ошибка при декодировании JSON ответа: {j}")
            return None
        except requests.HTTPError as http_err:
            print(f"{Fore.RED}HTTP ошибка: {http_err}")
            return None
        except requests.RequestException as req_err:
            print(f"{Fore.RED}Ошибка запроса: {req_err}")
            return None
        except Exception as ex:
            print(f"{Fore.RED}Неизвестная ошибка: {ex}")
            return None
    print(f"{Fore.CYAN}Три попытки получить токен не увенчались успехом.")
    return None