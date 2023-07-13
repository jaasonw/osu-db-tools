# osu-db-tools

This is my collection of libraries and scripts for manipulating the osu! .db files.


## Installation
```
pip install git+https://github.com/jaasonw/osu-db-tools.git
```

I may or may not add more in the future, depending on my personal needs or future 
project ideas

Here's an overview of what's included so far

| Function                                                                   | Usage                                                                 |
| -------------------------------------------------------------------------- |-----------------------------------------------------------------------|
| Utility functions for reading/writing binary data from all osu `.db` files | `from osu_db_tools import buffer`                                     |
| Merging 2 `score.db` files                                                 | `python -m merge_scores <score_1.db> <score_2.db> <final_scores.db>` |
| Export `osu.db` beatmap data to an sqlite3 database                        | `python -m osu_to_sqlite <osu!.db>`                                  |
| Export `collection.db` to json                                             | `python -m read_collection.py <collection.db>`                          |
| Export `collection.db` to dict                                             | `from osu_db_tools.read_collection import read_collection` <br />` read_collection("collection.db")` |
