import sys

import arrow
import discord


async def botinformation(cmd, message, args):
    version_data = cmd.bot.info.version.raw
    author_data = cmd.bot.info.authors.raw
    sigma_image = 'https://i.imgur.com/mGyqMe1.png'
    support_url = 'https://discordapp.com/invite/aEUCHwX'
    ver_nest = version_data["version"]
    full_version = f'{ver_nest["major"]}.{ver_nest["minor"]}.{ver_nest["patch"]}'
    if version_data['beta']:
        full_version += ' Beta'
    sigma_title = f'Apex Sigma: v{full_version}  {version_data["codename"]}'
    env_text = f'Language: **Python {sys.version.split()[0]}**'
    env_text += f'\nLibrary: **discord.py** {discord.__version__}'
    env_text += f'\nPlatform: **{sys.platform.upper()}**'
    auth_text = ''
    for author in author_data:
        auth = discord.utils.find(lambda x: x.id == author['id'], cmd.bot.get_all_members())
        if auth:
            auth_text += f'\n**{auth.name}**#{auth.discriminator}'
        else:
            auth_text += f'\n**{author["name"]}**#{author["discriminator"]}'
    response = discord.Embed(color=0x1B6F5F, timestamp=arrow.get(version_data['build_date']).datetime)
    response.set_author(name=sigma_title, icon_url=sigma_image, url=support_url)
    response.add_field(name='Authors', value=auth_text)
    response.add_field(name='Environment', value=env_text)
    response.set_footer(text=f'Last updated {arrow.get(version_data["build_date"]).humanize()}')
    await message.channel.send(embed=response)
