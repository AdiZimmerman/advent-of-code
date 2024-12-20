def part_one():
	with open('input.txt') as f:
		return parse(f.read())

def part_two():
	with open('input.txt') as f:
		return parse2(f.read())

def parse(s):
	ans = 0
	buf, first, sep, last = [], [], False, []
	for ch in s:
		if (len(buf) == 0 and ch == 'm') or (len(buf) == 1 and ch == 'u') or (len(buf) == 2 and ch == 'l') or (len(buf) == 3 and ch =='('):
			buf.append(ch)
		elif buf == ['m','u','l','(']:
			if ch.isdigit():
				if sep:
					last.append(ch)
				else:
					first.append(ch)
			elif ch == ',' and not sep:
				sep = True
			elif ch == ')' and sep:
				ans += int(''.join(first))*int(''.join(last))
				buf, first, sep, last = [], [], False, []
			else:
				buf, first, sep, last = [], [], False, []
		else:
			buf, first, sep, last = [], [], False, []
	return ans

def parse2(s):
	ans = 0
	buf, first, sep, last = [], [], False, []

	enabled = True
	buf_do = []

	for ch in s:
		if (len(buf) == 0 and ch == 'm') or (len(buf) == 1 and ch == 'u') or (len(buf) == 2 and ch == 'l') or (len(buf) == 3 and ch =='('):
			buf.append(ch)
		elif buf == ['m','u','l','(']:
			if ch.isdigit():
				if sep:
					last.append(ch)
				else:
					first.append(ch)
			elif ch == ',' and not sep:
				sep = True
			elif ch == ')' and sep:
				if enabled:
					ans += int(''.join(first))*int(''.join(last))
				buf, first, sep, last = [], [], False, []
			else:
				buf, first, sep, last = [], [], False, []
		else:
			buf, first, sep, last = [], [], False, []

		if (len(buf_do) == 0 and ch == 'd') or (len(buf_do) == 1 and ch=='o') or (len(buf_do) == 2 and (ch == '(' or ch == 'n')) or (len(buf_do) == 3 and (ch == ')' or ch == '\'')) or (len(buf_do) == 4 and ch == 't') or (len(buf_do) == 5 and ch == '(') or (len(buf_do) == 6 and ch == ')'):
			buf_do.append(ch)
		elif buf_do == ['d','o','(',')']:
			enabled = True
			buf_do = []
		elif buf_do == ['d','o','n','\'','t','(',')']:
			enabled = False
			buf_do = []
	return ans
