import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
IMAGE_URL = "https://freeimage.host/i/KQqd1Lb"
JOIN_LINK = "https://t.me/+__g33bhB5Z41MzM1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message with image and join link when the command /start is issued."""
    
    welcome_text = (
        "🎉 Welcome to our bot! 🎉\n\n"
        "Join our community to stay updated:\n"
        f"👉 {JOIN_LINK}"
    )
    
    # Send the image with caption
    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=welcome_text,
        parse_mode='HTML'
    )

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

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("join", join_command))

    # Start the Bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
