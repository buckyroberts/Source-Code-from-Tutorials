from gi.repository import Gtk


# UI elements
top_button = Gtk.Button()
button_1 = Gtk.Button("One")
button_2 = Gtk.Button("Two")
button_3 = Gtk.Button("Three")


def create_top(area):
    global top_button
    top_button = Gtk.Button(label="This is from toolbar")
    top_button.connect("clicked", button_clicked)

    toolbar = Gtk.Box()
    toolbar.pack_start(top_button, False, False, 0)
    toolbar.pack_start(button_1, False, False, 0)
    toolbar.pack_start(button_2, False, False, 0)
    toolbar.pack_start(button_3, False, False, 0)

    area.pack_start(toolbar, True, True, 0)


def button_clicked(self):
    print("Gametime")


def change_button_text(text):
    top_button.set_label(text)
