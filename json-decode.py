# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import json

with open("utf8.json") as fh:
    js = json.loads(fh.read(), "utf-8")
    print(js["hello"])
