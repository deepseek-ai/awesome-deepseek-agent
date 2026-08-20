[English](./dph_fleet.md) | [简体中文](./dph_fleet.zh-CN.md) · [← Back](../README.md)

# Integrate dph-fleet with DeepSeek

[dph-fleet](https://github.com/polaris-smart/dph-fleet) is an open-source plugin for the DeepSeek Harness (dsh) that turns your devices into a fleet: any agent running in a dsh session gains tools to discover devices on the LAN (mDNS), pair with them (key-based, WiFi-style), execute commands over SSH across networks, and transfer files. It mounts as a pure plugin — zero core changes, zero runtime npm dependencies, uninstall leaves nothing behind.

- **GitHub:** <https://github.com/polaris-smart/dph-fleet>

#### 1. Install dsh (DeepSeek Harness)

dph-fleet runs inside dsh, so you need dsh on every device you want in the fleet (Node 22+):

```sh
npx @deepseek-ai/dsh web
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then store it through dsh credentials (the web Models page writes it), or export it in the launching environment:

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. Install the dph-fleet plugin

On **each** device, install the plugin into the profile you use (default `web`):

```sh
npx @deepseek-ai/dsh plugin --profile web add dph-fleet
```

Then restart dsh. The plugin registers six agent tools automatically (`fleet_discover`, `fleet_pair`, `fleet_ssh_exec`, `fleet_workspace`, `fleet_upload`, `fleet_download`).

#### 4. First run — pair two devices and command one from the other

You need at least 2 devices with dph-fleet installed, connected either on the same LAN (mDNS) or via a publicly reachable SSH endpoint.

On device B (the controlled one), find its device key and start listening. On device A (the controller), just talk to your dsh agent:

```
> Pair with device 192.168.1.42, key fleet-d-xxxx
> Which devices do I have?          (fleet_discover)
> Run hostname on B                 (fleet_ssh_exec)
> Send /tmp/report.txt to B:/tmp/   (fleet_upload)
> Fetch /tmp/result.json from B     (fleet_download)
```

The agent calls the fleet tools directly — no extra CLI required. For LAN pairing, mDNS discovery (`fleet_discover`) lists neighboring devices automatically; for cross-network use, pair once with the device's SSH host and public key authorization.

#### Notes

- Model configuration (DeepSeek-V4 series, context window, reasoning effort) is handled by dsh itself — see the dsh documentation. dph-fleet only adds device-to-device tools and stays out of model routing.
- NAT-isolated devices (both behind home/office routers) cannot connect directly in the current version; a P2P route is planned.
- Requirements and the full walkthrough live in the [dph-fleet README](https://github.com/polaris-smart/dph-fleet).
