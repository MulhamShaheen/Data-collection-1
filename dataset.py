import pandas as pd
from yandex import search_playlists
from tunebat import search_tracks, props_dict


def scrap_playlist_data(keyword, count=50):
    tracks = search_playlists(keyword)
    results = []
    for i, track in enumerate(tracks):
        if i == count:
            break
        data = search_tracks(f"{track['title']} - {track['artists']}", 1)
        print(data)
        results.append(data)

    return results


def create_subset(query: list, label: str):
    cols = list(props_dict.values())
    rows = []
    for q in query:
        data = scrap_playlist_data(q)
        for track in data:
            rows.append(list(track.values()))

    df = pd.DataFrame(data=rows, columns=cols)
    df.to_csv(f"{label}.csv")

    return df


create_subset(["Best of jazz radio"], "dining")