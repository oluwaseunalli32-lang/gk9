import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Word list: add as many as you like ---
WORDS = [
    {
        "word": "serendipity",
        "review": "The occurrence of happy or beneficial events by chance."
    },
    {
        "word": "ephemeral",
        "review": "Lasting for a very short time."
    },
    {
        "word": "resilient",
        "review": "Able to recover quickly from difficulties."
    },
    {
        "word": "ubiquitous",
        "review": "Present or found everywhere."
    },
    {
        "word": "candid",
        "review": "Truthful and straightforward; frank."
    },
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to GK9!\n\n"
        "I send you a new word with a short review. "
        "Use /word to get today’s word, or /about to learn more."
    )

async def word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    item = random.choice(WORDS)
    await update.message.reply_text(
        f"📖 Word of the Day: **{item['word']}**\n\n{item['review']}",
        parse_mode="Markdown"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "GK9 — Word of the Day bot.\n\n"
        "Send /word to get a new word with a short review. "
        "This bot’s only destination is this chat; it does not redirect to any external page."
    )

def main():
    token = os.environ["BOT_TOKEN"]
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("word", word))
    app.add_handler(CommandHandler("about", about))

    app.run_polling()

if __name__ == "__main__":
    main()
