import tortoise


async def reset_db():
    sql = """
    DROP TABLE IF EXISTS "aerich" CASCADE;
    DROP TABLE IF EXISTS "citybikestation" CASCADE;
    DROP TABLE IF EXISTS "address" CASCADE;
    
    """
    conn = tortoise.Tortoise.get_connection("default")
    await conn.execute_script(sql)
