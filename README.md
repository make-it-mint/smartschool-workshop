# SmartSchool Workshop - Einführung IoT mit MQTT in Python und MicroPython

Dieses Repository beinhaltet den Programmcode für den Workshop "Einführung IoT mit MQTT" von MAKE IT MINT.

## Notwendige Hardware:
- Broker: Raspberry Pi 3B+/4B/400 mit Raspbian Bullseye
- Clients: Raspberry Pi Pico W oder andere WLAN-fähige Mikrocontroller, auf denen MicroPython installiert werden kann.([Übersicht](https://micropython.org/download/))
- Steckplatinen, Sensoren, Aktuatoren und weitere Bauteile für ausgewählte Clientfunktionen

## Notwendige Software:
- [Thonny](https://thonny.org/): Eine Python Entwicklungsumgebung. Gibt es für Windows als portable Version(ohne Installation) und für Windows, Linux und Mac zum Installieren

## Optionale Software:
- MyMQTT: Eine App zum Verbinden mit MQTT Brokern für Android & iOS. Kann zum Testen verwendet werden, alternativ kann auch eine Webseite wie [MQTT.Cool](https://testclient-cloud.mqtt.cool/) oder ein zweites IoT Gerät verwendet werden.
- Mosquitto (Installationsanleitung weiter unten): ein OpenSource MQTT Broker, der lokal installiert und betrieben werden kann
- node-red (Installationsanleitung weiter unten): eine Low-Code Entwicklungsumgebung. Programmieren mit Flows und Erstellung eines Online-Dashboards

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

## Mikrocontroller - Verbinden in Thonny

Auf den Mikrocontrollern müssen ein paar Skripte kopiert werden, damit sie für den Workshop nutzbar sind. Das muss einmalig für jeden Mikrocontroller gemacht werden. Dafür wird die Thonny Entwicklungsumgebung benötigt. Thonny hat den großen Vorteil, dass man mit ihr direkt auf dem Mikrocontroller programmieren kann. Es muss keine weitere Software hierfür installiert werden. Der Mikrocontroller mit MicroPython muss lediglich per USB Kabel an den Computer angeschlossen werden.

Ist Thonny geöffnet und der Mikrocontroller verbunden, klicke mit der linken Maustaste unten rechts in Thonny auf das Feld mit dem Text "Lokales Python 3". Der Text steht wirklichganz unten rechts auf grauem Untergrund. Wird er angeklickt, öffnet sich ein Menü mit mehreren Optionen zur Auswahl. Wähle die Option mit "MicroPython" aus. Sind mehrere verfügbar, wähle die oerste, es ist aber eigentlich egal.

In der Konsole sollte jetzt der folgende Text angezeigt werden:  
```
MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> 
```
Siehst du diesen Text nicht, oder kannst kein MicroPython Gerät in Thonny auswählen, wird dein Mikrocontroller nicht erkannt. Versuche noch einmal die Firmware neu zu installieren.

## Code auf dem Mikrocontroller kopieren
 Öffne alle Dateien des "microcontroller-files" Ordners in Thonny. Dabei sollte es sich um die folgenden Dateien handeln:  
 - `umqtt/simple.py` -> MQTT Bibliothek
 - `umqtt/robust.py`  -> MQTT Bibliothek
 - `iot_settings.py` -> Python Datei mit persönlichen Einstellungen
 - `Thing.py` -> Python Datei, die die Verbdindung mit einem Broker und dem Internet automatisch übernimmt

Sind die Dateien in Thonny geöffnet, können sie durch die "Speichern unter" Funktion direkt auf dem Mikrocontroller gespeichert werden.

- Wähle die Datei `umqtt/simple.py` aus.
- Zum Speichern auf dem Mikrocontroller, Wähle in Thonny oben "Datei" aus und dann "Speichern unter".
- Jetzt kannst du in einem Fenster "Dieser Computer" oder "RP2040 Gerät" auswählen. "RP2040" ist dein Mikrocontroller. Wähle ihn aus.
- Es öffnet sich ein neues Menü. Das ist der Speicher deines Mikrocontrollers. Die Dateien `simple.py` und `robust.py` müssen in einem Ordner mit dem Namen `umqtt` gespeichert werden
- Um in dem Menü einen neuen Ordner anzulegen, klicke mit der rechten Maustaste in den weißen Fensterbereich.
- Wähle "neuer Ordner" aus und erstelle einen Ordner mit dem Namen `umqtt` 
- Doppelklicke nun mit der linken Maustaste auf den Ordner und speichere die Datei in ihm. gib ihr den Namen `simple.py`

Speichere die `umqtt/robust.py` Datei ebenfalls in dem Ordner.

Die `iot_settings.py` und `Thing.py` Datei werden direkt im Hauptordner gespeichert.

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
