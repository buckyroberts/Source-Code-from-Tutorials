from gi.repository import Gtk
from Project.top import TopArea


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Boxes are Awesome")

        # Should have layout already created, then add these sections
        self.add(TopArea())


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
