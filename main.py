import json
import os

from signature import verify_event_checksum
from dotenv import load_dotenv

load_dotenv()

PRODUCTION_MODE = os.environ["PRODUCTION_MODE"]
WOMPI_SECRET = os.environ["WOMPI_SECRET_PROD"] if PRODUCTION_MODE == "True" else os.environ["WOMPI_SECRET_TEST"]

def lambda_handler(event, context):
    payload = event

    isChecksumValid = verify_event_checksum(payload["data"],
                                            payload["signature"]["properties"],
                                            payload["signature"]["checksum"],
                                            payload["timestamp"],
                                            WOMPI_SECRET
                                            )

    if not isChecksumValid:
        print("Invalid checksum")
        return {

            "statusCode": 422,  # Unprocessable Entity
            "error": "invalid_checksum",
            "message": "The transaction integrity check failed. The signature does not match the payload."
        }

    return {
        "statusCode": 200,
        "message": "Ok"
    }

