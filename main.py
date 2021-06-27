# coding=utf-8
import discord
from discord.ext import commands, tasks
import sqlite3

#хуй
bot = commands.Bot("!")
conn = sqlite3.connect('raptor.db')
c = conn.cursor()
target_channel_id = 848317285655511061
#c.execute("""CREATE TABLE raptors(num integer, id integer, bool integer)""")
c.execute("INSERT INTO raptors VALUES (1, 1, 0)")
conn.commit()
c.execute("SELECT * FROM raptors WHERE num = 1")
list = c.fetchone()
message_id = list[1]
bool = list[2]
print(bool)


@tasks.loop(hours=9999)
async def send_message():
    message_channel = bot.get_channel(target_channel_id)
    message = await message_channel.send("Ford Raptor ( раптор ). Свободен!", file=discord.File(fp="C:\Something\e55f7d70fbcbb685.png"))
    msg_id = message.id
    c.execute(f"UPDATE raptors SET id = {msg_id} WHERE num = 1")
    c.execute("UPDATE raptors SET bool = 1 WHERE num = 1")
    print("Сообщение отправлено!")
    conn.commit()
    conn.close()


@tasks.loop(hours=9999)
async def edit_message():
    channel = bot.get_channel(target_channel_id)
    message = channel.get_partial_message(message_id)
    await message.edit(content="Ford Raptor ( раптор ). Занято!")
    c.execute("UPDATE raptors SET bool = 0 WHERE num = 1")
    print("Msg edited!")
    conn.commit()
    conn.close()


@send_message.before_loop
async def before():
    await bot.wait_until_ready()

@edit_message.before_loop
async def before():
    await bot.wait_until_ready()

if bool == 0:
    send_message.start()
else:
    edit_message.start()

bot.run("mfa.46REDwxddyc_ybx9XFTrY7XaFoe3PBGuN6lwr8rUcuHzgAwfcBQF4npd8FAAM807CfYGfA4Azoz1aWDtIv05", bot=False)