import Keys
import random


class Encrypt:
    def __init__(self, entryData):
        self.valueIn = entryData
        self.KeysEncrypt = Keys()
        self.KeysEncrypt.GenerateKeys()

    def encryptASCII(self):
        ASCII_numbers = []
        for character in self.valueIn:
            valeur_ascii = ord(character)
            ASCII_numbers.append(valeur_ascii)

        return ASCII_numbers

    def transformASCII(self):
        tabNumbers = self.encryptASCII()
        for number in tabNumbers:
            condense_ASCII = + number

        lenMinus = len(str(self.KeysEncrypt.n)) - 1
        rest = len(condense_ASCII) % lenMinus

        decoupes = [condense_ASCII[i:i + lenMinus] for i in range(0, len(condense_ASCII), lenMinus)]




