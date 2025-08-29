def isPalindrome(x: int) -> bool:
        int_str=str(x)
        reverse_str=''
        for i in range(len(int_str)-1):
            print(int_str[-i])
            reverse_str+=int_str[-i]

isPalindrome(976479)