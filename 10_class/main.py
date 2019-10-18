# coding: UTF-8

from user import User

user1 = User("SampleUser1")

user1.hello()

"""
import user

user1 = user.User("SampleUser1")

user1.hello()

でも同じ意味になり、同じ動作になる！
"""

print("----------")

from super_user import SuperUser

user2 = SuperUser("SampleUser2", 20)

user2.hello()