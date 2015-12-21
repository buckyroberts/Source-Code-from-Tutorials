from gi.repository import Gtk
import toolbar


websites = [("thenewboston.com", "https://thenewboston.com"),
            ("reddit.com", "https://reddit.com"),
            ("youtube.com", "https://youtube.com"),
            ("amazon.com", "https://amazon.com")]


def create_left(area):

    # ListStore
    people_list_store = Gtk.ListStore(str, str)
    for item in websites:
        people_list_store.append(list(item))

    # View
    websites_tree_view = Gtk.TreeView(people_list_store)
    for i, title in enumerate(["Websites"]):
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(title, renderer, text=i)
        column.set_sort_column_id(i)
        websites_tree_view.append_column(column)

    # Handle selected
    selected_row = websites_tree_view.get_selection()
    selected_row.connect("changed", item_selected)
    area.pack_start(websites_tree_view, False, False, 0)


# User selected row
def item_selected(selection):
    model, row = selection.get_selected()
    if row is not None:
        print("Website: ", model[row][0])
        print("URL: ", model[row][1])
        print("")
        toolbar.change_button_text(model[row][1])
