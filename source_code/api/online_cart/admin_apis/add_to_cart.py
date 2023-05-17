from flask import Flask,jsonify
from online_cart.source_code.api.settings import logger, connection, handle_exceptions

from online_cart.source_code.api import app

@app.route("/cart/add", methods=["POST"], endpoint="add_to_cart")
@handle_exceptions
def buy_stocks():
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    if "item" and "price" and "quantity" not in request.json:
        raise Exception("details missing")
    data = request.get_json()
    item = data['item']
    price = data['price']
    quantity = data['quantity']
    cur.execute('INSERT INTO cart_data(item,quantity,price )''VALUES (%s, %s, %s);',
                (item, quantity, price))
    conn.commit()
    logger(__name__).warning("close the database connection")
    return jsonify({"message" : "created sucessfully"})