numerals = {0:"零", 1:"一", 2:"二", 3:"三", 4:"四", 5:"五", 6:"六", 7:"七", 8:"八", 9:"九"}
thespecialcharacter = "."

def convert_to_decimal(dec_num):
    string_dec = str(dec_num)
    theindex = 0
    for i in range(len(string_dec)):
        if string_dec[i] == ".":
            theindex = i
            break
    frst_string = string_dec[:theindex]
    second_string = string_dec[theindex+1:]
    output_one = to_chinese_numeral(int(frst_string))
    output_two = ""
    for u in range(len(second_string)):
        output_two += numerals[int(second_string[u])]
    return output_one + "点" + output_two    
def convert_to_negative(x):
    return "负" + to_chinese_numeral(-x)

def to_chinese_numeral(n):
    if(n == 0):
        return "零"
    elif(n == 1):
        return "一"
    elif(n > 0):
        string_n = str(n)
        if(thespecialcharacter not in string_n):
            array = []
            for x in range(len(string_n)):
                appended_string = string_n[x] + (len(string_n)-x-1) * "0"
                array.append(appended_string)
            newarr = []
            for u in range(len(array)):
                if len(array[u]) == 5:
                    newarr.append(numerals[int(array[u][0])] + "万")
                elif len(array[u]) == 4:
                    newarr.append(numerals[int(array[u][0])] + "千")
                elif len(array[u]) == 3:
                    newarr.append(numerals[int(array[u][0])] + "百")
                elif len(array[u]) == 2:
                    newarr.append(numerals[int(array[u][0])] + "十")
                else:
                    newarr.append(numerals[int(array[u])])
            finarr = []
            for d in newarr:
                if d[0] != "零":
                    finarr.append(d)
                else:
                    finarr.append("零")     
            fin_string = "".join(finarr)
            if fin_string[0] == "一" and fin_string[1] == "十":
                fin_ten_string = ""
                for a in range(len(fin_string)):
                    if(a != 0):
                        if fin_string[a] != "零":
                            fin_ten_string += fin_string[a]
                return fin_ten_string             
            real_fin_string = ""
            if(len(string_n) >= 3):
                u = 0
                while u < len(fin_string): 
                    try:
                        if fin_string[u] == "零" and fin_string[u+1] == "零" and fin_string[u+2] == "零" and fin_string[u+3] == "零":
                            real_fin_string += "零"
                            u += 4
                        elif fin_string[u] == "零" and fin_string[u+1] == "零" and fin_string[u+2] == "零":
                            real_fin_string += "零"
                            u += 3
                        elif fin_string[u] == "零" and fin_string[u+1] == "零":
                            real_fin_string += "零"
                            u += 2
                        else:
                            real_fin_string += fin_string[u]
                            u += 1                                
                    except IndexError:        
                        try:
                            if fin_string[u] == "零" and fin_string[u+1] == "零" and fin_string[u+2] == "零":
                                real_fin_string += "零"
                                u += 3
                            elif fin_string[u] == "零" and fin_string[u+1] == "零":
                                real_fin_string += "零"
                                u += 2
                            else:
                                real_fin_string += fin_string[u]
                                u += 1                                
                        except IndexError:
                            try:
                                if fin_string[u] == "零" and fin_string[u+1] == "零":
                                    real_fin_string += "零"
                                    u += 2
                                else:
                                    real_fin_string += fin_string[u]
                                    u += 1
                            except IndexError:
                                real_fin_string += fin_string[u]
                                u += 1

            else:
                real_fin_string = fin_string
            if real_fin_string[-1] == "零":
                xstring = ""
                for i in range(len(real_fin_string)-1):
                    xstring += real_fin_string[i]
                return xstring    
            return real_fin_string

        else:
            return convert_to_decimal(n)
    else:
        return convert_to_negative(n)

ist = "y"
while ist.lower() == "y":
    user_input = float(input("\nWhat integer or decimal number do you want to convert into chinese?(less than 100000 and greater than -100000, exclusive):\n"))
    x = str(user_input)
    if(x[-1] == "0"):
        user_input = int(user_input) 
    print("\nYour number in Chinese is {}\n".format(to_chinese_numeral(user_input)))
    ist = input("Would you like to input another number?(type 'y' for yes, enter anything else for no): \n")