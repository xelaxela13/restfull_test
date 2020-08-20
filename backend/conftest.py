import factory
import pytest
from string import ascii_letters, digits
from django.contrib.auth import get_user_model
from django.core.management import call_command
from faker import Faker
from faker.providers import BaseProvider
from random import choice
from pytest_factoryboy import register

fake = Faker()


@pytest.mark.django_db(transaction=True)
@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'fixture.json')


class MyProvider(BaseProvider):

    @property
    def password(self):
        return ''.join({choice(ascii_letters + digits) for _ in range(20)})


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope='session')
def faker():
    global fake
    fake.add_provider(MyProvider)
    yield fake


@register
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('email',)

    first_name = factory.Sequence(lambda n: fake.name())
    email = factory.Sequence(lambda n: "email_%d@mail.com" % n)

    @factory.post_generation
    def set_password(self, created, *args, **kwargs):
        if created:
            self.set_password('1234567890')
