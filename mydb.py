import mysql.connector

# Create a connection to MySQL using a config dictionary.
config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'aks@1998',
    'auth_plugin': 'caching_sha2_password',
    'port': 5432  # Specify the port you have configured in your MySQL server.
}

try:
    dataBase = mysql.connector.connect(**config)
    print("Connected to MySQL on port 5432")
    
    # You can perform database operations here.
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'dataBase' in locals():
        cursorObject = dataBase.cursor()
        # Create a database
        cursorObject.execute("CREATE DATABASE elderco")
        dataBase.close()
