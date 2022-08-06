
import PySimpleGUI as sg
import pyperclip

# gui layout
layout = [
    [sg.Text("LinkedIn:"), sg.Input("https://www.linkedin.com/in/andrewfungkinho/",key="linkedinURL"),sg.Button("Copy LinkedIn")],
    [sg.Text("YouTube:"), sg.Input("https://www.youtube.com/AndrewFungKinHo",key="youtubeURL"),sg.Button("Copy YouTube")],
    [sg.Text("Website:"), sg.Input("https://andrew-fungkinho.github.io/",key="websiteURL"),sg.Button("Copy Website")],
    [sg.Text("GitHub:"), sg.Input("https://github.com/Andrew-FungKinHo",key="githubURL"),sg.Button("Copy GitHub")],
    [sg.Text("Twitter:"), sg.Input("https://twitter.com/AndrewFungKinHo",key="twitterURL"),sg.Button("Copy Twitter")],
    [sg.Exit()]
]
window = sg.Window("Social Media Links Clipboard", layout, element_justification='center')

while True:
    event, values = window.read()
    if event == 'Copy LinkedIn':
        pyperclip.copy(values["linkedinURL"])
    if event == 'Copy YouTube':
        pyperclip.copy(values["youtubeURL"])
    if event == 'Copy Website':
        pyperclip.copy(values["websiteURL"])
    if event == 'Copy GitHub':
        pyperclip.copy(values["githubURL"])
    if event == 'Copy Twitter':
        pyperclip.copy(values["twitterURL"])

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break


window.close() 

