#super naive
def lcm(a,b):
    greater = max(a,b)
    while True:
        if greater%a == 0 and greater%b == 0:
            return greater
        else:
            greater  +=1


# Effeicient

"""

Note that the GCD and LCM are related to each otehr using the following formula

a*b = gcd(a,b)*lcm(a,b)
"""


#
def effiecient_lcm(a,b):
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b, a%b)
    
    return (a*b)/gcd(a,b)

print(lcm(4,6))
