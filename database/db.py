import aiosqlite
import logging

# Добавление пользователя в базу данных
async def add_user(tg_id):
    async with aiosqlite.connect('db.db') as db:
        async with db.execute("SELECT * FROM users WHERE tg=?", (tg_id,)) as cursor:
            user = await cursor.fetchone()
            if user:
                return True
            else:
                await db.execute("INSERT INTO users (tg) VALUES (?)", (tg_id,))
                await db.commit()
                return False

# Получение данных пользователя
async def get_user_data(tg_id):
    async with aiosqlite.connect('db.db') as db:
        async with db.execute("SELECT * FROM users WHERE tg=?", (tg_id,)) as cursor:
            return await cursor.fetchone()

# Сохранение ответа Таро в базу данных
async def save_taro_response(user_id, question, answer):
    async with aiosqlite.connect('db.db') as db:
        await db.execute(
            "INSERT INTO taro (tg, question, answer) VALUES (?, ?, ?)",
            (user_id, question, answer)
        )
        await db.commit()