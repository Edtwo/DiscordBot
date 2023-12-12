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

@client.command()
async def val(ctx):
    await ctx.send("""UNINSTALLING VALORANT
▇▇▇▇▇▇▇▇▇▇▇▇▇▇▢
　　╭━╮╭━╮╭╮　╱ 　　
　　╰━┫╰━┫╰╯╱╭╮ 　　
　　╰━╯╰━╯　╱　╰╯ 　　　　　
　　　     COMPLETE""")

@client.command()
async def eldenring(ctx):
    await ctx.send("""Shut the fuck up you maggot. You clearly don't understand what makes a great video game. Elden Ring is a beautifully crafted masterpiece with a rich-open, beautiful graphics, fantastical gameplay, a great narrative, great quest design and it gives a ton of freedom and an actual challenge. Meanwhile all the other games that came out this year are overrated, mediocre games with boring, generic and repetitive gameplay, boring and uninteresting narratives and keep telling you what to do every 5 seconds. You and the people that support these kinds of doghit games are everything that is wrong this the gaming industry. These companies give you garbage and you guys eat it up and ask for more. Elden Ring is literally the only game that deserves to be called a true video game. Everything else is a joke and a scam. So fuck you, fuck all the people that pay for it, and fuck these companies that keep pumping these shitty mediocre kiddy games. I hope all of you fuckers die. Elden Ring and FromSoftware deserve all the praise and much more. They are single-handedly carrying the entire gaming industry with their state of the art games.

""")

@client.command()
async def riley(ctx):
    await ctx.send("pho slurper chink")
    
@client.command()
async def kai(ctx):
    await ctx.send("6 ft korean boy who LOVES a good k drama (he likes looking at the big muscular men)")

@client.command()
async def ben(ctx):
    await ctx.send("silly korean boy is fr a egotist blue lockian")

@client.command()
async def derek(ctx):
    await ctx.send("bro is not a dino silly asian boy go back to where you came from!! (the land of the yellows)")

@client.command()
async def wick(ctx):
    await ctx.send("""INDIA IS SUPERIOR
I invite you to visit my great nation and see for yourself what it was BEFORE YOU MOTHERFUCKING BURGLARS LOOTED IT. You double crossing snakes left us in poverty. You think you magically became an advanced civilization brimming with technological marvels? I'm not asking you. There's no room for your worthless opinion. The answer is FUCK NO. Almost everything that separates you from a monkey originated in Maha Bharatha. Can you even begin to comprehend the depth of that sentence? I guess not, Average Joe. If I have to make it into a list, I'll have to publish a book. So yeah. Point at me in public. Tell the world I'm an Indian. There's nothing that makes me more proud. If you can't respect this great nation, it shows who you are. You can't bring India down. I'm the newest product from the world's oldest and most experienced company. I will crush you with my left foot so hard, even the vultures wont be able to scavenge your flesh.""")

@client.command()
async def mefr(ctx):
    await ctx.send("""I violently sharted in a McDonald’s, March 4th, 1998
nsfw
I violently, aggressively, explosively, intensely, passionately, vehemently sharted my jorts in a McDonald’s hamburger shaped seat on March 4th, 1998. It smelled like spiced Gouda aged in a hot metal can with a slight aura of pickled onions and expired diesel fuel. As I looked down my leg, I saw a trickle of what appeared to be an orange, brownish-red nuclear Shart substance, something akin to a chemical weapon. The liquid Shart scent filled the air of the restaurant, causing customers to dry heave, cover their nose; I even recall an employee asking the staff “who took a shit in the deep fryer?”

The health department ended up showing up and doing a thorough corporate investigation of that particular location. Turns out they were breaking all types of health protocols and were promptly shut down, and if you think about it, it was all because of sharting my jorts.""")

@client.command()
async def anthony(ctx):
    await ctx.send("ANTHONY STOP EATING ALL THE FOOODODDDD THATS CHEATTTTTING")

@client.command()
async def neel(ctx):
    await ctx.send("follow tyranno on soundcloud")

@client.command()
async def diko(ctx):
    await ctx.send("do you think anthony has big boobies")
    
@client.command()
async def saridh(ctx):
    await ctx.send("i can imagine brian being slurped up and NUDE")

@client.command()
async def john(ctx):
    await ctx.send("""I'd just like to interject for a moment. What you're refering to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.

Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called Linux, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.

There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called Linux distributions are really distributions of GNU/Linux!""")

client.run(TOKEN)
