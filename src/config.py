from dataclasses import dataclass
from zoneinfo import ZoneInfo


@dataclass(frozen=True)
class Config:
    timezone: str = "Asia/Tokyo"

    @property
    def zone_info(self):
        return ZoneInfo(self.timezone)


config = Config()
