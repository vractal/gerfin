from telegram.ext import Updater, CommandHandler
from .models import Entry
import re
from decimal import Decimal


updater = Updater(token='609565119:AAEiBqFAW5FM--Xc_AIdx3ikfAWu7kEhMLk')

dispatcher = updater.dispatcher

def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text="Oi, eu sou seu bot. Meu nome é Adão!")



start_handler = CommandHandler("start",start)
dispatcher.add_handler(start_handler)


def gasto(bot,update):
    """ Manipulates input from command 'gasto' """
    text = update.message.text[6:]
    if len(text) > 0:
        r = re.search(r'^\s*(?P<amount>[\d\.,]*)\s*(?P<description>.*)$',text)
        if r.group('amount'):
            amount = float(r.group('amount').replace(',','.'))
        else:
            amount = 0
        description = r.group('description')
        Entry.objects.create(amount=amount,description=description)
        bot.send_message(chat_id=update.message.chat_id,text="Anotado!")
    else:
        bot.send_message(chat_id=update.message.chat_id,
                            text="Me parece que você não escreveu nada.. Gastou ou não gastou?\
                            siga esse formato: <comando> <valor> <descrição>. \nex: /gasto 5 batata frita ")


gasto_handler = CommandHandler("gasto",gasto)
dispatcher.add_handler(gasto_handler)


def saque(bot,update):
    """ Manipulates input from command 'saque' """
    text = update.message.text[6:]
    if len(text) > 0:
        r = re.search(r'^\s*(?P<amount>[\d\.,]*)\s*(?P<description>.*)$',text)
        if r.group('amount'):
            amount = float(r.group('amount').replace(',','.'))
        else:
            amount = 0
        description = r.group('description')
        Entry.objects.create(amount=amount,description=description,type="withdraw")
        bot.send_message(chat_id=update.message.chat_id,text="Anotado!")
    else:
        bot.send_message(chat_id=update.message.chat_id,
                            text="Me parece que você não escreveu nada.. Gastou ou não gastou?\
                            siga esse formato: <valor> <detalhes>. \n ex: /gasto 5 batata frita ")


def relatorio(bot,update):
    response = ""
    for item in Entry.objects.all():
        response += "-  " + item.get_amount + "   " + item.description + "\n"
    bot.send_message(chat_id=update.message.chat_id,text=response)

relatorio_handler = CommandHandler("relatorio",relatorio)
dispatcher.add_handler(relatorio_handler)
