from flask import Flask,jsonify
from online_cart.source_code.api.settings import logger, connection, handle_exceptions

from online_cart.source_code.api import app


@app.route("/cart/<int:id>", methods=["GET"], endpoint="particular_item")
@handle_exceptions
def particular_item(id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('SELECT item,price,quantity FROM cart_data WHERE id = %s',(id,))
    rows = cur.fetchone()
    if not rows:
        return jsonify({"message": f"No rows found "})
    data_list = []
    item, price, quantity = rows
    data = {
        "item": item,
        "quantity": quantity,
        "price": price
    }
    data_list.append(data)
    logger(__name__).warning("close the database connection")

    return jsonify({"message": "item",  "details": data_list})


