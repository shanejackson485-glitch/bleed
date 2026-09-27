import os
import discord


# ============================================================
# Discord
# ============================================================

token = os.environ["DISCORD_TOKEN"]

owner_ids = {
    int(os.environ["OWNER_ID"]),
}


# ============================================================
# Bot
# ============================================================

prefix = os.getenv("PREFIX", ",")


class Status:
    type = discord.ActivityType.playing
    name = os.getenv("STATUS", "bleed")


# ============================================================
# PostgreSQL
# ============================================================

class Database:
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    host = os.environ["POSTGRES_HOST"]
    name = os.environ["POSTGRES_DATABASE"]


# ============================================================
# Colors
# ============================================================

class Color:
    bleed = discord.Color.from_str("#2b2d31")
    cooldown = discord.Color.from_str("#2b2d31")


# ============================================================
# Emojis
# ============================================================

class Emoji:
    cooldown = "⏳"


# ============================================================
# Links
# ============================================================

support_server = "https://discord.gg/7QHPCxU"