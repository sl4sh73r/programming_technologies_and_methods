![чумплумп](https://media.tenor.com/DUAGrJNlAUcAAAAC/fuu-samurai.gif) 

---
## Задание
В рамках домашней работы №1 требуется программно Реализовать в виде программы абстрактный тип данных «Дерево» согласно варианту. 
Пусть А, В, С – деревья соответствующего типа, узлы которых могут содержать целочисленные значения.
Требуется реализовать начальное формирование деревьев А и В, путем добавления некоторой последовательности значений (узлов) в пустое дерево.
После чего требуется по варианту реализовать заданную операцию над деревьями без использования каких-либо вспомогательных структур
работая только с узлами деревьев А и В. 

Операция А=A ⋃прB означает, что элементы дерева В будут добавлены в дерево А в прямом порядке обхода дерева В,
соответственно А=A ⋃обрB  – в обратном, а А=A ⋃симB  – симметричном обходе дерева В.
Операция А = A ⋂ B означает, что из дерева А исключаются узлы, отсутствующие в дереве В.


**Реализовать задание (заданный алгоритм) с использованием методов АТД «Деревья двоичного поиска»**
| вар | Тип дерева| Вывод деревьев на экран | Алгоритм |
| --- | --- | --- | --- |
| №46 | Оптимальное дерево двоичного поиска, А–обратный, В – симметричный | Левый сын, правый брат (таблица, массив) | С=A ⋃прB |
---

## Теоритическая часть
### Оптимальное древо поиска
***Дерево поиска*** называется оптимальным, если его цена минимальна. То есть оптимальное бинарное дерево поиска –это бинарное дерево поиска, построенное в расчете на обеспечение максимальной производительности при заданном распределении вероятностей поиска требуемых данных.
Существует подход построения оптимальных деревьев поиска, при котором элементы вставляются в порядке уменьшения частот, что дает в среднем неплохие деревья поиска. Однако этот подход может дать вырожденное дерево поиска, которое будет далеко от оптимального. Еще один подход состоит в выборе корня k таким образом, чтобы максимальная сумма вероятностей для вершин левого поддерева или правого поддерева была настолько мала, насколько это возможно. Такой подход также может оказаться плохим в случае выбора в качестве корня элемента с малым значением pk. 
Припишем каждой вершине дерева Vi вес wi, 
пропорциональный частоте поиска этой вершины. Сумма 
весов всех вершин дает вес дерева W. Каждая вершина Vi расположена на высоте hi, корень расположен на высоте 1. 
Высота вершины равна количеству операций сравнения, необходимых для поиска этой вершины. Определим средневзвешенную высоту дерева с n вершинами следующим образом(1.1):

$$
\begin{align}
  \tag{1.1}
  h_{ср}=(w_1h_1+w_2h_2+...+w_n+h_n)/W
\end{align}
$$

Дерево поиска, имеющее минимальную средневзвешенную высоту, называется деревом оптимального поиска.

**Пример.** Рассмотрим множество из трех ключей V1=1, V2=2, V3=3 со следующими весами: w1=60, w2=30, w3=10, W=100. Эти три ключа можно расставить в дереве поиска пятью различными способами.
![Пример](https://github.com/sl4sh73r/programming_technologies_and_methods/blob/main/прак%203/OBST_BE_LIKE.jpg) 

---

## Практическая часть
___Структура узла___
```java
static class Node{
        int KEY;
        Node left, right;
    }
```
___Обход древа___
```java
void preOrder(Node ROOT){
        if(ROOT != null) {
            System.out.print(ROOT.KEY+" ");
            preOrder(ROOT.left);
            preOrder(ROOT.right);
        }
    }
    ArrayList<Integer> B = new ArrayList<>();
    void inOrder(Node ROOT){
        if(ROOT != null) {
            inOrder(ROOT.left);
            B.add(ROOT.KEY);
            inOrder(ROOT.right);
        }
    }
    ArrayList<Integer> A = new ArrayList<>();
    void postOrder(Node ROOT){
        if(ROOT != null) {
            postOrder(ROOT.left);
            postOrder(ROOT.right);
            A.add(ROOT.KEY);
        }
    }
```
___Методы заполнения и построения оптимального древа___
```java
    public Node CONSTRUCT_OBST(int i, int j){
        Node p=new Node();
        if(i == j)
            p = null;
        else{
            p.KEY = KEYS[R[i][j]];
            p.left = CONSTRUCT_OBST(i, R[i][j] - 1); //left subtree
            p.right = CONSTRUCT_OBST(R[i][j], j); //right subtree
        }
        return p;
    }
    static void DISPLAY(Node ROOT, int nivel){
        int i;
        if(ROOT != null) {
            DISPLAY(ROOT.left, nivel + 1);
            for(i = 0; i <= nivel; i++)
                System.out.print(" ");
            System.out.println(ROOT.KEY);
            DISPLAY(ROOT.right, nivel+1);
        }
    }

void OPTIMAL_BINARY_SEARCH_TREE(int NUMBER_OF_KEYS)
    {
        float average_cost_per_weight;
        COMPUTE_W_C_R(NUMBER_OF_KEYS);
        System.out.println("C[0]="+C[0][NUMBER_OF_KEYS]+" "+"W[0]="+W[0][NUMBER_OF_KEYS]);
        average_cost_per_weight = C[0][NUMBER_OF_KEYS]/(float)W[0][NUMBER_OF_KEYS];
        System.out.println("The cost per weight ratio is:\n" + average_cost_per_weight);
        ROOT = CONSTRUCT_OBST(0, NUMBER_OF_KEYS);
        inOrder(ROOT);
        postOrder(ROOT);
        System.out.println("\nTree");
        DISPLAY(ROOT,0);
    }
```

___Метод расчета весов и цены___
```java
void COMPUTE_W_C_R(int NUMBER_OF_KEYS){

        int x, min;
        int i, j, k, h, m;
        //Construct weight matrix W
        for(i = 0; i <= NUMBER_OF_KEYS; i++) {
            W[i][i] = 0;
            for(j = i + 1; j <= NUMBER_OF_KEYS; j++)
                W[i][j] = W[i][j-1] + p[j];
        }

        //Construct cost matrix C and root matrix R
        for(i = 0; i <= NUMBER_OF_KEYS; i++)
            C[i][i] = W[i][i];
        for(i = 0; i <= NUMBER_OF_KEYS - 1; i++) {
            j = i + 1;
            C[i][j] = C[i][i] + C[j][j] + W[i][j];
            R[i][j] = j;
        }
        for(h = 2; h <= NUMBER_OF_KEYS; h++)
            for(i = 0; i <= NUMBER_OF_KEYS - h; i++) {
                j = i + h;
                m = R[i][j-1];
                min = C[i][m-1] + C[m][j];
                for(k = m+1; k <= R[i+1][j]; k++){
                    x = C[i][k-1] + C[k][j];
                    if(x < min) {
                        m = k;
                        min = x;
                    }
                }
                C[i][j] = W[i][j] + min;
                R[i][j] = m;
            }

        //Display weight matrix W
        System.out.println("\nThe weight matrix W:");
        for(i = 0; i <= NUMBER_OF_KEYS; i++){
            for(j = i; j <= NUMBER_OF_KEYS; j++)
                System.out.print(W[i][j]+" ");
            System.out.print("\n");
        }

        //Display Cost matrix C
        System.out.print("\nThe cost matrix C:\n");
        for(i = 0; i <= NUMBER_OF_KEYS; i++) {
            for(j = i; j <= NUMBER_OF_KEYS; j++)
                System.out.print(C[i][j]+" ");
            System.out.print("\n");
        }

        //Display root matrix R 8

        System.out.print("\nThe root matrix R:\n");
        for(i = 0; i <= NUMBER_OF_KEYS; i++) {
            for(j = i; j <= NUMBER_OF_KEYS; j++)
                System.out.print(R[i][j]+" ");
            System.out.print("\n");
        }
    }
```
---


