import asyncio
from orm import orm
from tests.user_test import *
from tests.user_comment_test import *
from tests.user_evaluation_test import *


loop = asyncio.get_event_loop()

sql_config = dict(host='localhost',
                  port=3306,
                  user='root',
                  password='wshwoaini',
                  db='itemmail',
                  charset='utf8',
                  autocommit=True,
                  maxsize=10,
                  minsize=1,
                  )

loop.run_until_complete(orm.create_pool(loop, **sql_config))





if __name__ == '__main__':
    loop.run_until_complete(find_users())
