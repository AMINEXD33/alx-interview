def canUnlockAll(boxes):
    count = 1
    cach = {}
    for box_index in range(len(boxes)):

        for key in boxes[box_index]:
            if key == box_index:
                count += 1
            else:
                # cache the key
                cach[key] = True

        if cach.get(box_index):
            count += 1
    if count == len(boxes):
        return True
    return False
