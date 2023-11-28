import os
import json
import shutil

def delete_results_folders(config):
    for info_need in config['information_needs']:
        folder_path = f'evaluation/{info_need["id"]}/results'
        if os.path.exists(folder_path):
            print(f'Deleting folder: {folder_path}')
            try:
                shutil.rmtree(folder_path)
                print(f'Folder deleted successfully.')
            except OSError as e:
                print(f'Error deleting folder: {e}')

if __name__ == "__main__":
    # Load the configuration from JSON
    with open('queries.json', 'r') as config_file:
        config = json.load(config_file)

    # Delete results folders based on the information needs
    delete_results_folders(config)
