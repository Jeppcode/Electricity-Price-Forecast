from pathlib import Path
import os
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class ElectricitySettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    PROJECT_DIR: Path = Path(__file__).resolve().parent.parent

    # Hopsworks
    HOPSWORKS_API_KEY: SecretStr | None = None
    HOPSWORKS_PROJECT: str | None = None

    # Elpris API
    ELPRICE_BASE_URL: str = "https://www.elprisetjustnu.se/api/v1/prices"
    ELPRICE_AREA: str = "SE3"  # default Stockholm

    def model_post_init(self, __context):
        """Körs efter init. Sätter env vars så hopsworks.login() funkar."""
        print("ElectricitySettings initialized")

        # Sätt env vars om de inte redan finns
        if os.getenv("HOPSWORKS_API_KEY") is None and self.HOPSWORKS_API_KEY is not None:
            os.environ["HOPSWORKS_API_KEY"] = self.HOPSWORKS_API_KEY.get_secret_value()

        if os.getenv("HOPSWORKS_PROJECT") is None and self.HOPSWORKS_PROJECT is not None:
            os.environ["HOPSWORKS_PROJECT"] = self.HOPSWORKS_PROJECT

        # Kolla kritiska
        missing = []
        if not (self.HOPSWORKS_API_KEY or os.getenv("HOPSWORKS_API_KEY")):
            missing.append("HOPSWORKS_API_KEY")
        if not (self.HOPSWORKS_PROJECT or os.getenv("HOPSWORKS_PROJECT")):
            missing.append("HOPSWORKS_PROJECT")

        if missing:
            raise ValueError(
                "Följande inställningar saknas i .env eller environment:\n  "
                + "\n  ".join(missing)
            )
