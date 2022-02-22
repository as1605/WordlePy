# WordlePy

Python utilities to query and get stats from the loaded wordlist for NYTime's Wordle game

## Files

* `wordlist.csv` is scraped from the wordle source code's minified `main.js` file
* `wordle.py` contains functions to `load`, `query` and get `stats` for a list of words. Can also use alias `l`, `q`, `s`
* `245.ipynb` shows an example how this code can be used to solve wordle

## Example

```python
import wordle as wd

L = wd.load("wordlist.csv") 
# or wd.load() or even wd.l()

print(wd.stats(L)) 
# or wd.s(L)

L1 = wd.query(L, contains = ['A','R'], not_contains=['I'], positions={4:'E'}, not_positions={2:'A'})
# or wd.q(...) 

print(L1)

print(wd.stats(L1))
```
```
{'A': 975, 'C': 475, 'B': 280, 'E': 1230, 'D': 393, 'G': 310, 'F': 229, 'I': 670, 'H': 387, 'K': 210, 'J': 27, 'M': 316, 'L': 716, 'O': 753, 'N': 573, 'Q': 29, 'P': 365, 'S': 668, 'R': 897, 'U': 466, 'T': 729, 'W': 194, 'V': 152, 'Y': 424, 'X': 37, 'Z': 40}
['ADORE', 'AGREE', 'ARGUE', 'AROSE', 'AZURE', 'BARGE', 'CARVE', 'FARCE', 'LARGE', 'PARSE', 'RANGE']
{'A': 11, 'C': 2, 'B': 1, 'E': 12, 'D': 1, 'G': 5, 'F': 1, 'I': 0, 'H': 0, 'K': 0, 'J': 0, 'M': 0, 'L': 1, 'O': 2, 'N': 1, 'Q': 0, 'P': 1, 'S': 2, 'R': 11, 'U': 2, 'T': 0, 'W': 0, 'V': 1, 'Y': 0, 'X': 0, 'Z': 1}
```

## Results

### Wordle 245 4/6

⬛⬛⬛🟨⬛

⬛⬛⬛🟨🟩

⬛⬛🟨⬛⬛

🟩🟩🟩🟩🟩

### Wordle 246 3/6

🟨🟨⬛⬛⬛

🟨⬛⬛⬛🟩

🟩🟩🟩🟩🟩

### Wordle 247 4/6

⬛⬛⬛⬛🟨

⬛⬛🟨🟨🟨

🟨🟨⬛🟩🟩

🟩🟩🟩🟩🟩

### Wordle 248 3/6

⬛⬛⬛⬛⬛

⬛🟨🟩🟨⬛

🟩🟩🟩🟩🟩
