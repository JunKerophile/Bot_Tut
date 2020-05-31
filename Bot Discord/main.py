# On importe le module discord.py
import discord

# Ajouter un composant de discord.py
from discord.ext import commands

# Une commande 
# !regles =regles #regles

# Créer le bot
bot = commands.Bot(command_prefix='!')

# Détecter quand le bot est prêt
@bot.event
async def on_ready():
    print("Bot on")
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("Essayez !commandes"))

# Détecter quand quelqu'un ajoute une réaction sur un message
@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    print(emoji)
    

# Créer la commande !regles
@bot.command()
async def commandes(ctx):
    await ctx.send("!drive \n!trello \n!github \n!unsplash")

@bot.command()
async def drive(ctx):
    await ctx.send("https://drive.google.com/drive/folders/1eGnQFkmH8tJOTJtpDaHrHE7zSYZh_oAU")

@bot.command()
async def trello(ctx):
    await ctx.send("https://trello.com/b/8iz24nig/projet-tutor%C3%A9")

@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/MatteoL-W/instant-gourmand")

@bot.command()
async def unsplash(ctx):
    await ctx.send("https://unsplash.com/")

@bot.command()
async def anissa(ctx):
    await ctx.send("des ptits gateaux la")

@bot.command()
async def edouard(ctx):
    await ctx.send("Homme au charisme et à la préstance incroyable")

@bot.command()
async def mattéo(ctx):
    await ctx.send("fatigué")

@bot.command()
async def valentin(ctx):
    await ctx.send("Arrête de jouer à Animal Crossing bg d'la vie la")

@bot.command()
async def benjamin(ctx):
    await ctx.send("https://www.twitch.tv/shinezeogames")

@bot.command()
async def justine(ctx):
    await ctx.send("je sais pas quoi mettre pour toi désolé :(")

@bot.command()
async def charnay(ctx):
    await ctx.send("Modifiez l'affiche, on dirait un artchitecte qui présente ses couleurs")

# Donner le jeton pour la connexion du bot
jeton = "NzE2Njc4NjI3MTc3MTM2MjE5.XtPRWg.WrRqrnZ4qHHbJKKBwM8hcpjabAQ"

# Connecter au serveur
bot.run(jeton)

print("Lancement du bot")