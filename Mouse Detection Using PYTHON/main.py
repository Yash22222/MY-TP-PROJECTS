# Mouse Tracker using python and pynput

from pynput.mouse import Listener


def on_move(x, y):
    print("Mouse Is Moved To ({0},{1})".format(x, y))


def on_click(x, y, button, pressed):
    if pressed:
        print("Mouse Clicked At ({0},{1} with {2})".format(x, y, button))


def on_scroll(x, y, dx, dy):
    print("Mouse Is Scrolled At ({0},{1}) ({2},{3})".format(x, y, dx, dy))


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
