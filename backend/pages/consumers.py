import json 
from random import randint
from time import sleep
 
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer


class ChartConsumer(WebsocketConsumer):
    def connect(self):
         self.accept()
         
         for i in range(1000):
              self.send(json.dumps({'value':randint(1,100)}))
              sleep(1)

# class ChartConsumer(WebsocketConsumer):

#       async def connect(self):
#            await self.accept()

#       async def receive(self, text_data=None, bytes_data=None, **kwargs):
#             if text_data == 'PING':
#                  await self.send('PONG')