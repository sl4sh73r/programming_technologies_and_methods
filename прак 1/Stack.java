    import java.util.ArrayList;
    import java.util.EmptyStackException;
    public class Stack<T> extends ArrayList<T> {
        Global global = new Global();
        public void push(T t){ // 3
            add(t);
            global.nop=global.nop+3;
        }

        public T pop(){ // 8
            int currentSize = size();
            T t = get(currentSize - 1);
            remove(currentSize-1);
            global.nop=global.nop+8;
            return t;
        }
        public T peek(){ // 7
            int currentSize = size();
            T t = get(currentSize - 1);
            global.nop=global.nop+7;
            return t;
        }

        public boolean empty() { // 3
            global.nop=global.nop+3;
            return size() == 0;
        }
    }
