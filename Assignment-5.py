#Frication Calculator
print('Press 1 for sum of frication')
print('Press 2 for Subtraction of frication')
print('Press 3 for Multiplication of frication')
print('Press 4 for Divoision of frication')
choice = input()
nominator_first_num = int(input('Enter nominator for 1st number:   '))
denominator_first_num = int(input('Enter denominator for 1st number :  '))
nominator_second_num = int(input('Enter nominator for 2nd number:  '))
denominator_second_num = int(input('Enter denominator for 2nd number:  '))
nominator_result = 0
denominator_result = 0
final_result_nominator = 0
final_result_denominator = 0
message_out_put = ''
if choice == '1':
	nominator_result = nominator_first_num * denominator_second_num
	denominator_result = nominator_second_num * denominator_first_num
	final_result_nominator = nominator_result + denominator_result
	final_result_denominator = denominator_first_num * denominator_second_num
	message_out_put = '{} / {} '.format(final_result_nominator,final_result_denominator)
elif choice == '2':
	nominator_result = nominator_first_num * denominator_second_num
	denominator_result = nominator_second_num * denominator_first_num
	final_result_nominator = nominator_result - denominator_result
	final_result_denominator = denominator_first_num * denominator_second_num
	message_out_put = '{} / {} '.format(final_result_nominator,final_result_denominator)
elif choice == '3':
	nominator_result = nominator_first_num * nominator_second_num
	denominator_result = denominator_second_num * denominator_first_num
	message_out_put = '{} / {} '.format(nominator_result,denominator_result)
elif choice == '4':
	nominator_result = nominator_first_num * denominator_second_num
	denominator_result = denominator_first_num * nominator_second_num
	message_out_put = '{} / {}'.format(nominator_result,denominator_result)
else:
	message_out_put = 'invalid input'
print(message_out_put)