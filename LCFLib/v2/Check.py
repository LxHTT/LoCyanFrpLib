from requests import Response
from LCFLib.NetworkController import get, APIV2BASEURL

def checkToken(token: str) -> Response:
    """
    Check token.\n

    :param token: The token.\n
    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/check/token?token={token}"
    )