import discord
from discord.ext import commands, tasks
from datetime import datetime
import database

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.messages = True
client = commands.Bot(command_prefix=".", intents=intents)

now = str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
now = now.replace("/", ".")
now = now.replace(":", ".")
file = open(f'Logs from ' + str(now) + ".txt", "a")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('with your mama'))
    print('Startup succesful')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write('Startup succesful')
    filee.close()


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {member} has joined the server')
    filee.close()
    channel = client.get_channel(879397026826166323)
    await channel.send(f'{member} has joined.')
    database.newUser(member.id)


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {member} has left the server')
    filee.close()
    channel = client.get_channel(879397026826166323)
    await channel.send(f'{member} has left.')
    database.userLeave(member.id)


@client.event
async def on_member_ban(guild, member):
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    logs = logs[0]
    if logs.target == member:
        filee = open(f'Logs from ' + str(now) + ".txt", "a")
        filee.write(
            f'\n {logs.user} has just banned {logs.target} (Time: {logs.created_at}), reason was: {logs.reason}')
        filee.close()
        print(f'{logs.user} has just banned {logs.target} (Time: {logs.created_at}), reason was: {logs.reason}')


@client.command()
@commands.has_role(879467629948067840)
async def clear(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount)
    print(f'just purged {ammount} messages from {ctx.channel}             full string {ctx}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n just purged {ammount} messages from {ctx.channel}             full string {ctx}')
    filee.close()


@client.command()
async def ping(ctx):
    await ctx.send('The ping is ' + str(round(client.latency, 7)))
    print('The ping is ' + str(round(client.latency, 7)))
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write('\n The ping is ' + str(round(client.latency, 7)))
    filee.close()


@client.command()
@commands.has_role(879467629948067840)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.send(f'You were kicked from hardy ms discord for {reason}')
    print(f'{member} was kicked for: {reason}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {member} was kicked for: {reason}')
    filee.close()
    await member.kick(reason=reason)


@client.command()
@commands.has_role(879467629948067840)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.send(f'You were ban from hardy ms discord for {reason}')
    print(f'{member} was banned for: {reason}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {member} was banned for: {reason}')
    filee.close()
    await member.ban(reason=reason)


@client.command()
async def suggest(ctx, member, *, suggestions):
    print(f'{ctx.author} suggested: {suggestions}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {ctx.author} suggested: {suggestions}')
    filee.close()
    channel = client.get_channel(879397026826166323)
    await channel.send(f'{ctx.author} suggested: {suggestions}')


@client.command()
@commands.has_role(879467629948067840)
async def unban(ctx, *, memberid):
    memberidint = int(memberid)
    bannedusers = await ctx.guild.bans()
    print(bannedusers)
    for ban_entry in bannedusers:
        user = ban_entry.user
        print(user.id)
        if user.id == memberidint:
            await ctx.guild.unban(user)
            print(f'{memberidint} was unbanned by {ctx.author}')
            filee = open(f'Logs from ' + str(now) + ".txt", "a")
            filee.write(f'\n {memberidint} was unbanned by {ctx.author}')
            filee.close()
            channel = client.get_channel(879397026826166323)
            await channel.send(f'{memberidint} was unbanned by {ctx.author}')
            break
        else:
            print(f'{memberidint} was not found or is not banned')


@client.event
async def on_message_delete(message):
    print(f'{message.content} was deleted. Full string: {message}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n {message.content} was deleted. Full string: {message}')
    filee.close()


@client.event
async def on_message_edit(before, after):
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(
        f'\n {before.author} has edit the messaage from {before.content} to {after.content}. The  full string of before and after. {before} ........... and after {after}')
    filee.close()
    print(
        f'{before.author} has edit the messaage from {before.content} to {after.content}. The  full string of before and after. {before} ........... and after {after}')


@client.event
async def on_message(checkmessage):
    if not checkmessage.author.bot:
        author = checkmessage.author.id
        oldMes = database.getTotalMessages(author)
        oldXP = database.getTotalXP(author)
        database.addMessage(UUID=author, oldMessageNum=oldMes, oldXPNum=oldXP)

@client.command()
async def clear(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount)
    print(f'just purged {ammount} messages from {ctx.channel}             full string {ctx}')
    filee = open(f'Logs from ' + str(now) + ".txt", "a")
    filee.write(f'\n just purged {ammount} messages from {ctx.channel}             full string {ctx}')
    filee.close() 

client.run('TOKEN')
