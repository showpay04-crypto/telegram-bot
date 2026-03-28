import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Join Now", url="https://t.me/+L3hwr8UfKuw3MjVl")],
        [InlineKeyboardButton("💰 Earn Info", callback_data="earn")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to ProPlay Bot!\n\n💸 Earn daily income easily\n👇 Click below to start",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "earn":
        await query.edit_message_text(
            "💰 Earning Plan:\n\n"
            "✔ Daily profit available\n"
            "✔ Easy withdraw\n"
            "✔ Start with simple steps\n\n"
            "👉 Click JOIN NOW to begin 🚀"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
