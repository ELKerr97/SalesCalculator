from money import calculate_sales_needed

rookie_payscale = [
    [0, 0.25], 
    [50, 0.27], 
    [85, 0.30],
    [115, 0.35],
    [200, 0.37],
    [250, 0.40],
    [300, 0.45],
    [350, 0.47],
    [400, 0.50]
    ]
experienced_payscale = [
    [0, 0.3], 
    [50, 0.32], 
    [85, 0.35],
    [115, 0.40],
    [200, 0.43],
    [250, 0.45],
    [300, 0.50],
    [350, 0.52],
    [400, 0.55]
    ]
custom_payscale = [
    [0,0.45],
    [200,0.5]
    ]

cancel_rate = 0.2
acv = 700

def should_return0_when_givenRookiePayScaleZeroTarget():
    print("Given $0 and Rookie Pay, should return 0:", end=' ')
    target_earnings = 0
    actual = calculate_sales_needed(rookie_payscale, target_earnings, cancel_rate,acv)
    expected = 0
    if actual != expected:
        print(f"FAILED. Actual: {actual}, Expected: {expected}")
    else:
        print("SUCCESS👍")

def should_return0_when_givenRookiePayScaleNegativeTarget():
    print("Given $-100 and Rookie Pay, should return 0:", end=' ')
    target_earnings = -100
    actual = calculate_sales_needed(rookie_payscale, target_earnings, cancel_rate,acv)
    expected = 0
    if actual != expected:
        print(f"FAILED. Actual: {actual}, Expected: {expected}")
    else:
        print("SUCCESS👍")

def should_return563_when_givenExpPayScaleAnd173250():
    print("Given $173250 and Experienced Pay, should return 563:", end=' ')
    target_earnings = 173250
    actual = calculate_sales_needed(experienced_payscale, target_earnings, cancel_rate,acv)
    expected = 563
    if actual != expected:
        print(f"FAILED. Actual: {actual}, Expected: {expected}")
    else:
        print("SUCCESS👍")

def should_return344_when_givenExpPayScaleAnd86625():
    print("Given $86625 and Experienced Pay, should return 344:", end=' ')
    target_earnings = 86625
    actual = calculate_sales_needed(experienced_payscale, target_earnings, cancel_rate,acv)
    expected = 344
    if actual != expected:
        print(f"FAILED. Actual: {actual}, Expected: {expected}")
    else:
        print("SUCCESS👍")

# Run tests
print("Running Tests\n")
should_return0_when_givenRookiePayScaleZeroTarget()
should_return0_when_givenRookiePayScaleNegativeTarget()
should_return563_when_givenExpPayScaleAnd173250()
should_return344_when_givenExpPayScaleAnd86625()
