def main():
    print("This program converts US dollars to Pounds Sterling")
    print()                # print a blank line


    dollars = eval(input("Enter amount in dollars: "))   # eval eta kno use korche???

    pounds = convert_to_pounds(dollars)

    print("That is: ",pounds,"pounds.")


convert_to_pounds = lambda dollars: dollars * 0.82

main()