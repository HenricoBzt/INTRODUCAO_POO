import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('America/Recife'))
datainter = datetime.now(pytz.timezone('Europe/London'))
print(data)
print(datainter)