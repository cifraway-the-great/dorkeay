# 📌 Presentation

This tool was developed for security verification purposes, focusing on detecting protections such as **Captcha** and **Cloudflare**.

The system uses **SearXNG** as its search engine base for collecting results and follows the **MVC (Model - View - Controller)** architectural pattern, ensuring organization, scalability, and maintainability.

Below is the complete installation guide for **Termux** (also compatible with Linux environments on computers).

---

# 🚀 Installation

## 📱 1. Installation on Termux / Linux

### 🔧 Install dependencies

```bash
pkg install git python3 python3-pip python3-venv build-essential libffi-dev libssl-dev
```

---

## 🔎 2. Installing SearXNG

```bash
git clone https://github.com/searxng/searxng.git
cd searxng
```

---

## 🔐 (Optional) Create a virtual environment

Recommended to keep dependencies isolated from the system.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If using a virtual environment, always activate it before starting:

```bash
source .venv/bin/activate
```

---

## 📦 Install SearXNG dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Generate secret key (run only once)

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the generated hash.

Edit the file:

```bash
nano searx/settings.yml
```

Find:

```bash
server:
  secret_key: "ultrasecretkey"
```

Replace with:

```bash
server:
  secret_key: "PASTE_YOUR_GENERATED_KEY_HERE"
```

Save the file.

---

## ▶️ Start SearXNG

Whenever you want to start it:

```bash
cd searxng
python3 -m searx.webapp &
```

---

## 🛠️ 3. Installing Dorkeay

```bash
git clone https://github.com/cifraway-ogrande/dorkeay.git
cd dorkeay
```

---

## 🔐 (Optional) Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If using a virtual environment, always activate it before running the project.

---

## 📦 Install dependencies

```bash
pip install python-dotenv requests beautifulsoup4 aiohttp colorama
```

---

## ⚙️ 4. .env File Configuration

The project uses a `.env` file to define the connection settings for SearXNG.

### 📄 Create the file

Inside the `dorkeay` folder:

```bash
touch .env
nano .env
```

---

## 📝 .env File Content

```bash
SEARXNG_IP=127.0.0.1
SEARXNG_PORT=8888
SEARXNG_PAGES=40
SEARXNG_LANGUAGE=auto
```

---

## 📌 Variable Explanation

### SEARXNG_IP  
IP address where SearXNG is running.  
127.0.0.1 → Local execution (Termux or computer)  
VPS → Use your VPS public IP  

### SEARXNG_PORT  
Port used by SearXNG.  
Default: 8888  

### SEARXNG_PAGES  
Number of result pages the system will process per search.  
Example: 40  

### SEARXNG_LANGUAGE  
Search language.  
auto → Automatic detection  
Examples: pt, en, es  

Save the file after configuration.

---

## ▶️ 5. Start Dorkeay

```bash
python3 main.py
```

Enter your search term and wait for the verification process to complete.

---

# ⚠️ Troubleshooting

## ❌ SearXNG not returning results

Search engines may be blocking requests.

---

## 🔎 Identify active process

```bash
ps aux | grep searx
```

If using the default port:

```bash
lsof -i :8888
```

---

## 🛑 Kill process

After identifying the PID:

```bash
kill -9 PID_HERE
```

---

# 🌍 Recommendations to Avoid Blocking

- Use a VPS with IP rotation  
- Use a VPN before starting SearXNG  
- Avoid excessive request volume  

Recommended execution flow:

1. Connect VPN (if necessary)  
2. Start SearXNG  
3. Start Dorkeay  
4. Perform searches  

---

# 📁 Architecture

The project follows the:

MVC (Model - View - Controller) pattern  

## Benefits:

- Clear separation of responsibilities  
- Organized codebase  
- Better maintainability and scalability  

---

# 📌 Disclaimer

This tool was developed for educational purposes and security verification testing.

Any misuse is the sole responsibility of the user.