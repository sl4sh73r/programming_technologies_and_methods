import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class QuickSort {

    Global global=new Global();
    public static void main(String[] args) {
        QuickSort sort = new QuickSort();
        for (int n=300; n<=3000; n+=300){
            System.out.println("n="+n);
            long start = System.currentTimeMillis();
            Queue<Integer> input = sort.generateRandomNumbers(n);
            //System.out.println(sort.quicksort(input));
            sort.quicksort(input);
            long finish = System.currentTimeMillis();
            long elapsed = finish - start;
            System.out.println("Прошло времени, мс: " + elapsed);
        }
    }

        private Queue<Integer> quicksort (Queue <Integer> input) {

            if (input.size() <= 1) {
                return input;
            }

            int middle = (int) Math.ceil((double) input.size() / 2);
            int pivot = input.getEl(middle);

            Queue<Integer> less = new Queue<Integer>();
            Queue<Integer> greater = new Queue<Integer>();

            for (int i = 0; i < input.size(); i++) {
                if (input.getEl(i) <= pivot) {
                    if (i == middle) {
                        continue;
                    }
                    less.enqueue(input.getEl(i));
                } else {
                    greater.enqueue(input.getEl(i));
                }
            }

            return concatenate(quicksort(less), pivot, quicksort(greater));
        }

        private Queue<Integer> concatenate (Queue < Integer > less,int pivot, Queue<Integer > greater){

            Queue<Integer> list = new Queue<Integer>();

            for (int i = 0; i < less.size(); i++) {
                list.enqueue(less.getEl(i));
            }

            list.enqueue(pivot);

            for (int i = 0; i < greater.size(); i++) {
                list.enqueue(greater.getEl(i));
            }

            return list;
        }

        private Queue<Integer> generateRandomNumbers (int n){

            Queue<Integer> queue = new Queue<>();
            Random random = new Random();

            for (int i = 0; i < n; i++) {
                queue.enqueue(random.nextInt(n * 10));
            }

            return queue;
        }
}