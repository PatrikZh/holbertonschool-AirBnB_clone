#!/usr/bin/python3
import cmd
import sys
import os

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        ''' Exit the program'''
        return True

    def do_EOF(self, arg):
        ''' Exit the program using EOF'''
        print()
        return True

    def empty_line(self, arg):
        ''' Do nothing when empty line entered'''
        pass

    def precmd(self, line):
        ''' Executes commands line arguments if provided'''
        if line and not line.isspace():
            print(self.prompt + line)
        return line

if __name__ == '__main__':
    HBNBCommand().cmdloop()
