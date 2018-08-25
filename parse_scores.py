import os
import sys
from typing import List

import buffer
from buffer import WriteBuffer
from score import Beatmap, Score


def unpack_scores(filename: str):
    # https://osu.ppy.sh/help/wiki/osu!_File_Formats/Db_(file_format)#scores.db
    with open(filename, "rb") as db:
        version = buffer.read_uint(db)
        numOfMaps = buffer.read_uint(db)
        beatmaps = []
        for _ in range(numOfMaps):
            beatmap = Beatmap()
            beatmap.scores = []
            beatmap.md5 = buffer.read_string(db)
            beatmap.num_scores = buffer.read_uint(db)
            for _ in range(beatmap.num_scores):
                score = Score()
                score.mode              = buffer.read_ubyte(db)
                score.version           = buffer.read_uint(db)
                score.md5               = buffer.read_string(db)
                score.player_name       = buffer.read_string(db)
                score.replay_md5        = buffer.read_string(db)
                score.num_300s          = buffer.read_ushort(db)
                score.num_100s          = buffer.read_ushort(db)
                score.num_50s           = buffer.read_ushort(db)
                score.num_gekis         = buffer.read_ushort(db)
                score.num_katus         = buffer.read_ushort(db)
                score.num_misses        = buffer.read_ushort(db)
                score.replay_score      = buffer.read_uint(db)
                score.max_combo         = buffer.read_ushort(db)
                score.perfect_combo     = buffer.read_bool(db)
                score.mods              = buffer.read_uint(db)
                score.empty_string      = buffer.read_string(db)
                score.timestamp         = buffer.read_ulong(db)
                score.negative_one      = buffer.read_uint(db)
                score.online_score_id   = buffer.read_ulong(db)
                
                beatmap.scores.append(score)
                # print(score.toJSON())
            beatmaps.append(beatmap)
    db.close()
    return (beatmaps, version)

def pack_scores(beatmap_scores: List[Beatmap], version: int, filename: str):
    try:
        os.remove(filename)
    except OSError:
        pass
    db = open(filename, "xb")
    b = WriteBuffer()
    b.write_uint(version)
    b.write_uint(len(beatmap_scores))
    for beatmap in beatmap_scores:
        b.write_string(beatmap.md5)
        b.write_uint(len(beatmap.scores))
        for score in beatmap.scores:
            b.write_ubyte(score.mode)
            b.write_uint(score.version)
            b.write_string(score.md5)
            b.write_string(score.player_name)
            b.write_string(score.replay_md5)
            b.write_ushort(score.num_300s)
            b.write_ushort(score.num_100s)
            b.write_ushort(score.num_50s)
            b.write_ushort(score.num_gekis)
            b.write_ushort(score.num_katus)
            b.write_ushort(score.num_misses)
            b.write_uint(score.replay_score)
            b.write_ushort(score.max_combo)
            b.write_bool(score.perfect_combo)
            b.write_uint(score.mods)
            b.write_string(score.empty_string)
            b.write_ulong(score.timestamp)
            b.write_uint(score.negative_one)
            b.write_ulong(score.online_score_id)

    db.write(b.data)
    db.close()
    pass

def merge_scores(maps1: List[Beatmap], maps2: List[Beatmap]):
    # the result should be the larger array
    if len(maps1) < len(maps2):
        swap = maps1
        maps1 = maps2
        maps2 = swap
    # disgustingly inefficient searching happening here
    for beatmap in maps1:
        if beatmap in maps2:
            counter = 0
            for _score in maps2[maps2.index(beatmap)].scores:
                if _score not in beatmap.scores:
                    beatmap.scores.append(_score)
                    counter += 1
                    # print(" added score from beatmap with hash:", beatmap.md5, "with timestamp: ", _score.timestamp)
            if counter > 0:
                print("added", counter, "score(s) from beatmap with hash:", beatmap.md5)
    for beatmap in maps2:
        if beatmap not in maps1:
            maps1.append(beatmap)
            # print("appended entire beatmap: ", beatmap, " with ", len(beatmap.scores), " scores")
            print("added", len(beatmap.scores), "score(s) from beatmap with hash:", beatmap.md5)
        beatmap.num_scores = len(beatmap.scores)
    return maps1

beatmaps1, version1 = unpack_scores(sys.argv[1])
beatmaps2, version2 = unpack_scores(sys.argv[2])

final = merge_scores(beatmaps1, beatmaps2)

pack_scores(final, version1 if version1 > version2 else version2, sys.argv[3])