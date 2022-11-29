from flask import Flask
from logic import *

app = Flask(__name__)


@app.route('/game')
def game():
    if play():
        response = {
            'Name:': f' {screen_name}',
            'Distance Travelled': f' {total_distance_travelled}',
            'Fuel Consumed: ': f' {round(Fuel_consumed_during_flight, 2)}',
            'Score: ': f' {round((Fuel_consumed_during_flight / passenger_sum), 2)}'
        }
        return response
    else:
        return 'Error'


app.run(use_reloader=True, host='127.0.0.1', port=5000)
