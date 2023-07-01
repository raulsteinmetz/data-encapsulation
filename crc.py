crc_polynomium = "11010110"

def remove_non_significant_zeroes(str):
    i = 0
    broke = False
    while i < len(str):
        if str[i] == '1':
            str = str[i:]
            broke = True
            break
        i+= 1
    if not broke:
        return ""
    return str

def greater_or_equal_than(v1, v2):
    lv1 = remove_non_significant_zeroes(v1)
    lv2 = remove_non_significant_zeroes(v2)
    if len(lv1) > len(lv2):
        return True
    elif len(lv2) > len(lv1):
        return False
    else: #equal
        for i in range(len(lv1)):
            if lv1[i] == '1' and lv2[i] == '0':
                return True #greater
            elif lv1[i] == '0' and lv2[i] == '1':
                return False #less
        return True #equal


def subtract(v1, v2): #v1 - v2
    subtracted = ''
    mv2 = ('0'*(len(v1) - len(v2))) + v2 # fills v2 with non significant zeroes to make them have the same size
    lv1 = list(v1)
    lv2 = list(mv2) #creating lists so we can change the content
    i = len(v1) - 1 #v1 is always greather than v2
    while i >= 0:
        if lv1[i] == '1' and lv2[i] == '1':
            subtracted += '0'
        elif lv1[i] == '1' and lv2[i] == '0':
            subtracted += '1'
        elif lv1[i] == '0' and lv2[i] == '0':
            subtracted += '0'
        elif lv1[i] == '0' and lv2[i] == '1':
            subtracted += '1'
            j = i - 1
            while j >= 0:
                if lv1[j] == '1':
                    lv1[j] = '0'
                    break
                lv1[j] = '1'
                j -= 1

        i -= 1
    print(f'subtracted {v2} from {v1} and the result is {remove_non_significant_zeroes(subtracted[::-1])}')
    return remove_non_significant_zeroes(subtracted[::-1]) #reverses number

def xor(c1, c2):
    if c1 == "1" and c2 == "1":
        return "0"
    elif c1 == "1" and c2 == "0":
        return "1"
    elif c1 == "0" and c2 == "0":
        return "0"
    elif c1 == "0" and c2 == "1":
        return "1"

def xor_division(recDividend, divisor):
    dividend = list(recDividend)
    i = 0
    while i < len(dividend) - len(divisor) + 1:
        j = 0
        nextDividend = dividend[i]
        while j < len(divisor):
            if nextDividend == '0':
                break
            dividend[i+j] = xor(dividend[i+j], divisor[j])
            j+= 1
        i += 1
    return remove_non_significant_zeroes("".join(dividend))

def generate_crc(data, polynomium):
    #maybe transform the polynomium instead of just passing a binary divisor
    if len(polynomium) < 4:
        return
    division_data = data + ("0"*(len(polynomium)-1)) #evil string multiplication
    divisor = polynomium
    remainder = xor_division(division_data, divisor)
    generatedBin = data + remainder
    print(f'o binario gerado eh {generatedBin} com resto {remainder}')
    return generatedBin

def check_crc(encoded, polynomium):
    remainder = xor_division(encoded, polynomium)
    # print(f"o resto eh {remainder}")
    if len(remainder) == 0:
        return True
    else:
        print("Error in message CRC!")
        return False


if __name__ == '__main__':
    to_encode = "11100110111001101110011011100110"
    polynomium = "11010110"
    encoded = generate_crc(to_encode, polynomium)
    crc_right = check_crc(encoded, polynomium)
    print('Lenght of encoded: ', len(encoded))
    print('Original Lenght: ', len(to_encode))

