import unittest

from . import business_logic
from . import fact_objects
from . import objects


class MyTestCase(unittest.TestCase):

    def test_send_mail(self):
        account = fact_objects.AccountFactory()
        email = business_logic.prepare_email(account, subject='Foo', text='Bar')

        self.assertEqual(email.to, account.email)