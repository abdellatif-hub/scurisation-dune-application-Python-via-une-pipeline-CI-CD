# 🔐 Sécurisation d’une Application Python via une Pipeline DevSecOps CI/CD

![DevSecOps](https://img.shields.io/badge/DevSecOps-CI%2FCD-blue)
![Security](https://img.shields.io/badge/Security-Automated-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-informational)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-black)

---

## 📌 Présentation du projet

Ce projet met en œuvre une démarche **DevSecOps complète** pour sécuriser une application web Python (Flask) vulnérable, en intégrant automatiquement la sécurité dans une pipeline CI/CD GitHub Actions.

---

## 🏗️ Architecture du projet

````
devsecops-assignment/
├── api/
│ └── app.py
├── requirements.txt
├── Dockerfile
├── .github/workflows/
│ └── devsecops.yml
└── README.md

````

---

<img width="1947" height="1183" alt="image" src="https://github.com/user-attachments/assets/0b63137c-0ef0-4682-89b1-1a633da580dd" />


## 🔄 Pipeline DevSecOps

1. CodeQL — Analyse SAST  
2. Bandit — Analyse de sécurité Python  
3. Safety — Scan des dépendances (Supply Chain)  
4. Docker Build  
5. Trivy — Scan de l’image Docker  

➡️ La pipeline bloque automatiquement toute faille CRITICAL ou HIGH.

---

## 🧪 Vulnérabilités détectées (Avant correction)

| Endpoint | Faille | Outil | OWASP |
|---------|------|-----|-----|
| /auth | SQL Injection | CodeQL | A03 |
| /exec | Command Injection | Bandit | A03 |
| /deserialize | Insecure Deserialization | Bandit | A08 |
| /encrypt | Weak Crypto (MD5) | Bandit | A02 |
| /file | Path Traversal | CodeQL | A01 |
| /debug | Sensitive Data Exposure | CodeQL | A02 |
| API_KEY | Hardcoded Secret | Bandit | A02 |
| /log | Log Injection | Bandit | A09 |

---







---



## 🔐 Corrections appliquées

| Vulnérabilité | Correction |
|--------------|-----------|
| SQL Injection | Requêtes paramétrées |
| Command Exec | Endpoint supprimé |
| Désérialisation | Endpoint supprimé |
| Crypto faible | bcrypt |
| Path Traversal | Validation stricte |
| Secrets exposés | Variables d’environnement |
| Docker | Image slim + user non-root |

---

## 📸 Captures d’écran

### 🔴 Pipeline avant correction
*(Ajouter capture ici)*

### 🟢 Pipeline après correction
*(Ajouter capture ici)*

### 🔍 Résultats des outils
*(Ajouter captures ici)*

---

## 📊 Résultat final

✔ Application sécurisée  
✔ Pipeline automatisée  
✔ Blocage des failles critiques  
✔ Conforme OWASP Top 10  

---

## 🏁 Conclusion

Ce projet démontre l’importance de l’intégration de la sécurité dans le cycle de développement grâce à DevSecOps.

---

👤 **Auteur : Abdellatif**  
🎓 **Projet pédagogique DevSecOps**


