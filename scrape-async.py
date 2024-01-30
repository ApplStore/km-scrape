import asyncio
import aiohttp
import json

async def fetch_data(session, url, headers):
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def main():
    headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VydHlwZSI6InN0dWRlbnQiLCJ1c2VyaWQiOjI4MTE2MzEsIm1haW5pZCI6NzUzNjIzLCJjbGFzc2lkIjoxNzE0NTQsImNsYXNzYWNjZXNzIjpbMTcxNDU0XSwiY291cnNlaWQiOjE5NSwidGVhY2hlcmlkIjo0NjExMCwic2Nob29saWQiOjExNiwic2Nob29sbmFtZSI6IlRcdTAwZTRieSBFbnNraWxkYSBneW1uYXNpdW0iLCJpYXQiOjE3MDY2NDEyMjUsIm5iZiI6MTcwNjY0MTIyNSwiZXhwIjoxNzA2NjU5MjI1fQ.xQvmuMg4knucLwQzfMVySXuhlEmXJfBRGJC7rd927jk'}  # Replace with your actual headers
    base_url = 'https://km-prod-euw-01-api.azurewebsites.net/uppgifter/'
    tasks = []
    response_data = {}
    start_id = 1
    end_id = 1000

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        for i in range(start_id, end_id+1, 1):
            url = (f'https://km-prod-euw-01-api.azurewebsites.net/uppgifter/{i}')
            print(url)
            task = asyncio.create_task(fetch_data(session, url, headers))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

    for i, response in zip(range(start_id, end_id+1, 1), responses):

        response_data.update({str(i): response})

        with open("data.json", "r") as json_file:
            cached_data = json.load(json_file)
        
        cached_data = cached_data | response_data

        with open("data.json", "w") as json_file:
            json.dump(cached_data, json_file)

        if len(response["sqldata"]) == 0:     
            print(f"{base_url}{i}: EMPTY")
        else:
            print(f"{base_url}{i}: QUESTION")


if __name__ == "__main__":
    asyncio.run(main())