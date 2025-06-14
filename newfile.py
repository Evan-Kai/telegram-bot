from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Main menu
async def show_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("📞 Admin နဲ့ဆက်သွယ်မယ်", url="https://t.me/CryptoWith_Evan")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🤖 မင်္ဂလာပါ။ LearnWith_Evan Bot မှ ကြိုဆိုပါတယ်။\n\nဖော်ပြထားတဲ့ menu ကို အသုံးပြုနိုင်ပါတယ်။👇",
        reply_markup=reply_markup
    )

# Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_menu(update, context)

# Handle only About and Back buttons
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.answer()
    except:
        pass

    if query.data == "about":
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="ℹ️ LearnWith_Evan Bot သည် မေးခွန်းများကို ဖြေဆိုပေးသော Q&A Assistant တစ်ခုဖြစ်ပါသည်။",
            reply_markup=reply_markup
        )

    elif query.data == "main_menu":
        keyboard = [
            [InlineKeyboardButton("📞 Admin နဲ့ဆက်သွယ်မယ်", url="https://t.me/CryptoWith_Evan")],
            [InlineKeyboardButton("ℹ️ About", callback_data="about")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="🤖 ပြန်လာပါပြီ။ LearnWith_Evan Main Menu 👇",
            reply_markup=reply_markup
        )

# App setup
app = ApplicationBuilder().token("8148704481:AAHj_vfh6tRa5HrK_z_NFPuUcTixjQEEuj4").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()