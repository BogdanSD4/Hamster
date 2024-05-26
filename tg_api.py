from telethon import TelegramClient

api_id = '29219023'
api_hash = 'd819aae666c77410272c662c0424048f'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Сессия уже сохранена, поэтому не нужно вводить номер телефона и код подтверждения
    await client.connect()

    if not await client.is_user_authorized():
        raise Exception("User is not authorized")

    user = await client.get_entity('sukhomlyn69')
    await client.send_message(user, 'не звертай уваги')

with client:
    client.loop.run_until_complete(main())