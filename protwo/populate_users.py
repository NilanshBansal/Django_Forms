import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')

import django
django.setup()

## FAKE POP SCRIPT

import random
from users.models import User

from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        user = User()
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()

        user = User.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)[0]

        user.save()






if __name__ == '__main__':
    print("populating script !")
    populate(20)
    print("populating complete !")