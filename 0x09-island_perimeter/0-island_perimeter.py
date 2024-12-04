#!/usr/bin/python3
"""this module contains a function that solves the island perimiter problem"""

def island_perimeter(grid):
    def look_right(i: int, j: int):
        """
        a helper function that returns true if the
        next element right is 1
        """
        if j + 1 < len(grid[i]):
            if grid[i][j + 1] == 1:
                return True
        return False

    def find_first_configuration():
        """
        this function searches for the start of an island
        and it returns the position in wich it was found (the i or row)
        and a list of the blocks , each element is just the j in which
        1 wa found
        """
        flag_out = False
        for i in range(len(grid)):
            expected_connections = []
            for j in range(len(grid)):
                element = grid[i][j]
                if (element == 1):
                    expected_connections.append(j)
                    # keep lookin right
                    while look_right(i, j):
                        expected_connections.append(j + 1)
                        j = j + 1
                    flag_out = True
                    break
            if flag_out:
                return (i, expected_connections)

    def calc_initial_perimiter(len_first_configuration: int):
        """calculates the perimiter of the inital configuration"""
        term1 = (len_first_configuration * 4)
        term2 = ((len_first_configuration - 1) * 2)
        return term1 - term2

    def calc_perimiter_n(len_found_connection: int, connection_count: int):
        """
        calculates the perimiter of a found part(row) with respect
        to the previous connections
        """
        term1 = (len_found_connection * 4)
        term2 = ((len_found_connection - 1) * 2)
        term3 = (connection_count * 2)
        return term1 - term2 - term3

    # get the first configuration for the island
    i, first_configuration = find_first_configuration()
    # if we are at the limit of our grid vertically
    if i + 1 >= len(grid):
        # just return the perimiter of the configuration because
        # it's the island
        return calc_initial_perimiter(len(first_configuration))

    perimiter = calc_initial_perimiter(len(first_configuration))
    for i in range(i + 1, len(grid)):
        found_blocks = []
        connections_count = 0
        last_j = first_configuration[len(first_configuration)-1]
        # search for blocks that we expect a connection into first
        for j in range(len(grid[i])):
            element = grid[i][j]
            if element == 1:
                found_blocks.append(j)
                # we only add a connection if
                # we expect this block to be connected
                # to some other block at i - 1
                if j in first_configuration:
                    connections_count += 1

        # we add to the perimiter only when connection count is positive
        if connections_count > 0:
            perimiter += calc_perimiter_n(len(found_blocks), connections_count)

        # if no connection count , no need to go further
        if connections_count == 0:
            return perimiter

        # set the configuration for the next itter
        first_configuration = found_blocks
