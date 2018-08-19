import buffer
from score import Beatmap
from score import Score

# https://osu.ppy.sh/help/wiki/osu!_File_Formats/Db_(file_format)#scores.db
with open("scores.db", "rb") as db:
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
            beatmap.scores.append(score)
            print(score.toJSON())
db.close()

