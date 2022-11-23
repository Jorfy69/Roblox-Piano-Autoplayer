import tkinter
import tkinter.filedialog
import mido
import keyboard
import time
def autoPlayer(filePath):
    mid = mido.MidiFile(filePath, clip=True, ticks_per_beat=800)
    notes = {
        20: "ctrl + 0",
        21: "ctrl + 1",
        22: "ctrl + 2",
        23: "ctrl + 3",
        24: "ctrl + 4",
        25: "ctrl + 5",
        26: "ctrl + 6",
        27: "ctrl + 7",
        28: "ctrl + 8",
        29: "ctrl + 9",
        30: "ctrl + 0",
        31: "ctrl + q",
        32: "ctrl + w",
        33: "ctrl + e",
        34: "ctrl + r",
        35: "ctrl + t",
        36: "1",
        37: "shift + 1",
        38: "2",
        39: "shift + 2",
        40: "3",
        41: "4",
        42: "shift + 4",
        43: "5",
        44: "shift + 5",
        45: "6",
        46: "shift + 6",
        47: "7",
        48: "8",
        49: "shift + 8",
        50: "9",
        51: "shift + 9",
        52: "0",
        53: "q",
        54: "shift + q",
        55: "w",
        56: "shift + w",
        57: "e",
        58: "shift + e",
        59: "r",
        60: "t",
        61: "shift + t",
        62: "y",
        63: "shift + y",
        64: "u",
        65: "i",
        66: "shift + i",
        67: "o",
        68: "shift + o",
        69: "p",# nice
        70: "shift + P",
        71: "a",
        72: "s", 
        73: "shift + s",
        74: "d",
        75: "shift + d",
        76: "f",
        77: "g",
        78: "shift + g",
        79: "h",
        80: "shift + h",
        81: "j",
        82: "shift + j",
        83: "k",
        84: "l",
        85: "shift + l",
        86: "z",
        87: "shift + z",
        88: "x",
        89: "c",
        90: "shift + c",
        91: "v",
        92: "shift + v",
        93: "b",
        94: "shift + b",
        95: "n",
        96: "m",
        97: "ctrl + y",   
        98: "ctrl + u",        
        99: "ctrl + i",
        100: "ctrl + o",
        101: "ctrl + p",
        102: "ctrl + a",
        103: "ctrl + s",
        104: "ctrl + d",
        105: "ctrl + f",
        106: "ctrl + g",
        107: "ctrl + h",
        108: "ctrl + j"
    }
    time.sleep(0.5)
    # mid.ticks_per_beat=50
    for msg in mid.play():
        if keyboard.is_pressed('alt') == True:
            for i in notes():
                keyboard.release(notes[i])
                
            print('released all')
            break
   
        try:
            if msg.type == 'note_on' and msg.velocity > 0:
                # if msg.velocity >= 105.875:
                #     keyboard.press_and_release('alt + c')
                # elif msg.velocity >= 95.75:
                #     keyboard.press_and_release('alt + x')
                # elif msg.velocity >= 90.625:
                #     keyboard.press_and_release('alt + z')
                # elif msg.velocity >= 87.5:
                #     keyboard.press_and_release('alt + l')   
                # elif msg.velocity >= 84.375:
                #     keyboard.press_and_release('alt + k')
                # elif msg.velocity >= 81.25:
                #     keyboard.press_and_release('alt + j')
                # elif msg.velocity >= 78.125:
                #     keyboard.press_and_release('alt + h')
                # elif msg.velocity >= 75:
                #     keyboard.press_and_release('alt + g')
                # elif msg.velocity >= 71.875:
                #     keyboard.press_and_release('alt + f')   
                # elif msg.velocity >= 68.75:
                #     keyboard.press_and_release('alt + d')
                # elif msg.velocity >= 65.625:
                #     keyboard.press_and_release('alt + s')
                # elif msg.velocity >= 62.5:
                #     keyboard.press_and_release('alt + a')
                # elif msg.velocity >= 59.375:
                #     keyboard.press_and_release('alt + p')
                # elif msg.velocity >= 56.25:
                #     keyboard.press_and_release('alt + o')   
                # elif msg.velocity >= 53.125:
                #     keyboard.press_and_release('alt + i')
                # elif msg.velocity >= 50:
                #     keyboard.press_and_release('alt + u')                   
                # elif msg.velocity >= 46.875:
                #     keyboard.press_and_release('alt + y')
                # elif msg.velocity >= 43.75:
                #     keyboard.press_and_release('alt + t')
                # elif msg.velocity >= 40.625:
                #     keyboard.press_and_release('alt + r')   
                # elif msg.velocity >= 37.375:
                #     keyboard.press_and_release('alt + e')
                # elif msg.velocity >= 34.25:
                #     keyboard.press_and_release('alt + w')
                # elif msg.velocity >= 31.125:
                #     keyboard.press_and_release('alt + q')
                # elif msg.velocity >= 28:
                #     keyboard.press_and_release('alt + 0')
                # elif msg.velocity >= 24.875:
                #     keyboard.press_and_release('alt + 9')   
                # elif msg.velocity >= 21.75:
                #     keyboard.press_and_release('alt + 8')
                # elif msg.velocity >= 18.625:
                #     keyboard.press_and_release('alt + 7')
                # elif msg.velocity >= 15.5:
                #     keyboard.press_and_release('alt + 6')
                # elif msg.velocity >= 12.375:
                #     keyboard.press_and_release('alt + 5')
                # elif msg.velocity >= 9.25:
                #     keyboard.press_and_release('alt + 4')   
                # elif msg.velocity >= 6.125:
                #     keyboard.press_and_release('alt + 3')
                # elif msg.velocity >= 3:
                #     keyboard.press_and_release('alt + 2')
                # elif msg.velocity > 0:
                #     keyboard.press_and_release('alt + 1')
                
                keyboard.press(notes[msg.note])
                keyboard.release('shift')
                keyboard.release('ctrl')                
                print(msg)
            elif msg.type == 'note_off' or msg.velocity == 0:
                keyboard.release(notes[msg.note])
                

            else:
                print(msg)

        except:
            pass

def prompt_file():
    top = tkinter.Tk()
    top.withdraw() 
    global file_name 
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()

def begin():
    root = tkinter.Tk()
    root.geometry('160x100')
    root.title('Auto Player')
    B = tkinter.Button(root, text ="File", command= prompt_file)
    B.config(width=10, height=6)
    B.grid(row=0, column=0)
    P = tkinter.Button(root, text = "Play", command= lambda : autoPlayer(file_name))
    P.config(width=10, height=6)
    P.grid(row=0, column=20)
    root.mainloop()

if __name__ == '__main__':
    begin()