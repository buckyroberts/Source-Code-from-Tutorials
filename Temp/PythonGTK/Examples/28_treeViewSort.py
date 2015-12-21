from gi.repository import Gtk

# List of tuples (this is the model, aka the data that will be displayed by the TreeView)
people = [("Bucky Roberts", 67, "Exotic Dancer"),
          ("Jenny Blue", 21, "Shepherd"),
          ("John Smith", 55, "Programmer"),
          ("Emma Anderson", 43, "Nurse"),
          ("Emily Wilson", 28, "Teacher")]


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="People Finder")
        layout = Gtk.Box()
        self.add(layout)

        people_list_store = Gtk.ListStore(str, int, str)

        for item in people:
            people_list_store.append(list(item))

        people_tree_view = Gtk.TreeView(people_list_store)

        for i, col_title in enumerate(["Name", "Age", "Profession"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Make column sortable and selectable
            column.set_sort_column_id(i)

            people_tree_view.append_column(column)

        # Handle selection
        selected_row = people_tree_view.get_selection()
        selected_row.connect("changed", self.item_selected)

        layout.pack_start(people_tree_view, True, True, 0)

    # User selected row
    def item_selected(self, selection):
        model, row = selection.get_selected()
        if row is not None:
            print("Name: ", model[row][0])
            print("Age: ", model[row][1])
            print("Job: ", model[row][2])
            print("")


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

