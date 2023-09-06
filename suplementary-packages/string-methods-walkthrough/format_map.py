'''
Format Map
'''

coordinates = {'x': 10, 'y': -5}
text = "Coordinates: ({x}, {y})"
print(text.format_map(coordinates))