import math

# class Rep:
#     def __init__(self, payscale):
#         self.payscale = []


def calculate_sales_needed(payscale, target_earnings, cancellation_rate=0.2, avg_contract_value=700, recruits=0):
    if target_earnings <= 0:
        return 0
    
    debug = False
    # Sort the payscale based on the number of sales in ascending order
    payscale.sort(key=lambda x: x[0])
    
    # Initialize variables for tracking the total sales and total earnings
    total_earnings = 0
    lower_bound = 0

    # Iterate through the payscale to calculate earnings at each commission rate
    # Finding the lower bound of sales needed
    for i in range(len(payscale)):

        sales = payscale[i][0]
        commission_rate = payscale[i][1]

        # Calculate earnings for the current commission rate
        earnings = sales * (commission_rate) * avg_contract_value
        
        # Check if the total earnings exceed the target earnings
        if earnings <= target_earnings:
            lower_bound = i  # Convert to integer as it represents the number of sales needed
        else:
            break
    
    # Use lowerbound to find remaining sales
    total_sales_needed = payscale[lower_bound][0]
    if debug: print(total_sales_needed)
    commission_rate = payscale[lower_bound][1]
    if debug: print(commission_rate)
    total_earnings = total_sales_needed * commission_rate * avg_contract_value
    if debug: print(total_earnings)

    if total_earnings < target_earnings:
        earnings_left = target_earnings - total_earnings
        if debug: print(earnings_left)
        sales_left = math.ceil(earnings_left/(avg_contract_value*commission_rate))
        if debug: print(sales_left)
        total_sales_needed += sales_left

    if debug: print(total_sales_needed)
    total_sales_needed = math.ceil(total_sales_needed/(1-cancellation_rate))
    
    return total_sales_needed

def calculate_recruiting_override(recruits):
    # TODO: Finish function
    return 0