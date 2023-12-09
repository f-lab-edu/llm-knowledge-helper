import dataclasses
from zoneinfo import ZoneInfo


@dataclasses.dataclass(frozen=True)
class Config:
    timezone: str = "Asia/Tokyo"

    @property
    def zone_info(self) -> ZoneInfo:
        return ZoneInfo(self.timezone)


config = Config()
