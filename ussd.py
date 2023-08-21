print('Dial *312# to get started otherwise run exit()\n')
ussd_code = input('Enter a USSD Code: ')

def run_ussd():
    if ussd_code == '*312#':
        response = "\nWelcome to Test USSD Code\n1. Data Plans\n2. Enjoy 150MB for N100\n3. Social Bundles\n4. Business Plans\n5. Roaming/Int'l\n6. Borrow Credit/Recharge\n7. Gift Data\n8. Video Packs\n"
        print(response)
        check_code()
    else:
        print('\nInvalid USSD Code. Thank you!')
        quit()

def check_code():
    res = int(input(''))
    if res == 1:
        data_plans()
    elif res == 2:
        enjoy_150mb()
    elif res == 3: 
        socialbundles()
    elif res >8:
        print('\nInvalid Response, Please opt for numbers between 1-8')
        ussd_code = '*312#'
        run_ussd()
    else:
        print('\nService currently unavailable. Coming Soon!')

def data_plans():
    print("\nBuy Data Plans\n1.Daily\n2.Weekly\n3.Monthly\n4.5G Plans\n6.Hot Deals\n7.FREE Youtube\n8.Manage Data\n0.Back\n")
    res = int(input(''))
    if res == 0:
        ussd_code = '*312#'
        run_ussd()
    elif res > 8:
        print('\nInvalid Response, Please opt for numbers between 1-8')
        data_plans()
    else:
        print('\nComing Soon!')

def enjoy_150mb():
    print("\nEnjoy 150MB with N100.\nYou get 100MB + EXTRA 50MB Bonus. Data is valid for 1day. NO Bonus on autorenewal\n1.Activate\n0.Back\n")
    res = int(input(''))
    if res == 0:
        ussd_code = '*312#'
        run_ussd()
    elif res == 1:
        print('\n150MB activated successfully!')
    else:
        print('Invalid response')
        
def socialbundles():
    print("\nSocial Bundles\n1.WhatsApp\n2.Facebook\n3.Instagram\n4.Tiktok\n5.Opera Mini & News\n6.Youtube\n0.Back\n99.Next\n")
    res = int(input(''))
    if res == 0:
        ussd_code = '*312#'
        run_ussd()
    elif res == 99:
        print("\n7.2Go\n8.WeChat\n0.Back\n")
        res = int(input(''))
        if res == 0:
            socialbundles()
        else:
            print('\nComing Soon!')
    else: 
        print('\nService temporarily unavailable')
        
run_ussd()