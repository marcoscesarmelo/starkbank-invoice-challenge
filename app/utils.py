import random

names = ["Customer 6", "Customer 7", "Customer 8", "Customer 9", "Customer 10"]

def generate_random_name_cpf():
    name = random.choice(names)
    cpf = f"{random.randint(100,999)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(10,99)}"
    return name, cpf