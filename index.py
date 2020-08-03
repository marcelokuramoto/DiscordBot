from discord_config import TOKEN_Bot as TOKEN
from dialog_flow import detect_intent_text
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: #Evitar Loop com a mensagem do Proprio Bot
        return
    else:
        ID_Conversa = message.author
        texto = message.content
        analise = detect_intent_text(ID_Conversa,texto)

        intent = analise.get('intencao')
        if intent == 'Saudacoes':
            resposta = "Seja bem-vindo(a) {}!\nSou o Sherlock, a Chinchila da MilqSimmer =D \nRespeite os coleguinhas e se divirta!".format(message.author)
        else:
            resposta = analise.get('frase')

        await message.channel.send(resposta)
        
client.run(TOKEN)