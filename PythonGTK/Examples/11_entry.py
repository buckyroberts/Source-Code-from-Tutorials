from gi.repository import Gtk


class UserInput(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Messenger 2.0")
        self.set_border_width(10)
        self.set_size_request(200, 100)

        # Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Username
        self.username = Gtk.Entry()
        self.username.set_text("Username")
        vbox.pack_start(self.username, True, True, 0)

        # Password
        self.password = Gtk.Entry()
        self.password.set_text("Password")
        self.password.set_visibility(False)
        vbox.pack_start(self.password, True, True, 0)

        # Sign In Button
        self.button = Gtk.Button(label="Sign In")
        self.button.connect("clicked", self.sign_in)
        vbox.pack_start(self.button, True, True, 0)

    def sign_in(self, widget):
        print(self.username.get_text())
        print(self.password.get_text())


window = UserInput()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
