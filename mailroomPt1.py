import sys
donors = {"Dulcie Pong": [100.98, 8.75, 1000.99],
"Susan Pong": [663.23, 423, 122.32],
"Minkie Bong": [663.23, 43.87, 1.32],
"Prince Nelson": [1000, 2000, 3000],
"MC Hammer": [6000, 500]}

prompt = "\n".join(("Welcome to your email command dashboard",
"Would you like to send a Thank You email or Create a Report?",
"Press 1 send a thank you email or Press 2 to see a Report or Press 3 to exit,\n"
">>>"))

def view_donors():
    print ("\n".join(donors))

def email_or_list():
    choice = input (" Would you like to send an email or see a list of donors?\n Press 1 to send an email or type 'list' to see a list\n Type 'q' to quit\n"
    ">>>")
    if choice == "q":
        main()
    if choice == "list":
        print()
        view_donors()
    if choice == "1":
        print ()
        new_donor_onboarding()

def new_donor_onboarding():
    donor = input("Whom would you like to send an email to?\n Or type 'q' to exit\n"
    ">>>")
    if donor == 'q':
        main()
    if donor in donors.keys():
        donation = int(input ("How much is the donation?"))
        donors[donor].append(donation)
        print (f"Thank you {donor} for your generous donation of ${donation} to keep us from going broke.  We'll be asking for more soon enough\n"
        "Sincerely\n"
        "The Ken Patner Foundation\n")
    elif donor not in donors.keys():
        donors[donor] = []
        donation = int(input ("How much is the donation?"))
        donors[donor].append(donation)
        print (f"Thank you {donor} for your generous donation of ${donation} to keep us from going broke.  \nWe'll be asking for more soon enough\n"
        "Sincerely\n"
        "The Ken Patner Foundation\n")

def donation_report():
    header = ("{:<30} | {:>15} | {:>20} | {:>30}".format("Donors", "Total Given", "Num Gifts", "Average Gift"))
    print (header)
    print (len(header)*("-"))
    for k,v in donors.items():
        total_donated= sum(v)
        num_donations = len(v)
        avg_donation = total_donated / num_donations       
        total_donated = ("$""{:.2f}".format(total_donated))
        avg_donation = ("$""{:.2f}".format(avg_donation))
        print (f"{k:<30} | {total_donated:>15} | {num_donations:>20} | {avg_donation:>30}")

#Donor Name                | Total Given | Num Gifts | Average Gift
#------------------------------------------------------------------
#William Gates, III         $  653784.49           2  $   326892.24
#Mark Zuckerberg            $   16396.10           3  $     5465.37
#Jeff Bezos                 $     877.33           1  $      877.33
#Paul Allen                 $     708.42           3  $      236.14


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        response = input(prompt)
        if response == "1":
            email_or_list()
        elif response == "2":
            donation_report()
        elif response == "3":
            exit_program()
        else:
            print ("not a valid option")


if __name__ == "__main__":
    main()
