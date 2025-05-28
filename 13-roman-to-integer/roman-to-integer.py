class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0

        while i < len(s):
            # Get the value of the current symbol
            current_val = romanValues[s[i]]

            # Look ahead to the next symbol, if it exists
            if i + 1 < len(s):
                next_val = romanValues[s[i + 1]]
                # If the next value is larger, it's a subtractive case
                if current_val < next_val:
                    total += (next_val - current_val)
                    i += 2  # skip the next character
                    continue

            # Else just add the current value
            total += current_val
            i += 1

        return total
