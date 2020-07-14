try:
    import re
    import os
    import sys
except:
    print("Install required packages")


# Function which takes a word and checks if it is numeric type also returns the numeric value of the word.

def get_number_set(word, boolean = False):
    word = word.lower()
    order_1 = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    order_2 = {"ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, 
               "seventeen":17, "eighteen":18, "nineteen":19}
    power_1 = {"twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninty":90}
    power_2 = {"hundred":100, "thousand":1000, "million":1000000}
    other = {"point": -1, "and":" "}
    
    if boolean == True:
        return(word in order_1.keys() or word in order_2.keys() or word in power_1.keys() or word in power_2.keys())
    
    else:
        if word in order_1.keys():
            return(order_1[word], 1)
               
        if word in order_2.keys():
            return(order_2[word], 2)
               
        if word in power_1.keys():
            return(power_1[word], 3)
        
        if word in power_2.keys():
            return(power_2[word], 4)
        
        if word in other.keys():
            return(other[word], 5)
        
# Function which converts word to number        

def get_numbers(numbers):
    final_result = []
    result_temp = 0
    result = 0
    point_flag = 0
    point_count = 1
    number = numbers.split()
    
    Old_Type = -1
    for i in number:
        digit, Type = get_number_set(i)
        
        if point_flag == 1:
            Type = 5
        
        if Type == 1:
            if Old_Type == 2 or Old_Type == 1:
                final_result.append(result + result_temp)
                result_temp = digit
            else:
                result_temp += digit


        if Type == 2:
            if Old_Type != 1 and Old_Type != 2:
                result_temp += digit
            elif Old_Type == 1 or Old_Type == 2:
                final_result.append(result + result_temp)
                result_temp = digit

        if Type == 3:
            if Old_Type == 1:
                result_temp = (100 * result_temp) + digit
            elif Old_Type != 2:
                result_temp += digit
            else:
                final_result.append(result + result_temp)
                result_temp = digit
                
        if Type == 4:
            if Old_Type == 4:
                result *= digit
            else:
                result_temp *= digit
                result += result_temp
                result_temp = 0
            
        if Type == 5 and digit == -1:
            point_flag = 1
            result += result_temp + 0.0
            result_temp = 0
            Old_Type = 5
        
        if point_flag == 1 and digit != -1 and Type == 5:
            result_temp += digit * round((0.1) ** point_count, 8)
            point_count += 1
                      
          
        if point_flag == 0:
            Old_Type = Type
    
    final_result.append(result + result_temp)
    return(final_result)


# Function which takes a string finds the numeric word part of that and use "get_numbers" to convert it.

def word2num(string):
    new_string = ""

    flag = 0
    numbers = []
    number = ""
    words = string.split()
    end_count = len(words)
    
    if len(words) > 0:
        for word in words:
            end_count -= 1
            
            
            if get_number_set(word, boolean = True) or (word == "point" and flag == 1) or (word == "and" and flag == 1):
                flag = 1
                number += " " + word
                
            elif flag == 1:
                numbers = get_numbers(number)
                flag = 0
                number = ""
            
            if flag == 1 and end_count == 0:
                numbers = get_numbers(number)
                number = ""
                for i in numbers:
                    new_string += str(i) + " "
                numbers = []
            
            if flag == 0:             
                if len(numbers) > 0:
                    for i in numbers:
                        new_string += str(i) + " "
                    numbers = []
                new_string += word + " "
                
    return(merge_punct(new_string))


# Functions to control/handle punctuations' position

def seperate_punct(string):
    string =  re.sub("="," = ", string)
    string =  re.sub("-"," - ", string)
    string =  re.sub("/"," / ", string)
    string =  re.sub(","," , ", string)
    string =  re.sub("!"," ! ", string)
    string =  re.sub("@"," @ ", string)
    string =  re.sub("="," = ", string)
    string =  re.sub("&"," & ", string)
    string =  re.sub("#"," # ", string) 
    string =  re.sub(":"," : ", string)
    string =  re.sub(";"," ; ", string)
    string =  re.sub("\n"," \n ", string)
    return(string)




def merge_punct(string):
    string =  re.sub(" = ","=", string)
    string =  re.sub(" - ","-", string)
    string =  re.sub(" / ","/", string)
    string =  re.sub(" , ",", ", string)
    string =  re.sub(" ! ","!", string)
    string =  re.sub(" @ ","@", string)
    string =  re.sub(" = ","=", string)
    string =  re.sub(" & ","&", string)
    string =  re.sub(" # ","#", string) 
    string =  re.sub(" : ",": ", string)
    string =  re.sub(" ; ","; ", string)
    string =  re.sub(" \n ","\n", string)
    return(string)


# Function which takes a full document, split it by sentences and run "word2num" on that part

def document_to_number(document):
    new_document = ""
    sentences = document.split(".")
    for sentence in sentences:
        sentence = seperate_punct(sentence)
        new_document += word2num(sentence)[:-1] + "." + " "
    return(new_document)


if __name__ == "__main__":
    try:
        input_path = (sys.argv[1])
    except:
        print("Order should be:: \npython txt2num.py <input path of txt file> <Output path (optional)>")
        sys.exit(0)
    
    try:
        output_path = (sys.argv[2])
    except:
        output_path = os.getcwd()
        print("Default output directory set as:: \n", output_path)
        
    input_dir = open(input_path, "r")
    file = input_dir.read()
    input_dir.close()
    
    output = document_to_number(file)
    
    output_dir = open(output_path + r"\output.txt", "w")
    output_dir.write(output)
    output_dir.close()




































