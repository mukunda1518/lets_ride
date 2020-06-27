from django_swagger_utils.utils.test import CustomAPITestCase


class CustomTestUtils(CustomAPITestCase):

    def setupUser(self, username, password):
        super(CustomTestUtils, self).setupUser(username=username, password=password)