from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    try:
        raise Exception("testing Exception module")
    except Exception as e:
        error_message = HousingException(e)
        logging.info(error_message.error_message)
        logging.info("testing logging module")
    return "this is a machine learning project"

if __name__=="__main__":
    app.run(debug=True)

