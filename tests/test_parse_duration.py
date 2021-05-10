from facebook_scraper.utils import parse_duration

class TestParseDuration:
    durations = [
        'T26S',
        'T33M8S'
    ]

    def test_all_durations(self):
        for duration in self.durations:
            try:
                assert parse_duration(duration) is not None
            except AssertionError as e:
                print(f'Failed to parse {date}')
                raise e
