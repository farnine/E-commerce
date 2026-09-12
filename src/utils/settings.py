from pydantic_settings import BaseSettings,SettingsConfigDict

class Setting(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env", extra="ignore")

    DB_CONNECTION:str
    SECRET_KEY:str
    ALGORITHM:str
    TOKEN_EXPIRY_TIME:int


settings=Setting()