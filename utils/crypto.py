import hashlib


def md5(plain: str) -> str:
    return hashlib.md5(plain.encode()).hexdigest()
