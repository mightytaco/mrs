import Decrypt as morse
import winsound
import time
import Spectrum as spec
import ToneSound as ts

def main():
    message = input('enter text: ')
    result = morse.encrypt(message.upper())
    print(result)
    bandymas = spec.
    # Play sound in windows
    playsound = input('do u want to play morse code as sound? (y/n)')
    if playsound.upper() == 'Y':
        ts.sound(result)

# Main call
if __name__ == "__main__":
    main()
