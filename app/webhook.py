from flask import Flask, request
import starkbank
import os
from dotenv import load_dotenv
from transfer import make_transfer

load_dotenv()
app = Flask(__name__)

with open(os.getenv("STARKBANK_PRIVATE_KEY_PATH"), "r") as key_file:
    private_key = key_file.read()

starkbank.user = starkbank.Project(
    environment="sandbox",
    id=os.getenv("STARKBANK_PROJECT_ID"),
    private_key=private_key,
)

@app.route("/webhook/invoice", methods=["POST"])
def invoice_callback():
    content = request.data.decode("utf-8")
    signature = request.headers["Digital-Signature"]
    try:
        event = starkbank.event.parse(content=content, signature=signature)
        if "invoice" in event.subscription:
            invoice_log = starkbank.invoice.log.get(event.log.id)
            invoice = invoice_log.invoice
            if invoice.status == "paid":
                print(f"💰 Invoice {invoice.id} paga com valor {invoice.amount}")
                make_transfer(invoice.amount)
            else:
                print(invoice.status)
        return "", 200
    except Exception as e:
        print(f"Error executing webhook: {e}")
        return "Error", 400

if __name__ == "__main__":
    app.run(port=5000)