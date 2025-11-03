import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.error import TelegramError

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
IMAGE_URL = "https://freeimage.host/i/KQqd1Lb"
JOIN_LINK = "https://t.me/+__g33bhB5Z41MzM1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message with image and join link when the command /start is issued."""
    try:
        welcome_text = (
            "🎉 Welcome to our bot! 🎉\n\n"
            "Join our community to stay updated:\n"
            f"👉 {JOIN_LINK}"
        )
        
        # Send the image with caption
        await update.message.reply_photo(
            photo=IMAGE_URL,
            caption=welcome_text
        )
        logger.info(f"Sent welcome message to user {update.effective_user.id}")
        
    except TelegramError as e:
        logger.error(f"Error sending welcome message: {e}")
        await update.message.reply_text("Sorry, I couldn't send the image. Please try again later.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "Available commands:\n"
        "/start - Start the bot and get welcome message\n"
        "/help - Show this help message\n"
        "/join - Get the join link"
    )
    await update.message.reply_text(help_text)

async def join_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the join link when the command /join is issued."""
    join_text = f"Join our community here: {JOIN_LINK}"
    await update.message.reply_text(join_text)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by Updates."""
    logger.error(f"Update {update} caused error {context.error}")

def main() -> None:
    """Start the bot."""
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN environment variable is not set!")
        return

    try:
        # Create the Application
        application = Application.builder().token(BOT_TOKEN).build()

        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("join", join_command))
        
        # Add error handler
        application.add_error_handler(error_handler)

        # Start the Bot
        logger.info("Bot is starting...")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

if __name__ == '__main__':
    main()
