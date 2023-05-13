import tkinter
import tkinter.filedialog
import mido
import keyboard
import time
def autoPlayer(filePath):
    mid = mido.MidiFile(filePath, clip=True, ticks_per_beat=800)
    keyboard_chars = "1234567890qwertyuiopasdfghjklzxcvbnm"
    full_key_support_left = "1234567890qwert"
    full_key_support_right = "yuiopasdfghj"
    keyboard_map = {}
    start = 2
    offset = 19
    for i in full_key_support_left:
        keyboard_map[start + offset] = "ctrl + " + i
        offset += 1
    offset = 95
    for i in full_key_support_right:
        keyboard_map[start + offset] = "ctrl + " + i
        offset += 1
    offset = 34
    for i in keyboard_chars:
        keyboard_map[start + offset] = i
        if start % 12 in [2,4,7,9,11]:
            start +=1
            keyboard_map[start + offset] = "shift + " + i
        start +=1
    time.sleep(0.5)
    # mid.ticks_per_beat=500
    for msg in mid.play():
        if keyboard.is_pressed('alt') == True:
            for i in keyboard_map():
                keyboard.release(keyboard_map[i])
                
            print('released all')
            break
        try:
            if msg.type == 'note_on' and msg.velocity > 0:
                keyboard.press(keyboard_map[msg.note])
                keyboard.release('shift')
                keyboard.release('ctrl')                

            elif msg.type == 'note_off' or msg.velocity == 0:
                keyboard.release(keyboard_map[msg.note])
                print(msg)

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