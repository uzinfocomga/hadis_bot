import asyncio

from aiohttp import ClientSession
from icecream import ic


class HTTPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self._session = None

    async def _get_session(self):
        if self._session is None:
            self._session = ClientSession()
        return self._session

    async def close(self):
        if self._session is not None:
            await self._session.close()


class CMCHTTPClient(HTTPClient):

    # @alru_cache
    async def add_read_hadith(self, user_id, hadith_id):
        data = {
            "user_id": user_id,
            "hadith_id": hadith_id
        }
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.post(self.base_url + "/read/", json=data) as resp:
                    return await resp.json()
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def add_liked_hadith(self, user_id, hadith_id):
        data = {
            "user_id": user_id,
            "hadith_id": hadith_id,
        }
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.post(self.base_url + "/like/", json=data) as resp:
                    return await resp.json()
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def update_read_hadith_id(self, user_id, hadith_id=1):
        data = {
            "pending_hadith_id": hadith_id
        }
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.patch(self.base_url + f"/user/{user_id}", json=data) as resp:
                    return await resp.json()
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def get_user(self, chat_id):
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.get(self.base_url + f"/user/{chat_id}") as resp:
                    if resp.status == 200:
                        return await resp.json()
                    return None
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def add_user(self, chat_id, full_name, username, language):
        data = {
            "chat_id": chat_id,
            "full_name": full_name,
            "username": username,
            "language": language,
        }
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.post(self.base_url + "/user/", json=data) as resp:
                    return await resp.json()
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def create_read_history(self, user_id, hadith_id=1):
        data = {
            "user_id": user_id,
            "hadith_id": hadith_id
        }
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.post(self.base_url + "/read_history/", json=data) as resp:
                    if resp.status == 200:
                        return await resp.json()
                    return None
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def get_hadith(self, hadith_id=1):
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.get(self.base_url + f"/hadith/{hadith_id}") as resp:
                    return await resp.json()
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def get_hadiths(self, start_num: int, size: int = 50):
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.get(self.base_url + "/hadith/all") as resp:
                    data = await resp.json()
                    all_items: list = data.get('hadiths')
                    overall_items_count: int = len(all_items)

                    # Если результатов больше нет, отправляем пустой список
                    if start_num >= overall_items_count:
                        return []
                    # Отправка неполной пачки (последней)
                    elif start_num + size >= overall_items_count:
                        return all_items[start_num:overall_items_count + 1]
                    else:
                        return all_items[start_num:start_num + size]
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def search_hadith(self, title: str, start_num: int, size: int = 50):
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.get(f"{self.base_url}/hadith/search",
                                       params={"title": title, "offset": start_num, "size": size}) as resp:
                    data = await resp.json()
                    ic(data)
                    return data.get('hadiths', [])
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def get_current_books(self, skip=0, limit=10):
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.get(self.base_url + f"/necessary_book/?skip={skip}&limit={limit}") as resp:
                    return await resp.json()
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    async def get_friends(self, start_num: int, size: int = 50):
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.get(self.base_url + "/user/all") as resp:
                    data = await resp.json()
                    ic(data)
                    ic(start_num)
                    all_items: list = data.get('users')
                    overall_items_count: int = len(all_items)

                    # Если результатов больше нет, отправляем пустой список
                    if start_num >= overall_items_count:
                        return []
                    # Отправка неполной пачки (последней)
                    elif start_num + size >= overall_items_count:
                        return all_items[start_num:overall_items_count + 1]
                    else:
                        return all_items[start_num:start_num + size]
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def get_user_read_count(self, chat_id, today=False, week=False):
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                # ex = "http://localhost:5173/read/user/557407324?today=false&week=false"
                async with session.get(self.base_url + f"/read/user/{chat_id}?today={today}&week={week}") as resp:
                    data = await resp.json()
                    ic(data)
                    return data.get('read_count')
        except asyncio.TimeoutError:
            print("Request timed out")
            return None

    # @alru_cache
    async def get_top_users_stats(self, top_total=False, top_week=False, top_today=False):
        session = await self._get_session()
        try:
            async with asyncio.timeout(10):  # Set a timeout for the request
                async with session.get(self.base_url + f"/read/?top_total={top_total}&top_week={top_week}&top_today={top_today}") as resp:
                    data = await resp.json()
                    ic(data)
                    return data
        except asyncio.TimeoutError:
            print("Request timed out")
            return None
