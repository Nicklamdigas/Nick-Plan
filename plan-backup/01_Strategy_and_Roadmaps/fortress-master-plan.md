# Detailed Master Plan: OpenClaw Fortress System (Nick-OS v5.0)

## 🎯 Project Goal
Create a hardware-isolated, self-evolving AI agent ecosystem on an external SSD. The system will be physically and digitally separated from Nick's personal Linux data, communicating only through a secure "Neutral Zone."

---

## 🛠️ Phase 0: Prerequisites & Hardware Identification
**Goal:** Identify the external SSD and prepare the host machine.

1.  **Plug in the External SSD.**
2.  **Identify the Drive Path:**
    - Run: `lsblk`
    - Look for your external SSD (likely labeled by size, e.g., 250G or 500G).
    - **Crucial:** Note the path (e.g., `/dev/sdb` or `/dev/sdc`). **DO NOT** mistake it for your primary `/dev/sda` drive.
3.  **Install Virtualization Tools on Host (Personal Linux):**
    ```bash
    sudo apt update
    sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients virt-manager
    sudo adduser $USER libvirt
    sudo adduser $USER kvm
    ```

---

## 🧹 Phase 1: Clearing the Fortress (Wiping the SSD)
**Goal:** Complete destruction of existing data on the secondary SSD.

1.  **Unmount the drive:**
    - `sudo umount /dev/sdX*` (replace X with your drive letter).
2.  **Wipe the partition table:**
    - `sudo wipefs -a /dev/sdX`
3.  **Create a fresh ext4 partition (Optional, but good for testing):**
    - `sudo mkfs.ext4 /dev/sdX`

---

## 🏗️ Phase 2: Building the "Ghost" VM
**Goal:** Install an isolated OS inside the secondary SSD using Hardware Passthrough.

1.  **Open Virt-Manager:**
    - Create a new Virtual Machine.
2.  **OS Selection:** Use **Ubuntu Server 24.04 LTS** (fastest, no bloat) or Lubuntu.
3.  **Storage Configuration (Passthrough):**
    - Instead of creating a virtual disk file, select **"Select or create custom storage."**
    - Provide the direct path to the SSD: `/dev/sdX`.
    - This gives the VM raw access to the hardware.
4.  **Network Setup:**
    - Choose **"Isolated"** network mode during setup, then switch to "NAT" only when installing software.

---

## 🧬 Phase 3: Software Installation (Inside the Fortress)
**Goal:** Set up the "Brain" and the "Utility Belt."

1.  **Update System:**
    - `sudo apt update && sudo apt upgrade -y`
2.  **Install Node.js 22+ (for OpenClaw):**
    ```bash
    curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
    sudo apt install -y nodejs
    ```
3.  **Install OpenClaw:**
    ```bash
    curl -fsSL https://openclaw.ai/install.sh | bash
    ```
4.  **Install Python 3.12 & CrewAI:**
    ```bash
    sudo apt install -y python3-pip python3-venv
    python3 -m venv venv
    source venv/bin/activate
    pip install crewai langchain-google-genai
    ```

---

## 🛡️ Phase 4: Security Hardening (The Walls)
**Goal:** Prevent the Agents from escaping or seeing your home Wi-Fi.

1.  **Network Whitelisting (Inside VM):**
    - Configure `ufw` or `iptables` to only allow traffic to:
        - `generativelanguage.googleapis.com` (Gemini API)
        - `github.com` (for code updates)
    - Block all local network ranges: `192.168.1.0/24`, etc.
2.  **The "Neutral Zone" (VirtFS Shared Folder):**
    - In Virt-Manager, add a shared folder.
    - **Host Path:** `/home/lamdigas/Neutral_Zone`
    - **Guest Path:** `/mnt/Neutral_Zone`
    - **Constraint:** This is the *only* link. The agents cannot see your `/home/lamdigas/Pictures` or `/home/lamdigas/Documents`.

---

## 🧠 Phase 5: Creating the Self-Evolving Crew
**Goal:** Program the agents to think independently.

1.  **The "Knowledge Base" Folders:**
    - Create `/fortress/Mentor/`, `/fortress/Strategist/`, etc.
2.  **The "Thinking" Script:**
    - Program the agents to run every 2 hours.
    - **Task:** "Review any files in `/mnt/Neutral_Zone`. Research improvements. Update your specific Knowledge Base file."
3.  **The "Governor" (Quota Protection):**
    - Add a Python script that counts API calls. If calls > 50 per day, it pauses the agents.

---

## 📈 Phase 6: Operational Workflow
**How you will use it every day:**

1.  **The Input:** You finish writing `todo.py` on your personal Linux.
2.  **The Hand-off:** You drag a copy of `todo.py` into your `/home/lamdigas/Neutral_Zone` folder.
3.  **The Processing:** The VM (on the external SSD) wakes up. The Mentor agent sees the file, researches best practices, and writes a detailed critique in `MENTOR_KNOWLEDGE.md`.
4.  **The Feedback:** You open the shared folder and read the Mentor's findings. You learn *without* the agent ever touching your personal system.

---

## 📜 Prerequisite Checklist
- [ ] External SSD (Cleared of any important files).
- [ ] Laptop charger plugged in (VMs eat battery).
- [ ] Gemini API Key copied.
- [ ] Strong coffee (Complexity is high).

---

### 📅 Next Step
**When you return for your Growth block (19:00):**
We will start by running `lsblk` to identify your drive and begin Phase 1. 

**Are you ready to commit to this "Fortress" architecture, Nick?**
