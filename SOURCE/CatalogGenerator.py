def generate_config():
    with open("IDs.txt", "r") as file:
        ids = [line.strip() for line in file if line.strip()]

    config = {}

    for i, id in enumerate(ids, start=1):
        if id.startswith("EID_"):
            config[f"featured{i}"] = {
                "itemGrants": [f"AthenaDance:{id}"],
                "price": 0
            }
        elif id.startswith("Character_"):
            config[f"featured{i + len(ids)}"] = {
                "itemGrants": [f"AthenaCharacter:{id}"],
                "price": 0
            }
        elif id.startswith("MusicPack_"):
            config[f"featured{i + 2 * len(ids)}"] = {
                "itemGrants": [f"AthenaMusicPack:{id}"],
                "price": 0
            }

    with open("catalog_config.json", "w") as outfile:
        import json
        json.dump(config, outfile, indent=4)

if __name__ == "__main__":
    generate_config()
