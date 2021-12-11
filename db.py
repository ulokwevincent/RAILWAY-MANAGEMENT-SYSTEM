import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'vincent',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)


mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Train(
        ID INT NOT NULL AUTO_INCREMENT,
        trainname VARCHAR(255),
        destination VARCHAR(255),
        departuretime VARCHAR(255),
        price VARCHAR(255),
        availablesits VARCHAR(255),
        locationoftrain VARCHAR(255),
        PRIMARY KEY(ID)
        
    )
    """
)
