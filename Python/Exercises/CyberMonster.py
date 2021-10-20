
import string

signs = string.digits+string.punctuation+'\n'

Dict = {'s': 'L', 'b': 's', 'w': 'O', 'z': 'G', 'c': 'o', 'J': 'y', 'V': 't', 'P': 'w', 'B': 'f', 'Z': 'q', 'F': 'k', 'O': 'N', 'u': 'A', 'W': 'r', 'K': 'K', 'a': 'D', 'v': 'l', 'g': 'S', 'f': 'x', 'x': 'c', 'N': 'e', 'p': 'b', 'U': 'a', 'j': 'P', 'o': 'Q', 'i': 'I', 'M': 'd', 't': 'U', 'H': 'V', 'X': 'i', 'Y': 'T', 'R': 'H', 'h': 'X', 'L': 'z', 'G': 'F', 'A': 'W', 'm': 'n', 'T': 'u', 'l': 'B', 'C': 'Z', 'q': 'p', 'D': 'v', 'I': 'g', 'n': 'h', 'y': 'C', 'S': 'j', 'k': 'M', 'd': 'J', 'Q': 'E', 'e': 'Y', 'r': 'R', 'E': 'm'}

new_Dict= {}
for key,value in Dict.items():
    new_Dict[value] = key
print(new_Dict)
#Text = "YXu0hYq1xQ4,hQXUCw8Cs7nIu8BAxIUADYf\n\nLRYUYw5LI0RYUUYs6hDXU3UIoIBbcm\n. CBSA5LI7RYUUYs2hDXU8YBbnIj\n.UIoIBbnI2LI8RYUUYs7hDXU2cYBbnQZ\n.cYBbnQo1LI9R YUUYs7hDXU4UDBk\n.JYUDoIBbnQo4LI3RYUUYs8hDXU6YLRDbj\n.JYULYh8LI3RYUUYs8h DXU1CUIBIsDJDYH\n.YLhYJ7BDIoYbj\n.LUhAQo0LYLDo3U'hYRD2BDIoYbL2XSAQhY0QU0 MDYRs0YXU4XSAQXUBW\n.LYBAR8CUIBDoIUoDRb1LUDYs2LRQRRm\n.CUIRAb3JBAQXL 6RYlYh9LLDb0LLYBha\n.CBUhYBIL0CBUIoIBbcY9hg\n.JYohYBIL1YXU5YoDx7xQ6,CUIASIs nD8YLAxYR0YXU9hQIUDUbnYU4QU3YRYXu\n.LLYAS1JBAQXL7Ys3-- YhQ2JhD2CBsDRYxYRb2CBhQ9YhQ6LAQIlsQ-- 9CDO7QU1QJ0XSAQXUBW\n.UI4UDXU5CDO0CDn2UQh7Ys2LAQIlsQ0UD2ULRIx8LLYBhA2 YR'AQC1OQe\n.XoUAv7LI3RYUUYs0hDXU8XSAQXUBW\n.RYlYh0RYlYh5LI9hYUxQ0RYUU Ys2hDXU8*UXSIR*9xg\n.OQh4YXU3hQIUDUhYnYBbnI9LI1JRDX0QU6,hIDBbcY5L'UI3D7JDs 6xg\n.DYJI4YXU6hQIUDUhYnYBbnI9LI9CLDY4QU3,hIDBbcY2UI5CDn4Ys8D8JQQS1LYoDbL YnDe\n.DYJI0YRD9YhQ6ShIMhQX2UDYRS4DYJI3--9L'UYB5QJ8YRQn9xQ0!YLQXU"
Text = "YXu0hYq1xQ4,hQXUCw8Cs7nIu8BAxIUADYf\n\nLRYUYw5LI0RYUUYs6hDXU3UIoIBbcm\n.CBSA5LI7RYUUYs2hDXU8YBbnIj\n.UIoIBbnI2LI8RYUUYs7hDXU2cYBbnQZ\n.cYBbnQo1LI9RYUUYs7hDXU4UDBk\n.JYUDoIBbnQo4LI3RYUUYs8hDXU6YLRDbj\n.JYULYh8LI3RYUUYs8hDXU1CUIBIsDJDYH\n.YLhYJ7BDIoYbj\n.LUhAQo0LYLDo3U'hYRD2BDIoYbL2XSAQhY0QU0MDYRs0YXU4XSAQXUBW\n.LYBAR8CUIBDoIUoDRb1LUDYs2LRQRRm\n.CUIRAb3JBAQXL"
sentence  = []
letter = ""
for ch in Text:
    if ch in signs:
        if ch == '\n':
            sentence.append("\n")
        sentence.append(letter[::-1])
        sentence.append(" ")
        letter = ""
    else:
        letter += new_Dict[ch]
    print(sentence)
print("".join(sentence))
