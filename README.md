# BrainFur
## What does it even mean?
BrainFur is an BrainFuck dialect, but vibecoded in one night just because of one stupid idea. Its syntax is written in [furbish](https://official-furby.fandom.com/wiki/Furbish_(language)) language, with every BrainFuck command replaced to an equivalent in furbish. It is observed to be at least 70% cuter and 420% larger! _(source: trust me bro)_

## Why?
> Because furbies and brainfuck both make you question your life choices, so why not put them together?

## Syntax?
_Note, that BrainFur can be tabulated and split in lines, but it doesn't have to._ 

<details markdown='1'><summary>Syntax summary</summary>

|   Furbish   | Brainfuck |         C Equivalent         | Literal Meaning | Interpretation in Dialect         |
|:-----------:|:---------:|:-----------------------------|:----------------|:----------------------------------|
| **tee-toh** | *(start)* | `char arr[30000];`<br>`memset(arr, 0, sizeof(arr));`<br>`int i = 0;` | birthday        | Program start marker              |
|   **dah**   |     `+`   | `arr[i]++;`                  | big             | Increment current cell value      |
|   **dee**   |     `-`   | `arr[i]--;`                  | little          | Decrement current cell value      |
| **tee-dah** |     `>`   | `i++;`                       | life + big      | Move pointer right                |
| **tee-dee** |     `<`   | `i--;`                       | life + little   | Move pointer left                 |
| **kah-nah** |     `.`   | `putchar(arr[i]);`           | place           | Output current cell as character  |
| **tah-tah** |     `,`   | `arr[i] = getchar();`        | receive         | Input character into current cell |
| **ah-mah**  |     `[`   | `while (arr[i]) {`           | have            | Start loop if cell is non-zero    |
| **oo-bah**  |     `]`   | `}`                          | over            | End loop                          |

</details>

## Sample code?
<details markdown='1'><summary>Code on BrainFur, which prints "Hello, World!"</summary>

```brainfur
tee-toh
dah dah dah dah dah dah dah dah dah dah
ah-mah
  tee-dah dah dah dah dah dah dah
  tee-dah dah dah dah dah dah dah dah dah dah dah
  tee-dah dah dah dah
  tee-dah dah
  tee-dee tee-dee tee-dee tee-dee
  dee
oo-bah
tee-dah dah dah
kah-nah
tee-dah dah
kah-nah
dah dah dah dah dah dah dah
kah-nah kah-nah
dah dah dah
kah-nah
tee-dah dah dah
kah-nah
tee-dee tee-dee
dah dah dah dah dah dah dah dah dah dah dah dah dah dah dah
kah-nah
tee-dah kah-nah
dah dah dah kah-nah
dee dee dee dee dee dee kah-nah
dee dee dee dee dee dee dee dee kah-nah
tee-dah dah kah-nah
tee-dah kah-nah
```

</details>

<details markdown='1'><summary>Same code on BrainFuck</summary>

```brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++
.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.
------.--------.>+.>.
```

</details>

## How to interpret?
_You need vanilla python to interpret BrainFur code._ 
There is a file, called **brainfur.py** in the GitHub repository. You simply import this file (`import brainfur`) and execute function **run_brainfur(code_to_execute, (optional)user_input)**. 

<details markdown='1'><summary>Sample code</summary>

```python
import brainfur

run_brainfur("tah-tah kah-nah", input())
```

</details>

## What is done, what is left?
- [x] Come up with basic language
- [x] Create an interpreter on python
- [x] Write a README
- [ ] Add support of comments
- [ ] Syntax highlighting
- [ ] Esolang spec (?)
- [ ] Simple web playground
>  _And maybe something else..._

## License?
Do what you want with it, but specify original project and author. 

Basically, MIT license, as seen in LICENSE file. :)
