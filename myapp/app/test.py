#!/usr/bin/python3

from weboob.core import Weboob
from weboob.capabilities.bank import CapBank

from weboob.azetr import aretr

w = Weboob()
w.load_backends(CapBank)

print("ok")