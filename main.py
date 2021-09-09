import pyautogui as pag


def print_position():
    pos = pag.position()
    pos = f'X: {pos.x}, Y: {pos.y}'
    print(pos, end='')
    pag.sleep(1)
    print('\b' * len(pos), end='')


while True:
    try:
        print_position()
    except KeyboardInterrupt:
        pass
