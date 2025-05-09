import os
import random
import time
from datetime import datetime, timedelta, timezone

import starkbank
from starkbank import Invoice
from dotenv import load_dotenv

load_dotenv()

with open(os.getenv("STARKBANK_PRIVATE_KEY_PATH"), "r") as file:
    private_key = file.read()

starkbank.user = starkbank.Project(
    environment="sandbox",
    id=os.getenv("STARKBANK_PROJECT_ID"),
    private_key=private_key
)

cpfs_validos = [
    "012.345.678-90",
    "000.000.001-91",
    "111.444.777-35"
]

nomes = ["Customer 1", "Customer 2", "Customer 3", "Customer 4", "Customer 5"]

def gerar_invoices():
    quantidade = random.randint(8,12)
    invoices = []

    for _ in range(quantidade):
        nome = random.choice(nomes)
        tax_id = random.choice(cpfs_validos)
        amount = random.randint(10000, 50000)
        due = datetime.now(timezone.utc) + timedelta(days=2)

        invoices.append(
            Invoice(
                amount=amount,
                name=nome,
                tax_id=tax_id,
                due=due,
                expiration=60 * 60 * 24 * 2,
                fine=2.0,
                interest=1.0,
                tags=["desafio-tech"]
            )
        )

    return invoices

inicio = time.time()
fim = inicio + 60 * 60 * 24

while time.time() < fim:
    print(f"[{datetime.now()}] Generating invoices...")
    invoices = gerar_invoices()
    created = starkbank.invoice.create(invoices)

    for invoice in created:
        print("Invoice created:")
        print(invoice)

    print("Waiting 3h for the next execution...\n")
    time.sleep(3 * 60 * 60)
