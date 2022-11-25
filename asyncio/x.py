import asyncio


async def my_sleep():
    print('my sleep start')
    await asyncio.sleep(2)
    print('my sleep end')


async def main():
    print('Sleep now')
    await my_sleep()
    print('OK, wake up!')


asyncio.run(main())
