from pydantic import BaseModel
from typing import Union


class Host(BaseModel):
    """
    Result model for a single SNMP host.
    """
    address: str
    name: Union[str, None] = None
    ssid: Union[str, None] = None
    rss: Union[int, None] = None
    device_id: Union[str, None] = None

    error: Union[str, None] = None
