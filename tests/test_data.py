import json

from collections import Counter
from os.path import exists


DATA_PATH = 'data/'
FILES = ['2021_starters.json']


def test_player_validation():
    seen_ids = Counter()
    for file in FILES:
        with open(DATA_PATH + file) as json_file:
            players = json.load(json_file)
            for player, player_data in players.items():
                # self.assertTrue('\'' not in player)
                assert '.' not in player, f'{player} has a period in its name'
                id_mod = player_data['id'] % 5
                pos = player_data['position']
                if id_mod == 0:
                    assert 'PG' == pos, f'{player}\'s position may be incorrect.'
                elif id_mod == 1:
                    assert 'SG' == pos, f'{player}\'s position may be incorrect.'
                elif id_mod == 2:
                    assert 'SF' == pos, f'{player}\'s position may be incorrect.'
                elif id_mod == 3:
                    assert 'PF' == pos, f'{player}\'s position may be incorrect.'
                elif id_mod == 4:
                    assert 'C' == pos, f'{player}\'s position may be incorrect.'
                # Check all IDs are unique
                seen_ids[player_data['id']] += 1
                assert seen_ids[player_data['id']] == 1, f'{player}\'s id is a duplicate.'
                # Check if has image
                assert exists(f'assets/images/2021_starters/{player.replace(" ", "_")}.jpg'), (f'{player} does '
                                                                                               'not have an image.')
