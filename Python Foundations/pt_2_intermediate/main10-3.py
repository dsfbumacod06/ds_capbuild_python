# Implementing using the DOM Module part 2 - adding elements
import xml.dom.minidom

domtree = xml.dom.minidom.parse('data-changed.xml')
group = domtree.documentElement
persons = group.getElementsByTagName('person')

# for person in persons:
#     print("-----PERSON-----")
#     if person.hasAttribute('id'):
#         print(f'ID: {person.getAttribute("id")}')
#     print(f"Name: {person.getElementsByTagName('name')[0].childNodes[0].data}")
#     print(f"Age: {person.getElementsByTagName('age')[0].childNodes[0].data}")
#     print(f"Weight: {person.getElementsByTagName('weight')[0].childNodes[0].data}")
#     print(f"Height: {person.getElementsByTagName('height')[0].childNodes[0].data}")

newPerson = domtree.createElement('person')
newPerson.setAttribute("id", "6")

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode("Paul Pili"))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode("69"))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode("45"))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode("164"))

newPerson.appendChild(name)
newPerson.appendChild(age)
newPerson.appendChild(weight)
newPerson.appendChild(height)

group.appendChild(newPerson)
domtree.writexml(open('data-changed.xml','w'))

persons = group.getElementsByTagName('person')
for person in persons:
    print("-----PERSON-----")
    if person.hasAttribute('id'):
        print(f'ID: {person.getAttribute("id")}')
    print(f"Name: {person.getElementsByTagName('name')[0].childNodes[0].data}")
    print(f"Age: {person.getElementsByTagName('age')[0].childNodes[0].data}")
    print(f"Weight: {person.getElementsByTagName('weight')[0].childNodes[0].data}")
    print(f"Height: {person.getElementsByTagName('height')[0].childNodes[0].data}")