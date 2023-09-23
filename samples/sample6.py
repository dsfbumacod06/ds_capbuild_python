from collections import namedtuple


Bot = namedtuple('Bot', 'name state start_button stop_button')
somebot = Bot("Function1", "some state", "some start button", "some stop button")
print(somebot.name)
print(somebot.state)
print(somebot.start_button)
print(somebot.stop_button)