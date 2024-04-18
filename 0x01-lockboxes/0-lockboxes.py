#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Checks if each box may
    contain keys to the other boxes
    """

    if not boxes:
        return False

    keys = {0}
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.add(new_key)

    return len(keys) == len(boxes)
