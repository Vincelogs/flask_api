#!/usr/bin/env python3

import requests as req

resp = req.request(method='GET', url="http://www.webcode.me")
print(resp.text)
