from telegram import Update
from telegram.ext import CallbackContext


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum!")


def ban_command(update: Update, context: CallbackContext):
    update.message.reply_text("Ban!")


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Help!")
