from distutils.command.clean import clean


class Solution:
    def reformatNumber(self, number: str) -> str:
        def get_new_format(number: str) -> str:
            if len(number) == 2:
                return number
            elif len(number) == 3:
                return number
            elif len(number) == 4:
                return f"{number[:2]}-{number[2:]}"
            while len(number) > 4:
                tmp = number[:3]
                number = number[3:]
                return tmp + "-" + get_new_format(number)

        clean_number = ''
        for char in number:
            if char.isnumeric():
                clean_number += char
        print(clean_number)
        return get_new_format(clean_number)


s = Solution()
print(s.reformatNumber("1-23-45 6"))
