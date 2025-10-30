# ScreenTime Hacker iOS

Eine Web-App, die aus den LOG-Files eines iPhone-Backups den Bildschirmzeitcode für Bildungszwecke extrahiert.

## 🎯 Zweck

Dieses Tool wurde für **Bildungszwecke** entwickelt, um zu verstehen, wie iOS Bildschirmzeit-Passcodes speichert und verarbeitet. Es kann verwendet werden, um vergessene Bildschirmzeit-Passcodes von Ihren eigenen Geräten wiederherzustellen.

## ⚠️ Wichtiger Hinweis

**Verwenden Sie dieses Tool nur für:**
- Ihre eigenen Geräte
- Geräte, für die Sie die ausdrückliche Erlaubnis des Eigentümers haben
- Bildungs- und Forschungszwecke

Die missbräuchliche Verwendung dieses Tools ist illegal und unethisch.

## 🚀 Installation

### Voraussetzungen
- Python 3.7 oder höher
- pip (Python Package Manager)

### Schritte

1. **Repository klonen:**
```bash
git clone https://github.com/ProfessorEngineergit/ScreentimeHackerIOS.git
cd ScreentimeHackerIOS
```

2. **Abhängigkeiten installieren:**
```bash
pip install -r requirements.txt
```

3. **Anwendung starten:**

**Option A - Mit Convenience Script (empfohlen):**
```bash
# Für Linux/Mac:
./run.sh

# Für Windows:
run.bat
```

**Option B - Manuell:**
```bash
python app.py
```

4. **Browser öffnen:**
Öffnen Sie Ihren Browser und navigieren Sie zu:
```
http://localhost:5000
```

## 📱 Verwendung

### Schritt 1: iPhone Backup erstellen

1. Schließen Sie Ihr iPhone an Ihren Computer an
2. Öffnen Sie iTunes (Windows) oder Finder (macOS)
3. Erstellen Sie ein **unverschlüsseltes** Backup Ihres iPhones

### Schritt 2: Backup-Datei finden

**Backup-Speicherorte:**

- **macOS:** `~/Library/Application Support/MobileSync/Backup/`
- **Windows:** `%APPDATA%\Apple Computer\MobileSync\Backup\`

Im Backup-Ordner suchen Sie nach Dateien mit Namen wie:
- `398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b` (kann variieren)
- Oder andere `.plist` Dateien

Die relevante Datei enthält normalerweise "Restrictions" oder ähnliche Daten.

### Schritt 3: Datei hochladen

1. Öffnen Sie die Web-Anwendung
2. Laden Sie die Backup-Datei hoch
3. Klicken Sie auf "Code extrahieren"
4. Warten Sie, bis der Code angezeigt wird

## 🔧 Wie es funktioniert

Die Anwendung:
1. Liest die hochgeladene `.plist` Datei aus dem iPhone-Backup
2. Extrahiert den gehashten Bildschirmzeit-Passcode und das Salt
3. Verwendet Brute-Force, um den 4-6-stelligen Code zu knacken
4. Zeigt den gefundenen Code an

Der iOS Bildschirmzeit-Passcode wird mit PBKDF2-HMAC-SHA1 gehasht, was es ermöglicht, kürzere Codes durch Brute-Force zu knacken.

## 🛠️ Technischer Stack

- **Backend:** Python 3 + Flask
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Kryptografie:** hashlib (PBKDF2)
- **Datei-Parsing:** plistlib

## 📝 Unterstützte Dateiformate

- `.plist` - Property List Dateien (bevorzugt)
- `.log` - Log-Dateien
- `.db` / `.sqlite` - Datenbank-Dateien

## 🔐 Sicherheit

- Alle hochgeladenen Dateien werden nach der Verarbeitung automatisch gelöscht
- Keine Daten werden gespeichert oder an Dritte weitergegeben
- Die Anwendung läuft lokal auf Ihrem Computer

## 🤝 Beitragen

Beiträge sind willkommen! Bitte öffnen Sie ein Issue oder einen Pull Request.

## 📄 Lizenz

Dieses Projekt ist unter der Unlicense lizenziert - siehe [LICENSE](LICENSE) Datei für Details.

## 🙏 Danksagungen

Entwickelt für Bildungszwecke, um die iOS-Sicherheitsmechanismen besser zu verstehen.

## ⚖️ Haftungsausschluss

Die Entwickler dieses Tools übernehmen keine Verantwortung für missbräuchliche Verwendung. 
Dieses Tool ist ausschließlich für legale und ethische Zwecke bestimmt.