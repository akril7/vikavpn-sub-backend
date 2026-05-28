from config import TRUSTTUNNEL_CONFIG


def generate_trusttunnel(creds):
    result = []

    for username, password in creds:
        result.append("[[client]]")
        result.append(f'username = "{username}"')
        result.append(f'password = "{password}"')
        result.append("")

    with open(TRUSTTUNNEL_CONFIG, "w") as f:
        f.write("\n".join(result))
