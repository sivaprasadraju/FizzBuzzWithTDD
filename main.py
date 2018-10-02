def fizz_buzz():
	
	Fizz_Buzz_List = []
	
	for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            Fizz_Buzz_List.append('FizzBuzz')
		elif index % 3 == 0:
            Fizz_Buzz_List.append('Fizz')
		elif index % 5 == 0:
            Fizz_Buzz_List.append('Buzz')