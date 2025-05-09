import starkbank

def make_transfer(amount):
    transfer = starkbank.Transfer(
        amount=amount,
        bank_code="20018183",
        branch_code="0001",
        account_number="6341320293482496",
        name="Stark Bank S.A.",
        tax_id="20.018.183/0001-80",
        account_type="payment"
    )
    starkbank.transfer.create([transfer])
    print(f"✅ Transfer Done: R$ {amount / 100:.2f}")
