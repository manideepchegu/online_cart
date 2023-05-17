from flask import Flask,jsonify
from online_cart.source_code.api.settings import logger, connection, handle_exceptions

from online_cart.source_code.api import app


@app.route("/cart/delete/<int:id>", methods=["DELETE"], endpoint="delete_item")
@handle_exceptions
def delete_item(id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('DELETE FROM cart_data WHERE id=%s', (id,))
    logger(__name__).warning("close the database connection")
    conn.commit()
    if cur.rowcount > 0:
        return jsonify({"message": "item deleted successfully"})
    else:
        return jsonify({"message": "item not found"})