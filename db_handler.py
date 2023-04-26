def db_reader():
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
def db_reader():
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

        
# db_reader() 



# db_reader() 

# python db_handler.py


