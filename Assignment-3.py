#university fee 
university_fee_in_pound = 300
university_fee_in_pkr = round(300 * 196.31,2)
transcation_fee = round((9 / 100) * university_fee_in_pkr,2)
total_amount = university_fee_in_pkr + transcation_fee
print('Total amount is {} in pkr'.format(total_amount))