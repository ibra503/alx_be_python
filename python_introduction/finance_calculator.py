income = int(input( 'Enter your monthly income '))
expanses = int(input( 'Enter your monthly expanses '))
savings = income - expanses 
projected_savings = savings * 12 + (savings * 12 * 0.5)
print ("your monthly income is", income )
print ("your monthly expanses are", expanses )
print ("your monthly savings are", savings)
print ("your monthly savings after one year, with interest, is", projected_savings)