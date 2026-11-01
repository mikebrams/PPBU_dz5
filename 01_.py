import requests

COINS = {
    "bitcoin": "Bitcoin (BTC)",
    "ethereum": "Ethereum (ETH)",
    "binancecoin": "BNB (BNB)",
    "solana": "Solana (SOL)",
    "ripple": "XRP (XRP)",
    "cardano": "Cardano (ADA)",
    "dogecoin": "Dogecoin (DOGE)",
    "polkadot": "Polkadot (DOT)"
}

"""Запрос к API CoinGecko."""
ids = ",".join(COINS.keys())
print(ids)
url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"

# url = 'https://api.coingecko.com/api/v3/coins/markets'

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)

except Exception as e:
    print(e)
#
#     # Обновление интерфейса в основном потоке
#     self.root.after(0, self.update_table, data)
#
# except requests.exceptions.RequestException as e:
#     self.root.after(0, self.show_error, f"Ошибка сети или API: {e}")
# except Exception as e:
#     self.root.after(0, self.show_error, f"Неизвестная ошибка: {e}")



response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true')
data = response.json()

print(data)

