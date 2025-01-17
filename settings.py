from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    title: str = "SMPLAuth API"
    description: str = "A simple auth API."
    version: str = "0.0.1"
    contact_name: str = "Steve Xero"
    contact_url: str = "https://stevexero.com"
    contact_email: str = "hello@stevexero.com"
    license_name: str = "TBD"
    license_url: str = "https://smplauth.com/license"
    redirect_url: str = "/redoc"

    class Config:
        env_file = ".env"  # Specify the environment file to load variables from (will use later)

settings = Settings()
