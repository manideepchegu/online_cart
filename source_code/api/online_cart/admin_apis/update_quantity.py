from flask import Flask,jsonify
from online_cart.source_code.api.settings import logger, connection, handle_exceptions

from online_cart.source_code.api import app


@app.route("/cart/update/<int:id>", methods=["PUT"], endpoint="update_item")
@handle_exceptions
def update_item(id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    if "quantity" not in request.json:
        return Exception("details missing")
    data = request.get_json()
    quantity = data.get('quantity')
    cur.execute('SELECT quantity FROM cart_data WHERE id=%s', (id,))
    data = cur.fetchone()
    if data:
        cur.execute('UPDATE cart_data SET quantity= %s  WHERE id = %s', (quantity, id))
        conn.commit()
        return jsonify({"message": "updated successfully"})
    else:
        return jsonify({"message": "item not found"})
