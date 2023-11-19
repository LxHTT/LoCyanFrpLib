from requests import Response
from LCFLib.NetworkController import post, get, APIV2BASEURL


def login(username: str, password: str, customUA: str = "Py-LoCyanFrpLib") -> Response:
    """
    Logs in a user with the provided username and password.\n

    :param username: The username of the user.\n
    :param password: The password of the user.\n
    :param customUA: The custom User-Agent to use (default: "Py-LoCyanFrpLib").\n
    :return: Response
    """
    return post(
        url=f"{APIV2BASEURL}/api/v2/users/login",
        body={"username": username, "password": password},
        headers={"User-Agent": customUA},
    )


def register(
        username: str,
        password: str,
        confirm_password: str,
        email: str,
        verify: str,
        qq: str,
) -> Response:
    """
    Registers a user with the provided information.\n

    :param username: The username of the user.\n
    :param password: The password of the user.\n
    :param confirm_password: The password confirmation of the user.\n
    :param email: The email of the user.\n
    :param verify: The verification code of the user.\n
    :param qq: The QQ number of the user.\n
    :return: Response\n
    """
    return post(
        url=f"{APIV2BASEURL}/api/v2/users/register",
        body={
            "username": username,
            "password": password,
            "confirm_password": confirm_password,
            "email": email,
            "verify": verify,
            "qq": qq,
        },
    )


def sendRegisterMail(email: str) -> Response:
    """
    Sends a verification email to the user.\n

    :param email: The email of the user.\n
    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/users/send?email={email}",
    )


def getUserInfo(username: str) -> Response:
    """
    Gets the user information of the user.\n

    :param username: The username of the user.\n
    :return: Response
    """
    return get(
        url=f"{APIV2BASEURL}/api/v2/users/info?username={username}",
    )
