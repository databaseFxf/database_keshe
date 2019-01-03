class Transaction:
    def __init__(self, conn):
        self.conn = conn

    async def begin(self):
        await self.conn.begin()

    async def commit(self):
        await self.conn.commit()
        await self.conn.close()

    async def roll_back(self):
        await self.conn.roll_back()
        await self.conn.close()
