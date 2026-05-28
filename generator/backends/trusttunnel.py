import subprocess


def setup_trusttunnel(credentials):
    result = []

    for username, password in credentials.items():
        result.append("[[client]]")
        result.append(f'username = "{username}"')
        result.append(f'password = "{password}"')
        result.append("")

    with open("/opt/trusttunnel/credentials.toml", "w") as f:
        f.write("\n".join(result))

    subprocess.run(["systemctl", "restart", "trusttunnel"])
