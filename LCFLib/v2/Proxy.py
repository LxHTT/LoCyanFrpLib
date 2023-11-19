from typing import Optional
from requests import Response
from LCFLib.NetworkController import get, post, delete, APIV2BASEURL


def newProxy(
    username: str,
    name: str,
    key: str,
    ip: str,
    type: str,
    lp: str,
    rp: str,
    ue: str,
    uz: str,
    id: str,
    token: str,
    url: Optional[str] = None,
    sk: Optional[str] = None,
) -> Response:
    """
    Creates a new proxy.\n

    :param username: The username.\n
    :param name: The proxy name.\n
    :param key: The frp access key.\n
    :param ip: The local ip.\n
    :param type: The proxy type.\n
    :param lp: The local port.\n
    :param rp: The remote port.\n
    :param ue: Use encryption.\n
    :param uz: Use zip.\n
    :param id: The node id.\n
    :param token: The login token.\n
    :param url\n
    :param sk\n
    :return: Response
    """
    body = {
        "username": username,
        "name": name,
        "key": key,
        "ip": ip,
        "type": type,
        "lp": lp,
        "rp": rp,
        "ue": ue,
        "uz": uz,
        "id": id,
        "token": token,
        "url": url,
        "sk": sk,
    }
    if url is not None:
        body["url"] = url
    if sk is not None:
        body["sk"] = sk
    return post(
        url=f"{APIV2BASEURL}/api/v2/proxies/add",
        body=body,
    )


def updateProxy(
    name: str,
    key: str,
    ip: str,
    type: str,
    lp: str,
    rp: str,
    ue: str,
    uz: str,
    id: str,
    url: Optional[str] = None,
    sk: Optional[str] = None,
) -> Response:
    """
    Update a proxy.\n

    :param name: The proxy name.\n
    :param key: The frp access key.\n
    :param ip: The local ip.\n
    :param type: The proxy type.\n
    :param lp: The local port.\n
    :param rp: The remote port.\n
    :param ue: Use encryption.\n
    :param uz: Use zip.\n
    :param id: The node id.\n
    :param url\n
    :param sk\n
    :return: Response
    """
    body = {
        "name": name,
        "key": key,
        "ip": ip,
        "type": type,
        "lp": lp,
        "rp": rp,
        "ue": ue,
        "uz": uz,
        "id": id,
    }
    if url is not None:
        body["url"] = url
    if sk is not None:
        body["sk"] = sk
    return post(url=f"{APIV2BASEURL}/api/v2/proxies/update", body=body)


def deleteProxy(
    username: str,
    token: str,
    id: str,
) -> Response:
    """
    Deletes a proxy.\n

    :param username: The username.\n
    :param token: The login token.\n
    :param id: The node id.\n
    :return: Response
    """
    return delete(
        url=f"{APIV2BASEURL}/api/v2/proxies/delete?{username}&{token}&{id}",
    )


def getProxyConfig(id: str) -> Response:
    """
    Gets the proxy config.\n

    :param id: The node id.\n
    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/config/get?id={id}",
    )


def getProxiesList(username: str) -> Response:
    """
    Gets the proxy list.\n

    :param username: The username.\n
    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/proxies/getlist?username={username}",
    )
