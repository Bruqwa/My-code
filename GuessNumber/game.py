user_input = int(input('Enter range - from 0 to: '))
print('Now remember any number from entered range.')

def show_off(num):
    t = 0
    while num >= 1:
        num = int(num / 2)
	t += 1
	return t

tms = show_off(user_input)
print(f"I'll find your number from not more then {tms} time!")

def search(items):
    low = 0
    high = items
    times = 0	
    while low <= high:
	mid = int((low + high) / 2)
	print('Is it ', mid, '?')
	times += 1
	user_answer = input('Enter "yes" or "more" or "less": ')
	if user_answer == 'yes':
	    print('Got it! It is ', mid, '!')
	    print(f'I found the answer from {times} time!')
	    break
	elif user_answer == 'less':
	    high = mid - 1
	elif user_answer == 'more':
	    low = mid + 1
	else:
	    print("I didn't recognize your input.")
	    times -= 1
	    continue

search(user_input)
