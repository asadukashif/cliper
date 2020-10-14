
#! /usr/bin/python3
import pyperclip
from sys import exit, argv
import os
import subprocess


def Main():
    text = get_command_line_text()
    pyperclip.copy(text)


def get_command_line_text():
    """ Handles the command line args and checks for validates it """
    if len(argv) < 2:
        print("Usage: clip <text or file to read from>")
        exit(1)
    else:
        text = ""
        for i in range(1, len(argv)):
            text += argv[i] + " "

    text = text.strip()

    # If the inputted text is a file
    if os.path.isfile(text):
        path = text
        text = read_file(path)

    # if the inputted text is a shell command
    shell_result = read_shell_command(text)
    if shell_result != '':
        text = shell_result

    return text


def read_shell_command(command):
    PIPE = subprocess.PIPE
    with subprocess.Popen(command, shell=True, stderr=PIPE, stdout=PIPE, stdin=PIPE) as shell:
        text, strerr = shell.communicate()

    return text.decode().strip()


def read_file(path):
    """ Reads and returns the content of the file """
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        print("An error occured!")
        print('\t' + e)
        exit(1)


if __name__ == "__main__":
    Main()
