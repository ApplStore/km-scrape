import asyncio
import aiohttp
import json

async def fetch_data(session, url, headers):
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def main():
    headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VydHlwZSI6InN0dWRlbnQiLCJ1c2VyaWQiOjI4MTE2MzEsIm1haW5pZCI6NzUzNjIzLCJjbGFzc2lkIjoxNzE0NTQsImNsYXNzYWNjZXNzIjpbMTcxNDU0XSwiY291cnNlaWQiOjE5NSwidGVhY2hlcmlkIjo0NjExMCwic2Nob29saWQiOjExNiwic2Nob29sbmFtZSI6IlRcdTAwZTRieSBFbnNraWxkYSBneW1uYXNpdW0iLCJpYXQiOjE3MDY2MDI0ODYsIm5iZiI6MTcwNjYwMjQ4NiwiZXhwIjoxNzA2NjIwNDg2fQ.hDrr8-m8nTg26BJC0T8NikgPV0naA96X2Y0wdlmYE7M'}  # Replace with your actual headers
    base_url = 'https://km-prod-euw-01-api.azurewebsites.net/uppgifter/'
    tasks = []
    start_id = 278975
    end_id = 280000

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        for i in range(start_id, end_id, 1):
            url = (f'https://km-prod-euw-01-api.azurewebsites.net/uppgifter/{i}')
            print(url)
            task = asyncio.create_task(fetch_data(session, url, headers))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

    for i, response in zip(range(start_id, end_id, 1), responses):
        print(f"Response for {base_url}{i}: {response}")

if __name__ == "__main__":
    asyncio.run(main())