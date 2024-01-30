import json
import requests
import aiohttp
import asyncio

headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VydHlwZSI6InN0dWRlbnQiLCJ1c2VyaWQiOjI4MTE2MzEsIm1haW5pZCI6NzUzNjIzLCJjbGFzc2lkIjoxNzE0NTQsImNsYXNzYWNjZXNzIjpbMTcxNDU0XSwiY291cnNlaWQiOjE5NSwidGVhY2hlcmlkIjo0NjExMCwic2Nob29saWQiOjExNiwic2Nob29sbmFtZSI6IlRcdTAwZTRieSBFbnNraWxkYSBneW1uYXNpdW0iLCJpYXQiOjE3MDY2NDEyMjUsIm5iZiI6MTcwNjY0MTIyNSwiZXhwIjoxNzA2NjU5MjI1fQ.xQvmuMg4knucLwQzfMVySXuhlEmXJfBRGJC7rd927jk'}

#res = requests.get('https://km-prod-euw-01-api.azurewebsites.net/uppgifter/278975', headers=headers)

#print(res.json())

for i in range(278975, 279000, 1):
    i = str(i)
    print(f"https://km-prod-euw-01-api.azurewebsites.net/uppgifter/{i}")
    res = requests.get(f'https://km-prod-euw-01-api.azurewebsites.net/uppgifter/{i}', headers=headers)
    print(res.json())
  


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://km-prod-euw-01-api.azurewebsites.net/uppgifter/{i}', headers=headers) as resp:
            print(resp.status)
            print(await resp.text())

loop = asyncio.get_event_loop() 
loop.run_until_complete(main())
