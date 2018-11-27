#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.facebook import Facebook


username = ''
password = ''

#GermanKRAUTversion
greetings = [
            "Alles, alles Gute :) und einen wunderschönen Tag!",
            "Alles Gute zum Geburtstag :) !!!",
            "Happy Birthday :) !!!",
            ]

#here you could randomly import your greetings
#greetings = [
#            "happy birthday",
#            "Alles Gute zum Geburtstag",
#            "feliz cumpleaños",
#            ]


fb = Facebook()
fb.login(username, password)
fb.wishes(greetings)
