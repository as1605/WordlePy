# WordlePy

Python utilities to query and get stats from the loaded wordlist for NYTime's Wordle game

## Files

* `wordlist.csv` is scraped from the wordle source code's minified `main.js` file
* `wordle.py` contains functions to `load`, `query` and get `stats` for a list of words. Can also use alias `l`, `q`, `s`
* `245.ipynb` shows an example how this code can be used to solve wordle

## Example

```python
import wordle as wd

L = wd.load("wordlist.csv") # Can also do wd.load() or even wd.l()

print(wd.stats(L)) # or wd.s(L)

L1 = wd.query(L, contains = ['A','R'], not_contains=['I'], positions={4:'E'}, not_positions={2:'A', 3:'R'}) # or wd.q(...) 

print(L1)

print(wd.stats(L1))
```

## Results

Wordle 245 4/6

⬛⬛⬛🟨⬛
⬛⬛⬛🟨🟩
⬛⬛🟨⬛⬛
🟩🟩🟩🟩🟩

