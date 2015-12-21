from gi.repository import Gtk


# UI elements
left_label = Gtk.Label()
right_label = Gtk.Label()


def create_bottom(area):
    left_label.set_label("Bottom left")
    right_label.set_label("Bottom right")
    left_label.set_halign(1)
    right_label.set_halign(2)
    area.pack_start(left_label, True, True, 0)
    area.pack_start(right_label, True, True, 0)
