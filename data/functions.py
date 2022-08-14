async def check_passwd(passwd: str):
    passwd = passwd.strip()
    if len(passwd) >= 8:
        if " " not in passwd:
            return True
    return False
