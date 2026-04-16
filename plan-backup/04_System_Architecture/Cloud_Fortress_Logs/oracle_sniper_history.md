# PROJECT: NICK-OS CLOUD FORTRESS (ORACLE)
## THE ORACLE SNIPER LOG — APRIL 9-10, 2026

---

## 1. THE MISSION
- **Target:** Secure an "Always Free" Ampere A1.Flex Instance.
- **Specifications:** 4 OCPU, 24GB RAM (The highest free specs in the cloud world).
- **Location:** Johannesburg Data Center (Extreme capacity shortages).

---

## 2. THE SNIPER SCRIPT (`hunter.py`)
- **Location:** `/home/lamdigas/AndroidStudioProjects/academic_automator/hunter.py`
- **Logic:** 
  - Attempts instance creation every ~30 seconds.
  - Cycles through 3 Fault Domains (`FAULT-DOMAIN-1` to `3`).
  - Implements random "Jitter" to avoid bot detection.
  - Captures and retries on "Network drop" (internet flickers) or "Out of host capacity".

---

## 3. STATUS LOG
- **Start Date:** April 9, 2026, 5:22 PM.
- **Current Attempt Count:** ~1,200+.
- **Result:** Ongoing (No capacity yet).

---

## 4. OCI API KEYS (Paired with Laptop)
- **Tenancy OCID:** `ocid1.tenancy.oc1..aaaaaaaavmes5xq6zr5jsmvtnxmkfypvpkkctyz3gq7zegqamhsv5u4fh7gq`
- **Fingerprint:** `86:87:1c:8d:67:e5:26:87:5f:bf:91:94:6b:03:a9:b9`
- **Private Key:** `/home/lamdigas/Downloads/lamdigasndungu3901@gmail.com-2026-04-09T12_43_15.261Z.pem`
- **Config Path:** `~/.oci/config`

---

## 5. RECOVERY INSTRUCTIONS
**To resume the hunt:**
```bash
cd /home/lamdigas/AndroidStudioProjects/academic_automator
./venv/bin/python3 hunter.py
```
*Note: If victory is achieved, the script will print [VICTORY] and the OCID.*
