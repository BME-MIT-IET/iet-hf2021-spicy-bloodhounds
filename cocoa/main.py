from datetime import timedelta

import discord

from cocoa.helpers import envloader
from cocoa import booking, config, notifier, scheduler, controller, model

client = discord.Client()

meeting_length = timedelta(minutes=30)

modelsvc = model.ModelService()
bookingsvc = booking.BookingService(modelsvc)
notifiersvc = notifier.NotifierService(bookingsvc)
schedulersvc = scheduler.Scheduler(modelsvc, notifiersvc, meeting_length)
configsvc = config.ConfigService(modelsvc)
controllersvc = controller.Controller(configsvc, schedulersvc)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    controllersvc.handle_message(message, client)


client.run(envloader.config['bot_token'])