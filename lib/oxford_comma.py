def oxford_comma(elements):
    if len(elements) == 0:
        return ""
    elif len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        # Join all elements with commas and add "and" before the last element
        return f"{', '.join(elements[:-1])}, and {elements[-1]}"
