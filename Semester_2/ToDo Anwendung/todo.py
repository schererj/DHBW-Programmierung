# encoding=utf-8



'''

Implementierung einer einfachen ToDo Liste mit Objektorientierung

'''
pathtonotes = "./data/todo.tasks"


# Datei auslesen
def read_data_from_file(path):
    f = open(path)
    tasks = []
    for lines in f:
        tasks.append(lines.rstrip().split(";"))
    return tasks


# Datei schreiben
def write_data(path, tasks, append):
    # Zeilenweise schreiben
    if append == True:
        f = open(path, 'a')
    else:
        # ersetzen
        f = open(path, 'w')
    task = ""
    for t in tasks:
        print(t)
        task += t[0] + ";" + t[1] + "\n"
    f.write(task)
    f.close()


# Tabelle ausgeben

def print_data(data):
    print("NR\tTermin \t \t Aufgabe")
    print("_______________________________________")
    for i in range(len(data)):
        print(str(i) + "\t" + data[i][0] + "\t" + data[i][1])
        print("_______________________________________")


# Datenreihe löschen
def delete_data(id):
    data = read_data_from_file(pathtonotes)
    data.remove(data[id])
    write_data(pathtonotes, data, False)

def edit_task(id):
    data = read_data_from_file(pathtonotes)
    taskname = str(raw_input("Bitte neue Tätigkeit angeben: "))
    taskdate = str(raw_input("Bitte neues Datum angeben: "))
    data[id] = [taskdate, taskname]
    write_data(pathtonotes, data, False)


# Menüpunkt hinzufügen
def write_new_task():
    taskname = str(raw_input("Bitte Tätigkeit angeben: "))
    taskdate = str(raw_input("Bitte Datum angeben: "))
    payload = [taskdate, taskname]
    data = [payload]
    write_data(pathtonotes, data, True)

def edit_existing_task():
    print_data(read_data_from_file(pathtonotes))
    taskedit = int(raw_input("Bitte ID angeben: "))
    edit_task(taskedit)

# Menüpunkt löschen
def delete_task():
    print_data(read_data_from_file(pathtonotes))
    taskdel = int(raw_input("Bitte ID angeben: "))
    delete_data(taskdel)


# Hauptfunktion
def main_function():
    while True:

        userinput = str(raw_input("Neu Notiz hinzufügen (n), Notiz löschen (l), Programm beenden (q), Notiz bearbeiten (b): "))
        userinput = userinput.lower()
        if userinput == "q":
            exit()
        elif userinput == "n":
            write_new_task()
        elif userinput == "l":
            delete_task()
        elif userinput == "b":
            edit_existing_task()
        else:
            print("Bitte korrekten Wert angeben!")

        print_data(read_data_from_file(pathtonotes))


main_function()
