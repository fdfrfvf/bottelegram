import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Configurer le logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s',
    level=logging.INFO
)

# Remplace TOKEN par le token de ton bot
TOKEN = '7454422753:AAFQ6zu0v-7L9cNDjDFfVUXyVPkRg9NQtB8'
IMAGE_URL = 'https://drive.google.com/uc?export=download&id=14DZxx8aTCur1e1pcYhhB647NHqoj-58E'
MINI_APP_URL = 't.me/NotcoinxGames_bot/NotcoinGamesAirdrop'  # Remplace par l'URL de ta mini app

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
            [InlineKeyboardButton("News Twitter/X", url='https://x.com/thenotcoin')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Envoi de l'image avec le texte en légende et les boutons
        await bot.send_photo(chat_id=update.message.chat_id, photo=IMAGE_URL, caption=message_text, reply_markup=reply_markup)
        print("Image envoyée avec succès")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")
        await update.message.reply_text("Failed to send message.")

def main() -> None:
    # Initialiser l'application avec le token de ton bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Ajouter les gestionnaires
    application.add_handler(CommandHandler('start', start))

    # Démarrer le bot
    application.run_polling()

if __name__ == '__main__':
    main()
