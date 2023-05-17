from flask import Flask,jsonify
from online_cart.source_code.api.settings import logger, connection, handle_exceptions

from online_cart.source_code.api import app


@app.route("/cart/total/taxes", methods=["GET"], endpoint="total_cost_taxes")
@handle_exceptions
def total_cost():
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('SELECT item, quantity, price FROM cart_data')
    rows = cur.fetchall()
    if not rows:
        return jsonify({"message": f"No rows found "})
    total = 0
    for row in rows:
        item, price, quantity = row
        item_total = quantity*price
        total += item_total
        taxes =(total*12)/100
        total_value = total+taxes
    return jsonify({"total_value": total_value})
