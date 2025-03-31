from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pymysql

app = Flask(__name__)

# Conexión a la base de datos MySQL
def get_db_connection():
    return pymysql.connect(
        host="db_bi",
        user="user",
        password="password",
        database="bi",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "BI Service Running"}), 200

@app.route("/data/report", methods=["GET"])
def generate_report():
    conn = get_db_connection()
    query = "SELECT * FROM data_table"  # Modifica esto según la estructura de datos
    df = pd.read_sql(query, conn)
    conn.close()

    summary = {
        "total_rows": len(df),
        "columns": list(df.columns),
        "mean_values": df.mean().to_dict(),
        "median_values": df.median().to_dict(),
    }

    return jsonify(summary), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8005)
