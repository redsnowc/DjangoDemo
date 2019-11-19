from faker import Faker
from .models import User, UserProfile, Group, Diary
from random import randint, choice
import time

f = Faker()
f_z = Faker("zh-cn")


def fake_user(count):
    for i in range(0, count):
        user = User()
        user.username = f.name()
        user.age = 19
        user.phone = f_z.phone_number()
        user.email = f.email()
        user.info = f.sentence()
        user.save()


def fake_user_profile():
    for i in User.objects.all():
        up = UserProfile()
        up.birthday = f.date()
        up.user = i
        up.save()


def fake_diary(count):
    for i in User.objects.all():
        for j in range(0, count):
            diary = Diary()
            diary.content = f.sentence(40)
            diary.create_time = time.time()
            diary.user = i
            diary.save()


def fake_group(count):
    for i in range(0, count):
        group = Group()
        group.name = f.words(1)[0]
        group.create_time = time.time()
        group.update_time = time.time()
        group.save()
        for j in range(0, randint(1, 7)):
            group.user.add(choice(User.objects.all()))

