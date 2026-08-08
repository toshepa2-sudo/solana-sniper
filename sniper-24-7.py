import requests
import time
from datetime import datetime
NTFY_TOPIC ="ali-sniper-alam-77x9k2"
MIN_LIQUIDITY = 5000
CHECK_INTERVAL = 15
seen_tokens = set() 
def send_ntfy(title, message):
  try:
    requests.post(
      f"https://ntfy.sh/{NTFY_TOPIC}",
      data=message.encode('utf-8'),
      headers={ 
        "Title": title,
        "Priority": "high",
        "Tags": "rocket,moneybag"
      }, timeout=10
    ) print(f"[{datetime.now()}] تم ارسال: {title}") 
  except Exception as e:
    print(f"خطأ بالارسال: {e}")
    def check_new_pairs():
      try: 
        url = "https://api.dexscreener.com/token-boosts/latest/v1"
        r = requests.get(url, timeout=15) 
        data = r.json() 
        for item in data[:20]:
          token_addr = item.get('tokenAddress', '') 
          if token_addr in seen_tokens:
            continue
            try:
             url = "https://api.dexscreener.com/token-boosts/latest/v1"
              r = requests.get(url, timeout=15)
              data = r.json()
              for item in data[:20]:
                token_addr 
