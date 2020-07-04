# https://www.codewars.com/kata/551dc350bf4e526099000ae5/solutions/python

def song_decoder(song):
    return " ".join([i for i in song.split("WUB") if i])
