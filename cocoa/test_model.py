from unittest import TestCase

from cocoa.model import ModelService, User, Meeting, datetime, Schedule, timedelta


class TestModelService(TestCase):
    def test_add_meeting(self):
        model = ModelService()
        model.add_user(123, 'user 1', 'Testing adding meeting')
        model.add_user(1234, 'user 2', 'Testing adding meeting')
        start = datetime(2021, 6, 15, 12, 0, 0)
        end = datetime(2021, 6, 15, 13, 0, 0)
        meeting = Meeting(123, 1234, start, end)
        model.add_meeting(meeting)
        result = []
        result.append({
            'user1': 123,
            'user2': 1234,
            'start': start,
            'end': end,
        })
        self.assertEqual(model.get_meetings(123), result)

    def test_delete_meeting(self):
        model = ModelService()
        model.add_user(123, 'user 1', 'Testing deleting meeting')
        model.add_user(1234, 'user 2', 'Testing deleting meeting')
        start = datetime(2021, 6, 15, 12, 0, 0)
        end = datetime(2021, 6, 15, 13, 0, 0)
        meeting = Meeting(123, 1234, start, end)
        model.add_meeting(meeting)

        model.delete_meeting(123, 1234)
        result = []
        self.assertEqual(model.get_meetings(123), result)



    def test_get_meetings(self):
        model = ModelService()
        model.add_user(123, 'user 1', 'Testing getting meeting')
        model.add_user(1234, 'user 2', 'Testing getting meeting')
        start = datetime(2021, 6, 15, 12, 0, 0)
        end = datetime(2021, 6, 15, 13, 0, 0)
        meeting = Meeting(123, 1234, start, end)
        model.add_meeting(meeting)

        result = []
        result.append({
            'user1': 123,
            'user2': 1234,
            'start': start,
            'end': end,
        })
        self.assertEqual(model.get_meetings(123), result)


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
        model.add_user(123, 'user 1', 'Testing update functionality')
        updatedUser = User(123, 'user 2', 'Updated user 123')
        model.update_user(123, 'Updated user 123')
        self.assertEqual(model.read_user(123), updatedUser)

    def test_delete_user(self):
        model = ModelService()
        model.add_user(123, 'user 1', 'Testing delete user functionality')
        emptyUser = User()

        model.delete_user(123)
        self.assertEqual(model.read_user(123), emptyUser)

    def test_add_schedule(self):
        model = ModelService()
        start = datetime(2021, 6, 15, 12, 0, 0)
        end = datetime(2021, 6, 15, 13, 0, 0)
        schedule = Schedule(123, start, end)
        model.add_schedule(123, start, end)

        self.assertEqual(model.read_schedule(123, start, end), schedule)

    def test_get_user_schedules(self):
        model = ModelService()
        start = datetime(2021, 6, 15, 12, 0, 0)
        end = datetime(2021, 6, 15, 13, 0, 0)
        schedule = Schedule(123, start, end)
        model.add_schedule(123, start, end)

        self.assertEqual(model.get_user_schedules(123), schedule)

    def test_read_schedule(self):
        model = ModelService()
        start = datetime(2021, 6, 15, 12, 0, 0)
        end = datetime(2021, 6, 15, 13, 0, 0)
        schedule = Schedule(123, start, end)
        model.add_schedule(123, start, end)

        self.assertEqual(model.read_schedule(123, start, end), schedule)

    def test_update_schedule(self):
        model = ModelService()
        start = datetime(2021, 6, 15, 12, 0, 0)
        end = datetime(2021, 6, 15, 13, 0, 0)
        model.add_schedule(123, start, end)

        newStart = datetime(2021, 6, 15, 15, 0, 0)
        newEnd = datetime(2021, 6, 15, 17, 0, 0)
        newSchedule = Schedule(123, newStart, newEnd)
        model.update_schedule(123, start, end, newStart, newEnd)
        self.assertEqual(model.get_user_schedules(123), newSchedule)


    def test_delete_schedule(self):
        model = ModelService()
        start = datetime(2021, 6, 15, 12, 0, 0)
        end = datetime(2021, 6, 15, 13, 0, 0)
        model.add_schedule(123, start, end)

        emptySchedule = Schedule()
        self.assertEqual(model.delete_schedule(123, start, end), emptySchedule)

    def test_find_meetings(self):
        model = ModelService()
        start = datetime(2021, 6, 15, 12, 0, 0)
        end = datetime(2021, 6, 15, 13, 0, 0)
        model.add_schedule(123, start, end)

        length = timedelta(0, 0, 0, 0, 0, 1, 0)
        result = []
        result.append({
            'user': 123,
            'start': start,
            'end': end
        })
        self.assertEqual(model.find_meetings(start, end, length), result)