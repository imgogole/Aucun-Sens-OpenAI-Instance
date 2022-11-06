import discord
import OpenAI
import os
from Stack import Stack

def pushMessage(stack, message) :
    stack.push(message)

def run() :
    Token = os.environ.get("TOKEN_DISCORD")
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    lastDialogues = Stack(6, client)

    @client.event
    async def on_ready():
        print("Je suis prêt")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            pushMessage(lastDialogues, message)
            return

        if message.content.startswith("!") :
            return

        if message.channel.id in [904770002824097823, 941837130936774676]:
            pushMessage(lastDialogues, message)
            answer = OpenAI.ask(lastDialogues.getFormatDialogue())
            await message.reply(answer)

    client.run(Token)


if __name__ == "__main__" :
    run()