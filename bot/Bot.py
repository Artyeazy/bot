from telegram.ext import Updater, CommandHandler
from Handlers import start_handler,help_handler,random_handler, DeusVult_handler, Kpop_handler, copypasta_handler,thatface_handler, picsum_handler #Leo_handler

updater = Updater(token = '930001555:AAGadSOrdV4FEMU5w1fILnm3ZRVJBC_zDJk', use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(random_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(DeusVult_handler)
dispatcher.add_handler(Kpop_handler)
#dispatcher.add_handler(Leo_handler)
dispatcher.add_handler(copypasta_handler)
dispatcher.add_handler(thatface_handler)
dispatcher.add_handler(picsum_handler)

updater.start_polling() 