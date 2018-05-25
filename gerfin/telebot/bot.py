from telegram.ext import Updater, CommandHandler
from .models import Entry
import re
from .token import token

updater = Updater(token=token)

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
                            text="Me parece que você não escreveu nada.. Gastou ou não gastou?\n\
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
                            text="Me parece que você não escreveu nada.. Sacou mesmo?\n\
                            siga esse formato: <valor> <detalhes>. \nex: /gasto 5 batata frita ")


saque_handler = CommandHandler("saque",saque)
dispatcher.add_handler(saque_handler)

def relatorio(bot,update):
    response = ""
    for item in Entry.objects.all():
        if item.type == 'withdraw':
            response += "+  " + item.get_amount + "   " + item.description + "\n"
        else:
            response += "-  " + item.get_amount + "   " + item.description + "\n"
    bot.send_message(chat_id=update.message.chat_id,text=response)

relatorio_handler = CommandHandler("relatorio",relatorio)
dispatcher.add_handler(relatorio_handler)
