#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Checks if each box may contain keys to the other boxes
    """

    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        box = queue.pop()
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)
                if all(visited):
                    return True
    return all(visited)
