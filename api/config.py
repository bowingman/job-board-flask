postgresql = {
    'host': 'localhost',
    'user': 'postgres',
    'passwd': '123456',
    'db': 'flask-job-board'
}

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(
    postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])
