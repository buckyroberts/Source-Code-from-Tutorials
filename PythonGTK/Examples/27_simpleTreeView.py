from gi.repository import Gtk

# List of tuples (this is the model, aka the data that will be displayed by the TreeView)
people = [("Bucky Roberts", 67, "Exotic Dancer"),
          ("Jenny Blue", 21, "Shepherd"),
          ("John Smith", 55, "Programmer"),
          ("Emma Anderson", 43, "Nurse"),
          ("Emily Wilson", 28, "Teacher")]


class TreeViewFilterWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="People Finder")

        # Layout
        layout = Gtk.Box()
        self.add(layout)

        # Convert data to ListStore (lists that TreeViews can display) and specify data types
        people_list_store = Gtk.ListStore(str, int, str)
        for item in people:
            people_list_store.append(list(item))

        for row in people_list_store:
            print(row[:])  # Print all data
            print(row[2])  # Print third column (profession)

        # TreeView is the item that is displayed
        people_tree_view = Gtk.TreeView(people_list_store)

        # Enumerate to add counter (i) to loop
        for i, col_title in enumerate(["Name", "Age", "Profession"]):

            # Render means draw or display the data (just display as normal text)
            renderer = Gtk.CellRendererText()

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add columns to TreeView
            people_tree_view.append_column(column)

        # Add to layout
        layout.pack_start(people_tree_view, True, True, 0)


window = TreeViewFilterWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
