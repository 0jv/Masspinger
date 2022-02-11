
import aiohttp, asyncio, threading, os

class Pinger:

    def __init__(self):
      self.token = input("Token -> ")
      self.guild = input("Guild -> ")
      self.name = input("Name -> ")
      self.message = input("Message -> ")
      self.amount = int(input("Amount -> ")) 
      self.headers = {
        "Authorization" : f"Bot {self.token}"
      }
      self.channels = open("channels.txt").read().splitlines()
      self.clear = lambda: os.system("cls") if os.name == "nt" else os.system("clear")

    async def Create_Webhook(self, channel):
      try:
        async with aiohttp.ClientSession(headers = self.headers) as session:
          async with session.post(f"https://discord.com/api/v9/channels/{channel}/webhooks", headers = self.headers, json = {
            "name" : self.name
          }) as response:
            json = await response.json()
            webhook_id = json['id']
            webhook_token = json['token']
            return f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"
      except Exception:
        pass

    async def Send_Webhook(self, webhook):
      try:
        for i in range(self.amount):
          async with aiohttp.ClientSession(headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"}) as session:
            async with session.post(webhook, json = {
              "username" : self.name,
              "content" : self.message
            }) as response:
              if response.status in [200, 201, 204]:
                print(f"Spammed webhook -> {webhook}")
              else:
                print(f"Error spamming webhook -> {webhook}")
      except Exception:
        pass

    async def Start(self):
      self.clear()
      try:
        input("Press enter to start ->")
        for channel in self.channels:
          webhook = await self.Create_Webhook(channel)
          threading.Thread(target=asyncio.run, args=(self.Send_Webhook(webhook,),)).start() #:flushed:
      except:
        pass

if __name__ == "__main__":
  pinger = Pinger()
  asyncio.get_event_loop().run_until_complete(pinger.Start())
