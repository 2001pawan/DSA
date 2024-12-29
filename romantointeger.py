
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """

        roman_values = {
                            'I': 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000
                        }

        
        n=len(s)
        ans=0
        
        #condition when its not like 4,9...(the small valued letter wont appear before high valued??)
        
        for i in range(n):
            if i<n-1 and roman_values[s[i]]<roman_values[s[i+1]]:
              
                    ans=ans-roman_values[s[i]]

            else:
                   ans=ans+roman_values[s[i]]
            
        return ans


              

print(romanToInt("III"))
print(romanToInt("DMVIII"))
    

