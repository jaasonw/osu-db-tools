# osu-db-tools

This is my collection of libraries and scripts for manipulating the osu! .db files.

I may or may not add more in the future, depending on my personal needs or future 
project ideas

Here's an overview of what's included so far

| Function                                                                   | Usage                                                                 |
| -------------------------------------------------------------------------- |-----------------------------------------------------------------------|
| Utility functions for reading/writing binary data from all osu `.db` files | import `buffer.py` into your python project                           |
| Merging 2 `score.db` files                                                 | `python3 merge_scores.py <score_1.db> <score_2.db> <final_scores.db>` |
| Export `osu.db` beatmap data to an sqlite3 database                        | `python3 osu_to_sqlite.py <osu!.db>`                                  |