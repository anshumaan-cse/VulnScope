## 🔍 HTTP Security Header Analyzer

A lightweight CLI tool to analyze HTTP security headers and detect misconfigurations in web applications.
---

## 🚀 Features
- Detects missing security headers  
- Identifies potential security misconfigurations  
- Simple command-line interface  
- Lightweight and fast  

---

## 📦 Installation

```bash
git clone https://github.com/anshumaan-cse/VulnScope.git
cd VulnScope
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

Enter a target URL when prompted.

---

## 🛡️ Security Headers Checked
- Content-Security-Policy  
- Strict-Transport-Security  
- X-Frame-Options  
- X-Content-Type-Options  
- Referrer-Policy  
- Permissions-Policy  

---

## 📌 Example Output

```
[+] Checking https://example.com

[OK] X-Frame-Options present
[OK] X-Content-Type-Options present
[!] Missing Content-Security-Policy (HIGH RISK)
```

---

## ⚠️ Disclaimer
This tool is intended for educational and ethical security testing purposes only.
