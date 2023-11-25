import discord 
from discord.ext import commands
from discord import app_commands
import responses

TOKEN = 'PLACEHOLDER'
#place the token here
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.command()
async def koko(ctx):
    await ctx.send("so hot-sam")
    
@client.command()
async def anime(ctx):
    await ctx.send("""
                   ⣿⣿⣿⣿⡿⠟⠛⠋⠉⠉⠉⠉⠉⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠟⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠙⠾⣿⣾⣿⣾⣿⣾⣿⣾⣿
⠋⡁⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⢀⠠⠐⠈⠁⠀⠀⠁⠀⠈⠻⢾⣿⣾⣿⣾⣟⣿
⠊⠀⠀⠀⠀⢀⠔⠃⠀⠀⠠⠈⠁⠀⠀⠀⠀⠀⠀⠆⠀⠀⠄⠀⠙⣾⣷⣿⢿⣿
⠀⠀⠀⠀⡠⠉⠀⠀⠀⠀⠠⢰⢀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠈⡀⠀⠈⢿⣟⣿⣿
⠀⠀⢀⡜⣐⠃⠀⠀⠀⣠⠁⡄⠰⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠰⠀⠀⠈⢿⣿⣿
⠀⢠⠆⢠⡃⠀⠀⠀⣔⠆⡘⡇⢘⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⢀⡆⠀⡼⢣⠀⢀⠌⢸⢠⠇⡇⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿
⣼⣃⠀⠁⢸⢀⠎⠀⢸⠎⠀⢸⢸⡄⠀⠀⠀⠀⠀⠂⢀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠃⡏⠟⣷⣤⠁⠀⠀⠸⠀⠀⡾⢀⢇⠀⠀⠀⠀⠀⠄⠸⠀⠀⠀⠀⠄⠀⠀⠀⣿
⠀⠀⣀⣿⣿⣿⢦⠀⠀⠀⠀⡧⠋⠘⡄⠀⠀⠀⠀⡇⢸⠀⠀⠠⡘⠀⠀⠀⢠⣿
⠈⠀⢿⢗⡻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⢰⠁⡇⠀⠀⢨⠃⡄⢀⠀⣸⣿
⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣱⠀⠀⡎⠸⠁⠀⢀⠞⡸⠀⡜⢠⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣺⣿⣧⢰⣧⡁⡄⠀⡞⠰⠁⡸⣠⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡿⠏⣿⠟⢁⠾⢛⣧⢼⠁⠀⠀⢰⣿⡿⣷⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠡⠄⠀⡠⣚⡷⠊⠀⠀⠀⣿⡿⣿⡿⣿
⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⢸⠁⠀⠀⠀⢰⣿⣿⡿⣿⣿
⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⡞⠀⠀⠀⠀⢸⣿⣷⣿⣿⣿
⠀⠙⢦⣀⠀⠀⠀⠀⠀⢀⣀⣠⠖⠁⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⣸⣿⣾⡿⣷⣿
⠀⠀⠀⠀⠉⠉⣩⡞⠉⠁⠀⢸⡄⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⣿⣿⣷⣿⣿⣿
⡆⠀⠀⣀⡠⠞⠁⣧⢤⣀⣀⣀⡇⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⣿⣷⣿⣷⣿⣿
⣿⣷⠊⠁⠀⠀⡰⠁⠀⠀⠀⠀⣹⠶⢦⡀⠀⠀⡇⠀⠀⠀⠀⠀⢸⣿⣷⣿⣷⣿
⣿⢿⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⡇⠀⠀⠀⠀⠀⠈⣿⣾⣷⣿⣿
⠋⠈⠀⢀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠻⣿⣽⣾⣿
⢀⡄⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠁⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⣿⣿⣻⣿
⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠐⠀⠀⠀⠀⣀⡿⠀⠀⠀⠀⠀⠀⠀⢹⣿⣻⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⢀⣃⡇⠀⠲⡀⠀⠀⠀⠀⠈⣿⡿⣿
⣀⠤⠤⠤⡀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⢬⠞⡇⠀⠀⠇⠀⠀⠀⠀⠀⣿⣿⣿
⡁⢀⠀⠀⡇⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⣸⠁⠀⠇⠀⠀⡇⠀⠀⠀⠀⠀⣿⣿⣿
⠔⠃⠀⠀⡇⠀⠀⡼⠁⠀⠀⠀⠀⠀⢀⡇⠀⠀⡃⠀⠀⠙⢄⠀⠀⠀⠀⣿⣷⣿
⠒⠊⠀⠀⢸⠀⣸⠃⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⢅⠀⠀⡂⠸⡄⠀⠀⠀⣿⣟⣿
⠓⠀⠉⠀⢸⣰⠃⠀⠀⠀⠀⠀⠀⡜⡆⠀⠀⠀⢸⠀⠀⡇⢀⠇⠀⠀⠀⣿⣿⣿
⠉⠁⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⣰⠁⡇⠀⠀⠀⡇⠀⠀⡇⢸⠀⠀⠀⠀⣿⣷⣿
⡀⠀⢀⢿⣥⡤⠤⠤⠤⣀⣀⢠⠇⠀⢸⠀⠀⢰⠁⠀⢨⠀⢸⠀⠀⠀⠀⣿⣟⣿""")




@client.command()
async def dell(ctx):
    await ctx.send("Dell is dating every asian in honor band and orch (except ben)")

@client.command()
async def sam(ctx):
    await ctx.send("hottie <3")
    
@client.command()
async def bendonshoe(ctx):
    await ctx.send("""Goofy little boy your dumbass rolls down the hill as an efficient form of transportation your nigga ass grandparents freed from an emancipation proclamation with you pungy chubby bubbly butt mutt suckin stupid head Kys and hop off my dick before I whip out my Glock as well as my cock and shoot all over you get off my block cuh I’m from the crip and you ain’t part of my crip before I unload my clip and chop off your stick and eat your shit you dumbass monkey 🙉 and your stupid head your dumb to the head and your smooth racetrack textured brain doesn’t perform properly with your ignorant arrogant paired ballsacks with an elephant your brown undies got a dirty gooey cocoa tint never talk to me ever again you fatty stop eating your chicken bean Pattie’s like SpongeBob academic flop built like a rock follows pigeons with your dumb head in the flock and be quiet tooKys
""")
    
@client.command()
async def code(ctx):
    await ctx.send("177013")

@client.command()
async def nnn(ctx):
    await ctx.send("""Day 4 of No Nut November. The struggle is real, and the terror is setting in. As I wake up, I can't help but feel a sense of impending doom. The clock on the wall seems to taunt me, its hands ticking away, counting down the minutes until I face another day of this torturous challenge.

My morning routine, once a simple and mundane task, has now become a treacherous journey through a minefield of temptation. Even the innocent act of showering has turned into a battlefield. I avoid making any accidental contact with myself like my life depends on it, for fear that I might lose control and succumb to the desires that haunt me.
As I sit down for breakfast, even a harmless banana seems to have transformed into a forbidden fruit of temptation. I cast furtive glances around the room, half-expecting someone to burst through the door and catch me in the act, as if I were committing some heinous crime.

Throughout the day, I walk a tightrope between desire and self-control. Every passing glance at an attractive person or an alluring image sends shivers of terror down my spine. The fear of slipping up is constant, and it gnaws at my conscience like a relentless demon.
My friends, oblivious to my silent struggle, make jokes about No Nut November and the dire consequences of failing the challenge. Little do they know that I am living in a state of perpetual anxiety, desperately clinging to the last shreds of my willpower.

Nightfall brings no relief, as my dreams are now filled with nightmarish scenarios of me giving in to temptation. I wake up in a cold sweat, thankful that it was only a dream, yet still haunted by the terrifying prospect of breaking the vow I've made to myself.

Day 4 of No Nut November has been a relentless battle, and the fear of failure continues to grow. The road ahead seems long and filled with pitfalls, but I must press on, for the terror of giving in is nothing compared to the dread of admitting defeat.""")

@client.command()
async def whatcolorisit(ctx):
    await ctx.send("According to my calculations, I have reviewed the color for the entirety of No Nut November, and I can safely conclude that it is bubble gum pink. I have studies the colors of every single girl including daniels sister. It it bubble gum pink.")

@client.command()
async def master(ctx):
    await ctx.send("Please DO NOT announce to the server when you are going to masterbate. This has been a reoccuring issue, and I'm not sure why smoe people have such under developed social skills that they think that a server full of mostly male strangers would need to know that. No one is going to be impressed and give you a high five (especially considering where that hand has been). I don't wan tto add this to the rules, since it would be embrassing for new users to see that we have a problem with this, but it is going to be enforced as a rule from now on")
    
@client.command()
async def david(ctx):
    await ctx.send("Are you the new girl? heh, I thought so, I-I've never seen you before. Konnichiwa! I'm David-kun. It's so nice to finally meet you, you look just like my waifu- HEE-HEE-HEE-HEE. A-anyways, I'm so sorry about the jerks in class, they're all baka and they only want one thing. Not me, I just like to watch my favourite anime Ju justsu kaisen and watch manga. Also, I think you're really cool Aitetsune HEE-HEE-HEE-HEE-HEE-HEE... gah I-I'm sorry! I'm just nervous okay! I-it's just... Well...I-it's just!..m-m-I just want to know if I could suck on your niplets okay!.. Well, What do you say- IUHHhh")
    
@client.command()
async def rice(ctx):
    await ctx.send("Rice is a very popular grain in Asia, and all around the world. In Asia, we have it almost everyday with our meal. If you never seen rice before, then that is a shame. Rice comes in many colors. White, black, Yellow, you name it. But my favorite is white sticky rice. White sticky rice, is basically normal rice with but with more water so it is more moist. Genetics have shown that rice has been rice was domesticated 8,000-13,000 years ago in China, near the Pearl River Valley. There are myths about Rice and how it is a gift from the Animals in China. It was said that, during a flood, all the crops been wiped out, and so the people had nothing to eat. Then one day, a dog cane by and gave the people rice grain. They grew it and then hunger disappeared. My Grandpa owns a farm, in which he grows rice. Approximately in 1 cup of uncooked rice there are 2 cups of cooked rice. Rice in my opinion is one of world most creative carbohydrate. You can make anything out of rice. You name it. But what can you do with bread. Nothing. You can literally sculpts things with rice. But with bread, all you can do is stack it. Whats the fun for stacking. With Rice, you can make little balls out of it and chuck it. What can you do with bread. Chuck the whole loaf? Who would in the right mind chuck a loaf of bread. With rice, you can do anything. Anyways leave a comment saying whats your favorite type of grain.")
client.run(TOKEN)

@client.command()
async def (ctx):
    await ctx.send("")
    
@client.command()
async def (ctx):
    await ctx.send("")
    
    
    
client.run(TOKEN)
