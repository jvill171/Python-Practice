def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    ltrCount = {}

    for ltr in phrase:
        ltrCount[ltr] = ltrCount.get(ltr, 0) + 1
        
    return ltrCount