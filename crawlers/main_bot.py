import os

import telebot

from scraping.get_reddit_infos import RedditData

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=["NadaPraFazer"])
def nothing_to_do(message: dict) -> None:
    try:
        sub = message.text.split("/NadaPraFazer ")[1]
        reddit_data = RedditData("telegram", sub)
        send_message(message, reddit_data)
    except IndexError:
        bot.send_message(
            message.chat.id,
            f"<b>Por favor defina os subreddits</b>",
            parse_mode="HTML",
        )


@bot.message_handler(commands=["start"])
def response(message: dict) -> None:
    texto = """
    Para iniciar o bot informe a lista na opção ordem:
    /NadaPraFazer [+ Lista de subrredits]
    
    Utilizar qualquer outra opção não irá iniciar o bot"""
    bot.reply_to(message, texto)


@staticmethod
def send_message(message: dict, reddit_data: RedditData) -> None:
    response = reddit_data.extract_data()
    for data in response:
        message_reddit = format_message_html(data)
        bot.send_message(message.chat.id, message_reddit, parse_mode="HTML")


@staticmethod
def format_message_html(data: dict) -> str:
    message_reddit = (
        f"<b>Subreddit</b> : <i>{data['sub']}</i>\n\n"
        f"<b>Title</b> : <i>{data['title']}</i>\n\n"
        f"<b>Ups</b> : <i>{data['ups']}</i>\n\n"
        f"<b>Thread Comment Link</b> : <i><a href='{data['link']}'>Click for comment</a></i>\n\n"
        f"<b>Thread Link</b> : <i><a href='{data['thread_url']}'> Click for view thread </a></i>"
    )
    return message_reddit


bot.polling()
