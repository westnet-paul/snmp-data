from pydantic import ValidationError
import pytest
from snmpdata import Host


def test_emptyhost():
    with pytest.raises(ValidationError):
        host = Host()


def test_host():
    address = "1.2.3.4"
    name = "test name"
    ssid = "test ssid"
    rss = -99
    device_id = "test device id"
    host = Host(address=address, name=name, ssid=ssid, rss=rss, device_id=device_id)
    assert host.address == address
    assert host.name == name
    assert host.ssid == ssid
    assert host.rss == rss
    assert host.device_id == device_id
    assert host.error is None


def test_error():
    address = "1.2.3.4"
    error = "test error"
    host = Host(address=address,error=error)
    assert host.address == address
    assert host.error == error
    assert host.name is None
    assert host.ssid is None
    assert host.rss is None
    assert host.device_id is None

