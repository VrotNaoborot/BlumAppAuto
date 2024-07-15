from requests_data import *
from datetime import datetime


def view_balance_user(token, proxy):
    """Возвращает время до конца фарминга"""
    response = user_balance(token, proxy)
    if response is not None:
        print(f"{Fore.CYAN}[ BALANCE ] Баланс: {response.get('availableBalance', 'Нет данных')} токенов")
        print(f"{Fore.CYAN}[ BALANCE ] Билеты: {response.get('playPasses', 'Нет данных')} билетов")
        if 'farming' in response:
            farming_end = datetime.fromtimestamp(response['farming']['endTime'] // 1000)
            if farming_end < datetime.now():
                print(f"{Fore.CYAN}[ FARMING ] Фарминг закончился")
                farming_resp = farming_start(token, proxy)
                if farming_resp is not None:
                    if 'startTime' in farming_resp:
                        print(f"{Fore.CYAN}[ FARMING ] Фарминг начался.")
                        farming_end = datetime.fromtimestamp(farming_resp['endTime'] // 1000)
                        return (farming_end - datetime.now()).total_seconds()
                else:
                    print(f"{Fore.CYAN}[ FARMING ] Не удалось начать фарминг.")
                return -1
            else:
                print(f"{Fore.CYAN}[ FARMING ] Фарминг еще не закончился. Конец: {farming_end}")
                seconds_for_finish = farming_end - datetime.now()
                return seconds_for_finish.total_seconds()
        else:
            farming_resp = farming_start(token, proxy)
            if farming_resp is not None:
                if 'startTime' in farming_resp:
                    print(f"{Fore.CYAN}[ FARMING ] Фарминг начался.")
                    farming_end = datetime.fromtimestamp(farming_resp['endTime'] // 1000)
                    return (farming_end - datetime.now()).total_seconds()
    else:
        return -1


def view_balance_friends(token, proxy):
    response = friends_balance(token, proxy)
    if response is not None:
        ref_friends = response['usedInvitation']
        if int(ref_friends) > 0:
            print(f"{Fore.CYAN}[ FRIENDS ] Ваши рефералы: {response['usedInvitation']}")
            print(f"{Fore.CYAN}[ FRIENDS ] Рефералы принесли: {response['amountForClaim']}")
            can_claim = response['canClaim']
            if can_claim:
                resp_claim, code_claim = friends_claim(token, proxy)
                if resp_claim is not None and code_claim == 200:
                    if 'claimBalance' in resp_claim:
                        print(f"{Fore.CYAN}[ FRIENDS ] Токены за рефералов собраны.")
            else:
                print(f"{Fore.CYAN}[ FRIENDS ] Claim токенов не доступен.")
        else:
            print(f"{Fore.CYAN}[ FRIENDS ] У вас нет рефералов.")
    else:
        print(f"{Fore.CYAN}[ FRIENDS ] Ошибка.")


def view_daily_reward(token, proxy):
    response, status = daily_reward(token, proxy)
    if response is not None:
        if 'countInRow' in response and status == 200:
            claim_resp, claim_code = claim_daily_reward(token, proxy)
            if claim_code == 200 and claim_resp == "OK":
                print(f"{Fore.CYAN}[ DAILY ] Ежедневный бонус получен.")
            else:
                print(f"{Fore.RED}[ DAILY ] Не удалось получить ежедневный бонус.")
        elif response['message'] == 'Not Found':
            print(f"{Fore.CYAN}[ DAILY ] Ежедневный бонус уже собран.")
    else:
        print(f"{Fore.CYAN}[ DAILY ] Ошибка.")
