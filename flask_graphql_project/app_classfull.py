from flask import Flask
from flask_classful import FlaskView, route
import psycopg2
import json
from flask import jsonify


# we'll make a list to hold some quotes for our app
quotes = [
    "A noble spirit embiggens the smallest man! ~ Jebediah Springfield",
    "If there is a way to do it better... find it. ~ Thomas Edison",
    "No one knows what he can do till he tries. ~ Publilius Syrus"
]

app = Flask(__name__)

class QuotesView(FlaskView):
    def index(self):
        return "<br>".join(quotes)
    
    def home(self):
        return 'I am Ravi'

    @route('/kalyan/')
    def kalyan(self):
        return 'I am kalayan'

    
    @route('mydata')
    def show(self):
        conn = psycopg2.connect(database = "flaskbikes", user = "postgres", password = "Ravi@143", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT name from COMPANY")
        c_data = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        # data = json.dumps(c_data)
        data = [{'name': 'kalyan'}, {'name': 'prasad'}]
        ks = jsonify(data)
        return ks

QuotesView.register(app, route_base = '/')

if __name__ == '__main__':
    app.run(debug=True)