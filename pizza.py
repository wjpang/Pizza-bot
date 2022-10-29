"""Main bot module.

This module sets up the bot with required intents and cogs for main
functionality, before running the bot itself with all the cogs loaded. A bot
token defined in a '.env' file is required to run the bot. Once the token is
defined, this module can be run as is to start the bot.
"""

import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

_intents = discord.Intents.default()
_intents.members = True
_intents.message_content = True
_intents.messages = True
_intents.bans = True

load_dotenv()
_token = os.getenv("token")

_bot = commands.Bot(
    command_prefix="+",
    intents=_intents,
    description="A Pizza Pizza Bot",
    case_insensitive=True,
    reload=True,
    max_messages=1000000000,
)
_bot.remove_command("help")

_bot.run(_token, reconnect=True, log_handler=_handler, log_level=logging.DEBUG)
