import os
import sys
path = os.path.join(".", "Resources", "budget_data.csv")
path2=os.path.join(".",)

# The total number of months included in the dataset


with open (path,"r") as file:
    
    header=file.readline()
    data=file.readlines()
    listdata=[row.strip().split(",") for row in data]
       
    #total_number_of_months=len(listdata)
    
    
   # End of number of months


#The net total amount of "Profit/Losses" over the entire period

profit_loss=[int(element[1]) for element in listdata]

sum_profit=sum(profit_loss)
#End of Total Amount

#The average of the changes in "Profit/Losses" over the entire period
pv=listdata[0]
total_change=0
greatest_increase=[]


for e in listdata:
    total_change += int(e[1]) - int(pv[1])
    greatest_increase.append(total_change)
    pv = e
    

average_profitloss=total_change / (len(listdata)-1)
                                   
index_max=greatest_increase.index(max(greatest_increase))
index_min=greatest_increase.index(min(greatest_increase))
date_value_max=listdata[index_max]
date_value_min=listdata[index_min]



print("Financaial Analysis")
print("-------------------")
print("Total months:  " + str(len(listdata)))
print("Total : " + str(sum(profit_loss)))
print("Average Change : $" + str(average_profitloss)) 
print("Greatest Increase in Profits : " + str(date_value_max))
print("Greatest Decrease in Profits : " + str(date_value_min))

output_file = os.path.join(".","Analysis","pybank_revenue.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('======================================================\n')
    datafile.write('|                  Financial Analysis                |\n')
    datafile.write('======================================================\n')
    datafile.write("Total months:  " + str(len(listdata))+"\n")
    datafile.write('======================================================\n')
    datafile.write("Total : " + str(sum(profit_loss)) +"\n")
    datafile.write('======================================================\n')
    datafile.write("Average Change : $" + str(average_profitloss)+"\n")
    datafile.write('======================================================\n')
    datafile.write("Greatest Increase in Profits : " + str(date_value_max)+"\n")
    datafile.write('======================================================\n')
    datafile.write("Greatest Decrease in Profits : " + str(date_value_min))
