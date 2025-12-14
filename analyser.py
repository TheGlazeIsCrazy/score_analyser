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
    pass

def calculate_average(scores: list) -> float:
    pass

def analyse_scores(scores: list) -> float:
    pass

if __name__ == "__main__":
    path = input("Please enter a file path: ")
    pass_threshold = float(input("Please enter a pass threshold: "))
