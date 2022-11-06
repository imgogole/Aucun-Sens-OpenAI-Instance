import discord

import OpenAI

import os


def run() :
    Token = os.environ.get("TOKEN_DISCORD")
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("Je suis prêt")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith("!") :
            return

        if message.channel.id in [904770002824097823, 941837130936774676]:
            print("> Message : " + message.content)
            answer = OpenAI.ask(message.content)
            print("=> Answer : " + answer)
            await message.channel.send(answer)

    client.run(Token)

if __name__ == "__main__" :
    run()