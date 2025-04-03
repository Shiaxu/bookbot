def number_of_words(contents):
    words = contents.split()
    num_words = len(words)
    return num_words

def char_num_times(contents):
    dict = {}
    
    for char in contents:
        lower_case = char.lower()
        if lower_case in dict:
                dict[lower_case] += 1
        else:
                dict[lower_case] = 1
    return dict     

def sort_on(input):
    return input["num"]
    #return input["num"]


def sorted_dict(input_dict):
        combined_dict = []
        for char in input_dict:
        
            num = input_dict[char]
            new_dict = {}
            new_dict["char"] = char
            new_dict["num"] = num
            combined_dict.append(new_dict)
        combined_dict.sort(reverse=True, key=sort_on)
        return(combined_dict)

