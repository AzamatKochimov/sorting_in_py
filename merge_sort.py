def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the playlist
        left_half = arr[:mid]  # Divide the playlist into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i]["duration"] < right_half[j]["duration"]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements are left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage:
playlist = [
    {"title": "Song 1", "artist": "Artist A", "duration": 240},
    {"title": "Song 2", "artist": "Artist B", "duration": 180},
    {"title": "Song 3", "artist": "Artist C", "duration": 320},
    {"title": "Song 4", "artist": "Artist A", "duration": 200},
    {"title": "Song 5", "artist": "Artist B", "duration": 280},
    {"title": "Song 6", "artist": "Artist C", "duration": 220},
]

merge_sort(playlist)

# Now the 'playlist' is sorted by song duration
for song in playlist:
    print(
        f"Title: {song['title']}, Artist: {song['artist']}, Duration: {song['duration']} seconds")
