import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from AI import Agent, is_aws_related

# Não criamos Agent aqui; ele será passado como argumento


async def template_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Exemplo de comando template"""
    user_name = update.message.chat.first_name
    user_lastname = update.message.chat.last_name
    user_id = update.message.chat.id
    text = update.message.text
    await update.message.reply_text("Template command")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    user_name = update.message.chat.first_name
    await update.message.reply_text(f"Olá {user_name}, tudo bem?")


async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /ping"""
    await update.message.reply_text("Pong")


agent = Agent()

agent = Agent()


def aws_command(command_logger, error_logger):
    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = update.message.text
        try:
            # executa o agente em thread separada
            res = await context.application.run_in_executor(None, agent.get_response, msg)

            # loga o comando e resposta
            command_logger.info(
                f"User {update.effective_user.id} asked: {msg}")
            command_logger.info(f"Agent response: {res}")

            await update.message.reply_text(res)
        except Exception as e:
            error_logger.exception("Error in aws_command")
            await update.message.reply_text("⚠️ Sorry, something went wrong while processing your request.")
    return command
