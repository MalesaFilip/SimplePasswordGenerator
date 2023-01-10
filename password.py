import random

letters = "abcdefghijklmnoprstuwxyz"
big_letters = "ABCDEFGHIJKLMNOPRSTUWXYZ"
numbers = "1234567890"
characters = "!@#$%^&*(){}><"

summary = letters + big_letters + numbers + characters
length = 10
password = "".join(random.sample(summary, length))
