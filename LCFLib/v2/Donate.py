from requests import Response
from LCFLib.NetworkController import post, APIV2BASEURL


def createDonate(name: str,
                 money: str,
                 redirect_url: str,
                 notify_url: str,
                 username: str) -> Response:
    """
    Creates a new donate.\n

    :param name: The name of the donate.\n
    :param money: The money of the donate.\n
    :param redirect_url: The redirect url of the donate.\n
    :param notify_url: The notify url of the donate.\n
    :param username: The username of the donate.\n
    :return: Response
    """
    return post(
        url=f"{APIV2BASEURL}/api/v2/donate/create",
        body={
            "name": name,
            "money": money,
            "redirect_url": redirect_url,
            "notify_url": notify_url,
            "username": username
        }
    )
