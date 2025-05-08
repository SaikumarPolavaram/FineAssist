from flask import Flask, jsonify
from flask_cors import CORS

from src.endpoints.main import api

app = Flask(__name__)
CORS(app)


@app.get("/api")
def root():
    "***** Liveliness Check *****"
    try:
        response_dict = {
            "project": "SAF-FMBOP",
            "message": "Server is Running Successfully."
        }, 200
        return jsonify(response_dict)
    
    except Exception as e:
        return jsonify({"message":f"Error: {e}"}), 500


app.register_blueprint(api)



if __name__ == "__main__":
    # app.run(host='192.168.27.200', port=5050, debug=True, use_reloader=True)
    app.run(host="0.0.0.0",port=5050)
    