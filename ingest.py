import shutil
import zipfile

import requests


def download_zip_file(file_name: str, base_url: str):
    """
    Download .zip archive from base_url and save it to raw/{file_name}.zip.

    Parameters
    ----------
    file_name : str
    base_url : str

    Returns
    -------
    save_to_file_path
        Path where the .zip archive is saved to.

    Raises
    ----------
    HTTPError
    """
    zip_file_name = f"{file_name}.zip"
    download_url = f"{base_url}/{zip_file_name}"
    try:
        res = requests.get(download_url, timeout=30, stream=True)
        res.raise_for_status()
        save_to_file_path = f"raw/{zip_file_name}"
        with open(save_to_file_path, "wb") as f:
            # stolen from: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
            shutil.copyfileobj(res.raw, f)
        return save_to_file_path
    except requests.HTTPError as e:
        print(f"Something went wrong while downloading the file from: {download_url}")
        # Raise error after giving a friendly message to fail fast
        raise (e)


def extract_zip_archive(path_to_file: str):
    """
    Extract the given .zip archive into the /raw folder.

    Parameters
    ----------
    path_to_file : str
    """
    with zipfile.ZipFile(path_to_file, "r") as f:
        f.extractall("raw")
