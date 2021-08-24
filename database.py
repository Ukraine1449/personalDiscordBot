import mysql.connector as mysql

HOST = "brqkl53fr9bwvyse9qem-mysql.services.clever-cloud.com"
DATABASE = "brqkl53fr9bwvyse9qem"
USER = "u08pbd5nqpt09pgf"
PASSWORD = "F5rFojAJrcgUU2VPriSI"
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db_connection.get_server_info())
c = db_connection.cursor()
c.execute('CREATE TABLE IF NOT EXISTS UserActivity (UUID int, TotalMessages int, Rank int, XP int, PRIMARY KEY (UUID))')


def addMessage(UUID, oldMessageNum):
    c.execute(f'UPDATE UserActivity SET TotalMessages="{oldMessageNum + 1}" WHERE UUID={UUID}')
    db_connection.commit()


def newUser(UUID):
    c.execute(f"INSERT INTO UserActivity(UUID, TotalMessages, Rank, XP) VALUES ({UUID}, {0}, {0}, {0}) ON DUPLICATE KEY IGNORE")
    db_connection.commit()
