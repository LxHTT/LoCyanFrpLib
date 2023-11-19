from requests import Response
from LCFLib.NetworkController import get, APIV2BASEURL

def checkToken() -> Response:
    """
    Check token.\n

    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/status/nezha"
    )