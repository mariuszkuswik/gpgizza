# gpgizza
test


# fbchat 

- [Dokumentacja fbchat](https://fbchat.readthedocs.io/en/stable/examples.html)


```python
# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

client = Client("<email>", "<password>")

print("Own id: {}".format(client.uid))

client.send(Message(text="Hi me!"), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()
```


- [Dokumentacja facebook bot?](https://github.com/hartleybrody/fb-messenger-bot)