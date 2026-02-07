from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)

from .config import settings
from .handlers import (
    start_command,
    ban_command,
    help_command,
)
from .filters import CustomFilters


def main() -> None:
    updater = Updater(settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(
        handler=CommandHandler(
            command="start",
            callback=start_command,
        )
    )
    dispatcher.add_handler(
        handler=CommandHandler(
            command="ban", callback=ban_command, filters=CustomFilters.is_group
        )
    )
    dispatcher.add_handler(
        handler=CommandHandler(
            command="help", callback=help_command, filters=CustomFilters.is_private
        )
    )

    updater.start_polling()
    updater.idle()
