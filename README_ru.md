# BrainFur
## Что это вообще значит?
**BrainFur** — это диалект BrainFuck, написанный за одну ночь с нейросетями ради одной дурацкой идеи. Его синтаксис написан на [фёрбише](https://official-furby.fandom.com/wiki/Furbish_(language)), и каждая команда BrainFuck заменена на соответствующее слово из фёрбиша. Его код получится как минимум на 70 % милее и на 420 % больше! _(источник: поверь мне, бро)_

## Зачем?
> Потому что и фёрби, и brainfuck заставляют тебя сомневаться в правильности своих жизненных решений, так почему бы не совместить их?

## Синтаксис?
_Обратите внимание, что BrainFur можно табулировать и разбивать на строки, но это не обязательно._ 

<details markdown="1"><summary>Краткое описание синтаксиса</summary>

|   Furbish   | Brainfuck |         Эквивалент в C         | Буквальный перевод | Интерпретация в диалекте         |
|:-----------:|:---------:|:-------------------------------|:-------------------|:---------------------------------|
| **tee-toh** | *(start)* | `char arr[30000];`<br>`memset(arr, 0, sizeof(arr));`<br>`int i = 0;` | birthday           | Маркер начала программы          |
|   **dah**   |     `+`   | `arr[i]++;`                     | big                | Увеличить значение текущей ячейки |
|   **dee**   |     `-`   | `arr[i]--;`                     | little             | Уменьшить значение текущей ячейки |
| **tee-dah** |     `>`   | `i++;`                          | life + big         | Сдвинуть указатель вправо        |
| **tee-dee** |     `<`   | `i--;`                          | life + little      | Сдвинуть указатель влево         |
| **kah-nah** |     `.`   | `putchar(arr[i]);`              | place              | Вывести текущую ячейку как символ |
| **tah-tah** |     `,`   | `arr[i] = getchar();`           | receive            | Считать ввод пользователя в текущую ячейку |
| **ah-mah**  |     `[`   | `while (arr[i]) {`              | have               | Повторять пока ячейка ≠ 0     |
| **oo-bah**  |     `]`   | `}`                             | over               | Конец цикла                       |

</details>

## Пример кода
<details markdown="1"><summary>Код на BrainFur, выводящий "Hello, World!"</summary>

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
````

</details>

<details markdown="1"><summary>Тот же код на BrainFuck</summary>

```brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++
.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.
------.--------.>+.>.
```

</details>

## Как интерпретировать?

*Для запуска кода BrainFur нужен просто Python.*
В репозитории есть файл **brainfur.py**. Достаточно импортировать его (`import brainfur`) и вызвать функцию

```python
run_brainfur(code_to_execute, (необязательно)user_input)
```

<details markdown="1"><summary>Пример использования</summary>

```python
import brainfur

run_brainfur("tah-tah kah-nah", input())
```

</details>

## Что сделано и что осталось?

* [x] Придумать базовый язык
* [x] Написать интерпретатор на Python
* [x] Подготовить README
* [ ] Добавить поддержку комментариев
* [ ] Подсветку синтаксиса
* [ ] Спецификацию для esolang
* [ ] Простой веб‑плейграунд

> *И, возможно, ещё что‑нибудь…*

## Лицензия

Делай с этим, что хочешь, но указывай исходный проект и автора.

По сути — MIT License, см. файл LICENSE. :)