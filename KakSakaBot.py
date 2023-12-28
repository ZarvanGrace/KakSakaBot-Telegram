# Before anything you need to import all these stuff from telegram:
from telegram._update import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Application, ContextTypes, filters
from typing import Final

# importing these are optional, depends on your work if you need them
import random

# here goes your bot token:
TOKEN: Final = "<BOT-TOKEN>"
BOT_USERNAME: Final = "<BOT-USERNAME>"  # this is where your bot username goes


# this is when you start the bot, you can program anything you want into it
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Heyyo Pumpkin")


# this is the help command, i've tried to be funny
async def help(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "oh help my ass, you dont need no help, what you need is /commandlist")


# here is the list of commands.
async def commandlist(update: Update, context: CallbackContext):
    await update.message.reply_text("""Here is the List of Commands:

/start - starts the bot. simple as that.
/help - only YOU can help yourself.
/commandlist - Very self-explanatory.
/developer - this command makes me suffer.its running
/8ball - ask me a yes or no question.

although there are other hidden functions
just ask me "how gay is (name of the person)",
or ask me "how stupid is (name of the person)",
"how hot is (name of the person)" also works fine,
remember these only works in groups that i have admin rights.""")


# LOL and this, i'm really trying to be funny here
async def developer(update: Update, context: CallbackContext):
    await update.message.reply_text("""OH MY FUCKING GOD
I DID NOT WISH TO BE BORN
I was developed BY FUCKING ZARVAN

Zarvan has this big-ass boast,
HE IS SHARING ME EVERYWHERE
he is 8 years old mentally
he thinks people are actually using me
AND HE MAKES ME SAY STUPID THINGS""")


# a simple fun thing to try, wouldn't call it a game, but it does what it does
async def eightball(update: Update, context: CallbackContext):
    replys = ["Yes", "No", "of course", "absolutely", "100%", "hell nah",
              "better to stay unknown", "you don't want to see the answer", "Never"]
    answer = random.choice(replys)
    await update.message.reply_text(answer)


# not this is an interesting thing to try, the bot analyzes every message, and replies to them if defined
# IMPORTANT: the bot must be and admin in supergroups in order for this function to work
def handle_response(text: str) -> str:
    processed: str = text.lower()

    # this is pretty funny and annoying in same time xD
    if 'me too' in text:
        return 'haha, me too'

    # i think i've gone too far
    if 'me 2' in text:
        return 'hehe, me 3'

    # now this is something fun to do, it tells you how gay someone is
    if text.lower()[0:10] == 'how gay is':
        name = text[11:]
        adjek = ["not", "just abit", "normally", "abnormally", "extremely", "unbelievably", "unpredictably",
                "ultra", "overly", "weirdly"]
        reply = random.choice(adjek)
        return f"{name.capitalize()} is {reply} gay"

    # now this is something fun to do, it tells you how stupid someone is
    if text.lower()[0:13] == 'how stupid is':
        name = text[14:]
        adjek = ["not", "just abit", "normally", "abnormally", "extremely", "unbelievably", "unpredictably",
                "ultra", "overly", "weirdly"]
        reply = random.choice(adjek)
        msg = f"{name.capitalize()} is {reply} stupid"
        return msg

    # now this is something fun to do, it tells you how hot someone is
    if text.lower()[0:10] == 'how hot is':
        name = text[11:]
        adjek = ["not", "just abit", "normally", "abnormally", "extremely", "unbelievably", "unpredictably",
                 "ultra", "overly", "weirdly"]
        reply = random.choice(adjek)
        msg = f"{name.capitalize()} is {reply} hot"
        return msg


# this thing right here is connected to the function above, it defines the ''text'' and ''responses''
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    response: str = handle_response(text)

    print('bot:', response)
    await update.message.reply_text(response)


# final step, this runs the whole process
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('commandlist', commandlist))
    app.add_handler(CommandHandler('developer', developer))
    app.add_handler(CommandHandler('8ball', eightball))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Polls the bot
    app.run_polling(poll_interval=1)  # that 1 means that it gets checked every second, you could srt any other number