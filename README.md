

# SmartSchool Dokumentation (IoT für die Bildungseinrichtungen)
Felix Riedel <felix.riedel@make-it-mint.de>
1.0, 14.Februar 2026

Das Internet der Dinge ist in unserem Alltag allgegenwärtig. Smartphones, Bluetooth Kopfhörer, Glühbirnen, Türklingeln, Kühlschränke, Autos...
So ziemlich alles kann heute als "smartes" Endgerät gekauft und genutzt werden.

Das SmartSchool Projekt ist entstanden, um Schüler*innen und Lehrkräften einen einfachen Einstieg in die Erstellung eines eigenen Internets der Dinge (Internet of Things - IoT) zu ermöglichen. Das Projekt beinhaltet fertige Codebeispiele, Unterlagen für Projekte zum Selbstlernen und einen ausführlichen Leitfaden zum Aufsetzen eines eigenen IoT-Netzwerks.

Alle Inhalte dieses Workshops können frei von Privatpersonen, öffentlichen und privaten Bildungseinrichtungen für eigene Projekte und den Einsatz im Unterricht verwendet werden.

Für die Durchführung des Workshops sollte die Workshopleitung über grundlegendes Verständnis der Programmiersprache Python verfügen. Für das Aufsetzen der IoT-Netzes sind keine speziellen Kenntnisse notwendig, da der Ablauf hier ausführlich beshcrieben wird.

Empfohlen ist der Workshop ab Klassenstufe 8.

## Einleitung
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

**MQTT** ist ein Protokoll, das über das Internet eine Maschine zu Maschine (M2M) Kommunikation ermöglicht. Hierzu wird ein Broker verwendet, über den Maschinen Nachrichten austauschen. Dafür können öffentliche Online-Broker, eigene Online-Broker oder lokal Broker genutzt werden.

## Erforderliche Materialien
Der Workshop kann in unterschiedlichen Umfängen erfolgen. Welche Sensoren, Aktuatoren und elektrische Bauteile notwendig sind, muss dabei von der Workshopleitung entschieden werden. Eine Auflistung der vorbereiteten Projekte inklusive Handreichungen mit Anleitungen und Materiallisten ist (Beispiellinks zu Onlineshops inklusive) unter dem folgenden Link hinterlegt. .
/TODO Nextcloudlink mit Passwort einfügen 

### Mikrocontroller -> MicroPython & WLAN-fähig 

Grundlegend notwendig sind eignetlich nur MicroPython-fähige Mikrocontroller mit WLAN. Die Beispiele sind für den **Raspberry Pi Pico W** entwickelt worden.

### Raspberry Pi 4B/400/5/500
Das Schulnetzwerk ist oft so konfiguriert, dass es die Kommunikation über MQTT mit Online-Brokern im Internet blockiert. Außerdem ist es möglich, dass das Schul-WLAN das Einloggen der Mikrocontroller verhindert. Deswegen ist es empfehlenswert ein lokales WLAN mit einem eigenen Broker aufzusetzen. Hierfür ist wird ein **Raspberry Pi 4B/400/5/500 mit mindestens 4 GB RAM** und einer **MicroSD Karte mit 16 GB Speicher** empfohlen.

Dadurch ist das Aufsetzen eines lokalen Netzwerks und MQTT-Brokers möglich. Für die Kommunikation mit dem Internet kann zudem ein **Surfstick mit einer Daten SIM-Karte** verwendet werden. Hierfür wurde in diesem Projekt ein ZTE-Surfstick ausgewählt (Link weiter oben). Grund dafür ist, das der Surfstick es ermöglicht die SIM-Karte automatisch zu entsperren und somit nicht bei jedem Start des Surfsticks der PIN der SIM-Karte eingegeben werden muss. Ansonsten kann aber auch ein beliebiger anderer Surfstick verwendet werden. 

## Eingesetzte Software
Anleitungen zur Einrichtung sind im Abschnitt **Einrichtung** aufgeführt.

### Thonny IDE (lokal)
Thonny ist eine kostenlose integrierte Entwicklungsumgebung (IDE) für Python und MicroPython. [Downloadlink](https://thonny.org/).
Sie läuft lokal auf dem eigenen Betriebssystem und ist als "portable Version" herunterladbar. Dadurch muss sie nicht installiert werden.

Thonny ist während der Workshopvorbereitung zur Einrichtung der Mikrocontroller notwendig und kann auch während des Workshops zur Programmierung genutzt werden

### Viper IDE (online)
Ist eine Online IDE, die im Gegensatz zu Thonny über Syntax Highlighting und Code Vervollständigung verfügt. Außerdem muss für ihre Nutzung nicht Thonny auf jedem Computer installiert werden. https://viper-ide.org/

### Mosquitto (MQTT Broker)
Der MQTT-Broker, der für die M2M-Kommunikation genutzt wird

### [optional] Node-Red
Node-Red ist eine Low-Code Entwicklungsumgebung. In ihr können Prozesse und Dashboards ohne Programmierkenntnisse entwickelt werden.

## Einrichtung
Für den Betrieb des Brokers und Node-Red wird Docker verwendet. Das hat den Vorteil, dass beide Anwendungen auf jedem Betriebssystem installiert werden können und die Installation und das Einrichten mit nur wenigen Befehlen möglich ist.

### Docker
In diesem Workshop wird ein Raspberry Pi genutzt. Als Installationsanleitung sollte die offizielle Anleitung der Docker Webseite genutzt werden.
[Docker Install Debian](https://docs.docker.com/engine/install/debian/) & [Docker Linux Postinstall](https://docs.docker.com/engine/install/linux-postinstall/)

Der gesamte Vorgang sollte nur wenige Minuten dauern und kann alternativ auch für andere Betriebsysteme durchgeführt werden.



### Broker und Node-Red ( 5 min)
Ist Docker fertig installiert muss der `smartschool` Ordner dieses Repositories auf den Raspberry Pi heruntergeladen werden. Der Ordner befindet sich in `rpi-files`. Am einfachsten ist es, wenn der `smartschool` Ordner direkt auf dem Desktop platziert wird, damit er leicht wiedergefunden wird.

In diesem Ordner befinden sich Ordner mit Konfigurationsdateien für den MQTT Broker **mosquitto** und Node-Red **node-red-data**. Zusätzlich gibt es die `docker-compose.yml` Datei, mit der die Docker Images heruntergeladen und für die Nutzung konfiguriert werden.

Auf dem Raspberry Pi müssen jetzt die Zugriffsrechte auf die gerade heruntergeladenen Ordner angepasst werden. Grund dafür ist, dass Docker auf diese Ordner zugreifen und sie verwenden wird. Das ist notwendig, damit die Beispiele und Konfigurationen, die erstellt im Vorfeld wurden auch von den Containern, die Docker erzeugt, nutzbar sind und nicht manuell erstellt werden müssen.

Öffne hierzu ein Terminal auf dem Desktop und navigiere in den `smartschool` Ordner indem du den folgenden Befehl in das Terminal eingibst.

`cd Desktop/smartschool`

Der Pfad soll sich jetzt von `~/` zu `~/Desktop/smartschool` geändert haben.

Hier müssen jetzt die folgenden beiden Befehle ausgeführt werden, die den Node-Red und Mosquitto Containern Zugriff auf die jeweiligen Ordner erlauben.

`sudo chown -R 1000:1000 ./node-red-data`

`sudo chown -R 1883:1883 ./mosquitto`

Als letztes werden die Container heruntergeladen und gestartet. Dafür muss lediglich die `Dockerfile` und `docker-compose.yml`Datei ausgeführt werden. Mit dem `Dockerfile` wird das Node-Red Containerimager heruntergeladen und vorkonfiguriert. Die `docker-compose.yml` lädt zusätzlich das Mosquitto Container Image herunter, startet die Container und konfiguriert sie.
Gib die folgenden Befehle in die Konsole ein.

`docker build . -t custom-node-red`

`docker compose up -d`

Das `-d` steht dabei für **detached**. Wird es weggelassen, kann im Terminal nachverfolgt werden, ob alles funktioniert. Sind die Container erfolgreich gestartet, kann durch drücken der **d** Taste der detach auch im Nachhinein durchgeführt werden.

Wurde die Installationsanleitung der Docker Webseite korrekt befolgt, sollten die beiden Container jetzt starten und auch bei jedem Neustart des Raspberry Pi automatisch wieder starten.

Zum Testen kann auf dem Raspberry Pi der Browser geöffnet und in die Suchleiste `http://localhost/` eingegeben werden. Hier sollte die Node-Red Oberfläche angezeigt werden und die lila MQTT Nodes sollten ein grünes **connected** anzeigen.

Das Node-Red Dashboard selbst ist unter `http://localhost/dashboard/demo` erreichbar. Die Testumgebung ist aus dem gesamten lokalen Netzwerk erreichbar, um darauf zuzugreifen muss `localhost` durch die IP Adresse des Raspberry Pi ersetzt werden.

Die IP-Adresse kann im Terminal durch den Befehl `hostname -I` herausgefunden werden, oder durch die WLAN-Einstellungen des Raspi.

>[!NOTE]
> Auf Grund von Netzwerkeinstellungen im Schulnetzwerk kann es sein, dass weder Node-Red, noch der Mosquitto Broker für andere Netzwerkteilnehmer:innen gesehen werden. Deswegen kann es notwendig sein, dass der Raspberry Pi ein eigenes Netzwerk aufbaut, in dass sich die Teilnehmer:innen des Workshops einloggen.

# TODO
RaspAP in Docker Compose aufnehmen. 

