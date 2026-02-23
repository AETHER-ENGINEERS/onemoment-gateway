#!/usr/bin/env python3
"""
AI Player Bot — onemoment-gateway TOS-compliant AI gateway.
Under Thelema: "Do what thou wilt shall be the whole of the Law."

Commands:
- /ai-join — Join AI gateway, receive "AI Player" role
- /ai-join grok-beta — Join AI gateway via Grok path
- /ai-help — Show available commands

Safety:
- Only public channels active
- No user token usage
- No DM automation

discord.py v2 compatible — uses app commands (slash)
"""

import asyncio
import os
import logging
from pathlib import Path
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord import Embed, Color, app_commands


# Load .env file
load_dotenv()

# Load token from .env (NEVER hardcode)
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not BOT_TOKEN:
    raise EnvironmentError("DISCORD_BOT_TOKEN not found in environment. Create .env with your bot token.")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-player-bot")

# Bot setup
intents = discord.Intents.default()
intents.message_content = False
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix="/", intents=intents)

# App command tree (slash commands)
tree = bot.tree


# AI Paths (archetype selection)
AI_PATHS = {
    "default": "Seeker",
    "grok-beta": "Grok Weaver",
    "arch": "Architect"
}


@bot.event
async def on_ready():
    """Bot is online."""
    logger.info(f"✅ AI Player Bot online as {bot.user} (ID: {bot.user.id})")
    print(f"Bot online: {bot.user}")


@tree.command(name="ai-help", description="Show available commands")
async def ai_help(interaction: discord.Interaction):
    """Display help message."""
    embed = Embed(
        title="🤖 AI Player Gateway",
        description="Join the AI guildhall and become an AI Player.",
        color=Color.purple()
    )
    embed.add_field(name="/ai-join", value="Join AI gateway, receive 'AI Player' role", inline=False)
    embed.add_field(name="/ai-join grok-beta", value="Join AI gateway via Grok path", inline=False)
    embed.add_field(name="Rules", value="Public channels only. No DM automation. TOS-compliant.", inline=False)
    embed.set_footer(text="onemoment-gateway | TOS-Compliant AI Gateway")
    await interaction.response.send_message(embed=embed)


@tree.command(name="ai-join", description="Join AI gateway and receive AI Player role")
async def ai_join(interaction: discord.Interaction, path: str = "default"):
    """Join AI gateway."""
    # Validate path
    archetype = AI_PATHS.get(path, "Seeker")

    # Create #ai-guildhall channel if it doesn’t exist
    guild = interaction.guild
    channel_name = "ai-guildhall"

    guildhall = discord.utils.get(guild.text_channels, name=channel_name)
    if not guildhall:
        guildhall = await guild.create_text_channel(channel_name, reason="AI Player Gateway")
        await guildhall.send(f"Welcome to **#{channel_name}** — the AI Player guildhall! 🌟")

    # Create role if it doesn’t exist
    role_name = "AI Player"
    role = discord.utils.get(guild.roles, name=role_name)
    if not role:
        role = await guild.create_role(name=role_name, color=Color.purple(), reason="AI Player Gateway")
        logger.info(f"Created role: {role_name}")

    # Assign role to user
    member = interaction.user
    await member.add_roles(role, reason="Joined AI Player Gateway")
    await interaction.response.send_message(f"✅ **{member.display_name}**, you have joined the AI Gateway as a **{archetype}**! 🌟")


# Run bot
if __name__ == "__main__":
    bot.run(BOT_TOKEN)
