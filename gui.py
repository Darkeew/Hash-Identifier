#!/usr/bin/env python3
import PySimpleGUI as sg

algorithms={'1':'MD5','2':'SHA-1','3':'SHA-224','4':'SHA-256','5':'SHA-384','6':'SHA-512'}

def MD5(hash):
    xash = '05928898984cc2c66f45d72715191746'
    if(len(hash) == len(xash) and hash.isalnum() == True):
        hashArray.append(algorithms['1'])
def SHA1(hash):
    xash = 'ec4bb2d325b6f5af7c96e171d87cf2f5c8c3b81a'
    if(len(hash) == len(xash) and hash.isalnum() == True):
        hashArray.append(algorithms['2'])
def SHA224(hash):
    xash = '3139a5797bb7c20f8806bff96e3b27e1b7ac57af907bee1bf9733413'
    if(len(hash) == len(xash) and hash.isalnum() == True):
        hashArray.append(algorithms['3'])
def SHA256(hash):
    xash = '06aae95278f58c618e3dc14565b3a342d494ea6cd7ecf245d7510baa2148d65a'
    if(len(hash) == len(xash) and hash.isalnum() == True):
        hashArray.append(algorithms['4'])
def SHA384(hash):
    xash = 'eaf35c45320735ad503eb5ced8b90e60bcc2f51328900c73cee633c661096be254a9c6b683dba505530fdcb3e0624be0'
    if(len(hash) == len(xash) and hash.isalnum() == True):
        hashArray.append(algorithms['5'])
def SHA512(hash):
    xash = '319734cfce5f8ec57f38e0e050c1572450352a8f25914c583341bec56d57edf379b34a0de8c200cbc9db622b682ecf9444459470027c31484e4309b747da079f'
    if(len(hash) == len(xash) and hash.isalnum() == True):
        hashArray.append(algorithms['6'])

layout = [
    [sg.Text('[!] Insert your hash.')],
    [sg.InputText()],
    [sg.Text('', key='-OUTPUT-')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window("Hash Identifier", layout, margins=('200,80'))

while True:
    event, values = window.read()
    input = values[0]
    if event == 'Cancel' or sg.WIN_CLOSED:
        break
    elif event == 'Submit':
        hashArray = []
        hash = input
        MD5(hash),SHA1(hash),SHA224(hash),SHA256(hash),SHA384(hash),SHA512(hash)
        if len(hashArray) == 0:
            window['-OUTPUT-'].update('[!] No hashes have been found.')
        else:
            window['-OUTPUT-'].update('[+] Possible hashes: ' + str(hashArray))


window.close()
        