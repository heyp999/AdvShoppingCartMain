from faker import Faker

adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_username = 'gordonhe'
adshopcart_password = 'gordon!123'

# fake data generate
fake = Faker(locale='en_CA')
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
city = fake.city()
description = fake.sentence(nb_words=100)
pic_desc = fake.user_name()
phonetic_name = fake.user_name()
list_of_interests = [new_username, new_password, full_name, email, city]
web_page_url = fake.url()
icq_number = fake.pyint(111111, 999999)
institution = fake.lexify(text='????????????????????')
department = fake.lexify(text='???????')
phone = fake.phone_number()
mobile_phone = fake.phone_number()
address = fake.address().replace("\n", " ")
