from gi.repository import Gtk


# Top Toolbar area
class TopArea(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self)

        self.input_add_url = Gtk.Entry()
        self.button_plus = Gtk.Button()
        self.button_import = Gtk.Button()
        self.button_play = Gtk.Button()
        self.button_trash = Gtk.Button()

        self.style_items()
        self.create_structure()
        self.connect_signals()

    # Style items
    def style_items(self):
        self.set_spacing(5)
        self.set_border_width(5)

        self.input_add_url.set_placeholder_text("Add URL")
        self.button_plus.set_label("Add URL")
        self.button_import.set_label("Import")
        self.button_play.set_label("Start Scan")
        self.button_trash.set_label("Delete")

        self.button_plus.set_relief(Gtk.ReliefStyle.NONE)
        self.button_import.set_relief(Gtk.ReliefStyle.NONE)
        self.button_play.set_relief(Gtk.ReliefStyle.NONE)
        self.button_trash.set_relief(Gtk.ReliefStyle.NONE)

    # Create structure
    def create_structure(self):
        self.pack_start(self.input_add_url, False, False, 0)
        self.pack_start(self.button_plus, False, False, 0)
        self.pack_start(self.button_import, False, False, 0)
        self.pack_start(self.button_play, False, False, 0)
        self.pack_start(self.button_trash, False, False, 0)

    # Connect signals
    def connect_signals(self):
        self.button_plus.connect("clicked", self.button_plus_clicked)

    # Add button clicked
    def button_plus_clicked(self, widget):
        print("Add button clicked")
