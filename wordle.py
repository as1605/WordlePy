def load(fname = 'wordlist.csv'):
	a = open (fname, 'r')
	x = a.readlines()
	y = [w[:5] for w in x]
	return y

def query(wordlist = [], contains = [], not_contains = [], positions = {}, not_positions = {}):
	arr = []
	for w in wordlist:
		check = True
		for t in contains:
			if t not in w:
				check = False
		for t in not_contains:
			if t in w:
				check = False
		for t in positions:
			if w[t] != positions[t]:
				check = False
		for t in not_positions:
			if w[t] == not_positions[t]:
				check = False
			elif not_positions[t] not in w:
				check = False
		if check:
			arr.append(w)
	return arr

def stats(wordlist = []):
	count = { c:0 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
	for w in wordlist:
		for c in w:
			count[c] += 1
	out = dict(sorted(count.items(), key=lambda item: item[1]))
	return out


l = load
q = query
s = stats

