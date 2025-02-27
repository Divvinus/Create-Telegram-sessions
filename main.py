from create_session import create_sessions
from config import USE_PROXY 
import asyncio
import os

async def main():
    action = int(input('Select action:\n1. Create session\n>'))
    
    if not os.path.exists('sessions'):
        os.mkdir('sessions')

    if action == 1:
        await create_sessions()
                
        tasks = []
        if USE_PROXY:
            proxy_dict = {}
            with open('proxy.txt','r',encoding='utf-8') as file:
                proxy = [i.strip().split() for i in file.readlines() if len(i.strip().split()) == 2]
                for prox,name in proxy:
                    proxy_dict[name] = prox
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())