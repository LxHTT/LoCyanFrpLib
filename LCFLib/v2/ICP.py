from requests import Response
from LCFLib.NetworkController import get, delete, APIV2BASEURL


def checkICP(domain: str, token: str, username: str) -> Response:
    """
    Hand in the ICP domain.\n

    :param domain: The domain.\n
    :param token: The token.\n
    :param username: The username.\n
    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/icp/check",
        body={"domain": domain, "token": token, "username": username},
    )


def getICPList(token: str, username: str):
    """
    Gets the ICP list.\n

    :param token: The token.\n
    :param username: The username.\n
    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/icp/list",
        body={"token": token, "username": username},
    )


def removeICP(id: str, token: str, username: str) -> Response:
    """
    Removes the ICP domain.\n

    :param id: The domain.\n
    :param token: The token.\n
    :param username: The username.\n
    :return: Response
    """
    return delete(
        url=f"{APIV2BASEURL}/api/v2/icp/remove",
        body={"id": id, "token": token, "username": username},
    )
