from flask import Flask

app = Flask(__name__)
# CORS(app)
app.config['CACHE_TYPE'] = 'simple'
# cache.init_app(app)
from online_cart.source_code.api.online_cart.admin_apis import add_to_cart, update_quantity, delete_an_item
from online_cart.source_code.api.online_cart.functional_apis import all_items_information, total_price, total_including_taxes, particular_itm_information
