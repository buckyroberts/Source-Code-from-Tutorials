from Layouts.BorderPane.main_menu import *
from Layouts.BorderPane.toolbar import *
from Layouts.BorderPane.left import *
from Layouts.BorderPane.middle import *
from Layouts.BorderPane.right import *
from Layouts.BorderPane.bottom import *


# Window
window = Gtk.Window(title="Title")
window.connect("delete-event", Gtk.main_quit)
layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
window.add(layout)

# Top, toolbar, main, and bottom
main_menu_area = Gtk.Box()
toolbar_area = Gtk.Box()
main_area = Gtk.Box()
bottom_area = Gtk.Box()

# Divide main area into left, middle, and right
left_main = Gtk.Box()
middle_main = Gtk.Box()
right_main = Gtk.Box()
main_area.pack_start(left_main, False, False, 0)
main_area.pack_start(middle_main, True, True, 0)
main_area.pack_start(right_main, True, True, 0)

# Add to layout
layout.pack_start(main_menu_area, False, False, 0)
layout.pack_start(toolbar_area, False, False, 0)
layout.pack_start(main_area, True, True, 0)
layout.pack_start(bottom_area, False, False, 0)

# Create UI items (pass in the area where items should be displayed)
create_main_menu(main_menu_area)
create_top(toolbar_area)
create_left(left_main)
create_middle(middle_main)
create_right(right_main)
create_bottom(bottom_area)

# Display
window.show_all()
Gtk.main()
