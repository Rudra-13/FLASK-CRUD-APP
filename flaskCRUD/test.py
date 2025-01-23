# import pyodbc
# import pandas
# # cnxn_str = ("Driver={0DBC Driver 18 for SQL Server};"
# # "Server = localhost;"
# # "Database='student';"
# # "Trusted_Connection=yes;")

# # import pyodbc

# # # Define connection parameters
# server =  'localhost'
# database = 'student'
# username = 'root'
# password = 'Rudransh13$'

# # # Set up the connection string
# connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};USER={username};PASSWORD={password}'

# # # Establish connection
# # connection = pyodbc.connect(connection_string)

# # # Create cursor
# # cursor = connection.cursor()

# # # Example query
# # cursor.execute("SELECT * FROM your_table")

# # # Fetch and print results
# # rows = cursor.fetchall()
# # for row in rows:
# #     print(row)

# # # Close the cursor and connection
# # cursor.close()
# # connection.close()







# # import pyodbc

# # # Define connection parameters
# # server = 'localhost'  # or '127.0.0.1' or '192.168.x.x'
# # database = 'your_database'
# # username = 'your_username'
# # password = 'your_password'

# # # Use TCP/IP and ensure you're using the correct driver
# # connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=tcp:{server},1433;DATABASE={database};UID={username};PWD={password}'

# # Establish connection
# try:
#     connection = pyodbc.connect(connection_string)
#     cursor = connection.cursor()

#     # Example query
#     cursor.execute("SELECT * FROM your_table")
    
#     # Fetch and print results
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

#     # Close cursor and connection
#     cursor.close()
#     connection.close()
# except pyodbc.Error as e:
#     print(f"Error: {e}")




from sqlalchemy import create_engine,text

# Define connection parameters
username = 'root'  # replace with your MySQL username
password = '4321'  # replace with your MySQL password
host = 'localhost'  # assuming the server is local
port = '3306'  # default MySQL port
database = 'student'  # replace with the name of your database

# Create connection string
connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# Create the engine
engine = create_engine(connection_string)

# Test the connection by running a simple query
try:
    with engine.connect() as connection:
        print('connection success')

        result = connection.execute(text("SELECT * FROM student.student") )  # Simple query to check connection
        version = result.fetchall()
        print(f"MySQL: {version}")
except Exception as e:
    print(f"Error connecting to MySQL: {e}")
