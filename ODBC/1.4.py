from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__, template_folder=’templates’)

#functions to be added here for
#different actions

if __name__ == ’__main__’:
	# Run the Flask app
	app.run(host=’127.0.0.1’, debug=True, port=5000)