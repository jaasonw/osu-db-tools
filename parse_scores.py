import buffer
from buffer import WriteBuffer
from score import Beatmap, Score
from typing import List

def unpack_scores(filename: str):
    # https://osu.ppy.sh/help/wiki/osu!_File_Formats/Db_(file_format)#scores.db
    with open(filename, "rb") as db:
        version = buffer.read_uint(db)
        numOfMaps = buffer.read_uint(db)
        beatmaps = []
        for i in range(numOfMaps):
            beatmap = Beatmap()
            beatmap.scores = []
            beatmap.md5 = buffer.read_string(db)
            beatmap.num_scores = buffer.read_uint(db)
            for j in range(beatmap.num_scores):
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
                print(score.toJSON())
            beatmaps.append(beatmap)
    db.close()
    return (beatmaps, version)

def pack_scores(scores: List[Beatmap], version: int, filename: str):
    db = open(filename, "xb")
    b = WriteBuffer()
    b.write_uint(version)
    for beatmap in scores:
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

beatmaps, version = unpack_scores("scores.db")
# pack_scores(beatmaps, version, "repacked.db")
# beatmaps, version = unpack_scores("repacked.db")