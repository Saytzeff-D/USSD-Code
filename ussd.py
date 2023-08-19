ussd_code = input('Enter a USSD Code: ')

def run_ussd():
    if ussd_code == '*302#':
        response = '''Press 1 to check balance,
        Press 2 to check airtime balance,
        Press 3 to quit'''
        print(response)
        check_code()
    else:
        print('Invalid service Code, Dial *302# to get started. Thank you!')
        quit()

def check_code():
    res = int(input(''))
    if res == 1:
        print('Dear, User! You have exhausted your airtime bundle')
    elif res == 2:
        print('You do not have an active data bundle')
    elif res == 3: 
        quit()
    else:
        print('Invalid Response, Try again')
        
        
run_ussd()