#!/usr/bin/python3


# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

client = Client("login", "haslo")

print("Own id: {}".format(client.uid))

client.send(Message(text="Hi me!"), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()