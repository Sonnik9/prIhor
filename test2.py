import mysql.connector

try:
    # Establish connection to the database
    cnx = mysql.connector.connect(
        user='hote_tophot77_db',
        password='6lrMgXfBcwakSujt',
        host='5.75.140.137',
        port=8090,
        database='hote_tophot77_db',
        connect_timeout=200
    )
    print('ok')
    # Create a cursor to execute SQL queries
    cursor = cnx.cursor()
    cursor.execute("SET GLOBAL max_allowed_packet = 1073741824")

    # Execute a query
    # query = "SELECT * FROM upz_hotels"
    # query = "SELECT * FROM `upz_hotels` WHERE 1"
    # cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchone()

    # Print the fetched rows
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    cnx.close()


except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))



# class DBase:

#     config = {
#         'user': 'admin',
#         'password': '8dGBX2Kx',
#         'host': '5.75.140.137',
#         'port': 8090,
#         'database': 'hote_tophot77_db',
#         'raise_on_warnings': True,
#         # 'use_pure': 'False',
#         }
#     try:
#         def __init__(self):
#             import mysql.connector
#             self.cnx = mysql.connector.connect(**self.config)
#             self.cur = self.cnx.cursor(buffered=True)
#             print(self.cnx)
#         def __enter__(self):
#             return DBase()

#         def __exit__(self, exc_type, exc_val, exc_tb):
#             self.cnx.commit()
#             if self.cnx:
#                 self.cnx.close()
#     except Exception as ex:
#         print(ex)


# DBase() 




# def db_secReader():
#     import mysql.connector
#     # Connect to the database
#     cnx = mysql.connector.connect(
        # host="tophot77.mysql.tools",
        # user="tophot77_db",
        # password="8dGBX2Kx",
        # database="tophot77_db"
#     )

#     # Create a cursor object
#     cursor = cnx.cursor()

#     # Execute a query
#     query = "SELECT * FROM your_table"
#     cursor.execute(query)

#     # Fetch the results
#     results = cursor.fetchall()

#     # Print the results
#     for row in results:
#         print(row)

#     # Close the cursor and connection
#     cursor.close()
#     cnx.close() 

# db_secReader()  



# def musqlll():
#     import MySQLdb

#     # Set the database connection parameters
#     host = "https://5.75.140.137:8090/phpmyadmin/index.php?route=/database/structure&db=hote_tophot77_db"
#     user = "admin"
#     password = "6lrMgXfBcwakSujt"
#     database = "hote_tophot77_db"

#     # Connect to the database
#     db = MySQLdb.connect(host=host, user=user, password=password, db=database)

#     # Create a cursor object
#     cursor = db.cursor()

#     # Execute the SELECT query to fetch all the data from the upz_hotels table
#     cursor.execute("SELECT * FROM upz_hotels")

#     # Fetch all the rows and print them
#     rows = cursor.fetchall()
#     for row in rows[:20]:
#         print(row)

#     # Close the database connection
#     db.close() 


# musqlll()

