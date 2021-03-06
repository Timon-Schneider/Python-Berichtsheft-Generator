<h1 align="center">Python Berichtsheft Generator</h1>

<p align="center">
Erstelle dein Berichtsheft in kürzester Zeit! <br><br>
Einfach Ausbildungstätigkeiten gesammelt eintragen und dieses Tool erstellt so viele Seiten eines Berichtsheftes wie du möchtest.
Die Tätigkeiten werden zufällig angeordnet automatisch in jeden Tag eingetragen.
Das Tool ist im gegensatz zu anderen alternativen sehr flexibel konfigurierbar und auf viele verschiedene Bedürfnisse anpassbar.
</p>

## Verwendung

- [HIER](https://github.com/Timon-Schneider/Python-Berichtsheft-Generator/releases/latest) unter Assets die .zip Datei herunterladen
- "Berichtsheft-Generator.exe" (unter Windows) oder "Berichtsheft-Generator" unter Ubuntu starten.
- Ausbildungstätigkeiten gesammelt mit Kommata getrennt (OHNE Leerzeichen) in die Datei „./tasks/tasks.txt“ eintragen.
Es müssen mindestens so viele Tätigkeiten eingetragen werden wie später pro Tag generiert werden sollen.
(siehe TEMPLATE und CONFIG)
- Feiertage und Urlaubstage gesammelt in die Datei „./holidays/holidays.txt“ eintragen.
WICHTIG: Pro Zeile nur EINEN Tag eintragen. Datum und Text mit Komma und OHNE Leerzeichen trennen.
BEISPIEL FORMATIERUNG: "24.12.2021,Weihnachten"
- Schultage gesammelt in die Datei „./schooldays/schooldays.txt“ eintragen.
WICHTIG: Pro Zeile nur EINEN Tag eintragen. Nur Datum eintragen, der Text wird automatisch generiert.
Der Text kann in der config Datei verändert werden (siehe CONFIG)
BEISPIEL FORMATIERUNG: "05.01.2021"
UM ZEIT ZU SPAREN KANN DAS PROGRAMM DIE SCHULTAGE FÜR EINEN ANGEGEBENEN ZEITRAUM SELBST IN DIESE DATEI SCHREIBEN
(SOWOHL FÜR WÖCHENTLICHEN UNTERRICHT ALS AUCH FÜR BLOCKUNTERRICHT)
Diese option wird kurz nach dem Start des Programmes abgefragt.
- Weitere Anweisungen im Programm befolgen...

---
## CONFIG

TemplateEntriesPerDay=8     
- (Hier wird die maximal mögliche Anzahl an später generierten Einträgen angegeben.
Die Anzahl hängt davon ab wie viele Platzhalter in der template PDF eingesetzt wurden.
(Siehe TEMPLATE))

fontname=Times-Roman
- (Name der Schriftart die beim einsetzen der generierten Einträge verwendet werden soll)

fontsize=12
- (Größe der Schriftart die beim einsetzen der generierten Einträge verwendet werden soll)

workdays=["monday", "tuesday", "wednesday", "thursday", "friday"]
- (Hier kann verändert werden an welchen Tagen das Programm die generierten
Ausbildungstätigkeiten eintragen soll.)

freedays=["saturday", "sunday"]
- (An diesen Tagen werden keine Ausbildungstätigkeiten eingetragen sodern ein
gleichbleibender Text)

FreeDaysText=Frei
- (Vorher genannter "gleichbleibender Text" für freie Tage)

schooldaysText=Berufsschule
- (Gleichbleibender Text für alle angegebenen Schultage)

---
## TEMPLATE

Unter "./template/template.pdf" kann die Vorlage für den Berichtsheft Generator verändert werden.
Wichtig ist dabei, dass immer diese Platzhalter irgendwo nach belieben eingesetzt werden:

%name

%profession

%TrainingYear

%FirstWeekday

%LastWeekday

%page

%monday1
- (es können so viele "monday" oder "tuesday" etc. eingetragen werden wie gewünscht.
hierbei ist es wichtig für jeden weiteren Eintrag die Nummer hinter dem neuen Eintrag
zu erhöhen z.B. "monday1, monday2, monday3, etc" außerdem muss danach in der config Datei
die maximale Anzahl an Einträgen pro Tag entsprechend angepasst werden)

%tuesday1

%wednesday1

%thursday1

%friday1

%saturday1

%sunday1

%hoursmonday

%hourstuesday

%hourswednesday

%hoursthursday

%hoursfriday

%hourssaturday

%hourssunday

(Diese Platzhalter wurden direkt aus dem source code kopiert. Eventuelle Schreibfehler müssen übernommen werden,
da es sonst zu Fehlern kommen könnte)

### To Do
Schaue [hier](https://github.com/Timon-Schneider/Python-Berichtsheft-Generator/issues)

Vorschläge werden gerne gesehen!

### Spenden
<a href="https://www.paypal.com/donate?hosted_button_id=ULE8THN3EAHJL" target="_blank"><img src="https://www.paypalobjects.com/de_DE/DE/i/btn/btn_donateCC_LG.gif" alt="Spenden per Paypal"></a>

(Ja, Timon Schneider = MrMampalon)

----

## License

Python Berichtsheft Generator - generator for a portfolio needed in most german apprenticeships
Copyright (C) 2021  Timon Schneider
mail@timon-schneider.net

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.