from unittest import TestCase

from cocoa.model import ModelService, User


class TestModelService(TestCase):
    def test_add_meeting(self):
        self.fail()

    def test_delete_meeting(self):
        self.fail()

    def test_get_meetings(self):
        self.fail()

    def test_add_user(self):
        uid = 12334
        username = 'User'
        description = "I love pyhon"
        model = ModelService()

        user = User(UID=uid, Username=username, Description=description)
        model.add_user(uid=uid, username=username, description=description)

        self.assertEqual(model.read_user(uid=uid), user)

    def test_read_user(self):
        self.fail()

    def test_update_user(self):
        model = ModelService()
        user = User(UID=123, Username='testUpdateUser', Description='Testing update functionality')
        model.add_user(UID=123, Username='testUpdateUser', Description='Testing update functionality')
        updatedUser = User(UID=123, Username='testUpdateUser', Description='Updated user 123')
        model.update_user(123, 'Updated user 123')
        self.assertEqual(model.read_user(123), updatedUser)

    def test_delete_user(self):
        model = ModelService()
        user = User(UID=123, Username='testUpdateUser', Description='Testing update functionality')
        model.add_user(UID=123, Username='testUpdateUser', Description='Testing update functionality')

        model.delete_user(123)
        self.assertEqual(model.read_user(123), 0)
        

    def test_add_schedule(self):
        self.fail()

    def test_get_user_schedules(self):
        self.fail()

    def test_read_schedule(self):
        self.fail()

    def test_update_schedule(self):
        self.fail()

    def test_delete_schedule(self):
        self.fail()

    def test_find_meetings(self):
        self.fail()
