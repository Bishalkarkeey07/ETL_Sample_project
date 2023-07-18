from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from tabulate import tabulate

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Pass'
app.config['MYSQL_DB'] = 'twitter_api_task'
api = Api(app)
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def get_data():
    # Connect to the MySQL database
    cur = mysql.connection.cursor()

    # Execute the SELECT query
    cur.execute("SELECT * FROM fact_table")

    # Fetch all the data
    data = cur.fetchall()

    # Clos cx0cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx fce the cursor
    cur.close()

    column_names = [desc[0] for desc in cur.description]

    # Format the data as a table with visible columns
    table = tabulate(data, headers=column_names, tablefmt="psql")

    # Return the data as a table
    return table


if __name__ == '__main__':
    app.run()

