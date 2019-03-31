import web

db_host = 'localhost'
db_name = 'bot_shrek'
db_user = 'chay'
db_pw = 'chay'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )