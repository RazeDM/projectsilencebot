import time,requests,lxml,discord
from discord.ext.commands import Bot
from discord.ext import commands
from bs4 import BeautifulSoup as BS
import os

client = commands.Bot(command_prefix = '.')
client.remove_command('help')
@client.event
async def on_ready():
    activity = discord.Game(name="Project Silence \ GMOD / SWRP")
    await client.change_presence(activity=activity)
    print(client.user.id)
    print('ProjectSilenceOnlineBot Running...')
    futu = client.get_channel(689048821933670410) 
    mesajeje = await futu.send('bruh')
    while True:
        r = requests.get('https://gmod-servers.com/server/126798/')
        aw = BS(r.text,'lxml')
        wow = aw.findAll('strong')
        awaw = aw.findAll('button')
        powpow = aw.findAll('div',class_='col-12')
        powpaw = powpow[7].text.replace('\n','')
        mapa = wow[17].text
        status = awaw[2].text
        r = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow').json()
        wa = r['datetime']
        tome = wa[11:19]
        pl = wow[11].text.replace(' ','').replace('	','').replace('\n','')
        if pl == '0/60':
              powpaw = ''
        if status == 'Offline':
            messagetype = '> **__Статус__**: сервер выключен \n> **__Карта__**: -\n>**__Игроки__**: - \n\n> **__Быстрое подключение__**: - \n> Обновлен ' + tome
        else:
            messagetype = '> **__Статус__**: сервер включен \n> **__Карта__**: ' + mapa + '\n> **__Игроки__**: ' + pl +'\n> '+powpaw+ '\n\n> **__Быстрое подключение__**: steam://connect/185.209.30.32:27315 \n> Обновлен ' + tome
        await mesajeje.edit(content=messagetype)
        time.sleep(20)
        print('Обновляем информацию')

# token = os.environ.get('BOT_TOKEN')
