# Function to return all possible letter combinations
def letter_combinations(digits):
    # Mapping of digits to corresponding letters
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    
    # If the input is empty, return an empty list
    if not digits:
        return []
    
    # Backtracking function to generate combinations
    def backtrack(index, current_combination):
        # If we've processed all the digits, add the current combination to the result
        if index == len(digits):
            result.append(current_combination)
            return
        
        # Get the letters corresponding to the current digit
        current_digit = digits[index]
        for letter in digit_to_letters[current_digit]:
            # Continue building the combination
            backtrack(index + 1, current_combination + letter)
    
    result = []
    backtrack(0, "")
    return result

# Example usage
digits = "23"
combinations = letter_combinations(digits)

# Print the combinations
print(combinations)
