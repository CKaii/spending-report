import pandas as pd
import numpy as np

#imports bank statement
statement = pd.read_csv("PASTE YOUR BANK STATEMENT CSV HERE")
pd.set_option("display.max_rows", 125)

#sums total amount spent grouped by category
def categories():
    categories = statement.groupby(['Category'])
    return (categories['Debit'].agg(np.sum))

#sum total amount spent grouped by description
def description():
    description = statement.groupby(['Description'])
    return (description['Debit'].agg(np.sum))


print(categories())
print(description())
