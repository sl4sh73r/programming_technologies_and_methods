import java.io.Console;
import java.io.IOException;
import java.util.*;
class OBST{
    private static final int NMAX = 20;

    static class Node{
        int KEY;
        Node left, right;
    }

    //static Node ROOT=new Node();
    int[][] C =new int[NMAX][NMAX]; //cost matrix
    int[][] W =new int[NMAX][NMAX]; //weight matrix
    int[][] R =new int[NMAX][NMAX]; //root matrix
    //static int[] q =new int[NMAX]; //unsuccesful searches
    int[] p =new int[NMAX]; //frequencies
    //static int NUMBER_OF_KEYS; //number of keys in the tree

    public Node ROOT=new Node();
    int[] KEYS =new int[NMAX];
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
    //Construct the optimal binary search tree
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

    //Display the optimal binary search tree

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
}
class Main{
    static Scanner sc = new Scanner(System.in);
    static OBST treeA = new OBST();
    //static OBST.Node nodeA = new OBST.Node();
    static OBST treeB = new OBST();
    //static OBST.Node nodeB = new OBST.Node();
    public static void MENU(OBST treeA,OBST treeB, int NUMBER_OF_KEYSA, int NUMBER_OF_KEYSB)  {
        int k = 0;
        do {
            System.out.print("1.Construct tree\n2.Task\n3.Exit\n");
            k=sc.nextInt();
            switch(k) {
                case 1:
                    treeA.OPTIMAL_BINARY_SEARCH_TREE(NUMBER_OF_KEYSA);
                    treeB.OPTIMAL_BINARY_SEARCH_TREE(NUMBER_OF_KEYSB);
                    break;
                case 2:
                    System.out.println("\nTree A(postorder): " +treeA.A+"\n");
                    System.out.println("\nTree B(inorder): " +treeB.B+"\n");
                    System.out.println("\nTask): " +treeA.A+"\n");
                    treeA.A.addAll(treeB.B);
                    System.out.println("\nС=A ⋃прB\n C="+treeA.A+"\n");
                    break;
                case 3:
                    k = -1;
                    break;
            }
        } while (k != -1);
    }
    public static void PRINT_NUMBER_OF_KEYS(int NUMBER_OF_KEYS,OBST tree){
        for(int i = 1; i <= NUMBER_OF_KEYS; i++) {
            System.out.print("key["+i+"]=");
            tree.KEYS[i]=sc.nextInt();
            System.out.print(" frequency = ");
            tree.p[i]=sc.nextInt();
        }
    }
    public static void main(String[] args)  {

        System.out.print("Input number of keys A: ");
        int NUMBER_OF_KEYSA=sc.nextInt();
        PRINT_NUMBER_OF_KEYS(NUMBER_OF_KEYSA,treeA);

        System.out.print("Input number of keys B: ");
        int NUMBER_OF_KEYSB=sc.nextInt();
        PRINT_NUMBER_OF_KEYS(NUMBER_OF_KEYSB,treeB);

        MENU(treeA,treeB,NUMBER_OF_KEYSA,NUMBER_OF_KEYSB);
    }
}
