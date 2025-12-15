def parse_scores(path: str) -> list:
    with open(path) as data:
        try:
            return data.read().split(",")
        except:
            return "invalid path"

def throw_exception(scores: list, pass_threshold: float) -> str:
    if scores == "invalid path":
        return "Error. The provided file path does not exist."
    
    if not(0 <= pass_threshold <= 100):
        return "Error. The pass threshold is not between zero and 100."

    for score in scores:
        if type(score) != float:
            return "Error. The provided file contains non-numeric scores. Ensure that the list is comma-separated."
        
        if not(0 <= score <= 100):
            return "Error. The provided file contains scores not between 0 and 100."
        
    if scores == [""]:
        return "Error. The provided file is empty."

def convert_to_letters(scores: list) -> list:
    letters = []

    for score in scores:
        if score >= 90:
            letters.append("A")
        elif score >= 80:
            letters.append("B")
        elif score >= 70:
            letters.append("C")
        elif score >= 60:
            letters.append("D")
        else:
            letters.append("F")

    return letters

def calculate_average(scores: list) -> float:
    return sum(scores) / len(scores)

def analyse_scores(scores: list) -> str:
    pass_count = 0

    for score in scores:
        if score >= pass_threshold:
            pass_count += 1

    return f"""
    Scores: {",".join(scores)}
    Average: {average}, {convert_to_letters([average])[0]}
    Highest: {max(scores)}, {convert_to_letters([max(scores)])[0]}
    Lowest: {min(scores)}, {convert_to_letters([min(scores)])[0]}
    Pass count: {pass_count}
    """

if __name__ == "__main__":
    path = input("Please enter a file path: ")
    pass_threshold = float(input("Please enter a pass threshold: "))

    average = None
