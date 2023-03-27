#!/usr/bin/python

import os
import re


def rename_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            new_filename = re.sub(r"[^\w\s]+", "_", filename)
            new_filename = re.sub(r"[_\s]+", "_", new_filename)
            new_filename = new_filename.rstrip("_")
            new_filename = new_filename.lower()
            new_filename = os.path.join(directory, new_filename)
            os.rename(os.path.join(directory, filename), new_filename)


rename_json_files("/home/bekas/Projects/spotify-stats/src/tests/data/plays")
