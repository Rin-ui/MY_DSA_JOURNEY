def construct_subset(input_str, output_str):
    # base case
    if input_str =="":
        print(output_str)
        return
    ch = input_str[0]
    #include 1st char of string in output
    construct_subset(input_str[1:], output_str + ch)
    # exclude 1st char of string in o/p
    construct_subset(input_str[1:], output_str)

construct_subset("abc","")

    
