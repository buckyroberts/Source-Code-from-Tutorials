from gi.repository import Gtk


class LabelWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")
        self.set_border_width(20)
        self.set_default_size(500, 300)

        # set_homogeneous() - if True, all children get equal space
        hbox = Gtk.Box(spacing=20)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_right.set_homogeneous(False)

        # Make two columns
        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        # Normal
        label = Gtk.Label("This is a normal label")
        vbox_left.pack_start(label, True, True, 0)

        # Left justified
        label = Gtk.Label()
        label.set_text("This is a left-justified label.\nWith multiple lines.")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)

        # Right justified
        label = Gtk.Label("This is a right-justified label.\nWith multiple lines.")
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)

        # Line wrap
        label = Gtk.Label("Drumstick biltong chuck, tongue porchetta jerky jowl bacon pig kevin. Tail shankle cupim.")
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)

        # Fill (newspaper)
        label = Gtk.Label("Drumstick biltong chuck, tongue porchetta jerky jowl bacon pig kevin. Tail shankle.")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        # Markup
        label = Gtk.Label()
        label.set_markup("<small>small</small>\n "
                         "<big>big</big>\n"
                         "<b>bold</b>\n"
                         "<i>italic</i>\n"
                         "<a href=\"https://www.thenewboston.com\" title=\"Will appear on hover\">Learn Stuff</a>")
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)

        self.add(hbox)


window = LabelWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
