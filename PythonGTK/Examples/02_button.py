from gi.repository import Gtk


# inherit from Gtk.Window
class MainWindow(Gtk.Window):

    # for the constructor we call the constructor of the super class (and set window title)
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        
        # create button, connect its "clicked" signal to a function, and add it to the window
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)

    # make sure to pass in widget, wont work if you dont (more about widgets later) 
    def button_clicked(self, widget):
        print("Gametime")


# create an instance of that class
window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
