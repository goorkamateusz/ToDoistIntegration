
def read_token(filename: str) -> str:
    try:
        token_config_file = open(filename)
        return token_config_file.read()
    except:
        raise Exception(f"No token config file. Create file `{filename}` with API token")
