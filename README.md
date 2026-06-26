

# SmartSchool Dokumentation (IoT für die Bildungseinrichtungen)
Felix Riedel <felix.riedel@make-it-mint.de>
1.0, 14.Februar 2026

Getestet mit Raspberry Pi 4B(8GB) und Raspberry Pi 400, Debian Trixie 64-bit Desktop Version.

Die Unterlagen für den Workshop werden [hier](https://nextcloud.mintorinnen.de/s/K4Cg5SbmCTbWWMa) veröffentlicht.  
Passwort: SmartSchool!

## Einleitung 
Das Internet der Dinge ist in unserem Alltag allgegenwärtig. Smartphones, Bluetooth Kopfhörer, Glühbirnen, Türklingeln, Kühlschränke, Autos...
So ziemlich alles kann heute als "smartes" Endgerät gekauft und genutzt werden.

Das SmartSchool Projekt ist entstanden, um Schüler*innen und Lehrkräften einen einfachen Einstieg in die Erstellung eines eigenen Internets der Dinge (Internet of Things - IoT) zu ermöglichen. Das Projekt beinhaltet fertige Codebeispiele, Unterlagen für Projekte zum Selbstlernen und einen ausführlichen Leitfaden zum Aufsetzen eines eigenen IoT-Netzwerks.

Alle Inhalte dieses Workshops können frei von Privatpersonen, öffentlichen und privaten Bildungseinrichtungen für eigene Projekte und den Einsatz im Unterricht verwendet werden.

Für die Durchführung des Workshops sollte die Workshopleitung über grundlegendes Verständnis der Programmiersprache Python verfügen. Für das Aufsetzen der IoT-Netzes sind keine speziellen Kenntnisse notwendig, da der Ablauf hier ausführlich beshcrieben wird.

Empfohlen ist der Workshop ab Klassenstufe 8.

Das Aufsetzen eines IoT-Netzwerks und die Enticklung eigener "smarter" Geräte sind interdisziplinäre Aufgaben. Neben dem programmieren, werden elektrische Schaltungen aufgebaut, in denen die smarten Geräte Sensoren zum Erfassen von Messwerten und Aktuatoren zum Steuern von Maschinen und Geräten nutzen.

Zur Kommunikation der Geräte untereinander wird in diesem Projekt MQTT (Message Queuing Telemetry Transport) verwendet. Ein offenes und leichtgewichtiges Protokoll zum Austausch von Daten über das Internet oder ein lokales Netzwerk.

Als Programmiersprache wurde MicroPython gewählt. MQTT ist aber in allen Programmiersprachen nutzbar und kann beispielsweise auch mit Arduino Mikrocontrollern verwendet werden. Dafür müssen die Mikrocontroller aber WLAN-fähig sein.

Gründe für die Auswahl von MicroPython sind

* Filesystem auf den Mikrocontrollern
* Python ist eine einfache und gut dokumentierte Programmiersprache zum Einstieg
  * wird an Schulen als Sprache für die objektorientiert Programmieung im Lehrplan für informatik verwendet
  * MicroPython und Python haben den gleichen Syntax
* große Auswahl an Mikrocontrollern, auf denen MicroPython installiert werden kann ( https://micropython.org/download/ )
* große Community und Vielzahl an Projekten online verfügbar
* Python ist eine vielseitige Sprache -> "Python is Glue"

**MQTT** ist ein IoT-Protokoll, das über das Internet eine Maschine zu Maschine (M2M) Kommunikation ermöglicht. Hierzu wird ein Broker verwendet, über den Maschinen Nachrichten austauschen. Dafür können öffentliche Online-Broker, eigene Online-Broker oder lokal Broker genutzt werden.

## Erforderliche Materialien
Der Workshop kann in unterschiedlichen Umfängen erfolgen. Welche Sensoren, Aktuatoren und elektrische Bauteile notwendig sind, muss dabei von der Workshopleitung entschieden werden. Eine Auflistung der vorbereiteten Projekte inklusive Handreichungen mit Anleitungen und Materiallisten ist (Beispiellinks zu Onlineshops inklusive) unter dem folgenden Link hinterlegt. .
/TODO Nextcloudlink mit Passwort einfügen 

### Mikrocontroller -> MicroPython & WLAN-fähig 

Grundlegend notwendig sind eignetlich nur MicroPython-fähige Mikrocontroller mit WLAN. Die Beispiele sind für den **Raspberry Pi Pico W** entwickelt worden.

Eine Übersicht geeigneter MicroController und Downloadlinks findest du auf der [MicroPython Website](https://micropython.org/download/).

### Raspberry Pi 4B/400/5/500
Das Schulnetzwerk ist oft so konfiguriert, dass es die Kommunikation über MQTT mit Online-Brokern im Internet blockiert. Außerdem ist es möglich, dass das Schul-WLAN das Einloggen der Mikrocontroller verhindert. Deswegen ist es empfehlenswert ein lokales WLAN mit einem eigenen Broker aufzusetzen. Hierfür ist wird ein **Raspberry Pi 4B/400/5/500 mit mindestens 4 GB RAM** und einer **MicroSD Karte mit 16 GB Speicher** empfohlen.

Dadurch ist das Aufsetzen eines lokalen Netzwerks und MQTT-Brokers möglich. Für die Kommunikation mit dem Internet kann zudem ein **Surfstick mit einer Daten SIM-Karte** verwendet werden. Hierfür wurde in diesem Projekt ein ZTE-Surfstick ausgewählt (Link weiter oben). Grund dafür ist, das der Surfstick es ermöglicht die SIM-Karte automatisch zu entsperren und somit nicht bei jedem Start des Surfsticks der PIN der SIM-Karte eingegeben werden muss. Ansonsten kann aber auch ein beliebiger anderer Surfstick verwendet werden. 

## Eingesetzte Software
Anleitungen zur Einrichtung sind im Abschnitt **Einrichtung** aufgeführt. Der gesamte Einrichtungsprozess ist mit Hilfe von Docker soweit automatisiert, dass nur wenige manuelle Schritte notwendig sind. 

### Thonny IDE (lokal)
Thonny ist eine kostenlose integrierte Entwicklungsumgebung (IDE) für Python und MicroPython. [Downloadlink](https://thonny.org/).
Sie läuft lokal auf dem eigenen Betriebssystem und ist als "portable Version" herunterladbar. Dadurch muss sie nicht installiert werden.

Thonny ist während der Workshopvorbereitung zur Einrichtung der Mikrocontroller notwendig und kann auch während des Workshops zur Programmierung genutzt werden

### Viper IDE (online)
Ist eine Online IDE, die im Gegensatz zu Thonny über Syntax Highlighting und Code Vervollständigung verfügt. Außerdem muss für ihre Nutzung nicht Thonny auf jedem Computer installiert werden. https://viper-ide.org/

### Docker
Docker ermöglicht es Programme in einer eigenen Umgebung als isolierte Container laufen zu lassen. Hierzu werden vorbereitete Container Images verwendet. Dadurch gibt es das "Works on my machine" Problem nicht mehr, da Docker Betriebssystem -unabhängig funktioniert

### Mosquitto (MQTT Broker)`Installation mit Docker`
Der MQTT-Broker, der für die M2M-Kommunikation genutzt wird. 

### RaspAP `Installation mit Docker`
Mit RaspAP wird der Raspberry Pi zu einem eigenen Accesspoint. Schulnetzwerke sperren häufig MicroController davon, sich in das Netzwerk einzuloggen

### [optional] Node-Red `Installation mit Docker`
Node-Red ist eine Low-Code Entwicklungsumgebung. In ihr können Prozesse und Dashboards ohne Programmierkenntnisse entwickelt werden. Der Node-Red Container dieses Repositories beinhaltet ein Beispieldashboard für Demo-Zwecke, das für einen ersten Test genutzt werden kann.

### [optional] MySQL `Installation mit Docker`
MySQL ist ein von Oracle entwickltes kostenlose OpenSource System für relationale Datenbanken.

### [optional] phpMyAdmin `Installation mit Docker`
Kostenlose OpenSource Software, die eine grafische Nuzteroberfläche  zur Verwaltung von MySQL Datenbanken im Browser zur Verfügung stellt.

## Einrichtung

Für das Einrichten der Software werden bash-Skripte zur Verfügung gestellt, die fast den gesamten Prozess automatisieren. Im Folgenden werden die notwendigen Schritte der Einrichtung beschrieben. Es wird von einem Raspberry Pi mit Desktop ausgegangen. Solltest du die Server-Version ohne Desktopumgebung nutzen, passe die Schritte entsprechend an.

### Download des Repositories
Lade dieses Repository auf den Raspberry Pi, entpacke es und kopiere den `smartschool` Ordner auf den Desktop des Raspberry Pi. Der `smartschool` Ordner befindet sich in `rpi-files`.

Öffne jetzt den `smartschool` Ordner auf dem Desktop.

### Konfiguration des Accesspoints
Mit RaspAP wird der Raspberry Pi zu einem AccessPoint. Docker konfiguriert diesen Accespoint. Die Parameter kannst du selbst festleen. Öffne hierzu die `docker-compose.yml` Datei im `smartschool` Ordner und passe die folgenden Werte rechts vom `=` Zeichen an: 
- RASPAP_SSID=raspap-webgui <-Name des WLAN
- RASPAP_SSID_PASS=ChangeMe <-Passwort des WLAN
- RASPAP_WEBGUI_USER=admin  <-Nutzername für die Weboberfläche
- RASPAP_WEBGUI_PASS=secret <-Passwort für dei Weboberfläche

Du kannst diese Werte auch später verändern und den Accesspoint neu starten. Außerdem kannst du in dieser datei immer nachschauen, solltest du die Zugangsdaten vergessen haben.

Speichere die Änderungen und schließe die `docker-compose.yml` Datei wieder.

### Konfiguration der MySQL Datenbank
Genauso wie der Accesspoint, wird die MySQL Datenbank über die `docker-compose.yml` Datei im `smartschool` Ordner konfiguriert. Die folgenden Were rechts vom `=` Zeichen können hierfür angepasst werden:
- MYSQL_ROOT_PASSWORD: your_root_password
- MYSQL_DATABASE: your_database_name
- MYSQL_USER: your_username
- MYSQL_PASSWORD: your_password

In der Node-Red Demo ist eine beispielhafte Datenbankverbindung mit den hier vorhandenen Standardwerten beinhaltet. Passe die Werte der `database` Node entsprechende deiner angepassten Einstellungen an, damit die Verbindung hergestellt werden kann.

### Installation vorbereiten
Zur Einrichtung werden wie bereits beschrieben, zwei bash-Skripte verwendet. `install_packages.sh` und `setup_system.sh`. Die Aufteilung ist notwendig, da dass System zwischendurch neu gestartet werden muss, damit eine bestimmte Änderung übernommen wird.

Die bash-Skripte können über das Terminal ausgeführt werden, oder durch Doppelklick und Auswählen des "Ausführen" Buttons. Dafür muss dem Nutzerkonto die Berechtigung zum Ausführen der bash-Skripte erteilt werden. Dieser Schritt muss für dass `install_packages.sh` Skript manuell durchgeführt werden.

Führe hierzu einen Rechtsklick auf die `install_packages.sh` Datei durch und wähle aus dem Menü `Eigenschaften` aus.

Wähle in dem sich jetzt öffnenden Menü unter `Berechtigungen` -> `Zugriffsrechte`->`Ausführen` die Option `Jeder` aus. Bestätige mit **OK**.

Damit sind alle Vorbereitungen abgeschlossen. Die restliche Installation übernehmen die bash-Skripte.

### Installation
Doppelklicke jetzt auf das `install_packages.sh` Skript und wähle `Ausführen` oder `Ausführen mit Terminal` aus.

Das `install_packages.sh` bash-Skript führr die folgenden Aktivitäten durch:
- Aktualisierung der Packages
- Hinzufügen von Docker zu den Packages
- Installation von Docker
- macht das `setup_system.sh` bash-Skript ausführbar (für den nächsten Schritt)
- Fügt den aktuellen Nutzeraccount zur Gruppe "docker" hinzu. Dadurch muss Docker nicht als Administrator ausgeführt werden. Dieser Schritt erfordert den Neustart des Systems.

Öffne nach dem Neustart wieder den `smartschool` Ordner auf dem Desktop und führe jetzt das `setup_system.sh` Skript aus. Dieses Skript kannst du auch zukünftig, falls es Probleme gibt, erneut ausführen.

Das `setup_system.sh` Skript führt die folgenden Aktivitäten durch:
- gibt den Containern, die erstellt werden, Zugriffsrechte auf die Unterordner im `smartschool` Ordner. Das ist notwendig, da hier Dateien abgelegt sind, die die Container konfigurieren.
- Überprüfung ob das `custom-node-red` Docker Image bereits gebaut wurde und baut es neu, falls es noch nicht geschehen ist. Dieser Schritt wird beim ersten Ausführen durchlaufen und kann abhängig von der Internetverbindung **5-10 Minuten** dauern.
- Änderung am Betriebssystem, sodass das WLAN-Interface für RaspAP nutzbar wird
- Installation und Starten der Dockercontainer. In diesem Schritt werden beim ersten Ausführen die Container Images heruntergeladen. Abhängig von der Internetverbindung **5-10 Minuten** dauern. Bricht die Installation hier ab, kann es sein, dass das Netzwerk, in dem du dich befindest eine sehr schlechte Verbindung hat, oder den Download verhindert. Ist das der Fall (was im Schulnetzwerk passieren kann), muss für die weitere Installation ein anderes Netzwerk verwendet werden.
- Die Dockercontainer sind so eingerichtet, dass sie bei einem Neustart des Systems automatisch neu starten.

Öffnest du jetzt den Browser, kannst du die folgenden Seiten erreichen:
- Node-Red Entwicklungsumgebung: `http://localhost/`
- Node-Red Dashboard: `http://localhost/dashboard/demo`
- RaspAP Webinterface: `http://localhost:8081`
- phpMyAdmin: `http://localhost:8888`


Haben die lila-farbenen Nodes in der Node-Red Entwicklungsumgebung `grüne` Kästechen unter sich, ist auf der Mosquitto-Broker erfolgreich eingerichtet. Innerhalb deines Netzwerks können IoT-Geräte jetzt miteinander kommunizieren. Starte den Raspberry Pi noch ein letztes Mal neu, damit das WLAN-Interface auch sicher für dein Netzwerk freigegeben ist.

Hast du ein anderes Gerät in das Netzwerk eingeloggt, kannst du auf die Webseiten zugreifen, indem du anstatt `localhost` die IP-Adresse des Raspberry Pi eingibst. Die findest zu heraus, indem du ein Terminal öffnest und den Befehl `hostname -I` ausführst. Die Webadresse wäre dann beispielsweise:

`http://192.168.1.10/dashboard/demo`

## [Optional] Internet für dein Netzwerk

Das Netzwerk deines Raspberry Pi verfügt von sich aus über keine Internetverbindung. Du kannst den Geräten des Netzwerks Zugriff auf das Internet geben, indem du ein LAN-Kabel in den Ethernetport steckst. Die Internetverbindung wird dann weitergeleitet. Aber du machst dadurch auch das Netzwerk, an das du dich mit dem LAN-Kabel anschließt potentiell angreifbar und das Schulnetzwerk blockiert die MQTT-Kommunkation mit Online-Brokern.


### [Optional] Verwendung eines Surfsticks
Alternativ kann ein Surfstick verwendet werden. Um die Internetverbindung des Surfsticks für die teilnehmenden Geräte des Netwerks verfügbar zu machen, muss nur ein Eintrag in einer Datei geändert werden.

Im `smartschool` Ordner auf dem Desktop öffne die Datei `raspap-data/firewall-rules.sh`.

Diese Datei ist für die Weiterleitung der Internetanbindung verantwortlich. Standardmäßig ist dafür das LAN-Interface `eth0` eingestellt. Das kann aber in der folgenden Zeile geändert werden:

`surfstick=eth0`

Gibt für `eth0` die Bezeichnung deines Surfsticks ein, speichere die Änderung und starte den Raspberry Pi einmal neu. Jetzt sollte die Internetanbindung weitergeleitet werden und du hast einen Schul-WLAN unabhängigen Accesspoint. Die Bezeichnung, den Namen, deines Surfsticks findest du, wenn du die erweiterten Netzwerkeinstellungen öffnest.

