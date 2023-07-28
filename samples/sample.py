import os
import dotenv

dotenv.load_dotenv()

myName = os.environ.get('name')
print(myName)