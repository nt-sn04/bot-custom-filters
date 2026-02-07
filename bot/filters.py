from telegram.ext import BaseFilter, CallbackContext
from telegram import Update


class CustomFilters:
    class IsAdmin(BaseFilter):
        def __call__(self, update: Update):
            if update.effective_message:
                return update.effective_user.username in [
                    "diyorbek_jumanov",
                    "N_20o4_06_13",
                    "Tursunoff_19",
                ]
            return False

    class IsGroup(BaseFilter):
        def __call__(self, update: Update):
            return update.message.chat.type == "supergroup"

    class IsPrivate(BaseFilter):
        def __call__(self, update: Update):
            return update.message.chat.type == "private"

    is_admin = IsAdmin()
    is_group = IsGroup()
    is_private = IsPrivate()
