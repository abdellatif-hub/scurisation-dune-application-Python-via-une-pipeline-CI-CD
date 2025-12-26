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

## .github/workflows/devsecops.yml

<img width="2541" height="1249" alt="image" src="https://github.com/user-attachments/assets/94bf59f7-d516-49d6-8d14-c259a8560c0e" />

---
## Dockerfile sécurisé

<img width="2557" height="1237" alt="image" src="https://github.com/user-attachments/assets/82c7256d-b120-440e-9150-644eab07d491" />

---

## requirements.txt

<img width="2558" height="1265" alt="image" src="https://github.com/user-attachments/assets/a5c57281-b9e4-4f0e-b419-11ffbbac7406" />


---
## app.py

<img width="2555" height="1213" alt="image" src="https://github.com/user-attachments/assets/07ef57c4-46bf-4c53-a2a8-76c6677ade9c" />


---

### 🔴 Pipeline avant correction

<img width="2554" height="852" alt="image" src="https://github.com/user-attachments/assets/627d01f4-66a2-41ac-8f8b-7b6cae60ec89" />

---
## Push
````

git add .
git commit -m "Secure application DevSecOps Final"
git push


````

<img width="2547" height="1246" alt="image" src="https://github.com/user-attachments/assets/ec75362a-199f-4a69-9c92-a45c230a300d" />

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




### 🟢 Pipeline après correction
*(Ajouter capture ici)*


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


