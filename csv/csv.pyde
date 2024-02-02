csv = loadStrings('playlist.csv')
for entry in csv[1:]:  #[1:] skips the first entry and stars on the second line
    track=entry.split(',')
    print('{}. {}'.format(track[4],track[1]))
    
