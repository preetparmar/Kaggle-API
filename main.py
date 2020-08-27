# Importing Library
from kaggle.api.kaggle_api_extended import KaggleApi

# Initializing
api = KaggleApi()
api.authenticate()


def search_competition(name:str=None, category:str=None) -> list:
    """ 

    Returns a list of competitons available on Kaggle
    
    Parameters:
        name: str, optional
            text you want to search in the title of the competiton
        category: str, optional
            specific category you want to search
    Retuns:
        list of competions fiiting the search
    
    """
    category_list = ['all', 'featured', 'research', 'recruitment', 'gettingStarted', 'masters', 'playground']
    if category is not None and category not in category_list:
        print("Invalid Catgory Name!\nValid Options are: 'all', 'featured', 'research', 'recruitment', 'gettingStarted', 'masters', 'playground'")
    else:
        api.competitions_list_cli(search=name, category=category)
        comp_list = api.competitions_list(search=name, category=category)
        return [str(comp) for comp in comp_list]


def get_list_of_files(competition:str) -> list:
    return api.competitions_data_list_files(competition)


def download_all_files(competions:str, path:str=None):
    """
    Downloads all files from competion
    Parameters:
        competions: str
            name of the competition
        path: str, optional
            path where you want to save the file
            *if the path is invalid, it will create a folder with the given name in the base folder
            *it will create a folder if not present in the path
    Return:
        downloads all the file in the specified location
    """
    try:
        api.competition_download_files(competion, path, force=False, quiet=True)
        if path is None:
            print('All files were successfully downloaded to the base folder')
        else:
            print(f'All files were successfully downlaoded to {path}')
    except:
        print('Unable to download file\nPlease check the Competition Name or File Name')


def download_specific_file(competion:str, file_name:str, path:str=None):
    """
    Downloads a specific file from competion
    Parameters:
        competions: str
            name of the competition
        file_name: str
            name of the file you want to download
        path: str, optional
            path where you want to save the file
            *if the path is invalid, it will create a folder with the given name in the base folder
            *it will create a folder if not present in the path
    Return:
        downloads the file in the specified location
    """
    try:
        api.competition_download_file(competion, file_name, path, force=False, quiet=True)
        if path is None:
            print('File was successfully downloaded to the base folder')
        else:
            print(f'File was successfully downlaoded to {path}')
    except:
        print('Unable to download file\nPlease check the Competition Name or File Name')

