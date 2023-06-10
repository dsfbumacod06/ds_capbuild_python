# Implementing using the DOM Module
import xml.dom.minidom

domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement
persons = group.getElementsByTagName('person')

# for person in persons:
    # print("-----PERSON-----")
    # if person.hasAttribute('id'):
    #     print(f'ID: {person.getAttribute("id")}')
    # print(f"Name: {person.getElementsByTagName('name')[0].childNodes[0].data}")
    # print(f"Age: {person.getElementsByTagName('age')[0].childNodes[0].data}")
    # print(f"Weight: {person.getElementsByTagName('weight')[0].childNodes[0].data}")
    # print(f"Height: {person.getElementsByTagName('height')[0].childNodes[0].data}")

persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New name"
persons[0].setAttribute('id','100')
persons[4].getElementsByTagName('age')[0].childNodes[0].nodeValue = "-10"

domtree.writexml(open('data-changed.xml','w'))
