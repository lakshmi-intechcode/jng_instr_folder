def build_mcnugget_calc(nugget_sizes):
    calculator = []
    for size in nugget_sizes:
        for other in nugget_sizes:
            if size == other:
                continue
            # setting the arguments for the lambda to default values locks the values in
            calculator.append(lambda num,s=size,o=other: (num-o) > 0 and (num-o)%s == 0)
        calculator.append(lambda num,s=size: num > 0 and num%s == 0)
    def mcnugget_number(number):
        return any(equation(number) for equation in calculator)    
    return mcnugget_number
