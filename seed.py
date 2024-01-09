from faker import Faker
from models import session, Admin


faker = Faker()
adm = []

session.delete()

for i in range(50):
    admi = Admin(
        username = faker.name(),
        full_name = faker.name(),
        email = faker.name(),
        hashed_password = faker.word(),
        disabled = False
    )
    adm.append(admi)
    session.bulk_save_objects(adm)
    session.commit()