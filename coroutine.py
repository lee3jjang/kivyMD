import asyncio
from time import time
from urllib.request import Request, urlopen

urls = [f'https://www.google.co.kr/search?q={i}' for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]

async def fetch(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = await loop.run_in_executor(None, urlopen, request)
    page = await loop.run_in_executor(None, response.read)
    return len(page)

async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
    result = await asyncio.gather(*futures)
    print(result)

# urls = [f'https://www.google.co.kr/search?q={i}' for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]
# url = urls[0]
# request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# response = urlopen(request)
# response.read()


begin = time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
end = time()
print(f'실행 시간 : {end-begin:.3f}초')