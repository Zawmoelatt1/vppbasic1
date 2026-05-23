import requests
from stem import Signal
from stem.control import Controller
import time
import json

# Tor Proxy Setting
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def get_ip_details():
    try:
        # IP အပြင် နိုင်ငံနဲ့ မြို့ကိုပါ သိရအောင် ip-api ကို သုံးပါမယ်
        response = requests.get('http://ip-api.com/json/', proxies=proxies, timeout=20)
        data = response.json()
        return data
    except Exception as e:
        return None

def change_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            return True
    except Exception:
        return False

print("--- [ ZM IP Changer Pro Loaded ] ---")
rotate_count = 1

try:
    # ခဏခဏ ပြောင်းချင်ရင် ဒီ Loop ထဲမှာ ထည့်ထားပါမယ်
    while True:
        print(f"\n[{rotate_count}] IP ကို စစ်ဆေးနေသည်...")
        info = get_ip_details()
        
        if info and info.get('status') == 'success':
            print(f"📍 လက်ရှိ IP: {info.get('query')}")
            print(f"🌍 နိုင်ငံ: {info.get('country')} ({info.get('city')})")
            print(f"🏢 ISP: {info.get('isp')}")
        else:
            print("❌ Tor ချိတ်ဆက်မှု မရသေးပါ။ Tor run ထားတာ သေချာပါစေ။")

        print("\n⏳ (၁) မိနစ် စောင့်ဆိုင်းပြီးနောက် IP အသစ် ပြောင်းပါမည်...")
        time.sleep(60) # ဒီနေရာမှာ စက္ကန့်ကို စိတ်ကြိုက်ပြင်နိုင်ပါတယ်။ (ဥပမာ ၃၀၀ ဆိုရင် ၅ မိနစ်)

        print("🔄 IP အသစ် ပြောင်းလဲနေသည်...")
        if change_tor_ip():
            rotate_count += 1
            time.sleep(5) # Tor circuit အသစ်တည်ဆောက်ချိန် ခဏစောင့်ပေးခြင်း
        else:
            print("⚠️ Control Port ချိတ်မရပါ။ torrc file ကို စစ်ဆေးပါ။")

except KeyboardInterrupt:
    print("\n\n🛑 အစီအစဉ်ကို ရပ်တန့်လိုက်ပါပြီ။")
