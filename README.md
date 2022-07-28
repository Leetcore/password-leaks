# Statistik von Passwort Leaks der größten deutschen Unternehmen
Ich habe öffentliche Leaks der Top-100 der Unternehmen in Deutschland 
automatisch überprüft und daraus eine Statistik erstellt.

## Unternehmen
Airbus, Volkswagen, Mercedes Benz, BMW, Deutsche Bahn, Bosch, Siemens, Telekom 
und alle weiteren aus dieser Liste: https://de.wikipedia.org/wiki/Liste_der_gr%C3%B6%C3%9Ften_Unternehmen_in_Deutschland_(Wertsch%C3%B6pfung)

Es wurden 307.530 Passwörter dieser Unternehmen untersucht.

## Aufbau
Liste der Top-Unternehmen von Wikipedia. Filter eines 
Combo-Passwortleaks nach Domain. Zum Beispiel "@siemens.com", danach 
zähle ich die beliebtesten Passwörter und erstelle eine Statistik 
über die Zeichenlänge und Komplexität.

## Quelle
"Öffentliche Passwortleaks" bedeutet, dass sich jeder mit etwas Geschick und 
einem Torrent-Client die Leaks selbst herunterladen kann. Im Leak sind 
Passwörter im Klartext von Adobe, LinkedIn, MySpace und viele weitere... 
Es handelt sich um eine insgesamt 106 GB große entpackte Datei mit E-Mails 
und Passwörtern. Mein Rechner lief circa 30 Stunden, um 5 x per Regex durch 
die Daten zu gehen.

## Ergebnisse
Auf Platz 1 ist natürlich 123456, wie auch bei den meisten Listen über bekannte 
Passwörter. Danach wird es interessiert: Erstaunlich oft wird der Firmenname 
oder die Domain der Firma verwendet. Die Komplexeren Passwörter bestehen oft 
aus einem Ort und einer Jahreszahl mit Sonderzeichen.

## Beliebte Passwörter
```
1. 123456 (1085 Passwörter)
2. password (794 Passwörter)
3. Exigent (777 Passwörter)
4. passport (683 Passwörter)
5. 12345678 (656 Passwörter)
6. ********* (Projektname mit 443 am Ende) (582 Passwörter)
7. ********* (Firmendomain.com) (484 Passwörter)
8. dttesc (455 Passwörter)
9. aaron431 (356 Passwörter)
10. ********* (Firmendomain.com) (324 Passwörter)
11. ********* (Firmendomain.com) (318 Passwörter)
12. linkedin (283 Passwörter)
13. ********* (Firmenname) (280 Passwörter)
14. ********* (Firmenname) (190 Passwörter)
15. ********* (Firmendomain.com) (183 Passwörter)

Passwörter die ********* enthalten, musste ich zensieren, weil sich daraus 
direkt auf ein Unternehmen schließen lässt.
```

## Komplexität
Damit ich nicht einzelne Passwörter veröffentliche, zeige ich hier 
nur die Muster der "besten" Passwörter in der Liste.

```
1. Climbinging[ORT]2015
2. !!!![BLUME]2008!!!
3. [ORT]2015!1995
4. Ontherocks[ZAHL][SONDERZEICHEN]
5. [ORT]2016!!!
6. Pistol[NAME][ZAHL]][SONDERZEICHEN]
7. [NAME]]20rlovely_babes[ZAHL]
8. [PFLANZE]123!
9. [FIRMENNAME][ZAHL]_[WEBSEITE]
10. [PFLANZE]1!
```

## Weitere Passwörter

```
Password (109 Passwörter)
111111 (105 Passwörter)
adv24 (103 Passwörter)
research (96 Passwörter)
demo (94 Passwörter)
Password1 (89 Passwörter)
snowman (89 Passwörter)
sunshine (75 Passwörter)
password1 (72 Passwörter)
welcome1 (66 Passwörter)
daniel (52 Passwörter)
michelle (51 Passwörter)
abc123 (51 Passwörter)
michael (49 Passwörter)
654321 (47 Passwörter)
letmein (44 Passwörter)
london (42 Passwörter)
summer (41 Passwörter)
```