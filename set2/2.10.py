def number_of_words(line):
    words = line.split()
    return(len(words))

if __name__ == "__main__":
    line = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    In eget dui nulla. Mauris faucibus posuere ante ut gravida.
    Mauris faucibus volutpat dictum."""

    assert number_of_words(line) == 22

    line = """Nulla volutpat hendrerit sapien, at tempus ipsum efficitur non. 
    Duis blandit venenatis urna sit amet pulvinar. Morbi accumsan convallis sapien at
     rutrum. Nam ullamcorper semper dignissim. Nunc efficitur at risus in vestibulum.
      Sed elit urna, consequat dignissim ligula eu, posuere laoreet ante."""

    assert number_of_words(line) == 42

    line = """Lorem ipsum dolor sit amet, 
    consectetur                 adipiscing elit."""

    assert number_of_words(line) == 8
    