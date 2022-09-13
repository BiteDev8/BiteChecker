#script by Jansy-cc and review by bitedev8
#script by Jansy-cc and review by bitedev8

from colorama import Fore, Back, Style, init
from requests import get, post
from random import randint
import pyfiglet
init()
Tarace = "BiteChecker"
ASCII_art_1 = pyfiglet.figlet_format(Tarace)
print(ASCII_art_1)


def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'
print(Fore.GREEN+"Entré pour commencer")
input()
if __name__ == "__main__":
    try:
        checked = []
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
                    print(f'BiteToken: {token} is invalid')
                    checked.append(token)
                else:
                    print(f'BiteToken: {token} is Valid  <=== True')
        if len(checked) > 0:
            save = input('Save valid tokens\nSave to File (y/n)').lower()
            if save == 'y':
                with open('BiteToken.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print('Tokens Save To BiteToken.txt File!')
        input('Press Enter For Exit...')
    except:
        input('Can`t Open "tokens.txt" File!')

#script by Jansy-cc and review by bitedev8
#script by Jansy-cc and review by bitedev8
