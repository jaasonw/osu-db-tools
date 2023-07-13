import os
from typing import List
from typing import Dict

from osu_db_tools import buffer
from osu_db_tools.buffer import WriteBuffer
from osu_db_tools.score import Score


def unpack_scores(filename: str):
    # https://osu.ppy.sh/help/wiki/osu!_File_Formats/Db_(file_format)#scores.db
    with open(filename, "rb") as db:
        version = buffer.read_uint(db)
        numOfMaps = buffer.read_uint(db)
        beatmaps = {}  # beatmaps[md5] = [scores]
        for _ in range(numOfMaps):
            scores = []
            md5 = buffer.read_string(db)
            num_scores = buffer.read_uint(db)
            for _ in range(num_scores):
                score = Score()
                score.mode = buffer.read_ubyte(db)
                score.version = buffer.read_uint(db)
                score.md5 = buffer.read_string(db)
                score.player_name = buffer.read_string(db)
                score.replay_md5 = buffer.read_string(db)
                score.num_300s = buffer.read_ushort(db)
                score.num_100s = buffer.read_ushort(db)
                score.num_50s = buffer.read_ushort(db)
                score.num_gekis = buffer.read_ushort(db)
                score.num_katus = buffer.read_ushort(db)
                score.num_misses = buffer.read_ushort(db)
                score.replay_score = buffer.read_uint(db)
                score.max_combo = buffer.read_ushort(db)
                score.perfect_combo = buffer.read_bool(db)
                score.mods = buffer.read_uint(db)
                score.empty_string = buffer.read_string(db)
                score.timestamp = buffer.read_ulong(db)
                score.negative_one = buffer.read_uint(db)
                score.online_score_id = buffer.read_ulong(db)

                scores.append(score)
                # print(score.toJSON())
            beatmaps[md5] = scores
    db.close()
    return (beatmaps, version)


def pack_scores(beatmap_scores: Dict[str, List[Score]], version: int, filename: str):
    print("Packing scores to buffer")
    b = WriteBuffer()
    b.write_uint(version)
    b.write_uint(len(beatmap_scores))
    for md5 in beatmap_scores:
        b.write_string(md5)
        b.write_uint(len(beatmap_scores[md5]))
        for score in beatmap_scores[md5]:
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
    print("Writing scores to file")
    try:
        os.remove(filename)
    except OSError:
        pass
    db = open(filename, "xb")
    db.write(b.data)
    db.close()
    pass
