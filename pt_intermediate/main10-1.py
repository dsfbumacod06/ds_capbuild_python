# xml processing - extensible markup language
# hierarchically structures data
# platform and application independent
# can be implemented using the SAX or DOM module
# SAX - Simple API for XML - never loads full xml into the ram - useful for large xml files or limited local memory. - read only

#SAX
import xml.sax

# handler = xml.sax.ContentHandler()
# to customize handler ->

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("-----PERSON-----")
            print(f"ID: {attrs['id']}")
        # return super().startElement(name, attrs)

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content
        # return super().characters(content)

    def endElement(self, name):
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "age":
            print(f"Age: {self.age}")
        elif self.current == "weight":
            print(f"Weight: {self.weight}")
        elif self.current == "height":
            print(f"Height: {self.height}")
        self.current = ""
        # return super().endElement(name)



handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')
# handler.startElement 