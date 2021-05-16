from unittest import TestCase

from cocoa.model import ModelService, User, Meeting, datetime, Schedule, timedelta
from sqlalchemy.orm import sessionmaker


class TestModelService(TestCase):
    # def tearDown(self):
    #     model = ModelService()

    def test_add_meeting(self):
        model = ModelService()
        user1_uid = 11111111111
        user1_username = 'User 1'
        user1_description = "I love python"
        user2_uid = 22222222222
        user2_username = 'User 2'
        user2_description = "I love python too"

        model.add_user(uid=user1_uid, username=user1_username, description=user1_description)
        model.add_user(uid=user2_uid, username=user2_username, description=user2_description)

        start = "15/06 12:00"
        end = "15/06 13:00"

        formated_start = datetime.strptime(start, "%d/%m %H:%M")
        formated_end = datetime.strptime(end, "%d/%m %H:%M")

        # start = datetime.strptime(start.content, '%d/%m %H:%M')

        meeting = Meeting(UID1=user1_uid, UID2=user2_uid, StartTime=formated_start, EndTime=formated_end)
        model.add_meeting(meeting.UID1, meeting.UID2, meeting.StartTime, meeting.EndTime)
        result = []
        result.append({
            'user1': user1_uid,
            'user2': user2_uid,
            'start': meeting.StartTime,
            'end': meeting.EndTime,
        })
        self.assertEqual(model.get_meetings(uid=user1_uid)[0], result[0])

        # self.assertEqual(model.read_user(uid=user1_uid).Description, user2_description)
        model.delete_user(uid=user1_uid)
        model.delete_user(uid=user2_uid)

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
        uid = 53452
        username = 'User'
        description = "I love pyhon"
        model = ModelService()

        user = User(UID=uid, Username=username, Description=description)
        model.add_user(uid=uid, username=username, description=description)

        self.assertEqual(model.read_user(uid=uid).UID, user.UID)
        model.delete_user(uid=uid)


    def test_read_user(self):
        uid = 11113
        username = 'User'
        description = "I love python"
        model = ModelService()

        user = User(UID=uid, Username=username, Description=description)
        model.add_user(uid=uid, username=username, description=description)

        self.assertEqual(model.read_user(uid=uid).UID, user.UID)
        model.delete_user(uid=uid)

    def test_update_user(self):
        model = ModelService()
        user1_uid = 111111
        user1_username = 'User 1'
        user1_description = "I love python"
        user2_uid = 222222
        user2_username = 'User 2'
        user2_description = "I love python too"

        model.add_user(uid=user1_uid, username=user1_username, description=user1_description)
        model.update_user(uid=user1_uid, description=user2_description)
        self.assertEqual(model.read_user(uid=user1_uid).Description, user2_description)
        model.delete_user(uid=user1_uid)

    def test_delete_user(self):
        model = ModelService()
        user1_uid = 111111
        user1_username = 'User 1'
        user1_description = "I love python"
        model.add_user(uid=user1_uid, username=user1_username, description=user1_description)
        model.delete_user(uid=user1_uid)
        self.assertEqual(model.read_user(uid=user1_uid), None)


    def test_add_schedule(self):
        model = ModelService()
        start = "15/06 12:00"
        end = "15/06 13:00"
        formated_start = datetime.strptime(start, "%d/%m %H:%M")
        formated_end = datetime.strptime(end, "%d/%m %H:%M")

        user1_uid = 111111112
        user1_username = 'User 1'
        user1_description = "I love python"

        schedule = Schedule(UID=user1_uid, StartTime=formated_start, EndTime=formated_end)
        model.add_schedule(user1_uid, formated_start, formated_end)

        self.assertEqual(model.read_schedule(uid=user1_uid, start=formated_start, end=formated_end).UID, schedule.UID)
        model.delete_schedule(uid=user1_uid, start=formated_start, end=formated_end)

    def test_get_user_schedules(self):
        model = ModelService()
        start = "15/06 12:00"
        end = "15/06 13:00"
        formated_start = datetime.strptime(start, "%d/%m %H:%M")
        formated_end = datetime.strptime(end, "%d/%m %H:%M")

        user1_uid = 11111111211
        user1_username = 'User 1'
        user1_description = "I love python"

        schedule = Schedule(UID=user1_uid, StartTime=formated_start, EndTime=formated_end)
        model.add_schedule(user1_uid, formated_start, formated_end)

        self.assertEqual(model.get_user_schedules(uid=user1_uid)[0].UID, schedule.UID)
        model.delete_schedule(uid=user1_uid, start=formated_start, end=formated_end)

    def test_read_schedule(self):
        model = ModelService()
        start = "15/06 12:00"
        end = "15/06 13:00"
        formated_start = datetime.strptime(start, "%d/%m %H:%M")
        formated_end = datetime.strptime(end, "%d/%m %H:%M")

        user1_uid = 1111111121112
        user1_username = 'User 1'
        user1_description = "I love python"

        schedule = Schedule(UID=user1_uid, StartTime=formated_start, EndTime=formated_end)
        model.add_schedule(user1_uid, formated_start, formated_end)

        self.assertEqual(model.read_schedule(uid=user1_uid, start=formated_start, end=formated_end).UID, schedule.UID)
        model.delete_schedule(uid=user1_uid, start=formated_start, end=formated_end)

    def test_update_schedule(self):
        model = ModelService()
        start = "15/06 12:00"
        end = "15/06 13:00"
        formated_start = datetime.strptime(start, "%d/%m %H:%M")
        formated_end = datetime.strptime(end, "%d/%m %H:%M")

        user1_uid = 111111112111221
        user1_username = 'User 1'
        user1_description = "I love python"

        model.add_schedule(user1_uid, formated_start, formated_end)

        updated_start = "15/06 15:00"
        updated_end = "15/06 19:00"
        formated_updated_start = datetime.strptime(updated_start, "%d/%m %H:%M")
        formated_updated_end = datetime.strptime(updated_end, "%d/%m %H:%M")

        new_schedule = Schedule(UID=user1_uid, StartTime=formated_updated_start, EndTime=formated_updated_end)
        model.update_schedule(user1_uid, formated_start, formated_end, formated_updated_start, formated_updated_end)
        self.assertEqual(model.get_user_schedules(uid=user1_uid)[0].UID, new_schedule.UID)
        model.delete_schedule(uid=user1_uid, start=formated_updated_start, end=formated_updated_end)

    def test_delete_schedule(self):
        model = ModelService()
        start = "15/06 12:00"
        end = "15/06 13:00"
        formated_start = datetime.strptime(start, "%d/%m %H:%M")
        formated_end = datetime.strptime(end, "%d/%m %H:%M")

        user1_uid = 111111111
        user1_username = 'User 1'
        user1_description = "I love python"

        model.add_schedule(user1_uid, formated_start, formated_end)

        self.assertEqual(model.delete_schedule(uid=user1_uid, start=formated_start, end=formated_end), None)

    def test_find_meetings(self):
        model = ModelService()
        user1_uid = 9999
        start = "15/06 12:00"
        end = "15/06 13:00"
        formated_start = datetime.strptime(start, "%d/%m %H:%M")
        formated_end = datetime.strptime(end, "%d/%m %H:%M")

        length = timedelta(hours=1)

        model.add_schedule(user1_uid, formated_start, formated_end)

        result = []
        result.append({
            'user': user1_uid,
            'start': formated_start,
            'end': formated_end
        })
        self.assertEqual(model.find_meetings(start=formated_start, end=formated_end, meeting_length=length)[0], result[0])
        model.delete_schedule(uid=user1_uid, start=formated_start, end=formated_end)