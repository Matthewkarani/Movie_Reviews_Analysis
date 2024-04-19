import requests

# API Key
my_api_key = 'c7764722dac6a2e287a0924a16be4078'


def get_genre_names(api_key):
    """
    Retrieve genre names from TMDB API and return a dictionary mapping genre IDs to genre names.

    Parameters:
    - api_key (str): Your TMDB API key.

    Returns:
    - genre_dict (dict): A dictionary mapping genre IDs to genre names.
    """
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        genre_dict = {genre['id']: genre['name'] for genre in data['genres']}
        return genre_dict
    else:
        print("Failed to retrieve genre names from TMDB API.")
        return None


# Example usage:
# api_key = 'your_tmdb_api_key'
# genre_dict = get_genre_names(api_key)
# if genre_dict:
#     df = replace_genre_ids_with_names(df, genre_dict)
