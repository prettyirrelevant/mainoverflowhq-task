def compress(uncompressed: str) -> str:
    """The function shortens a string by representing consecutive identical characters as the character and its count.

    Note:
        If a character only occurs once, its count will not be added to the compressed string.

    Params:
        uncompressed (str): The string to be compressed.

    Returns:
        str: The compressed string.
    """
    # Initialize the compressed string as an empty list
    compressed = []

    # Initialize the current character and its count
    current_char = uncompressed[0]
    curr_char_count = 1

    # Iterate over the uncompressed string, starting from the second character
    for i in range(1, len(uncompressed)):
        # If the current character is the same as the previous one, increment the count
        if current_char == uncompressed[i]:
            curr_char_count += 1
        else:
            # If the current character is different, add the previous character
            # and its count (if more than 1) to the compressed list
            compressed.append(current_char)
            if curr_char_count > 1:
                compressed.append(str(curr_char_count))

            # Update the current character and reset the count
            current_char = uncompressed[i]
            curr_char_count = 1

    # Add the last character and its count (if more than 1) to the compressed list
    compressed += current_char
    if curr_char_count > 1:
        compressed.append(str(curr_char_count))

    return ''.join(compressed)
