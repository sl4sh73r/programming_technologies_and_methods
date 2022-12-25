import java.util.*;

//        1.	FIRST(v) - возвращает индекс первой вершины, смежной с вершиной v. Если вершина v не имеет смежных вершин, то возвращается "нулевая" вершина .
//        2.	NEXT(v, i)- возвращает индекс вершины, смежной с вершиной v, следующий за индексом i. Если i — это индекс последней вершины, смежной с вершиной v, то возвращается .
//        3.	VERTEX(v, i) - возвращает вершину с индексом i из множества вершин, смежных с v.
//        4.	ADD_V(<имя>, <метка, mark>) - добавить УЗЕЛ
//        5.	ADD_Е(v, w, c) - добавить ДУГУ (здесь c — вес, цена дуги (v,w))
//        6.	DEL_V(<имя>) - удалить УЗЕЛ
//        7.	DEL_Е(v, w) – удалить ДУГУ
//        8.	EDIT_V(<имя>, <новое значение метки или маркировки>) - изменить метку (маркировку) УЗЛА
//        9.	EDIT_Е(v, w, <новый вес дуги>) - изменить вес ДУГИ

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
    public void hasEdge(T s, T d)
    {
        if (map.get(s).contains(d)) {
            System.out.println("Граф имеет ребро между "
                    + s + " и " + d + ".");
        }
        else {
            System.out.println("Граф не имеет ребра между "
                    + s + " и " + d + ".");
        }
    }
    public void nextValue(T sourse,int i) {
        if (map.containsKey(i+1))
            System.out.println("индекс вершины, смежной с вершиной "+ sourse+", следующий за индексом "+ i+": " + map.get(sourse).get(0));
        else System.out.println("вершина \uF04C");
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

}

public class Main {

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
        g.addEdge(1, 4,"один","четыре",5, false);
        g.addEdge(2, 3,"два","три",6, false);
        g.addEdge(3, 4,"три","четыре",7, false);
        g.editEdge(0,1,2);
        g.addVertex(5,"a");
        g.editVertex(5,"b");
        g.addVertex(6,"c");
        g.deleteEdge(1,2);
        // выводит граф
        System.out.println("Graph(список инцидентности):\n"
                + g.toString());
        g.first(2);
        g.nextValue(2,5);
        // дает количество вершин графа.
        g.getVertexCount();

        // Дает количество ребер в графе.
        g.getEdgesCount(true);

        // Сообщает, присутствует ли край или нет.
        g.hasEdge(3, 4);

        // Сообщает, присутствует ли вершина или нет
        g.hasVertex(5);
    }
}