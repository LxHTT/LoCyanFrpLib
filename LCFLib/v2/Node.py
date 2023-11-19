from requests import Response
from LCFLib.NetworkController import get, APIV2BASEURL


def getNodeList() -> Response:
    """
    Gets the node list.\n
    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/nodes/list",
    )
