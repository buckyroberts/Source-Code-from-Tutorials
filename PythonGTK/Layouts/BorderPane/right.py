from gi.repository import Gtk


# UI elements
button = Gtk.Button()


def create_right(area):
    button.set_label("Right Area")
    area.pack_start(button, True, True, 0)
