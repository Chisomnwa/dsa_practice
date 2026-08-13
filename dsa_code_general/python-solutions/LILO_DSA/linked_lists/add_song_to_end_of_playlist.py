class Solution:
    def add_song_to_end(self, playlist: list[str], song: str) -> list[str]:
        """
        input: a playlist (a list of strings), and song (a string)

        output: a new playlist (a list of string) with song added at the end

        goal: to return an updated playlist after adding song to the end

        edge cases:
            - an empty list should return a list with only song in it

        Example walkthrough:

        Example A:
        ["Song A", "Song B"]

        head
          |
          ▼
        "Song A" -> "Song B" -> None

        To add: "Song C"

        The new update playslist:

        head
          |
          ▼
        "Song A" -> "Song B" -> "Song C" -> None

        Return = ["Song A", Song B", "Song C"]

        Pseudocode:
        Create a new playlist

        loop through the playlist:
            add each song to the new list

        add a new song

        return the new playlsit

        In code:
        updated = []

        for i in range(len(playslist)):
            updated.append(i)

        updated.append[song]

        return updated
        
        - - -
        Is this initial approach efficient?

        Yes, it is. In this approach, I am manually copying the songs into a new playlist, and finally adding
        the new song to the new playlist.

        Another approach could be using string concatenation in Python.

        How it works:
        updated = plalist + song

        But, we are still creating a new list in both cases and then returning a new playlist 
        with the new song to it. Both has O(n) space complexity, and O(n) time complexity.
        """
        # Return a new playlist with song added to the end.
        updated = []
        # YOUR CODE HERE
        n = len(playlist)

        # for value in playlist:
        #     updated.append(value)
        # updated.append(song)

        for i in range(n):
            updated.append(playlist[i])
        updated.append(song)

        return updated
