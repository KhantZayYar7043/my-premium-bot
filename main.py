import os
import time
from threading import Thread
from flask import Flask
import telebot

# ၁။ Render ပေါ်မှာ Bot ၂၄ နာရီ ရှင်သန်နေစေရန် Web Server ပတ်မောင်းခြင်း
app = Flask('')

@app.route('/')
def home():
    return "Premium Bot is Running 24/7!"

def run():
    # Render က ပေးမယ့် Port နံပါတ်ကို အလိုအလျောက် ဖတ်ခိုင်းခြင်း
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ၂။ ကိုယ့်ရဲ့ Telegram Bot Token ကို ဒီမှာ ထည့်ပါ
# (💡 လုံခြုံရေးအရ Render Environment Variable ထဲမှာလည်း ထည့်ထားလို့ ရပါတယ်)
BOT_TOKEN = "8606469842:AAGgd_dqx1fuR507GSwUzPnOIb3TJifa2E4"
bot = telebot.TeleBot(BOT_TOKEN)

# ၃။ Bot ရဲ့ အလုပ်လုပ်မည့် Function များ (အစ်ကို့ရဲ့ Premium Logic တွေ ဒီအောက်မှာ ထည့်ပါ)
@bot.message_handler(commands=['start'])
def start_command(message):
    welcome_text = (
        "👋 မင်္ဂလာပါ အစ်ကိုရေ!\n\n"
        "🚀 ဒီ Premium Bot ကို GitHub + Render စနစ်နဲ့ "
        "၂၄ နာရီပတ်လုံး အခမဲ့ အောင်အောင်မြင်မြင် မောင်းနှင်ထားပါတယ်ဗျာ။"
    )
    bot.reply_to(message, welcome_text)

# ၄။ Error တက်ပြီး Bot ရပ်မသွားစေရန် အဓိက မောင်းနှင်မည့် Loop အပိုင်း
if __name__ == "__main__":
    # အရင်ဆုံး Web Server ကို အနောက်မှာ အသက်သွင်းမည်
    keep_alive()
    print("Web Server Started. Starting Telegram Bot...")
    
    # Bot ကို အမြဲတမ်း Run နေစေပြီး Error တက်ရင်လည်း Auto ပြန်ပွင့်စေမည့်စနစ်
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Error အချို့ ဖြစ်ပွားခဲ့သည်: {e}")
            time.sleep(15)  # ၁၅ စက္ကန့် စောင့်ပြီး Auto ပြန်ပတ်မောင်းမည်
