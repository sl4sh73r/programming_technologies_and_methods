public class SortStack {
    static Global global = new Global();
    public static void main(String args[]) {

        for(int i=300;i<=3000;i+=300) {

            long start = System.currentTimeMillis();
            Stack stack = new Stack();
            for (int j = 0; j <= i; j++) {
                stack.push(i - j);
            }
            System.out.println("n="+i);
            sort(stack);

            long finish = System.currentTimeMillis();
            long elapsed = finish - start;
            System.out.println("Прошло времени, мс: " + elapsed);

            System.out.println("NOP="+global.nop);
            global.nop = 0;
        }
    }
//1+4+2+2+n(2+3+8+3+2)+n+89n+nlogn+blogn=9+n(18)+n*log(n)+n*log(n)+89n=2nlogn+107n+9
    private static void sort(Stack stack) {//1+4+2+
        global.nop+=1;
        Stack s1 = new Stack();
        Stack s2 = new Stack();
        global.nop+=4;
        global.nop += 2;
        while (stack.size() != 0) { // + 2 + n(2 + 3 + 8 + 3 + 2)
            global.nop+=2;
            global.nop += 3;
            if (stack.size() % 2 == 0) {
                s1.push(stack.pop());
                global.nop+=2;
            } else {
                s2.push(stack.pop());
                global.nop+=2;
            }
        }

        global.nop += 2;
        if (s1.size() > 1) {//n*log(n)
            global.nop+=1;
            sort(s1);
        }

        global.nop += 2;
        if (s2.size() > 1) {//n*log(n)
            global.nop += 1;
            sort(s2);
        }

        global.nop += 4;
        merge(s1, s2, stack);//+89n
    }

    private static void merge(Stack s1, Stack s2, Stack stack) {
        global.nop+=3;
        Stack mergedStack = new Stack();
        global.nop+=2;
        global.nop+=4;
        while (!s1.isEmpty() && !s2.isEmpty()) {//2n(4+3
            global.nop+=4;
            global.nop+=3;
            if ((Integer) s1.peek() < (Integer) s2.peek()) {//+5+3+8
                global.nop+=3;
                global.nop+=2;
                mergedStack.push(s2.pop());
            } else {
                global.nop+=2;
                mergedStack.push(s1.pop());
            }
        }
        global.nop+=2;
        while (!s1.isEmpty()) {//+n(+4+3+8)
            global.nop+=2;
            global.nop+=2;
            mergedStack.push(s1.pop());
        }
        global.nop+=2;
        while (!s2.isEmpty()) {//+n(+4+3+8)
            global.nop+=2;
            mergedStack.push(s2.pop());
        }
        global.nop+=2;
        while (!mergedStack.isEmpty()) {//+n(2+3+8)
            global.nop+=2;
            stack.push(mergedStack.pop());
        }
    }
}
