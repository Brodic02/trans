from starlette.config import Config


config = Config(".env")

# TOKEN: str = config("TOKEN")

key: str = config("KEY")
endpoint: str = config("ENDPOINT")
location: str = config("LOCATION")
