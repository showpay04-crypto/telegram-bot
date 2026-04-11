from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

import os
TOKEN = os.getenv("TOKEN")
ADMIN_ID = 8611367717

# ✅ START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Save user
    try:
        with open("users.txt", "r") as f:
            users = f.read().splitlines()
    except:
        users = []

    if str(user_id) not in users:
        with open("users.txt", "a") as f:
            f.write(str(user_id) + "\n")

    # Buttons
    keyboard = [
        [InlineKeyboardButton("📋 Register / Download App", url="http://www.sikkimgg.org/#/register?invitationCode=424436675902")],
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/+L3hwr8UfKuw3MjVl")],
        [InlineKeyboardButton("👨‍💼 Contact HR", url="https://t.me/Jerinn_1")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send poster + message
    await update.message.reply_photo(
        photo=open("poster.jpg", "rb"),
        caption=(
            "🚀 *Welcome to ProPlay Bot* 🚀\n\n"
            "💸 Turn your gameplay into real earning potential\n"
            "🚀 Join players who are leveling up every day	\n"
            "👑 VIP Access Unlocks:\n\n"
            "• Private forecasts\n"
            "• Priority support\n\n"
            "👉 Start now & build your winning journey!"
        ),
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# ✅ AUTO REPLY (FOR ANY MESSAGE)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id

    print(f"User {user_id}: {user_text}")

    # Reply with your contact
    await update.message.reply_text(
        "👨‍💼 Contact HR:\nhttps://t.me/Jerinn_1"
    )

    # Forward message to admin
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📩 User {user_id} says:\n{user_text}"
    )

# ✅ BROADCAST COMMAND
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    message = " ".join(context.args)

    try:
        with open("users.txt", "r") as f:
            users = f.read().splitlines()
    except:
        users = []

    for user in users:
        try:		
            await context.bot.send_message(chat_id=int(user), text=message)
        except:
            pass

    await update.message.reply_text("✅ Broadcast sent!")

# ✅ MAIN APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("broadcast", broadcast))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot running...")
app.run_polling()