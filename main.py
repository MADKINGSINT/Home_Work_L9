from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
spisok = []


updater = Updater("5651028696:AAEHXaCjyq7Xt4JJSUqpralSqoI-e-MaEig")
dp = updater.dispatcher

def show_menu(update, context) -> None:
    print("user is in choosing menu now")
    
    update.message.reply_text('Выберите команду:\n /1 - показать всех сотрудников\n'
        ' /2 - добавить сотрудника\n /3 - поиск сотрудника\n /4 - удалить сотрудника')
        
def append_data(update, context):
    
    print('appending data')
    spisok.append(update.message.text)
    update.message.reply_text("Данныe успешно отправлены")
    return conv_hand_add.END
        
    
    
    
def get_list(update, context) :
    print('user is looking for people now')
    update.message.reply_text('Список всех сотрудников :')  
    i = 1
    for line in spisok:
        
            update.message.reply_text(f'{i}: {line}')
            i += 1
        
 
def add_data (update, context):
    print("user is adding people now")
    update.message.reply_text("Пишите данные через пробел")
    return 1



def ask_user (update, context):
    update.message.reply_text("Введите имя или фамилию")
    text_handler_find = MessageHandler(Filters.text & ~Filters.command, find_data)
    dp.add_handler(text_handler_find)
    return 1
    


def find_data(update, context):
    finding = update.message.text
    for line in spisok:
        temp = str(line).split()
        for word in temp:
            if word == finding:
                update.message.reply_text(line)
                break
    return conv_hand_find.END
def ask_for_deleting(update, context):
    i =1
    for line in spisok:
        
        
            update.message.reply_text(f'{i}: {line}')
            i += 1
      
    update.message.reply_text("Введите номер строки, которую хотите удалить")
    return 1
def delete_data (update, context):
    number = update.message.text
    spisok.pop(int(number) - 1)
    update.message.reply_text("Готово")
    return conv_hand_delete.END

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
updater = Updater("5651028696:AAEHXaCjyq7Xt4JJSUqpralSqoI-e-MaEig")
dp = updater.dispatcher

print('starting server (Phase 1)')


print("starting server(Phase 2)")

print("server started")

dp.add_handler(CommandHandler("start", show_menu))
dp.add_handler(CommandHandler('1', get_list))
conv_hand_add = ConversationHandler(
    entry_points=[CommandHandler('2', add_data)],
    states={1: [MessageHandler(Filters.text & ~Filters.command, append_data)]
            
    },

    fallbacks=[CommandHandler('stop', show_menu)]
    )
dp.add_handler(conv_hand_add)



conv_hand_find = ConversationHandler(
    entry_points=[CommandHandler('3', ask_user)],
    states={1: [MessageHandler(Filters.text & ~Filters.command, find_data)]
            
    },

    fallbacks=[CommandHandler('stop', show_menu)]
    )
dp.add_handler(conv_hand_find)

conv_hand_delete = ConversationHandler(
    entry_points=[CommandHandler('4', ask_for_deleting)],
    states={1: [MessageHandler(Filters.text & ~Filters.command, delete_data)]
            
    },

    fallbacks=[CommandHandler('stop', show_menu)]
    )
dp.add_handler(conv_hand_delete)

updater.start_polling()
updater.idle()

