# 🔍 VulnScope — HTTP Security Header Analyzer

A Python-based CLI tool that analyzes HTTP security headers to identify misconfigurations and evaluate the security posture of web applications using a weighted risk model.

---

## ✨ Key Features

- Detects missing critical HTTP security headers  
- Weighted risk-based scoring (HIGH / MEDIUM / LOW)  
- Multi-URL scanning using urls.txt  
- Clean CLI output with severity indicators  
- JSON report generation (report.json)  
- Custom User-Agent and timeout handling for reliable requests  

---

## 🧠 Security Headers Covered

| Header                       | Purpose                                  | Risk  |
|-----------------------------|------------------------------------------|-------|
| Content-Security-Policy     | Prevents XSS and injection attacks       | High  |
| Strict-Transport-Security   | Enforces HTTPS (MITM protection)         | High  |
| X-Frame-Options             | Prevents clickjacking                    | Medium|
| X-Content-Type-Options      | Prevents MIME sniffing                   | Medium|
| Referrer-Policy             | Controls referrer leakage                | Low   |
| Permissions-Policy          | Restricts browser features/APIs          | Low   |

---

## ⚙️ Installation

bash
git clone https://github.com/anshumaan-cse/VulnScope.git
cd VulnScope
pip install -r requirements.txt


---

## ▶️ Usage

### Scan a single URL
bash
python main.py


Enter a target URL when prompted.

---

### Scan multiple URLs

Add URLs inside urls.txt:


https://example.com
https://google.com
https://github.com


Then run:

bash
python main.py


---

## 📊 Output

The tool displays:

- Present security headers  
- Missing headers with risk level  
- Security score (%)  
- Overall security assessment  

It also generates:

- report.json → structured scan results  

---

## 📁 Example Output


[OK] Content-Security-Policy
[OK] Strict-Transport-Security
[MISSING] Permissions-Policy (LOW)
   ↳ Restricts browser APIs

[+] Score: 83.3%
⚠ Moderate security


---

## 🧱 Project Structure


VulnScope/
 ├── scanner/
 │    ├── headers.py
 │    └── __init__.py
 ├── main.py
 ├── urls.txt
 ├── requirements.txt
 ├── report.json
 └── README.md


---

## 🛠 Tech Stack

- Python 3  
- Requests  
- Colorama  

---

## 🎯 Use Cases

- Quick security auditing of web applications  
- Identifying missing HTTP security protections  
- Learning and practicing web security fundamentals  

---

## 🔮 Future Improvements

- Multi-threaded scanning for performance  
- CSV/HTML report export  
- Subdomain scanning integration  
- CI/CD pipeline integration  

---

## 👨‍💻 Author

*Anshumaan*  
B.Tech CSE | Cybersecurity Enthusiast  

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐
