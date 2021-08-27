import mysql.connector as mysql

HOST = "brqkl53fr9bwvyse9qem-mysql.services.clever-cloud.com"
DATABASE = "brqkl53fr9bwvyse9qem"
USER = "u08pbd5nqpt09pgf"
PASSWORD = "F5rFojAJrcgUU2VPriSI"
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db_connection.get_server_info())
c = db_connection.cursor()
c.execute('CREATE TABLE IF NOT EXISTS UserActivity(UUID BIGINT, TotalMessages int, Level int, XP int)')


def addMessage(UUID, oldMessageNum, oldXPNum):
    c.execute(f'UPDATE UserActivity SET TotalMessages="{oldMessageNum + 1}" WHERE UUID={UUID}')
    db_connection.commit()
    c.execute(f'UPDATE UserActivity SET XP="{oldXPNum + 1}" WHERE UUID={UUID}')
    db_connection.commit()


def getTotalMessages(UUID):
    c.execute(f'SELECT TotalMessages FROM UserActivity where UUID ={UUID}')
    print(c.fetchone().index(1))
    #toreturn = c.fetchone().index(0)
    db_connection.commit()
    #return toreturn


def getTotalXP(UUID):
    c.execute(f'SELECT XP FROM UserActivity where UUID ={UUID}')
    toreturn = c.fetchone().index(0)
    db_connection.commit()
    return toreturn


def newUser(UUID):
    c.execute(f"INSERT INTO UserActivity(UUID) VALUES ({UUID})")
    db_connection.commit()


def userLeave(UUID):
    c.execute(f'DELETE FROM UserActivity WHERE UUID={UUID}')
    db_connection.commit()


def getLevel(UUID):
    c.execute(f'SELECT XP FROM UserActivity where UUID ={UUID}')
    toreturn = c.fetchone().index(0)
    db_connection.commit()
    return toreturn
