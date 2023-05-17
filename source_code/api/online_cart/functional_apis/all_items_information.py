from flask import Flask,jsonify
from online_cart.source_code.api.settings import logger, connection, handle_exceptions

from online_cart.source_code.api import app


@app.route("/cart/all", methods=["GET"], endpoint="all_items")
@handle_exceptions
def all_items():
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('SELECT *  FROM cart_data')
    rows = cur.fetchall()
    print(rows)
    if not rows:
        return jsonify({"message": f"No rows found "})
    data_list = []
    for row in rows:
        print("inside loop", row)
        id,item,price,quantity = row
        data = {
            "id" : id,
            "item" : item,
            "quantity" : quantity,
            "price" : price
        }
        data_list.append(data)
        logger(__name__).warning("close the database connection")
    print(data_list)
    return jsonify({"message":"all items","details":data_list})
