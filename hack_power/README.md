# Hack Power
Program that calculates the power of hacks from given string and returns the value, if not returns 0. 
- Given string can only contains letters from letters dictionary.
- Each letter has value. 
- Each repeated letter in a hack brings more power than its previous iteration.
- First instance of a letter in a hack is worth base power (for “b” it is 2), second instance of the letter is worth 2 times its base power, third instance of a letter is worth 3 times its base power, etc.
- Hack can get extra power from phrases dictionary.
- If phrases overlap — only the non-overlapping phrases generate power.

**Example**: 
```
letters = {'a': 1, 'b': 2, 'c': 3}
phrases = {'ba': 10, 'baa': 20}
```

| Hack | b | a | a | c | a |
| ------ | ------ | ------ | ------ | ------ | ------ |
| Letter power | 2 | 1 | 1 * 2 | 3 | 1 * 3 |
| "baa" phrase power |-|-| 20| | |

Hack “baaca” is worth 31 power.
