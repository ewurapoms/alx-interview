#!/usr/bin/python3
""" function unlocks boxes """


def canUnlockAll(boxes):
    """  """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    for box_num in range(num_boxes):
        if not unlocked[box_num]:
            continue

        keys = boxes[box_num]
        for key in keys:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True

    return all(unlocked)
