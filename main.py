from pycoingecko import CoinGeckoAPI
from colorama import Fore
import requests


cg = CoinGeckoAPI()

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET
spacer = "*" * 75
dashes = "-" * 18


prices = cg.get_price(ids=['dark-energy-crystals', 'splinterlands', 'shiba-inu', 'floki-inu'], vs_currencies='usd')
dec = prices['dark-energy-crystals']['usd']
sps = prices['splinterlands']['usd']
shib = prices['shiba-inu']['usd']
floki = prices['floki-inu']['usd']

def decPrice():
    decAmount = input('Amount: ')
    numberInDollars = float(decAmount) * float(dec)
    print(spacer)
    print(f"{GREEN} Current DEC Price: {dec}\n", decAmount, "DEC is equivalent to $", int(numberInDollars), f"{RESET}")
    print(spacer)



def spsPrice():
    spsAmount = input('Amount: ')
    numberInDollars = float(spsAmount) * float(sps)
    print(spacer)
    print(f"{GREEN} Current SPS Price: {sps}\n", spsAmount, "SPS is equivalent to $", int(numberInDollars), f"{RESET}")
    print(spacer)


def landPrice():
    url = "https://wax.api.atomicassets.io/atomicmarket/v1/sales?state=1&collection_name=splintrlands&schema_name=land.claims&page=1&limit=1&order=asc&sort=price"
    response = requests.get(url)
    response = response.json()
    data = response['data']

    storage = {}

    for k, v in [(key, d[key]) for d in data for key in d]:
        if k not in storage:
            storage[k] = [v]
        else:
            storage[k].append(v)

    data = storage['price']

    storage = {}

    for k, v in [(key, d[key]) for d in data for key in d]:
        if k not in storage:
            storage[k] = [v]
        else:
            storage[k].append(v)

    amount = storage['amount']
    amount = str(amount)[2:-10]

    waxAPI = "https://api.coingecko.com/api/v3/simple/price?ids=wax&vs_currencies=usd"
    response = requests.get(waxAPI)
    response = response.json()
    data = response['wax']
    waxPrice = data['usd']
    landPrice = float(amount) * float(waxPrice)

    print(spacer)
    print(f"{GREEN}Lowest available LAND price: $", int(landPrice), f"{RESET}")
    print(spacer)



def shibPrice():
    shibAmount = input('Amount: ')
    numberInDollars = float(shibAmount) * float(shib)
    print(spacer)
    print(f"{GREEN} Current SHIB Price: {shib}\n", shibAmount, "SHIB is equivalent to $", float(numberInDollars), f"{RESET}")
    print(spacer)


def flokiPrice():
    flokiAmount = input('Amount: ')
    numberInDollars = float(flokiAmount) * float(floki)
    print(spacer)
    print(f"{GREEN} Current Floki Price: {floki}\n", flokiAmount, "Floki is equivalent to $", float(numberInDollars), f"{RESET}")
    print(spacer)

#$end
def menu():
    selection = input("""
    Splinterlands Price Converter\n
    A: DEC
    B: SPS
    C: LAND
    D: SHIB
    E: FLOKI
    X: Exit
    Select which currency you would like to convert to USD:
    """)
    print(spacer)

    if selection.lower() == "a":
        decPrice(), menu()
    elif selection.lower() == "b":
        spsPrice(), menu()
    elif selection.lower() == "c":
        landPrice(), menu()
    elif selection.lower() == "d":
        shibPrice(), menu()
    elif selection.lower() == "e":
        flokiPrice(), menu()
    elif selection.lower() == "x":
        exit()
    else:
        print(spacer)
        print(dashes, f"{RED}ERROR: You picked an invalid option.", dashes)
        print(dashes, f"Returning to main menu.{RESET}", dashes)
        print(spacer)
        menu()


menu()