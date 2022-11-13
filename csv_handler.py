import csv
import sys
import os
import pandas as pd
from simple_term_menu import TerminalMenu


def add_record():
    event = input("Podaj Zdarzenie \r\n")
    date = input("Podaj termin \r\n")
    with open('zadania.csv', 'a', newline='') as csvfile:
        fieldnames = ['zdarzenie', 'termin']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'zdarzenie': event, 'termin': date})


def delete_record():
    name_to_delete = input("Podaj nazwe wydarzenia do usuniecia")
    df = pd.read_csv('zadania.csv')
    df = df[df.zdarzenie != name_to_delete]
    df.to_csv('zadania.csv')


def show_saved_records():
    with open('zadania.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print("Wpisy w terminarzu")
        for row in reader:
            print(row['zdarzenie'], '->', row['termin'])


if __name__ == "__main__":
    if not os.path.exists('zadania.csv'):
        with open('zadania.csv', 'w', newline='') as csvfile:
            fieldnames = ['zdarzenie', 'termin']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    with open('zadania.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print("Wpisy w terminarzu\r\n\r\n")
        for row in reader:
            print(row['zdarzenie'], '->', row['termin'])
    while 1:
        options = ["Dodaj", "Usun", "Pokaz"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            add_record()
        if menu_entry_index == 1:
            delete_record()
        if menu_entry_index == 2:
            show_saved_records()