import aiohttp

from data.constants import REG_URL


async def registration(login: str, passwd: str) -> int:
    """
    Запрос на регистрацию пользователя на сайте.
    :param login:
    :param passwd:
    :return Статус от ответа:
    """
    async with aiohttp.ClientSession() as session:
        data = {"login": login, "password": passwd}
        async with session.post(REG_URL, data=data) as response:
            return response.status
