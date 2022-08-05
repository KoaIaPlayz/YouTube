
import PySimpleGUI as sg

import pyperclip
import webbrowser


def create(detectedCodeList,headings):
    code_detected_table_window_layout = [
        [sg.Table(values=detectedCodeList, headings= headings, auto_size_columns=True, justification="center",
                max_col_width=500,
                enable_events=True, key='OUTPUT'),sg.InputText("", use_readonly_for_disable=True, disabled=True, key='CODE_STRING'),sg.Button("Copy"),sg.Button("Redeem")],
    ]

    code_detected_table_window = sg.Window("Detected Code List Table", code_detected_table_window_layout, element_justification='center',modal=True)

    while True:
        event, values = code_detected_table_window.read()
        if event == 'OUTPUT':
            code_selected = [detectedCodeList[row] for row in values[event]]
            print(code_selected[0])
            code_detected_table_window['CODE_STRING'].update(code_selected[0])
        if event == 'Copy':
            pyperclip.copy(str(code_detected_table_window['CODE_STRING'].get()))

        
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
    code_detected_table_window.close()

detectedCodeList = []
headings=["Code detected"]

# gui layout
layout = [
    [sg.Text("YouTube Link:"), sg.Input(key="URL")],
    [sg.Button("Detect"), sg.Exit()],

]
window = sg.Window("Social Media Links Clipboard", layout, element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

window.close() 