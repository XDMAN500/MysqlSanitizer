import gi
import re
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk



syntaxFilter = re.compile("\"|\\+", flags=re.MULTILINE)
symbolFilter = re.compile("\\?", flags=re.MULTILINE)


def convert_handler(object, source, destination):
	sourceBuffer = source.get_buffer()
	destBuffer = destination.get_buffer()
	
	sourceText = sourceBuffer.get_text(sourceBuffer.get_start_iter(), sourceBuffer.get_end_iter(), False)
	replacementtext = sourceText
	(replacementtext, _) = syntaxFilter.subn("", replacementtext)
	(replacementtext, _) = symbolFilter.subn("1",replacementtext)
	#(replacementtext, _) = syntaxFilter.subn(replacementtext, "")
	#(replacementtext, _) = symbolFilter.subn(replacementtext, "1")
	
	destBuffer.set_text(replacementtext, len(replacementtext))
	

builder = Gtk.Builder()
builder.add_from_file("SqlProjectWindow.glade")
window = builder.get_object("mainWindow")
button = builder.get_object("Convert")

rawTextView = builder.get_object("rawText")
formatedTextView = builder.get_object("formattedText")
window.connect("destroy", Gtk.main_quit)

button.connect("released", convert_handler, rawTextView, formatedTextView)

window.show_all()
Gtk.main()



	
	