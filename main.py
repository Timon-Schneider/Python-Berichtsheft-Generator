# Python Berichtsheft Generator - generator for a portfolio needed in most german apprenticeships
# Copyright (C) 2021  Timon Schneider
# mail@timon-schneider.net
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

def main():

    import fitz
    import sys
    import configparser
    import random
    import ast
    import datetime
    from random import shuffle

    # variable "fake" initialization just because the variables can not be undefined this way..
    month = None
    StartCalendarWeek = None
    year = None
    StartCalendarYear = None
    EndCalendarYear = None
    EndCalendarWeek = None
    StartDate = None
    TrainingYearChange = None
    TrainingYear = None
    StartPage = None
    EntriesPerDayMin = None
    EntriesPerDayMax = None
    HoursPerDay = None
    taskcount = None


    def GenerateSchooldays():
        OneDay = datetime.timedelta(days=1)
        schooltype = None
        SchoolWeekday = None
        FirstSchoolday = None
        LastSchoolday = None
        again = None
        SchoolKW = None
        Schoolyear = None
        while schooltype not in ("0", "1"):
            schooltype = input("\nMöchtest du wöchendlichen Schulunterricht(0) oder Blockunterricht(1) generieren? [0/1]:")
            if schooltype in ("0", "1"):
                break
            else:
                print("Bitte 0 oder 1 eingeben")
        schooltype = int(schooltype)
        if schooltype == 0:
            while True:
                try:
                    FirstSchoolday = input("\nBitte ersten Schultag eingeben (TT.MM.JJJJ):")
                    FirstSchoolday = datetime.datetime.strptime(FirstSchoolday, "%d.%m.%Y").date()
                except ValueError:
                    print("Das eingegebene Datum ist nicht richtig formatiert! Versuche es bitte erneut.")
                    continue
                else:
                    break
            while True:
                try:
                    LastSchoolday = input("\nBitte letzten Schultag eingeben (TT.MM.JJJJ):")
                    LastSchoolday = datetime.datetime.strptime(LastSchoolday, "%d.%m.%Y").date()
                except ValueError:
                    print("Das eingegebene Datum ist nicht richtig formatiert! Versuche es bitte erneut.")
                    continue
                else:
                    break
            while SchoolWeekday not in ("1", "2", "3", "4", "5", "6", "7"):
                SchoolWeekday = input(
                    "\nAuf welchen Wochentag fällt der Schultag? Montag[1] bis Sonntag[7] [1-7]")
                if SchoolWeekday in ("1", "2", "3", "4", "5", "6", "7"):
                    break
                else:
                    print("Bitte 1 bis 7 eingeben")
            SchoolWeekday = int(SchoolWeekday)
            print("\nGeneriere...")
            try:
                schooldaysfile = open('./schooldays/schooldays.txt', 'a')
            except Exception:
                print("failed to open ./schooldays/schooldays.txt (missing or corrupted?)")
                input("Press [ENTER]: ")
                sys.exit("schooldays file read error")
            while FirstSchoolday <= LastSchoolday:
                if int(FirstSchoolday.isoweekday()) == SchoolWeekday:
                    try:
                        schooldaysfile.write(str(FirstSchoolday.strftime("%d.%m.%Y")) + "\n")
                    except Exception:
                        print("failed to write to ./schooldays/schooldays.txt (missing or corrupted?)")
                        input("Press [ENTER]: ")
                        sys.exit("schooldays file write error")
                FirstSchoolday = FirstSchoolday + OneDay
            schooldaysfile.close()
            print("\nFertig! Bitte überprüfe die Datei (./schooldays/schooldays.txt) auf Fehler und entferne Einträge die in den Ferien oder Feiertagen liegen könnten.")
            while again not in ("j", "n"):
                again = input(
                    '\nWenn du jetzt noch nicht alle Schultage eingetragen hast, könntest du den Schultag-Generator erneut starten.\n'
                    'Antworte mit "j", wenn du das tun möchtest.\n'
                    ' Wenn alle Schultage eingetragen sind antworte mit "n" um mit dem Berichtsheft-Generator fortzufahren. [j/n]')
                if again == "n":
                    break
                elif again == "j":
                    GenerateSchooldays()
                else:
                    print("Bitte j oder n eingeben")
        if schooltype == 1:
            again = "j"
            while again == "j":
                again = None
                while True:
                    try:
                        SchoolKW = input("\nBitte Kalenderwoche und Jahr eingeben (KW.JJJJ):")
                        SchoolKW, Schoolyear = map(int, str(SchoolKW).split('.'))
                    except ValueError:
                        print("Das eingegebene Datum ist nicht richtig formatiert! Versuche es bitte erneut.")
                        continue
                    else:
                        break
                FirstDayInSchoolKW = datetime.datetime.strptime(f'{Schoolyear}-{SchoolKW}-1', "%G-%V-%w").date()
                LastDayInSchoolKW = datetime.datetime.strptime(f'{Schoolyear}-{SchoolKW}-5', "%G-%V-%w").date()
                print("\nGeneriere...")
                try:
                    schooldaysfile = open('./schooldays/schooldays.txt', 'a')
                except Exception:
                    print("failed to open ./schooldays/schooldays.txt (missing or corrupted?)")
                    input("Press [ENTER]: ")
                    sys.exit("schooldays file read error")
                while FirstDayInSchoolKW <= LastDayInSchoolKW:
                    try:
                        schooldaysfile.write(str(FirstDayInSchoolKW.strftime("%d.%m.%Y")) + "\n")
                    except Exception:
                        print("failed to write to ./schooldays/schooldays.txt (missing or corrupted?)")
                        input("Press [ENTER]: ")
                        sys.exit("schooldays file write error")
                    FirstDayInSchoolKW = FirstDayInSchoolKW + OneDay
                schooldaysfile.close()
                print("\nFertig!")
                while again not in ("j", "n"):
                    again = input(
                        "\nWeiteren Block generieren? [j/n]")
                    if again in ("j", "n"):
                        break
                    else:
                        print("Bitte j oder n eingeben")
            print(
                "\nBitte überprüfe die Datei (./schooldays/schooldays.txt) auf Fehler und entferne Einträge die in den Ferien oder Feiertagen liegen könnten.")
            again = None
            while again not in ("j", "n"):
                again = input(
                    '\nWenn du jetzt noch nicht alle Schultage eingetragen hast, könntest du den Schultag-Generator erneut starten.\n'
                    'Antworte mit "j", wenn du das tun möchtest.\n'
                    ' Wenn alle Schultage eingetragen sind antworte mit "n" um mit dem Berichtsheft-Generator fortzufahren. [j/n]')
                if again == "n":
                    break
                elif again == "j":
                    GenerateSchooldays()
                else:
                    print("Bitte j oder n eingeben")

    with open("copyright_text", "r") as copyright_file:
        for i in range(16):
            line = next(copyright_file).strip()
            print(line)

    config = configparser.ConfigParser()
    try:
        config.read('./config/config.txt')
    except Exception:
        print("failed to open ./config/config.txt (missing or corrupted?)")
        input("Press [ENTER]: ")
        sys.exit("config file read error")

    try:
        fontname = config.get('config', 'fontname')
        fontsize = int(config.get('config', 'fontsize'))
        TemplateEntriesPerDay = int(config.get('config', 'TemplateEntriesPerDay'))
        workdays = config.get('config', 'workdays')
        freedays = config.get('config', 'freedays')
        FreeDaysText = config.get('config', 'FreeDaysText')
        workdays = ast.literal_eval(workdays)
        freedays = ast.literal_eval(freedays)
        schooldaysText = config.get('config', 'schooldaysText')
    except Exception:
        print("wrong or missing entries in config file")
        input("Press [ENTER]: ")
        sys.exit("config content error")

    if int(len(workdays) + len(freedays)) != 7:
        print("wrong or missing workdays/freedays")
        input("Press [ENTER]: ")
        raise Exception('workdays/freedays error')

    file = "./template/template.pdf"
    try:
        fitzpdf = fitz.Document(file)
    except Exception:
        print("failed to open ./template/template.pdf (missing or corrupted?)")
        input("Press [ENTER]: ")
        sys.exit("template file read error")

    print('\n\nFür die korrekte Funktionsweise dieses Programmes ist es zwingend erforderlich, dass die Datei "./tasks/tasks.txt" mindestens acht persönliche Ausbildungstätigkeiten enthält. \nZur Überprüfung der Formatierung sind mehrere Einträge als Beispiel vorgegeben. Löschen Sie diese und tragen Sie in gleicher Form Ihre Eigenen ein.')
    input("Mit [ENTER] bestätigen: ")

    try:
        with open('./tasks/tasks.txt', 'r') as tasksfile:
            tasks = tasksfile.read()
    except Exception:
        print("failed to open ./tasks/tasks.txt (missing or corrupted?)")
        input("Press [ENTER]: ")
        sys.exit("tasks file read error")

    try:
        tasks = tasks.encode('iso8859-1').decode('utf-8').replace('\n', '').split(',')
    except:
        tasks = tasks.replace('\n', '').split(',')

    print('\n\nFür die korrekte Funktionsweise dieses Programmes ist es zwingend erforderlich, dass die Datei "./holidays/holidays.txt" die zu berücksichtigenden Urlaubstage und Feiertage enthält. \nZur Überprüfung der Formatierung sind mehrere Einträge als Beispiel vorgegeben. Löschen Sie diese und tragen Sie in gleicher Form Ihre Eigenen ein.')
    input("Mit [ENTER] bestätigen: ")

    try:
        with open('./holidays/holidays.txt', 'r') as holidaysfile:
            holidays = holidaysfile.read().replace('\n', ',').split(',')
            holidays[:] = [x for x in holidays if x]
            # print(holidays)
    except Exception:
        print("failed to open ./holidays/holidays.txt (missing or corrupted?)")
        input("Press [ENTER]: ")
        sys.exit("holidays file read error")

    holidaysDates = holidays[::2]
    holidaysText = holidays[1::2]

    print('\n\nFür die korrekte Funktionsweise dieses Programmes ist es zwingend erforderlich, dass die Datei "./schooldays/schooldays.txt" die zu berücksichtigenden Schultage enthält. \nZur Überprüfung der Formatierung sind mehrere Einträge als Beispiel vorgegeben. Löschen Sie diese und tragen Sie in gleicher Form Ihre Eigenen ein.')
    GenStart = None
    while GenStart not in ("j", "n"):
        GenStart = input(
            '\nUM ZEIT ZU SPAREN KANN DIESES PROGRAMM DIE SCHULTAGE FÜR EINEN ANGEGEBENEN ZEITRAUM SELBST IN DIESE DATEI SCHREIBEN (SOWOHL FÜR WÖCHENTLICHEN UNTERRICHT ALS AUCH FÜR BLOCKUNTERRICHT). \nSOLL DAS PROGRAMM DIES ÜBERNEHMEN? [j/n]:')
        if GenStart == "n":
            break
        elif GenStart == "j":
            GenerateSchooldays()
        else:
            print("Bitte j oder n eingeben")

    try:
        with open('./schooldays/schooldays.txt', 'r') as schooldaysfile:
            schooldays = schooldaysfile.read().replace('\n', ',').split(',')
            schooldays[:] = [x for x in schooldays if x]
            # print(holidays)
    except Exception:
        print("failed to open ./schooldays/schooldays.txt (missing or corrupted?)")
        input("Press [ENTER]: ")
        sys.exit("schooldays file read error")

    holidaysDates.extend(schooldays)
    for s in schooldays:
        holidaysText.append(schooldaysText)
    holidaysDates.append('1')

    try:
        forename = input("\nBitte Vornamen eingeben:")
        surname = input("\nBitte Nachnamen eingeben:")
        profession = input("\nBitte Ausbildungsberuf eingeben:")
    except Exception:
        print("I dont know how you managed to create this error")
        input("Press [ENTER]: ")
        sys.exit("name and profession string error")

    while True:
        try:
            StartDate = input("\nBitte Datum des ersten Eintrages eingeben (TT.MM.JJJJ):")
            StartDate = datetime.datetime.strptime(StartDate, "%d.%m.%Y").date()
            # print (StartDate)
            year, month, day = map(int, str(StartDate).split('-'))
            StartCalendarWeek = int(datetime.date(year, month, day).strftime("%V"))
            StartCalendarYear = year
            # print(StartCalendarWeek)
            # print(StartCalendarYear)
        except ValueError:
            print("Das eingegebene Datum ist nicht richtig formatiert! Versuche es bitte erneut.")
            continue
        else:
            break

    if month == 1 and StartCalendarWeek > 10:
        StartCalendarYear = year - 1
    FirstDayInStartWeek = datetime.datetime.strptime(f'{StartCalendarYear}-{StartCalendarWeek}-1', "%G-%V-%w").date()
    LastDayInStartWeek = datetime.datetime.strptime(f'{StartCalendarYear}-{StartCalendarWeek}-0', "%G-%V-%w").date()
    # print (FirstDayInStartWeek)
    # print (LastDayInStartWeek)
    OneWeek = datetime.timedelta(weeks=1)
    # FirstDayInStartWeek = FirstDayInStartWeek + OneWeek
    # LastDayInStartWeek = LastDayInStartWeek + OneWeek
    # print (FirstDayInStartWeek)
    # print (LastDayInStartWeek)

    while True:
        try:
            EndDate = input("\nBitte Datum des letzten Eintrages eingeben (TT.MM.JJJJ):")
            EndDate = datetime.datetime.strptime(EndDate, "%d.%m.%Y").date()
            # print (EndDate)
            year, month, day = map(int, str(EndDate).split('-'))
            EndCalendarWeek = int(datetime.date(year, month, day).strftime("%V"))
            EndCalendarYear = year
            # print(EndCalendarWeek)
            if month == 1 and EndCalendarWeek > 10:
                EndCalendarYear = year - 1
            # print(EndCalendarYear)
        except ValueError:
            print("Das eingegebene Datum ist nicht richtig formatiert! Versuche es bitte erneut.")
            continue
        else:
            break

    FirstDayInEndWeek = datetime.datetime.strptime(f'{EndCalendarYear}-{EndCalendarWeek}-1', "%G-%V-%w").date()
    LastDayInEndWeek = datetime.datetime.strptime(f'{EndCalendarYear}-{EndCalendarWeek}-0', "%G-%V-%w").date()
    # print (FirstDayInEndWeek)
    # print (LastDayInEndWeek)
    # OneWeek = datetime.timedelta(weeks=1)
    # FirstDayInEndWeek = FirstDayInEndWeek + OneWeek
    # LastDayInEndWeek = LastDayInEndWeek + OneWeek
    # print (FirstDayInEndWeek)
    # print (LastDayInEndWeek)

    DateDifference = LastDayInEndWeek - FirstDayInStartWeek
    OneDay = datetime.timedelta(days=1)
    DateDifference = DateDifference + OneDay
    DateDifference = int(DateDifference.days)
    DateDifference = int(DateDifference / 7)
    # print (DateDifference)

    for weeks in range(DateDifference):
        fitzpdf.fullcopyPage(0, -1)

    while True:
        try:
            TrainingYear = int(input("\nIn welchem Ausbildungsjahr befinden Sie sich am " + str(StartDate.strftime("%d.%m.%Y")) + "?:"))
        except ValueError:
            print("Keine ganze Zahl. Versuche es bitte erneut.")
            continue
        else:
            break

    while True:
        try:
            TrainingYearChange = int(input('\nBitte den Monat des Wechsels in das nächste Ausbildungsjahr angeben \nBsp.: "08" \n(auch angeben wenn '
                                 'der Wechsel nicht im vorher angegebenen Zeitraum liegt)\n:'))
            if TrainingYearChange > 12:
                print("Es gibt nicht mehr als 12 Monate. Bitte versuche es erneut")
                continue
        except ValueError:
            print("Keine ganze Zahl. Versuche es bitte erneut.")
            continue
        else:
            break

    while True:
        try:
            StartPage = int(input("\nBitte Seitenzahl der ersten Seite angeben:"))
        except ValueError:
            print("Keine ganze Zahl. Versuche es bitte erneut.")
            continue
        else:
            break

    while True:
        try:
            EntriesPerDayMin = int(input("\nBitte Minimale Anzahl der Einträge pro Tag angeben \n(7 sieht bei der standard Vorlage am besten aus):"))
            if EntriesPerDayMin > TemplateEntriesPerDay:
                print("Die Zahl überschreitet die maximal mögliche Anzahl an Einträgen (siehe CONFIG und TEMPLATE)")
                continue
        except ValueError:
            print("Keine ganze Zahl. Versuche es bitte erneut.")
            continue
        else:
            break

    while True:
        try:
            EntriesPerDayMax = int(input("\nBitte Maximale Anzahl der Einträge pro Tag angeben \n(8 sieht bei der standard Vorlage am besten aus):"))
            if EntriesPerDayMax > TemplateEntriesPerDay:
                print("Die Zahl überschreitet die maximal mögliche Anzahl an Einträgen (siehe CONFIG und TEMPLATE)")
                continue
        except ValueError:
            print("Keine ganze Zahl. Versuche es bitte erneut.")
            continue
        else:
            break

    while True:
        try:
            HoursPerDay = int(input("\nBitte die Arbeitsstunden pro Tag angeben:"))
        except ValueError:
            print("Keine ganze Zahl. Versuche es bitte erneut.")
            continue
        else:
            break

    nummer = 0

    page = fitzpdf[nummer]

    def FindTextAndReplace(text, text_replace, fontname_to_use, fontsize_to_use):
        text_instances = page.searchFor(text)
        for inst in text_instances:
            text_replace = str(text_replace)
            # print(text_replace)
            page.addRedactAnnot(inst, fill=False)
            page.apply_redactions()
            point = inst.bottom_left
            # print(point)
            # print("<----------------------------------------->")
            rc = page.insertText(point, text_replace,
                                 fontsize=fontsize_to_use,
                                 fontname=fontname_to_use, )

    def FindTextAndDelete(text):
        text_instances = page.searchFor(text)
        for inst in text_instances:
            # print(inst)
            page.addRedactAnnot(inst, fill=False)
            page.apply_redactions()

    holidaysCount = 0
    SixDays = datetime.timedelta(days=6)
    FirstWeekday = FirstDayInStartWeek
    LastWeekday = FirstDayInStartWeek + SixDays
    CheckTrainingYearChange1 = int(datetime.date(int(FirstWeekday.year), int(TrainingYearChange), 1).strftime("%V"))
    CheckTrainingYearChange2 = int(datetime.date(int(FirstWeekday.year), int(FirstWeekday.month), int(FirstWeekday.day)).strftime("%V"))
    if CheckTrainingYearChange1 == CheckTrainingYearChange2:
        TrainingYear -= 1

    for weeks in range(DateDifference):
        print("Verarbeite Seite " + str(StartPage))
        CheckTrainingYearChange1 = int(datetime.date(int(FirstWeekday.year), int(TrainingYearChange), 1).strftime("%V"))
        CheckTrainingYearChange2 = int(datetime.date(int(FirstWeekday.year), int(FirstWeekday.month), int(FirstWeekday.day)).strftime("%V"))
        if CheckTrainingYearChange1 == CheckTrainingYearChange2:
            TrainingYear += 1
        FindTextAndReplace("%profession", profession, fontname, fontsize)
        FindTextAndReplace("%TrainingYear", TrainingYear, fontname, fontsize)
        ForeAndSurname = forename + " " + surname
        FindTextAndReplace("%name", ForeAndSurname, fontname, fontsize)
        FindTextAndReplace("%page", StartPage, fontname, fontsize)
        StartPage += 1
        text_replace_FirstWeekday = str(str(FirstWeekday.day) + "." + str(FirstWeekday.month) + "." + str(FirstWeekday.year))
        FindTextAndReplace("%FirstWeekday", text_replace_FirstWeekday, fontname, fontsize)
        FirstWeekday = FirstWeekday + OneWeek
        text_replace_LastWeekday = str(str(LastWeekday.day) + "." + str(LastWeekday.month) + "." + str(LastWeekday.year))
        FindTextAndReplace("%LastWeekday", text_replace_LastWeekday, fontname, fontsize)
        LastWeekday = LastWeekday + OneWeek

        for workday in workdays:
            taskcount = 0
            shuffle(tasks)
            EntriesPerDayRand = random.randint(EntriesPerDayMin, EntriesPerDayMax)

            # print (workday)
            # holidaysDatesStripped = int(holidaysDates[holidaysCount].replace('.', ''))
            # FirstDayInStartWeekStripped = int(FirstDayInStartWeek.strftime("%d%m%Y"))
            for h in holidaysDates:
                if int(FirstDayInStartWeek.strftime("%d%m%Y")) == int(holidaysDates[holidaysCount].replace('.', '')):
                    FindText = "%hours" + workday
                    FindTextAndDelete(FindText)
                    for x in range(1):
                        EntryCount = x + 1
                        FindText = "%" + workday + str(EntryCount)
                        FindTextAndReplace(FindText, holidaysText[holidaysCount], fontname, fontsize)
                        taskcount += 1
                    for x in range(TemplateEntriesPerDay):
                        EntryCount = x + 1
                        FindText = "%" + workday + str(EntryCount)
                        FindTextAndDelete(FindText)
                holidaysCount += 1
            holidaysCount = 0
            taskcount = 0
            FirstDayInStartWeek = FirstDayInStartWeek + OneDay
            FindText = "%hours" + workday
            FindTextAndReplace(FindText, HoursPerDay, fontname, fontsize)
            for x in range(EntriesPerDayRand):
                EntryCount = x+1
                FindText = "%" + workday + str(EntryCount)
                FindTextAndReplace(FindText, tasks[taskcount], fontname, fontsize)
                taskcount += 1

            for x in range(TemplateEntriesPerDay):
                EntryCount = x+1
                FindText = "%" + workday + str(EntryCount)
                FindTextAndDelete(FindText)

        for freeday in freedays:
            # print (freeday)
            FindText = "%hours" + freeday
            FindTextAndDelete(FindText)
            # holidaysDatesStripped = int(holidaysDates[holidaysCount].replace('.', ''))
            # FirstDayInStartWeekStripped = int(FirstDayInStartWeek.strftime("%d%m%Y"))
            for h in holidaysDates:
                if int(FirstDayInStartWeek.strftime("%d%m%Y")) == int(holidaysDates[holidaysCount].replace('.', '')):
                    FindText = "%hours" + freeday
                    FindTextAndDelete(FindText)
                    for x in range(1):
                        EntryCount = x + 1
                        FindText = "%" + freeday + str(EntryCount)
                        FindTextAndReplace(FindText, holidaysText[holidaysCount], fontname, fontsize)
                        taskcount += 1
                    for x in range(TemplateEntriesPerDay):
                        EntryCount = x + 1
                        FindText = "%" + freeday + str(EntryCount)
                        FindTextAndDelete(FindText)
                holidaysCount += 1
            holidaysCount = 0
            taskcount = 0
            FirstDayInStartWeek = FirstDayInStartWeek + OneDay

            for x in range(1):
                EntryCount = x+1
                FindText = "%" + freeday + str(EntryCount)
                FindTextAndReplace(FindText, FreeDaysText, fontname, fontsize)

            for x in range(TemplateEntriesPerDay):
                EntryCount = x+1
                FindText = "%" + freeday + str(EntryCount)
                FindTextAndDelete(FindText)
        nummer += 1
        page = fitzpdf[nummer]

    fitzpdf.deletePage()
    fitzpdf.save("Berichtsheft.pdf", garbage=4, deflate=True, clean=True)
    print('\nFertig! Das Berichtsheft wurde mit dem Namen "Berichtsheft.pdf" gespeichert!')
