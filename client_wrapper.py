import os
import yadisk


class ClientWrapper:
    
    def __init__(self, api_token=None):
        self.api_token = api_token if api_token else os.getenv('YADISK_TOKEN') # validate?
        self.client = yadisk.Client(token=self.api_token)
        self.download_dir_path = "./"

    def download_file_from_disk(self, remote_path):
        local_path = self.download_dir_path + os.path.basename(remote_path)
        self.client.download(remote_path, local_path)
        return local_path

    def upload_file_to_disk(self, local_path, remote_path, overwrite=True):
        return self.client.upload(local_path, remote_path, overwrite=overwrite)
        