import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv("TOKEN")

# ===== START COMMAND =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Channel Link", url="https://t.me/+L3hwr8UfKuw3MjVl")],
        [InlineKeyboardButton("🎁 Bonus", callback_data="bonus")],
        [InlineKeyboardButton("👑 VIP", callback_data="vip")],
        [InlineKeyboardButton("📝 Register", url="http://www.sikkimgg.org/#/register?invitationCode=424436675902")],
        [InlineKeyboardButton("📞 Contact Support", url="https://t.me/Jerinn_1")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to ProPlay Bot!\n\n💸 Turn your gameplay into real earning potential\n\n🚀 Join players who are leveling up every day\n\n👑 VIP Access Unlocks:\n• Private forecasts\n• Premium insights\n• Priority support\n\n👉 Start now & build your winning journey!",
        reply_markup=reply_markup
    )

# ===== BUTTON HANDLER =====
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # ===== BONUS =====
    if query.data == "bonus":
        await query.message.reply_photo(
            photo="https://res.cloudinary.com/deolukh6f/image/upload/v1774716227/photo_2026-03-28_22-13-26_brbyrg.jpg",
            caption=(
                "🎁 *Big deposit = Big bonus*\n\n"
                "🔥 Get exciting bonuses daily!\n"
                "💸 Extra rewards on every activity\n"
                "🚀 Limited time offers available"
            ),
            parse_mode="Markdown"
        )

    # ===== VIP =====
    elif query.data == "vip":
        await query.message.reply_photo(
            photo="https://res.cloudinary.com/deolukh6f/image/upload/v1774716952/tggg_wrhdza.png",
            caption=(
                "👑 *VIP Plans*\n\n"
                "💰 Higher daily profits\n"
                "⚡️ Fast withdrawals\n"
                "🎯 Exclusive premium benefits"
            ),
            parse_mode="Markdown"
        )

# ===== APP RUN =====
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot is running...")
app.run_polling()
