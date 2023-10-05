# MainOverflowHQ Task

## String Compression Time Complexity

The initialization of variables `compressed`, `current_char`, and `curr_char_count` are constant time operations, i.e., O(1).
```python
def compress(uncompressed: str) -> str:
    compressed = []
    current_char = uncompressed[0]
    curr_char_count = 1
```

The function then enters a loop that runs for the length of the input string, starting from the second character. This is a linear operation, i.e., O(n), where n is the length of the input string.
```python
for i in range(1, len(uncompressed)):
```

Inside the loop, the function performs a series of operations: comparing the current character with the previous one, possibly appending to the `compressed` list, and updating `current_char` and `curr_char_count`. All these operations are constant time, i.e., O(1), within the loop.
```python
if current_char == uncompressed[i]:
    curr_char_count += 1
else:
    compressed.append(current_char)
    if curr_char_count > 1:
        compressed.append(str(curr_char_count))
    current_char = uncompressed[i]
    curr_char_count = 1
```

After the loop, the function performs a final series of operations to add the last character and its count to the `compressed` list and then join the list into a string. The string join operation is a linear operation, i.e., O(n), where n is the length of the `compressed` list.
```python
compressed += current_char
if curr_char_count > 1:
    compressed.append(str(curr_char_count))
return ''.join(compressed)
```

<br><br>
**TLDR**: Given that the loop is the dominant factor in the function and all operations inside the loop are constant time, the overall time complexity of the function is O(n), where n is the length of the input string.

## Network Failure Point Time Complexity

```python
def identify_router(network: Network) -> list[int]:
    max_connections = 0
    routers: list[int] = []
```
The function initializes `max_connections` and `routers` with a time complexity of O(1).

```python
    for _, router in network.routers.items():
```
It iterates over `n` routers in the network, giving a time complexity of O(n).

```python
        if router.total_connections > max_connections:
            max_connections = router.total_connections
            routers = [router.label]
        elif router.total_connections == max_connections:
            routers.append(router.label)
```
For each router, it checks and updates `max_connections` and `routers` in O(1) time.

```python
    return routers
```
Finally, it returns `routers` in O(1) time.

Overall, the time complexity of the `identify_router` function is O(n), where `n` is the number of routers in the network.