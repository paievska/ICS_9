## **ЛАБОРАТОРНИЙ ПРОЕКТ**

_з дисципліни **"Уведення в компютерні науки"**_

Студента 1 курсу 5 групи ФІТ
**Паєвської Діани**

***

## **Завдання №5**

**ПОСТАНОВКА ЗАДАЧІ**

Розробити прорамне запезпечення(ПЗ), яке вирішує задачу розрахунку і аналізу руху основних засобів на основі вхідних даних з таблиць 1 і 2.

**Вимоги до ПЗ:**

1. Мова програмування - **PYTHON**

2. Вхідні дані розміщені в локальних текстових файлах

3. Результати представляються у вигляді:
   - Таблиці на екрані комп'ютера
   - Текстового файла на диску
   - Структурованого файла в форматі JSON
   - Excel таблиці
   - Графіка на екрані комп'ютера

4. В процесі роботи програма повинна мати можливість виводити на екран вхідні дані у вигляді відповідних таблиць (дивю табл. 1,2) та надавати можливість відбору записів із довідика по критерію.

### __Вхідні дані__

Таблиця 1

__Статистичні дані про ринкові ціни__

| **Дата** | **Код ринку** | **Ціна за картоплю** | **Ціна за капусту** | **Ціна за цибулю**| 
|:--------:|:-------------:|:--------------------:|:-------------------:|:-----------------:|
| 02.11.2016 | 100 | 45 | 50 | 70 |
|02.11.2016|200|35|30|50|
|02.11.2016|300|35|30|45|
|14.11.2016|100|45|45|60|
|14.11.2016|200|40|40|50|
|14.11.2016|300|35|35|45|
|22.11.2016|100|40|40|60|
|22.11.2016|200|40|40|50|
|22.11.2016|300|40|40|60|
***
Таблиця 2

**Довідник ринків**

|Код ринку|Найменування ринку|
|:-------:|:-----------------|
|100|Besarabskyi|
|200|Zhytnyi|
|300|Volodymyrskyi|
***
### __Вихідні дані__

Таблиця 3

**Аналіз середніх ринкових цін на основі продуктів споживчого кошика**

|Код ринку|Найменування ринку |Дата|Ціна за картоплю|Ціна за капусту|Ціна за цибулю|Середня ціна|
|--------:|:------------------|---:|---------------:|--------------:|-------------:|------:|
|100|Besarabskyi|02.11.2016|45|50|70|55.00|
|100|Besarabskyi|14.11.2016|45|45|60|50.00|
|100|Besarabskyi|22.11.2016|40|40|60|46.67|
|...|...|...|...|...|...|...|
|300|Volodymyrskyi|02.11.2016|35|30|45|36.67|
|300|Volodymyrskyi|14.11.2016|35|35|45|38.33|
|300|Volodymyrskyi|22.11.2016|40|40|60|46.67|
