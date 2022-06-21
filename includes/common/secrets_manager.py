import os


def get_environment_secret(name: str) -> str:
    if not name or not os.environ.get(name):
        return ""
    with open(os.environ.get(name), "r") as secret:
        return secret.read()
