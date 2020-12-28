import random
import string
import datetime
import os

def get_random_string(length):
  letters = string.ascii_lowercase
  return ''.join(random.choice(letters) for i in range(length))

def get_file_name(base, instance, filename):
  now = datetime.datetime.now()
  path = base+"/{year}-{month}-{day}-{microsecond}-{userid}-{key}-{filename}".format(
    year = now.year,
    month = now.month,
    day = now.day,
    microsecond = now.microsecond,
    userid = instance.usuario.id,
    key = get_random_string(16),
    filename = filename
  )

  return path

