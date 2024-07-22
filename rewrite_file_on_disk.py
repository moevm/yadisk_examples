import os
import yadisk
token = os.getenv('YA_DISK_TOKEN')
client = yadisk.Client(token=token)
client.upload('example_table.csv', 'table.csv', overwrite=True)