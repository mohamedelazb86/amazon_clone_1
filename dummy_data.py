import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
import random
from faker import Faker
from product.models import Product,Brand, Review
from django.contrib.auth.models import User


def seed_brand(n):
    fake=Faker()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'image_brand/{images[random.randint(0,9)]}'
        )
def seed_product(n):
    fake=Faker()
    brands=Brand.objects.all()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    flag_type=['New','Sale','Feature']
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            price=round(random.uniform(5.55,99.99),2),
            sku=random.randint(100,10000000),
            subtitle=fake.text(max_nb_chars=4000),
            descriptions=fake.text(max_nb_chars=40000),
            brand=brands[random.randint(0,len(brands)-1)],
            image=f'photo_product/{images[random.randint(0,9)]}',
            flag=flag_type[random.randint(0,2)],
            quantity=round(random.uniform(1,2500),2),

        )

def seed_review(n):
    fake=Faker()
    users=User.objects.all()
    products=Product.objects.all()
    for _ in range(n):
        Review.objects.create(
            user=users[random.randint(0,len(users)-1)],
            product=products[random.randint(0,len(products)-1)],
            review=fake.text(max_nb_chars=100),
            rate=random.randint(1,6),

        )

# seed_brand(150)
# seed_product(1000)
seed_review(150)

