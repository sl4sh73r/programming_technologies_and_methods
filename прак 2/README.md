![бипбоп](https://media.tenor.com/A44ug7s67TEAAAAC/food-noodles.gif) 

---
Реализовать в виде программы абстрактный тип данных «Граф» согласно варианту с учетом заданного представления графа. Операторы (операции) АТД «Граф» функционально должны выполнять следующие операции (названия операций – примерные) :
- 	FIRST(v) - возвращает индекс первой вершины, смежной с вершиной v. Если вершина v не имеет смежных вершин, то возвращается "нулевая" вершина .
- 	NEXT(v, i)- возвращает индекс вершины, смежной с вершиной v, следующий за индексом i. Если i — это индекс последней вершины, смежной с вершиной v, то возвращается.
- 	VERTEX(v, i) - возвращает вершину с индексом i из множества вершин, смежных с v.
- 	ADD_V(<имя>, <метка, mark>) - добавить УЗЕЛ 
- 	ADD_Е(v, w, c) - добавить ДУГУ (здесь c — вес, цена дуги (v,w))
- 	DEL_V(<имя>) - удалить УЗЕЛ
- 	DEL_Е(v, w) – удалить ДУГУ
- 	EDIT_V(<имя>, <новое значение метки или маркировки>) - изменить метку (маркировку) УЗЛА
EDIT_Е(v, w, <новый вес дуги>) - изменить вес ДУГИ

---

Реализовать задание (заданный алгоритм) с использованием методов АТД «Граф» (1 балл из 4)
| вар | Алгоритм | Способ представления графа | 
| --- | --- | --- |
| №46 | Вывести на экран все существующие пути в ациклическом орграфе | Матрица инцидентности |

| Оформление отчета не менее чем с двумя контрольными примерами, для каждого примера приводится рисунок (допускается скан рисунка «от руки» или изображение, построенное c помощью графического или специализированного редактора) графа). |
| --- |
| ![граф](https://github.com/sl4sh73r/programming_technologies_and_methods/blob/main/прак%202/46вар_graph.jpg) |

---


FIRST(v) - возвращает индекс первой вершины, смежной с вершиной v. Если вершина v не имеет смежных вершин, то возвращается "нулевая" вершина
```java
   public void first(T sourse) {
        System.out.println("первая смежная вершина с " + sourse + ":" + map.get(sourse).get(0));
    }
```
NEXT(v, i)- возвращает индекс вершины, смежной с вершиной v, следующий за индексом i. Если i — это индекс последней вершины, смежной с вершиной v, то возвращается.
```java
 public void nextValue(T sourse, int i) {
        if (map.containsKey(i + 1)) {
            if (map.get(sourse).isEmpty()) {//если в заданном значении ниче нет
                for (T kek : map.keySet()) {//проверяем для всех значений графа
                    if (map.get(kek).contains(sourse)) {//если кто-то из значений имеет наше значение
                        if ((int) kek > i) {//и если оно больше i
                            System.out.println(kek);//выводим его
                        }
                    }
                }
            }
            for (T kek : map.get(sourse)) {
                System.out.print(kek + ">" + i + ":");
                if ((int) kek > i) {
                    System.out.println("индекс вершины, смежной с вершиной " + sourse + ", следующий за индексом " + i + ": ");
                }
            }
        } else {
            System.out.println("такой вешины нет \uF04C");
        }
    }
```
ADD_V(<имя>, <метка, mark>) - добавить УЗЕЛ 
```java
 public void addVertex(T s, String mark) {
        markslist.put(s, mark);
        map.put(s, new LinkedList<T>());
    }
 ```
ADD_Е(v, w, c) - добавить ДУГУ (здесь c — вес, цена дуги (v,w))
```java
public void addEdge(T source, T destination, int weight, boolean bidirectional) {
        String indexEdge = (source + "" + destination);
        if (!map.containsKey(source)) addVertex(source);

        if (!map.containsKey(destination)) addVertex(destination);
        map.get(source).add(destination);
        weightlist.put(indexEdge, weight);
        if (bidirectional == true) {
            String indexEdgeRev = (destination + "" + source);
            map.get(destination).add(source);
            weightlist.put(indexEdgeRev, weight);
        }
    }
```
DEL_V(<имя>) - удалить УЗЕЛ
```java
public void deleteVertex(T s) {
        map.remove(s);
    }
```
DEL_Е(v, w) – удалить ДУГУ
```java
public void deleteEdge(T source, T destination) {
        map.get(source).remove(destination);
    }
```
