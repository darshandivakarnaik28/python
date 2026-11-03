
insert(10, 500): Key 10 already exists, update its value to 500. Map = {10: 500}.
get(10): Key 10 exists with value 500, so return 500.
remove(10): Key 10 exists, remove key 10. Map = {}.
size(): The map is empty, so return 0.
Constraints:

1 ≤ queries.size() ≤ 103
1 ≤ queries[i].size() ≤ 3
0 ≤ queries[i][j] ≤ 103