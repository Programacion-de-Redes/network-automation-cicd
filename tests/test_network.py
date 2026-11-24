import yaml

def test_network_configuration():
    with open("configs/network.yml") as file:
        config = yaml.safe_load(file)

    assert "network" in config
    assert len(config["network"]["devices"]) > 0

def test_device_hostnames():
    with open("configs/network.yml") as file:
        config = yaml.safe_load(file)

    for device in config["network"]["devices"]:
        assert device["hostname"] != ""
