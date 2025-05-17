#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QTextEdit
import json

def show_note():
    key = listwidget1.selectedItems()[0].text()
    textedit.setText(notes[key]['текст'])
    listwidget2.clear()
    listwidget2.addItems(notes[key]['тэги'])

def add_note():
    notes_name, result = QInputDialog.getText(
        winda, 'добавление заметок', 'название'
    )
    if result:
        notes[notes_name] = {
            'текст': '',
            'тэги': []
        }
        listwidget1.addItem(notes_name)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def del_note():
    if listwidget1.selectedItems():
        key = listwidget1.selectedItems()[0].text()
        del notes[key]
        listwidget1.clear()
        listwidget1.addItems(notes)
        textedit.clear()
        listwidget2.clear()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def save_note():
    if listwidget1.selectedItems():
        key = listwidget1.selectedItems()[0].text()
        notes[key]['текст'] = textedit.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)


def add_tag():
    if listwidget1.selectedItems():
        key = listwidget1.selectedItems()[0].text()
        tag = lineedit.text()
        if tag != '' and not tag in notes[key]['тэги']:
            notes[key]['тэги'].append(tag)
            listwidget2.addItem(tag)
            lineedit.clear()
            with open('notes_data.json', 'w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def del_tag():
     if listwidget2.selectedItems():
        key = listwidget1.selectedItems()[0].text()
        tag = listwidget2.selectedItems()[0].text()
        notes[key]['тэги'].remove(tag)
        listwidget2.clear()
        listwidget2.addItems(notes[key]['тэги'])
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def search_tag():
    tag = lineedit.text()
    if tag and pushbutton6.text() == 'искать заметку по тэгу':
        notes_filtered = dict()
        for key in notes:
            if tag in notes[key]['тэги']:
                notes_filtered[key] = notes[key]
        pushbutton6.setText('сброс')
        listwidget1.clear()
        textedit.clear()
        listwidget2.clear()
        listwidget1.addItems(notes_filtered)
    else:
        lineedit.clear()
        pushbutton6.setText('искать заметку по тэгу')
        listwidget1.clear()
        listwidget1.addItems(notes)


app = QApplication([])
winda = QWidget()

winda.resize(900, 600)

textedit = QTextEdit()
label1 = QLabel('список заметок')
label2 = QLabel('спиcок тэгов')
listwidget1 = QListWidget()
listwidget2 = QListWidget()
lineedit = QLineEdit()
lineedit.setPlaceholderText('Введите тег')
pushbutton1 = QPushButton('создать заметку')
pushbutton2 = QPushButton('удалить заметку')
pushbutton3 = QPushButton('сохранить заметку')
pushbutton4 = QPushButton('добавить к заметке')
pushbutton5 = QPushButton('открепить от заметки')
pushbutton6 = QPushButton('искать заметку по тэгу')
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()

v1.addWidget(textedit)
v2.addWidget(label1)
v2.addWidget(listwidget1)
h1.addWidget(pushbutton1)
h1.addWidget(pushbutton2)
v2.addLayout(h1)
v2.addWidget(pushbutton3)
v2.addWidget(label2)
v2.addWidget(listwidget2)
v2.addWidget(lineedit)
h2.addWidget(pushbutton4)
h2.addWidget(pushbutton5)
v2.addLayout(h2)
v2.addWidget(pushbutton6)
h3.addLayout(v1)
h3.addLayout(v2)

with open ('notes_data.json', 'r') as file:
    notes = json.load(file)
listwidget1.addItems(notes)
listwidget1.itemClicked.connect(show_note)
pushbutton1.clicked.connect(add_note)
pushbutton2.clicked.connect(del_note)
pushbutton3.clicked.connect(save_note)
pushbutton4.clicked.connect(add_tag)
pushbutton5.clicked.connect(del_tag)
pushbutton6.clicked.connect(search_tag)

winda.setLayout(h3)
winda.show()
app.exec()