import os
import discord
from discord.ext import commands
from threading import Thread
from flask import Flask, render_template
intent = discord.Intents.all()
intent.message_content = True
app = Flask(__name__,template_folder="Templates")
bot = commands.Bot(command_prefix="~", intents=intent)

def run():
    app.run(host='0.0.0.0', port=10000, use_reloader=False, debug=True)
def stay():
    thread = Thread(target=run)
    thread.start()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    token = os.getenv("TOKEN")    
    stay()
    bot.run(token)
