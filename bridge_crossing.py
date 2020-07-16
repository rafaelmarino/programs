# Bridge and torch problem

"""
Four friends (a, b, c, d) need to cross a bridge. 
A maximum of 2 people can cross at a time. 
It is night and they have just 1 lamp. 
People that cross the bridge must carry the lamp to see the way.
A pair must walk together at the speed of the slower person.

Travel times:
{'b': 2, 'a': 1,  'c': 7, 'd': 10}

What is the total minimum time required by the 4 friends to cross the bridge?

(a+d)(10) (-a)(1) (a+c)(7) (-a)(1) (a+b)(2) = 21
(c+d)(10) (-c)(7) (a+c)(7) (-a)(1) (a+b)(2) = 27
(c+d)(10) (-c)(7) (c+b)(7) (-b)(2) (a+b)(2) = 28
(a+b)(2) (-a)(1) (c+d)(10) (-b)(2) (a+b)(2) = 17
# Order matters! Use the 2 fastest travelers for ferrying the lamp;
# cluster by speed, slowest with slowest, fastest with fastest. 
"""

import itertools


def get_fastest_pair(dic_times):
    """Return the first two entries from an ordered dictionary."""
    fastest = list(dic_times.keys())[:2]
    return fastest


def get_slowest_pair(endpoint_list, dic_times):
    """
    Find the two slowest people and compute their crossing time.

    Args:
        endpoint_list: list containing person labels. 
        dict_times: a dictionary with crossing times, {person:time, ...}
    Returns:
        A tuple (x, y, sum, max) with: slowest person, 2nd slowest person, 
            sum of their combined crossing times, max of their combined 
            crossing times.
    
        The sum is the selection criterion used to find the slowest pair;
        the max is the time added to the stopwatch.
        This is a local solution at one point in time.
    """ 
    pairs = list(itertools.combinations(endpoint_list, 2))
    # (person1, person2, sum of times, max of time)
    # sum of times is to get the slowest pair together, but
    # crossing is simultaneous, so add the max 
    pairs = [(x, y, dic_times[x] + dic_times[y], \
        max(dic_times[x], dic_times[y])) for x, y in pairs]
    pairs.sort(key=lambda x: x[2])
    # pairs[-1]
    return pairs[-1]


def crossing_routine(dict_times):
    """ 
    Compute an optimal crossing routine according to the following algorithm:

    1. identify the two fastest runners
    2. cross with fastest runners
    3. cross back with the fastest runner available
    4. cross with slowest pair 
    5. cross back with remaining fastest runner
    6. cross with fastest runners again
    """
    # sort the dictionary of crossing times, fastest to slowest
    dict_times = {k:v for k, v in sorted(dict_times.items(), \
        key=lambda item: item[1])}

    # endpoint_a = ['a', 'b', 'c', 'd']
    endpoint_a = list(single_times.keys())
    endpoint_b = []
    stopwatch = 0
    print("Initial state: ", endpoint_a, endpoint_b, stopwatch)

    def cross(people):
        """Cross the specified pair of people from A to B."""
        for person in people:
            endpoint_a.remove(person)
            endpoint_b.append(person)
        return

    def cross_back(person):
        """Cross *back* the specified person from B to A.""" 
        endpoint_b.remove(person)
        endpoint_a.append(person)
        return

    # define the fastest runners. global solution 
    fastest_pair = get_fastest_pair(dict_times)
    fastest1, fastest2 = fastest_pair[0], fastest_pair[1]
    # are there people in A that need to cross?
    while endpoint_a:
        # if the two fastest runners are in A then send them to B
        if set(endpoint_a).issuperset(fastest_pair):
            cross(fastest_pair)
            stopwatch += max(dict_times[fastest_pair[0]], dict_times[fastest_pair[1]])
        # if not, then send the two slowest runners
        else:
            slowest_pair = get_slowest_pair(endpoint_a, dict_times)[:2]
            cross(slowest_pair)
            stopwatch += max(dict_times[slowest_pair[0]], dict_times[slowest_pair[1]])
        # are there still people in A that require a fast runner to cross back?
        if endpoint_a:
            # is the fastest in B? send him to A
            if fastest1 in endpoint_b:
                cross_back(fastest1)
                stopwatch += dict_times[fastest1]
            # if not, send the second fastest
            elif fastest2 in endpoint_b:
                cross_back(fastest2)
                stopwatch += dict_times[fastest2]
    print("Final state: ", endpoint_a, endpoint_b, stopwatch)
    return 


if __name__ == "__main__":
    single_times = {'b': 2, 'a': 1,  'c': 7, 'd': 10}
    # single_times = {'b': 1, 'a': 2, 'c': 3}
    crossing_routine(single_times)
