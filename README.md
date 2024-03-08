# SmartSchool Workshop - Einführung IoT mit MQTT in Python und MicroPython

Dieses Repository beinhaltet den Programmcode für den Workshop "Einführung IoT mit MQTT" von MAKE IT MINT.

## Benötigte Hardware:
- Broker: Raspberry Pi 3B+/4B/400 mit Raspbian Bullseye
- Clients: Raspberry Pi Pico W oder andere WLAN-fähige Mikrocontroller, auf denen MicroPython installiert werden kann.([Übersicht](https://micropython.org/download/))
- Steckplatinen, Sensoren, Aktuatoren und weitere Bauteile für ausgewählte Clientfunktionen

Für den Broker wird hier eine Raspberry Pi 4B, mit Raspbian Bullseye installiert, verwendet. Er kann auch auf einem anderen Gerät installiert werden, dafür muss aber Eigenrecherche betrieben werden ;). Willst du keinen eigenen Broker einichten, kann auch ein öffentlicher Broker verwendet werden, wie ihn beispielsweise HiveMQ [hier](https://www.hivemq.com/public-mqtt-broker/) zur Verfügung stellt. Über Datenschutzrichtlinien im Vorfeld bitte selbst informieren.

Für das Flashen der Mikrocontroller werden Raspberry Pi 400 verwendet. Andere Linuxbetriebssysteme funktionieren aber auch.

## Installation des Brokers (RPi 4B)
Die Installationsanleitung basiert auf einem Tutorial der Website [pimylifeup.com](https://pimylifeup.com/raspberry-pi-mosquitto-mqtt-server/)

Öffne ein Terminal und aktualisiere die verfügbaren Pakete
`sudo apt update`

Installiere Broker und Client
`sudo apt install mosquitto mosquitto-clients`

Der Broker ermöglicht standardmäßig keine Kommunikation nach Außen. Um dies zu ermöglichen muss die Konfigurationsdatei des Broker angepasst werden.

Öffne die Konfigurationsdatei
`sudo nano /etc/mosquitto/mosquitto.conf`

und füge die folgenden Zeilen am Ende der Datei ein

`listener 1883`
`allow_anonymous true`

Drücke STRG + O -> Enter -> STRG + X zum Speichern und Schließen der Datei.

Diese Zeilen legen fest, dass der Broker über Port 1883 mit externen Geräten kommuniziert und auch Geräte ohne Namen zulässt. (Für diesen Workshop notwendig)

Prüfe ob der Broker aktiv ist indem du den folgenden Befehl in der Konsole eingibst
`sudo systemctl status mosquitto.service`
Es sollte ein grünes "(is running)" und weiterer Text angezeigt werden.

UUUUnd der Broker ist einsatzbereit. TOP!

## Installation von Node-Red auf dem Server (4B)

Node-Red wird in diesem Workshop verwendet, um ein Dashboard der "Dinge" über das Netzwerk bereitzustellen. Es wird auf dem gleichen Gerät installiert, wie der MQTT Broker.
Node-Red stellt einen Installationswizard zur Verfügung, der [hier](https://nodered.org/docs/getting-started/raspberrypi) gefunden werden kann.

Einfach ein Terminal öffnen und die folgende Zeile ausführen:
`bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)`
Die installation wird ein paar Minuten in Anspruch nehmen.
Sobald sie abgeschlossen ist, muss noch Dashboard Erweiterung installiert werden. Im Terminal folgenden Befehl ausführen:
`npm install node-red-dashboard`

Im Browser kann jetzt sowohl das Interface zum Erstellen von Workflows, als auch das Dashboard geöffnet werden. Node-Red verwendet standardmäßig Port 1880.
Öffne einen Browser und gib die folgende url ein:
localhost:1880      <- für Flows
localhost:1880      <- für Das Dashboard


#### Server von Netzwerkgeräten erreichen
Um diese Seiten von einem anderen Gerät im Netzerk zu erreichen muss die IP-Adresse des Servers ermittelt und für "localhost" ersetzt werden.

Die IP-Adresse des Servers kann durch Eingabe des folgenden Befehls in das Terminal ermittelt werden:
`ifconfig -a`
In der Ausgabe sollte eine Adresse der Form "192.168.0.110" als IPv4 Adresse erscheinen. Diese Adresse kann für den "localhost" eingesetzt werden.

#### Node-Red als Service einrichten
Damit Node-Red beim Starten des Raspberry Pi ebenfalls immer gestartet wird, muss es als Service eingerichtet werden.
Hierfür den folgenden Befehl im Terminal eingeben:
`sudo systemctl enable nodered.service`
Soll der Service deaktiviert werden, folgenden Befehl eingeben:
`sudo systemctl disable nodered.service`


#### Workshop-Flows importieren
Das Dashboard ist aktuell leer. Um das Workshop Dashboard zu verwenden, muss es importiert werden.
Hierfür im Browser die folgende url öffnen, falls das noch nicht getan wurde:
`localhost:1880` (oder die entsprechende IP anstatt localhost, wenn man an dieser Stelle einen anderen Computer verwendet)
Hier können Flow angelegt erstellt werden.
Oben links in dem Fenster befindet sich ein Symbol aus drei horizontalen Strichen. beim Anklicken öffnet sich ein Menü. Hier muss das Feld **Import** ausgewählt werden.
Beim jetzt geöffneten Fenster den Button **Datei für Import auswählen** anklicken und die Workshopflows auswählen.
Die Workshopflows sind in diesem Repository im Ordner **node_red** als Datei **flows.json** enthalten.
Hat alles funktioniert, oben Links auf den großen roten **Übernahme(deploy)** Button klicken.
Unter `localhost:1880/ui` ist jetzt das Workshop-Dashboard sichtbar.


<br>

> **_ANMERKUNG:_** Wird Thonny für diesen Workshop verwendet, kann die restliche Anleitung ignoriert werden. Sie befindet sich in den Workshopunterlagen.

## Mikrocontroller vorbereiten
Dieses Repo beinhaltet die Micropython Firmware für den Raspberry Pi Pico W. [Hier](https://micropython.org/download/rp2-pico-w/) kann überprüft werden, ob eine aktueller Version existiert.

Um die Firmware auf den Pico zu installieren, verbinde den Pico per Mikro-USB Kabel mit dem Raspberry Pi. Ist kein MicroPython installiert, sollte er als USB-Laufwerk mit den beiden Dateien "INDEX.HTM" und "INFO_UF2.TXT" erscheinen.

Falls der Mikrocontroller nicht erscheint, ist bereits eine MicroPython Version installiert und du kannst den Rest dieser Anleitung ignorieren.

    [Optional]
    Willst du die Firmware neu installieren?
    !!ACHTUNG, die folgende Anleitung löscht alle Daten auf dem Mikrocontroller!!
    Dann ziehe das Mikro-USB Kabel wieder ab.
    Halte den "BOOTSEL" Knopf auf dem Pico gedrückt und verbinde währenddessen das Mikro-USB Kabel wieder.
    Nach einigen Sekunden taucht ein neues USB Laufwerk auf.
    Der "BOOTSEL" Knopf kann wieder losgelassen werden.

Sollte keine MicroPython Firmware installiert sein, kopiere die Firmware Datei dieses repos das Laufwerk mit den beiden genannten Dateien.

Jetzt warte en paar Sekunden und \*PLOPP\* das Laufwerk sollte verschwunden sein. Der Mikrocontroller ist jetzt bereit für den Einsatz.

Benutzt du einen anderen Mikrocontroller, befolge bitte die Anleitung zu deiner Hardware auf [dieser](https://micropython.org/download/) Seite.

### Notwendige Python Packages installieren und den Mikrocontroller einrichten
Sollte auf deinem Gerät noch kein Python installiert sein, kannst du [hier](https://www.python.org/downloads/) eine für dein Betriebssystem passende Python Version herunterladen und installieren.

Für diesen Workshop wird die `ampy` Bibliothek von adafruit oder die IDE Thonny (wenn man direkt ein Raspberry Pi für die Programmierung des Pico benutzt) verwendet. Mit beiden Tools kann Code auf dem Mikrocontroller ausgeführt werden.
Die Anleitung für Thonny gibt es in den Workshopunterlagen.

Für `ampy` müssen zuerst die entsprechenden Python Packages installiert werden. Gib in der Konsole die folgenden Befehle ein.
`pip install adafruit-ampy`
`pip install esptool`

Nur noch zwei Aktionen, dann ist alles bereit.
Öffne die Datei `einstellungen.py` und Pflege hier die notwendigen Informationen zum Namen deines Mikrocontrollers, der im Netzwerk einzigartig sein sollte, der SSID, dem WLAN Passwort und der IP des Geräts, auf dem der Broker installiert ist.
Die BROKER_IP findest du heraus, indem du auf dem Raspberry Pi mit dem Broker eine Console öffnest und dort den folgenden Befehl eingibst:
`ifconfig -a`
Jetzt sollte viel Text erscheinen und irgendwo dabei die IP Adresse des Geräts stehen. Normalerweise hat sie diese oder eine ähnliche folgende Form
`192.168.1.10`
Trage diesen Wert dann als BROKER_IP ein.

Jetzt kann die `setup_microcontroller.py` Datei des Repositories ausführen. Dabei weren erst die Netzwerk und Client Informationen auf den Pico geschrieben und danach die notwendigen Pakete heruntergeladen.
`python setup_microcontroller.py`
Treten hierbei Fehler auf, überprüfe bitte,ob der `PORTNAME` in `setup_microcontroller.py` richtig ist und ob sowohl die SSID und das Passwort stimmen. Das sind die häufigsten Fehler.

Hat alles funktioniert, ist der Pico bereit für sein Leben im IoT Netzwerk :)

### Eigene Skripte ausführen
Eigene Skripte können auf dem Microcontroller auch mit `ampy` ausgeführt werden. Der Befehl `run` führt sie dabei aus, ohne die direkt auf den Microcontroller zu schreiben. Beim entfernen des USB Kabels wird das Skript unterbrochen und nicht wieder neu ausgeführt. Eigene Skripte können mit `ampy` wie folgt ausgeführt werden
`ampy --port "PORTNAME" run "SKRIPTNAME"`
Um zum Beispiel das `ding_vorlage.py` Skript des Repositories auszuführen
`ampy --port dev/ttyACM0 run ding_vorlage.py` 

#### Das wars, es kann losgehen.
Alle weiteren Anleitungsschritte befinden sich in den Workshopunterlagen.

[Downloadlink](https://nextcloud.mintorinnen.de/s/4bByDmG4WDnMAmA)
SmartSchool2024!
