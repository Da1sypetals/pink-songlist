import json
import copy
from songs import songs


def main():
    global songs

    def key(song):
        singers = song["singers"]
        return singers[0] if isinstance(singers, list) else singers

    try:
        songs = sorted(songs, key=key)
        print("Sorted songs by singers.")
    except Exception:
        print("Failed to sort songs, using original order.")
        pass

    seen_names = {}
    print("Checking for duplicate song names and printing on the fly:")

    duplicate_count = 0

    for song in songs:
        normalized_name = song["name"].lower().strip()

        if len(normalized_name) == 0:
            print("\n--- EMPTY SONG DETECTED ---")
            print("\Song Details:")
            for key, value in song.items():
                print(f"  {key}: {value}")
            print("-------------------------------\n")

        if normalized_name in seen_names:
            # Found a duplicate! Print information for both the original and the current duplicate immediately.
            duplicate_count += 1
            original_song_data = seen_names[normalized_name]["song_data"]

            print("\n--- DUPLICATE SONG DETECTED ---")
            print("Original Song Details:")
            for key, value in original_song_data.items():
                print(f"  {key}: {value}")

            print("\nDuplicate Entry Details:")
            for key, value in song.items():
                print(f"  {key}: {value}")
            print("-------------------------------\n")

        else:
            # First time seeing this song name (after normalization)
            seen_names[normalized_name] = {
                "original_name": song["name"],
                "song_data": copy.deepcopy(song),  # Store a deep copy of the full song data
            }

    # Generate the JSON file (proceeds as usual)
    with open("songs.json", "w", encoding="utf-8") as f:
        json.dump({"songs": songs}, f, indent=2, ensure_ascii=False)

    if duplicate_count > 0:
        print(f"\n{duplicate_count} suspected duplicate song(s) found!")
    else:
        print("No duplicate songs found!")
    print("songs.json generated successfully!")


if __name__ == "__main__":
    main()
