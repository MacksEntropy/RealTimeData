from faker import Faker
import random

#Module for generating dummy data for testing

fake = Faker()

def possible_error():
    if random.randint(0,10) >= 7:
        return -1
    else:
        return 1

def fake_transaction():
    return {
        "Name":fake.name(),
        "Email":fake.email(),
        "Price":round(random.uniform(0.0,100.0),2),
        "Quantity":random.randint(0,10),
        "Possible_error":possible_error()
    }

if __name__ == "__main__":
    print(fake_transaction())