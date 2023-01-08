import java.util.*;
class OBST{
    private static final int NMAX = 20;
    static class Node{
        int KEY;
        Node left, right;

    }


    //static Node ROOT=new Node();
    static int[][] C =new int[NMAX][NMAX]; //cost matrix
    static int[][] W =new int[NMAX][NMAX]; //weight matrix
    static int[][] R =new int[NMAX][NMAX]; //root matrix
    static int[] q =new int[NMAX]; //unsuccesful searches
    static int[] p =new int[NMAX]; //frequencies

    static int NUMBER_OF_KEYS; //number of keys in the tree
    static Node ROOT=new Node();
    static int[] KEYS =new int[NMAX];
    static void COMPUTE_W_C_R(){
        int x, min;
        int i, j, k, h, m;

        //Construct weight matrix W
        for(i = 0; i <= NUMBER_OF_KEYS; i++) {
            W[i][i] = q[i];
            for(j = i + 1; j <= NUMBER_OF_KEYS; j++)
                W[i][j] = W[i][j-1] + p[j] + q[j];
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
    public static Node CONSTRUCT_OBST(int i, int j){
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
    static void DISPLAY(Node ROOT, int nivel){
        int i;
        if(ROOT != null) {
            DISPLAY(ROOT.right, nivel + 1);
            for(i = 0; i <= nivel; i++)
                System.out.print(" ");
            System.out.println(ROOT.KEY);
            DISPLAY(ROOT.left, nivel+1);
        }
    }
    static void OPTIMAL_BINARY_SEARCH_TREE()
    {
        float average_cost_per_weight;

        COMPUTE_W_C_R();
        System.out.println("C[0]="+C[0][NUMBER_OF_KEYS]+" "+"W[0]="+W[0][NUMBER_OF_KEYS]);
        average_cost_per_weight = C[0][NUMBER_OF_KEYS]/(float)W[0][NUMBER_OF_KEYS];
        System.out.println("The cost per weight ratio is:\n" + average_cost_per_weight);
        ROOT = CONSTRUCT_OBST(0, NUMBER_OF_KEYS);
    }

    public static void main(String[] args) {

        int i;
        int k = 0;
        System.out.println("input A");
        Scanner sc = new Scanner(System.in);
        System.out.print("Input number of keys: ");
        NUMBER_OF_KEYS=sc.nextInt();
        for(i = 1; i <= NUMBER_OF_KEYS; i++) {
            System.out.print("key["+i+"]=");
            KEYS[i]=sc.nextInt();
            System.out.print(" frequency = ");
            p[i]=sc.nextInt();
        }
        for(i = 0; i <= NUMBER_OF_KEYS; i++) {

            System.out.print("q["+ i+"]=");
            q[i]=sc.nextInt();
        }
        do {
            System.out.print("1.Construct tree\n2.Display tree\n3.Exit\n");
            k=sc.nextInt();
            switch(k) {
                case 1:
                    OPTIMAL_BINARY_SEARCH_TREE();
                    break;
                case 2:
                    DISPLAY(ROOT, 0);
                    break;
                case 3:
                    k = -1;
                    break;
            }
        } while (k != -1);
    }
}
