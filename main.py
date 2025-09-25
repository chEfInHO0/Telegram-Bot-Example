###############################################################
################        ##################
###############################################################
###############################################################


from telegram import Update, ReplyKeyboardMarkup  # type:ignore
from telegram.ext import Application, CommandHandler, MessageHandler,  filters, ContextTypes, ConversationHandler  # type:ignore
from os import environ
from dotenv import load_dotenv
from EmailFinder.email.main import get_pwd
from BlockBot.main import blockbot
from Logs.main import setup_logger
from datetime import datetime
from Utils.alert import Alert


PREVENT_EXECUTION = False

if PREVENT_EXECUTION:
    alert = Alert(
        "CONFIRA SE O SEU .env ESTÁ CONFIGURADO CORRETAMENTE", "warning")
    alert.display()
    alert = Alert(
        "CONFIRA SE O SEU .env ESTÁ INCLUSO EM SEU GITIGNORE", "critical")
    alert.display()
    alert = Alert(
        "ALTERE A CONSTANTE `PREVENT_EXECUTION APOS VERIFICAR OS ITENS ACIMA`", "critical")
    alert.display()
    raise SystemExit


DEBUG = 10
INFO = 20
WARN = 30
ERROR = 40
CRITICAL = 50

user_interaction = list()

ACTION, EMAIL = range(2)

debug_log = setup_logger('debugger.logger', 'debug.log', DEBUG)
command_log = setup_logger('command_logger', 'commands.log', INFO)
warning_log = setup_logger('warning_logger', 'warnings.log', WARN)
error_log = setup_logger('error_logger', 'errors.log', ERROR)

load_dotenv()

BOT_NAME = environ.get("BOT_NAME")
TOKEN = environ.get("TOKEN")
AUTH_GRANTED = environ.get("AUTH_GRANTED")


async def template_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name: str = update.message.chat.first_name  # Pegar o nome do usuario
    user_lastname: str = update.message.chat.last_name  # Pegar o sobrenome do usuario
    id = update.message.chat.id  # Pegar o ID do usuario
    text = update.message.text  # Pegar o texto enviado pelo usuario
    await update.message.reply_text('Template command')  # Responder o usuario


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name: str = update.message.chat.first_name
    user_lastname: str = update.message.chat.last_name
    await update.message.reply_text(f'Olá {user_name}, tudo bem?')


async def e_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = update.message.chat.id
    text = update.message.text
    if blockbot():
        await update.message.reply_text(
            f'por questões de segurança esse função é inativa após as 17:30 🕠'
        )
        command_log.info(f'User {id} enviou {text} após as 17:30')
    else:
        command_log.info(f'User {id} enviou {text}')
        if str(id) in AUTH_GRANTED:
            text = text.split('/e')[-1].strip()
            if '@' not in text:
                await update.message.reply_text(
                    f'{text} não é um email'
                )
            else:
                print(text)
                pwd = get_pwd(email=text)
                print(pwd)
                if pwd != None:
                    await update.message.reply_text(
                        pwd
                    )
                else:
                    await update.message.reply_text(
                        'Email não localizado ☹'
                    )
        else:
            await update.message.reply_text(
                "Não autorizado 🤚🛑"
            )


async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Testando"
    )


async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Pong')


def handle_responses(user_id: int, text: str) -> str:
    message = text.lower()
    command_log.info(f'User {user_id} enviou {text}')
    print(f'Mensagem de {user_id}')
    if str(user_id) in AUTH_GRANTED:
        if str(user_id) == "5967543461":
            return "✨ Este é um bot de um assassino Lívia ✨"

        return 'Você está na lista de autorizados! 😁'
    else:
        return 'Me desculpe, mas momento apenas usuários autorizados podem receber mensagens personalizadas aqui 😢'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    user_id: int = update.message.chat.id
    user_name: str = update.message.chat.first_name
    user_lastname: str = update.message.chat.last_name
    if len(user_interaction) == 0:
        user_interaction.append([user_name, user_lastname, user_id])
    else:
        for interection in user_interaction:
            if user_id not in interection:
                user_interaction.append([user_name, user_lastname, user_id])

    if message_type == 'group':
        if BOT_NAME in text:
            group_text: str = text.replace(BOT_NAME, '').strip()
            response: str = handle_responses(user_id, group_text)
        else:
            return
    else:
        response: str = handle_responses(user_id, text)
    print('Bot : ', response)
    command_log.info(
        f'Usuario {user_id} envio em {message_type} a mesagem {text}')
    command_log.info(user_interaction)
    await update.message.reply_text(response)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Msg : {update}, ocasionou o erro {context.error}')
    error_log.error(f'Msg : {update}, ocasionou o erro {context.error}')


def main():
    print('Starting...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('test', test_command))
    app.add_handler(CommandHandler('ping', ping_command))
    app.add_handler(CommandHandler('e', e_command))

    app.add_handler(MessageHandler(filters.TEXT,  handle_message))

    app.add_error_handler(error_handler)
    print('Refreshing...')
    app.run_polling(poll_interval=3)


if __name__ == '__main__':
    command_log.info(f'Bot iniciado as {datetime.today()}')
    main()
    command_log.info(f'Bot encerrado as {datetime.today()}')
