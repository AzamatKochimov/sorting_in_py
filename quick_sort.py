def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]["duration"]  # Choose a pivot element
    left = [song for song in arr if song["duration"] < pivot]
    middle = [song for song in arr if song["duration"] == pivot]
    right = [song for song in arr if song["duration"] > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Example usage:
playlist = [
    {"title": "Song 1", "artist": "Artist A", "duration": 240},
    {"title": "Song 2", "artist": "Artist B", "duration": 180},
    {"title": "Song 3", "artist": "Artist C", "duration": 320},
    {"title": "Song 4", "artist": "Artist A", "duration": 200},
    {"title": "Song 5", "artist": "Artist B", "duration": 280},
    {"title": "Song 6", "artist": "Artist C", "duration": 220},
]

playlist = quick_sort(playlist)

# Now the 'playlist' is sorted by song duration
for song in playlist:
    print(
        f"Title: {song['title']}, Artist: {song['artist']}, Duration: {song['duration']} seconds")
