from tkinter import *
import clipboard

bgColor = "#191919"

win = Tk()
win.title("RevCipher")
win.configure(bg=bgColor)

def revCipher():
    msg = msgEntry.get()
    newMsg = ""
    ansBox.delete("1.0", "end")
    
    for letter in msg:
        cipheredLetter = letter.lower()
        if ord(letter.lower()) >= ord("a") and ord(letter.lower()) <= ord("z"):
            cipheredLetter = chr(ord("z") - (ord(letter.lower()) - ord("a")))
        if letter.isupper():
            cipheredLetter = cipheredLetter.upper()
        newMsg += cipheredLetter

    ansBox.insert(END, newMsg)

def copyOutput():
    clipboard.copy(ansBox.get("1.0", "end"))

#Labels
Label(win, text="Enter message to cipher/decipher: ", bg=bgColor, fg="White").grid(row=0, column=0)
Label(win, text="Ciphered/Deciphered message is: ", bg=bgColor, fg="White").grid(row=1, column=0)
#Text box
ansBox = Text(win, width=20, height=1, font = ("Segoe UI", 9))
ansBox.grid(row=1, column=1)
#Entry box
msgEntry = Entry(win)
msgEntry.grid(row=0, column=1)
#Button
button = Button(win, text="Cipher/Decipher", command = revCipher, bg=bgColor, fg="White")
button.grid(row=2, column=0)
copyButton = Button(win, text="Copy output", command = copyOutput, bg=bgColor, fg="White")
copyButton.grid(row=2, column=1)

mainloop()