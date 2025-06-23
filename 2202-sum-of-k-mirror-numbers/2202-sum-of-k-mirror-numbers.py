class Solution:
    def kMirror(self, base: int, count: int) -> int:
        def next_symmetric(digits: list[str]) -> list[str]:
            half = len(digits) // 2  # Midpoint for symmetry
            for i in range(half, len(digits)):
                if int(digits[i]) + 1 < base:
                    # Increment and mirror
                    digits[i] = digits[~i] = str(int(digits[i]) + 1)
                    # Reset inner digits to '0'
                    for j in range(half, i):
                        digits[j] = digits[~j] = '0'
                    return digits
            # Increase length: '999' → '1001'
            return ['1'] + ['0'] * (len(digits) - 1) + ['1']

        current = ['0']  # Initial base-k symmetric number
        total = 0  # Sum of valid numbers

        for _ in range(count):
            while True:
                current = next_symmetric(current)  # Generate next base-k palindrome
                val = int(''.join(current), base)  # Convert to base-10
                if str(val) == str(val)[::-1]:     # Check base-10 palindrome
                    break
            total += val  # Add to sum

        return total