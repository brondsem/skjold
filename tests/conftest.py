# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def requirements_txt_with_hashes() -> str:
    return """appdirs==1.4.3 \\
        --hash=sha256:d8b24664561d0d34ddfaec54636d502d7cea6e29c3eaf68f3df6180863e2166e \\
        --hash=sha256:9e5896d1372858f8dd3344faf4e5014d21849c756c8d5701f78f8a103b372d92
    argh==0.26.2 \\
        --hash=sha256:a9b3aaa1904eeb78e32394cd46c6f37ac0fb4af6dc488daa58971bdc7d7fcaf3 \\
        --hash=sha256:e9535b8c84dc9571a48999094fda7f33e63c3f1b74f3e5f3ac0105a58405bb65
    aspy.yaml==1.3.0 \\
        --hash=sha256:463372c043f70160a9ec950c3f1e4c3a82db5fca01d334b6bc89c7164d744bdc \\
        --hash=sha256:e7c742382eff2caed61f87a39d13f99109088e5e93f04d76eb8d4b28aa143f45
    atomicwrites==1.3.0; sys_platform == "win32" \\
        --hash=sha256:03472c30eb2c5d1ba9227e4c2ca66ab8287fbfbbda3888aa93dc2e28fc6811b4 \\
        --hash=sha256:75a9445bac02d8d058d5e1fe689654ba5a6556a1dfd8ce6ec55a0ed79866cfa6
    attrs==19.3.0 \\
        --hash=sha256:08a96c641c3a74e44eb59afb61a24f2cb9f4d7188748e76ba4bb5edfa3cb7d1c \\
        --hash=sha256:f7b7ce16570fe9965acd6d30101a28f62fb4a7f9e926b3bbc9b61f8b04247e72"""


@pytest.fixture()
def cache_dir() -> str:
    return ".skjold_cache"
