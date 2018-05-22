
USA = 'USA'
USSR = 'USSR'
NEU = 'NEU'

# battlefield, stability, influence-USA, influence-USSR
country = {
    'UK': [False, 5, 5, 0],
    'France': [False, 3, 1, 0],
    'Canada': [False, 4, 2, 0],
    'Iraq': [True, 2, 0, 0]
}

region = {
    'Europe': {
        'Eastern Europe': [],
        'Western Europe': ['UK', 'France', 'Canada']
    },
    'Middle East': ['Iraq']
}