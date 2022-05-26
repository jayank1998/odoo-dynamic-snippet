from datetime import datetime
import requests
from odoo import http, _
from odoo.http import content_disposition, request


class WebsiteController(http.Controller):

    @http.route('/get_bitcoin_history', type='http', auth='public', website=True)
    def get_bitcoin_history(self):
        url = 'https://api.coinstats.app/public/v1/charts?period=24h&coinId=bitcoin&currency=USD'
        temp_data = requests.get(url).json()
        count = 0
        price = {}
        price1, time1 = [], []
        key = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
        data = requests.get(key)
        current_price = data.json()

        for key, value in temp_data.items():
            for sm_data in value:
                time = sm_data[0]
                dt_object = datetime.fromtimestamp(time)
                date = dt_object.date()
                time1.append(str(dt_object.time()))
                price1.append(sm_data[1])
                price[count] = [str(date), sm_data[1]]
                count = count + 1

        vals = {'price': price1, 'time1': time1,
                'current_price': "%.2f" % float(current_price['price'])}
        # vals = {'price': price1, 'time1':time1}

        return request.render('bitcoin_track.report_found', vals)

    @http.route('/get_bitcoin_data_json', type='json', auth='public', website=True)
    def get_bitcoin_data(self):
        return 23
