############################################################

from os import environ

############################################################

import slapi

############################################################

def test_login():

    print("logging in")

    lila2 = slapi.login("lishadowapps", environ["LICHPASS"])

    assert "sessionId" in lila2

    print("passed")

############################################################