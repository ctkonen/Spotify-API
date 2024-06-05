# Spotify Top Tracks Finder

This Python application interacts with the Spotify API to fetch and display the top tracks of a specified artist. The application also includes a feature to visualize these tracks in a bar chart using Matplotlib.

## Features
- **Fetch Access Token**: Securely fetches an access token using Spotify's Client Credentials flow.
- **Search for Artist**: Searches Spotify for an artist by name and retrieves the artist's ID.
- **Get Top Tracks**: Retrieves the top tracks of the specified artist.
- **Visualization**: Plots the top tracks in a horizontal bar chart using Matplotlib.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/spotify-top-tracks-finder.git
    cd spotify-top-tracks-finder
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your Spotify API credentials:
    - Create a `.env` file in the root directory.
    - Add your Spotify Client ID and Client Secret to the `.env` file:
    ```plaintext
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. Enter the name of the artist when prompted:
    ```plaintext
    Enter the artist that you would like to see the top 10 songs for: [artist_name]
    ```

3. The top 10 tracks of the specified artist will be displayed in the console.

4. A horizontal bar chart visualizing the top tracks will be generated and displayed.

## Code Overview

- **Fetching Access Token**: The `get_token()` function fetches an access token from Spotify using the Client Credentials flow.
- **Authorization Header**: The `get_auth_header(token)` function returns the authorization header required for making authenticated requests to the Spotify API.
- **Search for Artist**: The `search_for_artist(token, artist_name)` function searches for an artist by name and returns the artist's details.
- **Get Top Tracks**: The `get_songs_by_artist(token, artist_id)` function fetches the top tracks of the specified artist.
- **Plotting**: The `plot_top_tracks_stacked(tracks)` function generates a horizontal bar chart of the top tracks using Matplotlib.

## Example

Here is an example of what the output might look like:

```plaintext
Enter the artist that you would like to see the top 10 songs for: Taylor Swift
1. All Too Well (10 Minute Version) (Taylor's Version) (From The Vault)
2. Anti-Hero
3. Lavender Haze
4. Blank Space
5. Love Story (Taylor's Version)
6. Shake It Off
7. I Knew You Were Trouble
8. You Belong With Me (Taylor's Version)
9. Look What You Made Me Do
10. cardigan
```


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.


- [Spotify API](https://developer.spotify.com/documentation/web-api/)
- [Matplotlib](https://matplotlib.org/)
- [Requests Library](https://docs.python-requests.org/en/latest/)
- [Dotenv](https://pypi.org/project/python-dotenv/)

Feel free to reach out with any questions or feedback. Happy coding!
