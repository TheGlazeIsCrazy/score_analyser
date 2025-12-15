def parse_scores(path: str) -> list: # This returns an arbitrarily long list of strings.
    try:
        with open(path) as data: # This automatically closes the file after the scores are parsed.
            return data.read().split(",")
    except:
        return "invalid path" # This tells the throw_exception(scores, pass_threshold) function that the file path doesn't exist.

def throw_exception(scores: list, pass_threshold: float) -> str:
    if scores == "invalid path":
        return "Error. The provided file path does not exist."
        
    if scores == [""]:
        return "Error. The provided file is empty."
    
    if not(0 <= pass_threshold <= 100):
        return "Error. The pass threshold is not between zero and 100."

    for score in scores: # This handles non-numeric scores and invalid scores in a single loop.
        if type(score) != float:
            return "Error. The provided file may contain non-numeric scores. If this is not the case, ensure that the list is comma-separated." # This error message also considers formatting mistakes, like space-separated lists.
        
        if not(0 <= score <= 100):
            return "Error. The provided file contains scores not between 0 and 100."

def convert_to_letters(scores: list) -> list: # This returns two arbitrarily long lists of strings.
    letters = []
    counts = [0, 0, 0, 0, 0] # The first element is the number of "A"s, the second is the number of "B"s, etc.

    for score in scores: # This loop is based on a common US percentage scale.
        if score >= 90:
            letters.append("A")
            counts[0] += 1
        elif score >= 80:
            letters.append("B")
            counts[1] += 1
        elif score >= 70:
            letters.append("C")
            counts[2] += 1
        elif score >= 60:
            letters.append("D")
            counts[3] += 1
        else:
            letters.append("F")
            counts[4] += 1

    return letters, counts

def calculate_average(scores: list) -> float:
    return sum(scores) / len(scores)

def analyse_scores(scores: list) -> str: # Most of the statistics are calculated directly inside the f-string.
    pass_count = 0

    for score in scores:
        if score >= pass_threshold:
            pass_count += 1

    return f"""
    A: {counts[0]},
    B: {counts[1]},
    C: {counts[2]},
    D: {counts[3]},
    F: {counts[4]}.

    Scores: {",".join(parsed_scores)}
    Average: {average}, {convert_to_letters([average])[0][0]}
    Highest: {max(scores)}, {convert_to_letters([max(scores)])[0][0]}
    Lowest: {min(scores)}, {convert_to_letters([min(scores)])[0][0]}
    Pass count: {pass_count}.
    """

    # Line 54 puts the variable average inside a list in order to satisfy the convert_to_letters(scores) function.
    # The above function returns two lists of strings, which each have a length of 1, in this case.
    # To format this as a string instead of a 1-element list, for aesthetic purposes, [0][0] is used to return a string.
    # Therefore, the full formatting is: f"Average: {average}, {convert_to_letters([average])[0][0]}"

    # A similar principle is used on lines 55 and 56.

if __name__ == "__main__":
    path = input("Please enter a file path: ")
    pass_threshold = float(input("Please enter a pass threshold: "))

    parsed_scores = parse_scores(path)

    scores = [] # This list will contain a usable version of the parsed scores, converting each score into a float if possible.

    if parsed_scores == "invalid path":
        scores = "invalid path"
    else:
        for to_parse in parsed_scores:
            try:
                scores.append(float(to_parse))
            except:
                scores.append(to_parse) # If a score can't be converted into a float, the score is appended to the list scores.
                                        # Any unconverted scores will be discovered to be invalid by the throw_exception(scores, pass_threshold) function.

    exception = throw_exception(scores, pass_threshold)

    if exception:
        print(exception)
    else:
        letters, counts = convert_to_letters(scores)
        average = calculate_average(scores)

        print(analyse_scores(scores))
