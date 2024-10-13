#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #: 0433704
#Student Name: Zachary Rudolf

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # Total Data Usage 	                        Rate of Charge 
    # Up to and including 200Mb 	                $20.00 flat rate 
    # Over 200Mb and up to and including 500Mb 	$0.105 per Mb 
    # Over 500Mb and up to and including 1Gb 	    $0.110 per Mb 
    # Over 1Gb 	                                $118.00 flat rate 
    usage=0.0
    cost=20.0
    costPerMb=0.0
    totalCost=0.0
    #greetings
    print("Welcome to Erewhon Mobile.")
    #input for data used
    usage=int(input("\nEnter data usage (Mb): "))
    #if statements to find cost
    if usage > 200 and usage <=500:
        costPerMb=(usage-200)*0.105
    elif usage > 500 and usage <= 1000:
        costPerMb=(usage-200)*0.110 
    elif usage > 1000:
        cost=118.00
    totalCost= cost+costPerMb
    #print command for output
    print("\nTotal charge is: ${0:,.2f}".format(totalCost)) 
    # YOUR CODE ENDS HERE

main()