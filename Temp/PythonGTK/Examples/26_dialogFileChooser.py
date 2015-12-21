from gi.repository import Gtk


class FileChooserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_border_width(30)
        layout = Gtk.Box(spacing=6)
        self.add(layout)

        button = Gtk.Button("Choose File")
        button.connect("clicked", self.on_file_clicked)
        layout.add(button)

    # User clicked open file button
    def on_file_clicked(self, widget):

        # Gtk.FileChooserAction.SELECT_FOLDER
        dialog = Gtk.FileChooserDialog("Select a file Hoss", self, Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("Open button clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")

        dialog.destroy()


window = FileChooserWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
