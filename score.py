import json
from typing import List


class Score:
    mode = -1
    version = 0
    replay_md5 = ""
    player_name = ""
    num_300s = 0
    num_100s = 0
    num_50s = 0
    num_gekis = 0
    num_katus = 0
    num_misses = 0
    replay_score = 0
    max_combo = 0
    perfect_combo = False
    mods = 0
    empty_string = ""
    timestamp = 0
    negative_one = 0xffffffff
    online_score_id = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Beatmap:
    md5 = ""
    num_scores = 0
    scores: List[Score] = []

    def __eq__(self, other):
        return self.md5 == other.md5
