import java.util.*;

import static java.lang.System.exit;
import static java.lang.System.setOut;
/*      1.	FIRST(v) - возвращает индекс первой вершины, смежной с вершиной v. Если вершина v не имеет смежных вершин, то возвращается "нулевая" вершина .
        2.	NEXT(v, i)- возвращает индекс вершины, смежной с вершиной v, следующий за индексом i. Если i — это индекс последней вершины, смежной с вершиной v, то возвращается .
        3.	VERTEX(v, i) - возвращает вершину с индексом i из множества вершин, смежных с v.
        4.	ADD_V(<имя>, <метка, mark>) - добавить УЗЕЛ
        5.	ADD_Е(v, w, c) - добавить ДУГУ (здесь c — вес, цена дуги (v,w))
        6.	DEL_V(<имя>) - удалить УЗЕЛ
        7.	DEL_Е(v, w) – удалить ДУГУ
        8.	EDIT_V(<имя>, <новое значение метки или маркировки>) - изменить метку (маркировку) УЗЛА
        9.	EDIT_Е(v, w, <новый вес дуги>) - изменить вес ДУГИ*/

class Graph<T> {

    // Мы используем Hashmap для хранения ребер в графе

    private Map<T, List<T>> map = new HashMap<>();
    private Map<T,String> markslist=new HashMap<>();
    private Map<String,Integer> weightlist=new HashMap<>();
    //добавить узел
    public void addVertex(T s){
        map.put(s, new LinkedList<T>());
    }
    //добавить узел и (маркер)
    public void addVertex(T s,String mark){
        markslist.put(s,mark);
        map.put(s, new LinkedList<T>());
    }

    // Эта функция создает дугу
    // между source и destination
    public void addEdge(T source,
                        T destination,
                        int weight,
                        boolean bidirectional)
    {
        String indexEdge=(source +""+ destination);
        if (!map.containsKey(source))
            addVertex(source);

        if (!map.containsKey(destination))
            addVertex(destination);
        map.get(source).add(destination);
        weightlist.put(indexEdge,weight);
        if (bidirectional == true) {
            String indexEdgeRev=(destination +""+ source);
            map.get(destination).add(source);
            weightlist.put(indexEdgeRev,weight);
        }
    }

    public void addEdge(T source,
                        T destination,
                        String mark1,
                        String mark2,
                        int weight,
                        boolean bidirectional)
    {
        String indexEdge=(source +""+ destination);
        if (!map.containsKey(source))
            addVertex(source,mark1);

        if (!map.containsKey(destination))
            addVertex(destination,mark2);

        map.get(source).add(destination);
        weightlist.put(indexEdge,weight);
        if (bidirectional == true) {
            String indexEdgeRev=(destination +""+ source);
            map.get(destination).add(source);
            weightlist.put(indexEdgeRev,weight);
        }
    }
    //удалить узел
    public void deleteVertex(T s){
        map.remove(s);
    }
    //удалить дугу
    public void deleteEdge(T source, T destination){
        map.get(source).remove(destination);
    }
    // Эта функция дает количество вершин
    public void getVertexCount()
    {
        System.out.println("У графа "
                + map.keySet().size()
                + " вершин(ы)");
    }

    // Эта функция дает количество ребер
    public void getEdgesCount(boolean bidirection)
    {
        int count = 0;
        for (T v : map.keySet()) {
            count += map.get(v).size();
        }
        if (bidirection == true) {
            count = count / 2;
        }
        System.out.println("у графа "
                + count
                + " ребер.");
    }

    // Эта функция дает условие вершин
    // вершина есть или нет.
    public void hasVertex(T s)
    {
        if (map.containsKey(s)) {
            System.out.println("у графа есть "
                    + s + " вершина.");
        }
        else {
            System.out.println("У графа нет "
                    + s + " вершины");
        }
    }
    // Эта функция показывает, присутствует ли ребро или нет.
    public boolean hasEdge(T s, T d)
    {
        if (map.get(s).contains(d)) {
            return true;
        }
        else {
            return false;
        }
    }
    public void nextValue(T sourse,int i){
        if (map.containsKey(i+1)){
            if (map.get(sourse).isEmpty()){//если в заданном значении ниче нет
                for (T kek:map.keySet()){//проверяем для всех значений графа
                    if (map.get(kek).contains(sourse)){//если кто-то из значений имеет наше значение
                        if ((int)kek>i){//и если оно больше i
                            System.out.println(kek);//выводим его
                        }
                    }
                }
            }
            for (T kek:map.get(sourse)){
                System.out.print(kek+">"+i+":");
                if ((int)kek>i){
                    System.out.println("индекс вершины, смежной с вершиной "+ sourse+", следующий за индексом "+ i+": ");
                }
            }
        }else {System.out.println("такой вешины нет \uF04C");}
    }
    public void first(T sourse) {
        System.out.println("первая смежная вершина с "+ sourse + ":" + map.get(sourse).get(0));
    }

    public void editVertex(int index,String mark){
        for(T keys: map.keySet()){
            if(keys.equals(index)){
                markslist.replace(keys,mark);
            }
        }
    }
    public void editEdge(T source,T destination, int newweight){
        String indexEdge=(source +""+ destination);
        for (T v : map.keySet()) {
            if(v.equals(source)){
                for (T w : map.get(v)) {
                    if(w.equals(source)){
                        weightlist.replace(indexEdge,newweight);
                    }
                }
            }

        }
    }
    Map <T,Boolean> visited = new HashMap<>();
    ArrayList <T> path=new ArrayList<>();
    public void dfs(T vertex){
        visited.put(vertex,true);
        ListIterator<T> ite = map.get(vertex).listIterator();
        if (map.get(vertex).isEmpty()){
            path.add(vertex);
            System.out.println(path);
            path.remove(vertex);
        }
        while (ite.hasNext()) {
            T adj = ite.next();
            path.remove(vertex);
            if (visited.get(adj)==null){
                path.add(vertex);
                dfs(adj);
            }
        }
    }
//    public void dfsiterator(){
//        for(T v : map.keySet()){
//            dfs(v);
//        }
//    }
    // Выводит список смежности каждой вершины.
    @Override
    public String toString()
    {
        StringBuilder builder = new StringBuilder();

        for (T v : map.keySet()) {
            if((map.get(v).isEmpty())){
                builder.append(v.toString()+"("+markslist.get(v)+")"+":я пустой");
            }
            else{
                builder.append(v.toString()+"("+markslist.get(v)+")"+"=>");
                for (T w : map.get(v)) {
                    builder.append(w.toString() +"{"+weightlist.get(v+""+w)+"}"+ "; " );
                }
            }
            builder.append("\n");
        }

        return (builder.toString());
    }
    public String showGraph(){
        StringBuilder builder1 = new StringBuilder();
        ArrayList<String> rowlist = new ArrayList();
        ArrayList<String> columnlist = new ArrayList();
        final String RESET="\u001B[0m";
        final String RED = "\u001B[31m";

        //получаем массивы с элементами row и column
        for (T v : map.keySet()) {
            rowlist.add(v+"");
            for (T w : map.get(v)) {
                columnlist.add(v+""+w);
            }
        }

        //заподняем билдер элементами(подписанная матрица инцидентности)
        builder1.append("\t");
        for (int i = 0; i < columnlist.size(); i++) {
            builder1.append(RED+""+"["+columnlist.get(i)+"]  "+RESET);
        }
        builder1.append("\n");

        //заполняем двумерный массив
        int[][] matrix = new int[columnlist.size()][rowlist.size()];
        for (int i=0;i<columnlist.size();i++){
            for (int j=0;j<rowlist.size();j++){
                String tmp1=columnlist.get(i);
                String tmp2=rowlist.get(j);
                if (columnlist.get(i).contains(rowlist.get(j))){
                    if(columnlist.get(i).indexOf(rowlist.get(j))==0){
                        matrix[j][i]=-1;
                    }
                    else {
                        matrix[j][i]=1;
                    }
                }
                else{
                    matrix[j][i]=0;
                }
            }
        }
        //заподняем билдер элементами(подписанная матрица инцидентности)(column)
        int i=0;
        for (T v : map.keySet()) {
            builder1.append(RED+"["+v+"]"+ RESET +" ");
            for (int j=0;j<columnlist.size();j++){
                if (matrix[i][j]==-1){
                    builder1.append("|"+matrix[i][j]+"|  ");
                }
                else {
                    builder1.append("| "+matrix[i][j]+"|  ");
                }
            }
            i++;
            builder1.append("\n");
        }

        return (builder1.toString());
    }
}

public class Main {
    public static void printMenu(String[] options){
        for (String option : options){
            System.out.println(option);
        }
        System.out.print("Выберите свой вариант: ");
    }
    public static void main(String args[])
    {
        // Объект графа создан.
        Graph<Integer> g = new Graph<Integer>();
//        добавляются ребра.
//        Поскольку граф является двунаправленным, логическое двунаправленное значение передается как истинное.
        g.addEdge(0, 1,"ноль","один",1, false);
        g.addEdge(0, 4,"один","четыре",2, false);
        g.addEdge(1, 2,"один","два",3, false);
        g.addEdge(1, 3,"один","три",4, false);
        g.addEdge(3, 4,"один","четыре",5, false);
        g.addEdge(3, 5,"два","пять",6, false);
        String[] options = {"1- ПОКАЗАТЬ СПИСОК ИНЦИДЕНТНОСТИ",
                "2- ПОКАЗАТЬ МАТРИЦУ ИНЦИДЕНТНОСТИ",
                "3- ПОКАЗАТЬ ПУТИ(на)",
                "4- Exit",
        };
        Scanner scanner = new Scanner(System.in);
        int option = 1;
        while (option!=4){
            printMenu(options);
            try {
                option = scanner.nextInt();
                switch (option){
                    case 1: System.out.println("Graph(список инцидентности):\n"
                            + g.toString()); break;
                    case 2:  System.out.println("Graph(матрица инцидентности):\n"
                            +g.showGraph()); break;
                    case 3:  System.out.println("Graph(все пути):\n");
                        g.dfs(0);
                        break;

                    case 4: exit(0);
                }
            }
            catch (Exception ex){
                System.out.println("Введите целое число от 1 до " + options.length);
                scanner.next();
            }
        }
        // выводит граф



    }
}
