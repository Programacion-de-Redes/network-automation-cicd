import yaml

def load_config():
    with open("configs/network.yml") as file:
        return yaml.safe_load(file)

def validate_network():
    config = load_config()

    devices = config["network"]["devices"]

    for device in devices:
        assert device["hostname"]
        assert device["role"]
        assert device["expected_status"] == "reachable"

    print("Validacion de configuracion exitosa")

if __name__ == "__main__":
    validate_network()
