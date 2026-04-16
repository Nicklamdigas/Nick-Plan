# PROJECT: NICK-OS CLOUD FORTRESS (DigitalOcean)
## ARCHITECTURAL SNAPSHOT — APRIL 10, 2026

---

## 1. INFRASTRUCTURE OVERVIEW
| Component | Detail |
|-----------|--------|
| **Provider** | DigitalOcean (GitHub Student Pack) |
| **Server Name** | `nick-cloud-fortress` |
| **Public IP** | `46.101.120.169` |
| **Specs** | 4GB RAM, 2 CPUs, 80GB NVMe SSD |
| **OS** | Ubuntu 24.04.3 LTS (Noble Numbat) |
| **Access** | SSH Key Auth (No passwords) |
| **SSH Key (Local)** | `/home/lamdigas/.ssh/do_ed25519` |

---

## 2. SYSTEM STATE
### Software Installed:
- **Docker Engine:** v29.4.0 (Ready for containerization)
- **Node.js:** v22.22.2 (Latest LTS)
- **OpenClaw:** v2026.4.9 (Core installed via npm)

### Configured Components:
- **Gemini Brain:** API Key integrated via `openclaw.json`.
- **Neutral Zone:** `/root/Neutral_Zone` folder created on server.
- **MCP Server:** Filesystem server configured to watch the cloud Neutral Zone.
- **Bonjour:** Disabled (Prevents cloud crash loops).
- **Control UI Origin:** Set to `*` (allowing remote access).

---

## 3. THE "FIVE WALLS" (CURRENT BLOCKERS)
We are currently stuck on the **Login Interface**.
1. **Browser Security:** Chrome/Brave blocks the login button over `http://IP`.
2. **Secure Context:** Needs `localhost` or `HTTPS`.
3. **Tunnel Stability:** Local laptop Wi-Fi flickering kills the SSH `-L` bridge.
4. **Auth Paradox:** OpenClaw refuses to run without a token if exposed to LAN.
5. **Origin Mismatch:** The Web UI and Gateway must agree on the source address.

---

## 4. NEXT MISSION (PHASE 3: NETWORK MASTERY)
**Objective:** Solve the "Security Context" once and for all.

### Strategy A: The Web Architect Path (Nginx + SSL)
- Install **Nginx** as a Reverse Proxy.
- Use **Certbot** to get a free "Let's Encrypt" certificate.
- Access via: `https://your-domain.com` (Professional grade).

### Strategy B: The Stealth Specialist Path (Tailscale)
- Install **Tailscale** on both Laptop and Cloud.
- This creates a "Mesh VPN" (Private LAN).
- Access via: `http://nick-cloud-fortress:18789` (Fastest and most secure).

---

## 5. RECOVERY COMMANDS
**To log into the server:**
`ssh -i ~/.ssh/do_ed25519 root@46.101.120.169`

**To see if the brain is alive:**
`screen -ls` (Look for the `openclaw` session)
`journalctl -u openclaw-gateway.service`

**To fix the tunnel (from laptop):**
`pkill -f "ssh -i ~/.ssh/do_ed25519 -L"`
`ssh -i ~/.ssh/do_ed25519 -N -f -L 8888:127.0.0.1:18789 root@46.101.120.169`
