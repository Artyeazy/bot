from telegram.ext import CommandHandler
from functions import start_response, help_response, random_response, DeusVult_response, Kpop_response, copypasta_response, thatface_response,picsum_response #Leo_response

start_handler = CommandHandler('start', start_response)
help_handler = CommandHandler('help', help_response)
random_handler = CommandHandler('random', random_response)
DeusVult_handler = CommandHandler('DeusVult', DeusVult_response)
Kpop_handler = CommandHandler('Kpop', Kpop_response)
#Leo_handler = CommandHandler('Leo', Leo_response)
copypasta_handler = CommandHandler('copy', copypasta_response)
thatface_handler= CommandHandler('That face', thatface_response)
picsum_handler= CommandHandler('IMG',picsum_response)