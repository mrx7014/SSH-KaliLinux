# SSH Kali Linux on Segfault

A practical guide for connecting to a temporary Kali Linux environment provided through [THC Segfault][1]. Use it for authorized security testing, learning, development, and other legitimate workloads.

> **Important:** This repository does not create or host the server. It documents a connection workflow for a third-party service. Availability, limits, credentials, images, and server specifications may change. Always follow the provider's current documentation and terms of use.

## Contents

- [What this repository provides](#what-this-repository-provides)
- [Requirements](#requirements)
- [Connect from a client](#connect-from-a-client)
- [Reconnect to your assigned server](#reconnect-to-your-assigned-server)
- [Optional VNC access](#optional-vnc-access)
- [The `247.py` helper](#the-247py-helper)
- [Security and acceptable use](#security-and-acceptable-use)
- [Troubleshooting](#troubleshooting)
- [Project files](#project-files)
- [Contributing](#contributing)
- [Credits](#credits)

## What this repository provides

This repository contains:

- Platform-neutral SSH connection instructions.
- Optional instructions for forwarding a VNC display over SSH.
- `247.py`, a small terminal timer that can be used as a visible session indicator.
- Screenshots illustrating the original workflow.

The repository does **not** include a server image, credentials, private keys, or a method for bypassing provider limits.

## Requirements

You need the following:

| Client | Required software |
| --- | --- |
| Linux | OpenSSH client |
| Termux | Termux and the OpenSSH package |
| Windows | OpenSSH or [PuTTY][2] |
| iOS | [iSH][3] or another SSH client |
| VNC client | A compatible VNC viewer, only if you enable VNC access |

### Install an SSH client

#### Linux

```bash
sudo apt update
sudo apt install openssh-client
```

#### Termux

```bash
pkg update
pkg upgrade
pkg install openssh
```

Install Termux from the [official Termux releases page][4].

#### Windows

Windows includes OpenSSH on current versions. You can also use [PuTTY][2] and follow the provider's [PuTTY guide][5].

## Connect from a client

Start with the connection details supplied by the provider. Do not copy credentials from old screenshots or from third-party posts.

```bash
ssh root@segfault.net
```

The service may display a **secret** and a server-specific SSH command after the initial connection. Treat that command as a credential:

1. Copy the complete command to a secure location.
2. Do not publish the secret in an issue, screenshot, commit, or chat.
3. Use the server-specific command for future connections.
4. Do not assume that the example hostname, username, password, or secret in an old guide is still valid.

A server-specific command generally has this structure:

```bash
ssh -o 'SetEnv SECRET=YOUR_SECRET' root@YOUR_ASSIGNED_HOST
```

Replace the placeholders with the values shown by the service. The placeholder values above are intentionally not real credentials.

For browser-based access, use the provider's current web shell if it is available. See the [official Segfault documentation][1] for the current endpoint and access requirements.

## Reconnect to your assigned server

Your work may be associated with the secret and hostname issued during the initial session. Save the complete SSH command locally, for example in `~/.ssh/config`, rather than placing secrets in a public script:

```sshconfig
Host my-segfault-server
    HostName YOUR_ASSIGNED_HOST
    User root
    SetEnv SECRET=YOUR_SECRET
```

Then connect with:

```bash
ssh my-segfault-server
```

Protect the configuration file:

```bash
chmod 600 ~/.ssh/config
```

> Never commit a real secret, private key, access token, or provider password to this repository.

## Optional VNC access

VNC is optional. SSH port forwarding keeps the VNC port bound to your local machine instead of exposing it publicly.

### 1. Create the SSH tunnel

Append the local port-forwarding option to your server-specific SSH command:

```bash
ssh -L 5900:127.0.0.1:5900 \
    -o 'SetEnv SECRET=YOUR_SECRET' \
    root@YOUR_ASSIGNED_HOST
```

Keep this SSH session open.

### 2. Start the desktop/VNC service

In the SSH session, run the command supported by the server image:

```bash
startxvnc
```

Use the display and password shown by the server. Do not reuse a password from an old screenshot or publish it.

### 3. Connect with a VNC viewer

Open a VNC client and connect to:

```text
127.0.0.1:5900
```

Possible clients include [RealVNC Viewer][6] and [Remmina][7]. Use the port and display number reported by the server if they differ from the example above.

## The `247.py` helper

`247.py` prints an elapsed-time counter in the terminal:

```bash
python3 247.py
```

It is a lightweight session indicator. **It does not prevent shutdown, renew a lease, reconnect SSH, or guarantee 24/7 availability.** Do not use it to evade service limits or provider policies.

To run it from a fresh checkout:

```bash
git clone https://github.com/mrx7014/SSH-KaliLinux.git
cd SSH-KaliLinux
python3 247.py
```

For long-running sessions, use only provider-approved mechanisms and read the current [Segfault documentation][1].

## Security and acceptable use

Use the environment only on systems and networks for which you have explicit permission. In particular:

- Do not scan, exploit, brute-force, or access third-party systems without authorization.
- Do not expose VNC or SSH ports directly to the public internet when an SSH tunnel is sufficient.
- Do not store secrets in shell history, public logs, screenshots, or source control.
- Verify commands before running them, especially commands involving `sudo`, package signing keys, or remote scripts.
- Follow the provider's acceptable-use policy, resource limits, and abuse-reporting process.

Network anonymity is not guaranteed. A VPN or provider-controlled network path does not make unauthorized activity legal or untraceable.

## Troubleshooting

### `Permission denied` or authentication failure

Confirm that you are using the current server-specific SSH command and secret. Do not keep retrying an expired or copied command.

### `No public key` or package-signature errors

Do not blindly import a key from an old blog post or screenshot. Check the current Kali documentation and verify the key fingerprint through a trusted official source before changing APT trust configuration.

### VNC cannot connect

Check that the SSH tunnel is still open, that the VNC service is running on the remote host, and that the VNC client is using the forwarded local address and port. Do not expose port `5900` publicly as a workaround.

### The server is unavailable

The service is temporary and may be at capacity, rate-limited, or changed by the provider. Check the [official Segfault channels and documentation][1] before opening an issue here.

## Project files

| File | Purpose |
| --- | --- |
| `247.py` | Displays elapsed time in the terminal; it does not provide persistence. |
| `img/` | Screenshots from the documented workflow. |
| `README.md` | Usage, security, and troubleshooting guide. |

## Contributing

Issues and pull requests are welcome. When proposing an update:

1. Verify the behavior against current provider documentation.
2. Remove secrets, personal data, and credentials from examples and screenshots.
3. Explain changes to commands or security guidance.
4. Test shell commands on a clean client where practical.

## Credits

- [THC Segfault][1] for the referenced service and documentation.

[1]: https://www.thc.org/segfault/ "THC Segfault official website"
[2]: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html "PuTTY official download page"
[3]: https://apps.apple.com/us/app/ish-shell/id1436902243 "iSH Shell on the App Store"
[4]: https://github.com/termux/termux-app/releases "Termux official releases"
[5]: https://www.thc.org/segfault/faq/putty/ "THC Segfault PuTTY guide"
[6]: https://www.realvnc.com/en/connect/download/viewer/ "RealVNC Viewer downloads"
[7]: https://remmina.org/how-to-install-remmina/ "Remmina installation guide"
[8]: https://github.com/mrx7014/SSH-KaliLinux "SSH Kali Linux repository"
