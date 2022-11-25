import asyncio


# async указывает, что функция асинхронна
async def waiter():
    task1 = asyncio.create_task(cook('Паста', 8))
    task3 = asyncio.create_task(cook('Салат Цезарь', 3))
    task2 = asyncio.create_task(cook('Отбивные', 16))

    await task1  # вызываем асинхронно
    await task2
    await task3


# time_to_prepare - секунды ожидания блюда

async def cook(order, time_to_prepare):
    print(f'Новый заказ: {order}')
    await asyncio.sleep(time_to_prepare)  # в это время можно выполнять другие задачи
    print(f'{order} - готово')

asyncio.run(waiter())
