import discord
import OpenAI
import os
from Stack import Stack

def pushMessage(stack, author, message) :
    stack.push(author, message)

def run() :
    Token = os.environ.get("TOKEN_DISCORD")
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    allowedChannel = [904770002824097823, 941837130936774676]
    lastDialogues = {}

    AI_Name = "Arnaud le bigorneau"

    @client.event
    async def on_ready():
        print("Je suis prêt")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith("!") :
            return

        if message.channel.id in allowedChannel:

            if message.channel.id not in lastDialogues :
                lastDialogues[message.channel.id] = Stack()

            dialogues = lastDialogues[message.channel.id]
            pushMessage(dialogues, message.author.name, message.content)
            answer = OpenAI.ask(dialogues.getFormatDialogue())
            pushMessage(dialogues, AI_Name, answer)
            await message.reply(answer)

    client.run(Token)


if __name__ == "__main__" :
    run()