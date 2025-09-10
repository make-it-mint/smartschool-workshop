# SmartSchool Workshop - Einführung IoT mit MQTT in Python und MicroPython

Dieses Repository beinhaltet den Programmcode für den SmartSchool Workshop

## Notwendige Hardware:
- Broker: Raspberry Pi 3B+/4B/400 mit Raspbian Bullseye
- Clients: Raspberry Pi Pico W oder andere WLAN-fähige Mikrocontroller, auf denen MicroPython installiert werden kann.([Übersicht](https://micropython.org/download/))
- Steckplatinen, Sensoren, Aktuatoren und weitere Bauteile für ausgewählte Clientfunktionen

## Entwicklungsumgebung:
In diesem Workshop wird die Online IDE Viper genutzt. https://viper-ide.org/# (Funktioniert nicht in Firefox)

## Optionale Software:
- MyMQTT: Eine App zum Verbinden mit MQTT Brokern für Android & iOS. Kann zum Testen verwendet werden, alternativ kann auch eine Webseite wie [MQTT.Cool](https://testclient-cloud.mqtt.cool/) oder ein zweites IoT Gerät verwendet werden.
- Mosquitto (Installationsanleitung weiter unten): ein OpenSource MQTT Broker, der lokal installiert und betrieben werden kann
- node-red (Installationsanleitung weiter unten): eine Low-Code Entwicklungsumgebung. Programmieren mit Flows und Erstellung eines Online-Dashboards
- die Viper IDE kann auch lokal gebaut und auf einem eigenen Server gehostet werden (https://github.com/vshymanskyy/ViperIDE)

Für den Broker wird hier eine Raspberry Pi 4B, mit Raspbian Bullseye installiert, verwendet.  
Willst du keinen eigenen Broker einichten, kann auch ein öffentlicher Broker verwendet werden, wie ihn beispielsweise HiveMQ [hier](https://www.hivemq.com/public-mqtt-broker/) zur Verfügung stellt. Über Datenschutzrichtlinien im Vorfeld bitte selbst informieren.

## Mikrocontroller - Firmware installieren
Dieses Repo beinhaltet die Micropython Firmware für den Raspberry Pi Pico W. [Hier](https://micropython.org/download/rp2-pico-w/) kann überprüft werden, ob eine aktueller Version existiert.

Um die Firmware auf den Pico zu installieren, verbinde den Pico per Mikro-USB Kabel mit dem Raspberry Pi. Ist kein MicroPython installiert, sollte er als USB-Laufwerk mit den beiden Dateien "INDEX.HTM" und "INFO_UF2.TXT" erscheinen.

Falls der Mikrocontroller nicht erscheint, ist bereits eine MicroPython Version installiert und du kannst den Rest dieser Anleitung ignorieren.

    [Optional]
    Willst du die Firmware neu installieren?
    Das kannst du machen, ohne die Dateien auf deinem Mikrocontroller zu löschen.  
    - Ziehe das Mikro-USB Kabel wieder ab.
    - Halte den "BOOTSEL" Knopf auf dem Pico W gedrückt und verbinde währenddessen das Mikro-USB Kabel wieder.
    - Nach einigen Sekunden taucht der Mikrocontroller als USB Laufwerk auf.
    - Der "BOOTSEL" Knopf kann wieder losgelassen werden.
    - Folge dem Leitfaden weiter.

Sollte keine MicroPython Firmware installiert sein, kopiere die Firmware Datei dieses repos das Laufwerk mit den beiden genannten Dateien.

Jetzt warte en paar Sekunden und **_plopp_**, das Laufwerk sollte verschwunden sein. Der Mikrocontroller ist jetzt bereit für den Einsatz.

Benutzt du einen anderen Mikrocontroller, befolge bitte die Anleitung zu deiner Hardware auf [dieser](https://micropython.org/download/) Seite.

## Mikrocontroller - Verbinden in Viper

Verbinde den Mikrocontroller mit dem Computer und klicke oben rechts in der Viper IDE auf das USB Symbol. Wähle aus der Liste, die sich öffnet den Mikrocontroller aus. Auf der linken Seite sollte nun ein Menü mit deinen Dateien erscheinen.

## Code auf dem Mikrocontroller kopieren
- Erstelle die folgenden Dateien und kopiere die Inhalte aus den gleichnamigen Dateien diese Repositories in die Dateien:
  - `iot_settings.py` -> Python Datei mit persönlichen Einstellungen
  - `Thing.py` -> Python Datei, die die Verbdindung mit einem Broker und dem Internet automatisch übernimmt
  - `things_collection.py` -> [Optional] beinhaltet Beispielprogramme und benötigt noch die folgenden in diesem Repository beinhalteten Bibliotheken, die genauso erstellt werden müssen:
    - `mfrc522.py`


- Erstelle im File Manager Menü den Ordner `umqtt` 
  - innerhalb des Ordners die folgenden Dateien und kopiere die Inhalte aus den gleichnamigen Dateien diese Repositories in die Dateien:
  - `simple.py` -> MQTT Bibliothek
  - `robust.py`  -> MQTT Bibliothek


Damit ist der Mikrocontroller für den Workshop vorbereitet.



## [Optional] Installation des Brokers (RPi 4B)
Die Installationsanleitung basiert auf einem Tutorial der Website [pimylifeup.com](https://pimylifeup.com/raspberry-pi-mosquitto-mqtt-server/)

Öffne ein Terminal und aktualisiere die verfügbaren Pakete  
`sudo apt update`

Installiere Broker und Client  
`sudo apt install mosquitto mosquitto-clients`

Der Broker ermöglicht standardmäßig keine Kommunikation nach Außen. Um dies zu ermöglichen muss die Konfigurationsdatei des Broker angepasst werden.

Öffne die Konfigurationsdatei  
`sudo nano /etc/mosquitto/mosquitto.conf`

und füge die folgenden Zeilen am Ende der Datei ein  
```
listener 1883
allow_anonymous true
```
Drücke STRG + O -> Enter -> STRG + X zum Speichern und Schließen der Datei.

Diese Zeilen legen fest, dass der Broker über Port 1883 mit externen Geräten kommuniziert und auch Geräte ohne Namen zulässt. (Für diesen Workshop notwendig)

Prüfe ob der Broker aktiv ist indem du den folgenden Befehl in der Konsole eingibst  
`sudo systemctl status mosquitto.service`  
Es sollte ein grünes "(is running)" und weiterer Text angezeigt werden.

Der Broker ist einsatzbereit.

## [Optional] Installation von Node-Red auf dem Server (4B)

Node-Red wird in diesem Workshop verwendet, um ein Dashboard der "Dinge" über das Netzwerk bereitzustellen. Es wird auf dem gleichen Gerät installiert, wie der MQTT Broker.
Node-Red stellt einen Installationswizard  und umfangreiches Infomaterial zur Verfügung, die [hier](https://nodered.org/docs/getting-started/raspberrypi) gefunden werden können.

Öffne ein Terminal und führe die folgende Zeile aus:  
`bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)`

Die installation wird ein paar Minuten in Anspruch nehmen und du wirst aufgefordert einige Einstellung vorzunehmen.

Sobald sie abgeschlossen ist, muss noch die "Dashboard" Erweiterung installiert werden, damit die Elemente zur Erstellung grafischer Oberflächen verfügbar sind. Im Terminal folgenden Befehl ausführen:  
`npm install node-red-dashboard`

Im Browser kann jetzt sowohl das Interface zum Erstellen von Workflows, als auch das Dashboard geöffnet werden. Node-Red verwendet standardmäßig Port 1880.
Öffne einen Browser und gib die folgende url ein:

http://localhost:1880      <- Entwicklungsumgebung für Flows  
http://localhost:1880/ui      <- Webseite mit dem Dashboard

#### Server von Netzwerkgeräten erreichen
Um diese Seiten von einem anderen Gerät im Netzerk zu erreichen muss die IP-Adresse des Servers ermittelt und für "localhost" ersetzt werden.

Die IP-Adresse des Servers kann durch Eingabe des folgenden Befehls in das Terminal auf dem Raspberry Pi ermittelt werden:  
`ifconfig -a`  
In der Ausgabe sollte eine Adresse der Form "192.168.0.110" als IPv4 Adresse erscheinen. Diese Adresse kann für den "localhost" eingesetzt werden.  
Beispiel: http://192.168.0.110:1880

#### Node-Red als Service einrichten
Damit Node-Red beim Starten des Raspberry Pi ebenfalls immer gestartet wird, muss es als Service eingerichtet werden.
Hierfür den folgenden Befehl im Terminal eingeben:  
`sudo systemctl enable nodered.service`  
Soll der Service deaktiviert werden, folgenden Befehl eingeben:  
`sudo systemctl disable nodered.service`


#### Entwicklungsumgebung aufrufen


Hier können Flow angelegt erstellt werden.
Oben links in dem Fenster befindet sich ein Symbol aus drei horizontalen Strichen.  
- Beim Anklicken öffnet sich ein Menü. Hier muss das Feld **Import** ausgewählt werden.  
- Beim jetzt geöffneten Fenster den Button **Datei für Import auswählen** anklicken und die Workshopflows auswählen.
- Die Workshopflows sind in diesem Repository im Ordner **node_red** als Datei **flows.json** enthalten.
- Hat alles funktioniert, oben Links auf den großen roten **Übernahme(deploy)** Button klicken.
- Unter `localhost:1880/ui` ist jetzt das Workshop-Dashboard sichtbar.


## Workshopunterlagen
Alle weiteren Anleitungsschritte befinden sich in den Workshopunterlagen.

[Downloadlink](https://nextcloud.mintorinnen.de/s/4bByDmG4WDnMAmA)  
SmartSchool2024!
