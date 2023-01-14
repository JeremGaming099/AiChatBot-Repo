import discord
import openai

# Configurer la clé d'API
openai.api_key = "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"

# Initialiser le client Discord
intents = discord.Intents().default()
client = discord.Client(intents=intents)

# Événement lorsque le bot es prêt
@client.event
async def on_ready():
    print(f'{client.user} es connecté !')

# Événement lorsque le bot reçoit un message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content:
        prompt = message.content[1:]
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completions.choices[0].text
        await message.channel.send(response)

# Exécuter le bot
client.run("MTA1MzU2NDE1MDM4ODg5OTkyNw.GjC2P2.OzKCn1oswnD52Fri82agKmdv2aU7PO93dl5fgA")