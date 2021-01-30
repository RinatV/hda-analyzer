# -*- coding: utf-8 -*-
import pytest
from mock import Mock
from hda_proc import ProcNode


def test_add_device():
    codec = Mock()
    codec.proc_nids = {}
    nid = 8
    wcaps = 1053
    node = ProcNode(codec, nid, wcaps)
    line = '  Device: name="VT1802 Analog", type="Audio", device=0'
    assert line.startswith('  Device: ')
    node.add_device(line[10:])
    # Второй девайс вызывает ошибку
    line = '  Device: name="VT1802 Alt Analog", type="Audio", device=2'
    assert line.startswith('  Device: ')
    # with pytest.raises(ValueError):
    node.add_device(line[10:])

    assert node.device.name == 'VT1802 Alt Analog'
    assert node.devices[0].name == 'VT1802 Analog'
    assert node.devices[1].name == 'VT1802 Alt Analog'

