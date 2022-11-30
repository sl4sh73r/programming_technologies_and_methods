import java.util.Collections;

public class Heaps { // Static class so you can access it through the main class.
    static Global global=new Global();
    public static void maxHeap(Stack<Integer> array, int index, int size) {//3+5+5+5+6+nlogn+6+nlogn+9+nlogn+nlogn==4nlogn+39
        global.nop+=3;
        int largest = index; // Root Node
        global.nop+=5;
        int left = 2 * index + 1; // Left Child node
        global.nop+=5;
        int right = 2 * index + 2; // Right Child node

        global.nop +=5;
        if (left < size && array.get(left) > array.get(largest)) {//6+nlogn
            global.nop+=1;
            largest = left;
        }
        global.nop+=5;
        if (right < size && array.get(right) > array.get(largest)) {//6+nlogn
            global.nop+=1;
            largest = right;
        }
        global.nop+=1;
        if (largest != index) {
            global.nop+=8;
            Collections.swap(array, index, largest); // nlogn
            maxHeap(array, largest, size);//nlogn
        }

    }
    public static void sort(Stack<Integer> array, int size){//5+n(9+4nlogn+39)+4+n(10+nlogn+4nlogn+39)==9+97n+9n^2+logn
        global.nop+=5;
        for (int i = size / 2 - 1; i >= 0; i--) {//5+n(9+4nlogn+39)
            global.nop+=5;
            global.nop+=4;
            maxHeap(array, i, size);//4nlogn+39
        }
        global.nop+=4;
        for (int i = size - 1; i >= 0; i--) {//4+n(10+nlogn+4nlogn+39)
            global.nop+=4;
            global.nop+=6;
            Collections.swap(array, i, 0);//nlogn
            maxHeap(array, 0, i);//4nlogn+39
        }
    }
    
    public static void main(String[] args) {



        for(int k=300;k<=3000;k+=300) {
            Stack<Integer> array = new Stack<>();
            long start = System.currentTimeMillis();
            for (int j = 0; j <= k; j++) {
                array.push(k - j);}
            System.out.println("n=" + k);
            int size = array.size();
//            System.out.println(array);
            sort(array,size);
//            System.out.println(array);
            long finish = System.currentTimeMillis();
            long elapsed = finish - start;
            System.out.println("Прошло времени, мс: " + elapsed);
            System.out.println("NOP "+global.nop);
            global.nop=0;
        }
    }
}
