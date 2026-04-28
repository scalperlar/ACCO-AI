import os
import io
import logging
import asyncio
import docx
import openpyxl
import fitz  # PyMuPDF
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# API KALITLAR
TELEGRAM_BOT_TOKEN = "8653684955:AAEQbIvoAtgBT8CPix6vHSCGZCfUhVdCmww"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 ACCO AI tayyor! Faylni yuboring.")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Tahlil qilinmoqda...")

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_document))
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
