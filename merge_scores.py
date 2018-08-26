import sys
import time
from typing import Dict, List

from score import Score
from parse_scores import unpack_scores
from parse_scores import pack_scores

def merge_scores(maps1: Dict[str, List[Score]], maps2: Dict[str, List[Score]]):
    # the result should be the larger array
    if len(maps1) < len(maps2):
        swap = maps1
        maps1 = maps2
        maps2 = swap
    # i think this should be more efficient?
    for md5 in maps1:
        if md5 in maps2:
            counter = 0
            for score in maps2[md5]:
                if score not in maps1[md5]:
                    maps1[md5].append(score)
                    counter += 1
                if counter > 0:
                    print("added", counter,
                          "score(s) from beatmap with hash:", md5)
    for md5 in maps2:
        if md5 not in maps1:
            maps1[md5] = maps2[md5]
            print("added", len(maps2[md5]),
                    "score(s) from beatmap with hash:", md5)
    return maps1

if __name__ == "__main__":
    # beatmaps1, version1 = unpack_scores("scores.db")
    # pack_scores(beatmaps1, version1, "repacked.db")
    beatmaps1, version1 = unpack_scores(sys.argv[1])
    beatmaps2, version2 = unpack_scores(sys.argv[2])

    t0 = time.time()
    final = merge_scores(beatmaps1, beatmaps2)
    t1 = time.time()
    print("merge took:", t1 - t0, "seconds")

    pack_scores(final, version1 if version1 >
                version2 else version2, sys.argv[3])
