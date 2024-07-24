# usage: python3 write_sheet_to_file.py remote_path_to_file local_path_to_file

import os
import sys
from openpyxl import load_workbook
from client_wrapper import ClientWrapper
from utils import add_csv_to_table
from dotenv import load_dotenv


def write_sheet_to_file(remote_path, csv_path):
    cw = ClientWrapper()
    
    # download file to filesystem
    local_path = cw.download_file_from_disk(remote_path) 
    
    # create openpyxl.Workbook from existing xlsx file
    wb = load_workbook(filename=local_path)
    
    # add csv to table as sheet 
    add_csv_to_table(csv_path, wb, sheet_name='export')
    
    # save openpyxl.Workbook to filesystem with same name
    wb.save(local_path)

    # download file to disk
    cw.upload_file_to_disk(local_path, remote_path) 

    os.remove(local_path)


if __name__ == "__main__":
    load_dotenv()

    if len(sys.argv) < 3: 
        print("usage: python3 write_sheet_to_file.py remote_path_to_file local_path_to_file")
        exit(1)

    remote_path = sys.argv[1] # disk path
    csv_path = sys.argv[2] # csv path
    
    write_sheet_to_file(remote_path, csv_path)