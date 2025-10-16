# 🚀 **Projet Symfony CI/CD : Exercice Pratique**

---

## 📋 **Introduction**

Ce dépôt contient le code de base pour un projet Symfony, conçu pour vous permettre de mettre en pratique les concepts d'intégration et de déploiement continus (CI/CD). À travers cet exercice, vous allez configurer et exécuter une chaîne CI/CD complète, en utilisant des outils comme **PHP-CS-Fixer**, **PHPStan**, **PHPUnit**, **Composer Audit** et **GitHub Actions**.

Le support de cours est consultable ici : [WRA508D | Introduction au CI/CD](https://t15o.notion.site/WRA508D-Introduction-au-CI-CD-19458e133eeb80fc9328f1194a849435)

---

## 🛠️ **Objectifs de l'exercice**

1. **Configurer une chaîne CI/CD** pour un projet Symfony.
2. **Automatiser les tests et les vérifications** à chaque `push` ou `pull request`.
3. **Apprendre à utiliser des outils de qualité de code** comme PHP-CS-Fixer et PHPStan.
4. **Découvrir GitHub Actions** pour exécuter des workflows CI/CD.
5. **Tester localement les workflows** avec l'outil `act`.

---

## 📂 **Structure du projet**

Le projet est structuré comme suit :

```
td_cd-cd/
├── .github/
│   └── workflows/
│       └── run-tests.yml       # Workflow GitHub Actions pour la CI
├── bin/
├── config/
├── public/
├── src/
│   └── Controller/
│       └── BuggyController.php # Contrôleur avec un bug à corriger
│   └── Service/
│       └── DiscountCalculator.php # Service de calcul de remise
├── tests/
│   └── Service/
│       └── DiscountCalculatorTest.php # Tests unitaires pour le service
├── docker-compose.yml          # Configuration Docker pour l'environnement
├── phpstan.dist.neon           # Configuration PHPStan
├── composer.json               # Dépendances du projet
└── README.md                   # Ce fichier
```

---

## 🚀 **Instructions pour démarrer**

### **1. Prérequis**

Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :

- **Docker** et **Docker Compose** : Pour exécuter l'environnement de développement.
- **Git** : Pour cloner le dépôt et gérer les versions.
- **Composer** : Pour installer les dépendances PHP.
- **act** (optionnel) : Pour exécuter localement les workflows GitHub Actions.

---

### **2. Cloner le dépôt**

Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/langouste/td_cd-cd.git
cd td_cd-cd
```

---

### **3. Configurer l'environnement Docker**

Construisez et démarrez les conteneurs Docker :

```bash
docker compose build php
docker compose up -d
```

Accédez au shell du conteneur PHP :

```bash
docker compose exec php bash
```

---

### **4. Installer les dépendances**

Installez les dépendances du projet avec Composer :

```bash
docker compose run php composer install
```

---

### **5. Exécuter les étapes de la CI/CD**

#### **Linting avec PHP-CS-Fixer**
```bash
./vendor/bin/php-cs-fixer fix --dry-run --diff
```

#### **Vérification de la syntaxe PHP**
```bash
find src tests -name "*.php" -exec php -l {} \;
```

#### **Analyse statique avec PHPStan**
```bash
./vendor/bin/phpstan analyse
```

#### **Tests unitaires avec PHPUnit**
```bash
./vendor/bin/phpunit
```

#### **Audit de sécurité avec Composer Audit**
```bash
composer audit --format=json --no-interaction
```

---

### **6. Tester le workflow GitHub Actions localement**

Installez `act` pour exécuter les workflows GitHub Actions localement :

```bash
act -j ci
```

---

## 🤖 **GitHub Actions**

Le fichier `.github/workflows/run-tests.yml` définit un workflow GitHub Actions qui exécute automatiquement les étapes de la CI/CD à chaque `push`. Voici un aperçu des étapes :

1. **Checkout du code** : Récupère le code du dépôt.
2. **Configuration de PHP** : Installe PHP 8.2 avec PCOV.
3. **Installation des dépendances** : Installe les dépendances avec Composer.
4. **Linting** : Exécute PHP-CS-Fixer.
5. **Syntax-checking** : Vérifie la syntaxe PHP.
6. **Analyse statique** : Exécute PHPStan.
7. **Tests unitaires** : Exécute PHPUnit.
8. **Audit de sécurité** : Vérifie les vulnérabilités avec Composer Audit.

---

## 🐛 **Correction des bugs**

Le projet contient un contrôleur `BuggyController` avec un bug à corriger. Votre mission est de :

1. Identifier le bug avec PHPStan.
2. Corriger le code pour éviter un accès à une clé inexistante.
3. Vérifier que les tests unitaires passent.

---

## 📝 **Ressources utiles**

- [Documentation GitHub Actions](https://docs.github.com/en/actions)
- [Documentation PHPUnit](https://phpunit.de/)
- [Documentation PHPStan](https://phpstan.org/)
- [Documentation PHP-CS-Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)
- [Documentation Composer Audit](https://getcomposer.org/doc/03-cli.md#audit)

