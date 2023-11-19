from requests import Response
from LCFLib.NetworkController import get, APIV2BASEURL

def getQQLoginURL(redirect_url: str) -> Response:
    """
    Gets the QQ login URL.\n

    :param redirect_url: The redirect URL.\n
    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/oauth/qq/login?redirect_url={redirect_url}"
    )