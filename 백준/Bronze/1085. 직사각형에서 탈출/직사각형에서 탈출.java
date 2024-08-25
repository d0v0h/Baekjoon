import java.util.Scanner;
import java.util.StringTokenizer;

import static java.lang.Integer.parseInt;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int x = scanner.nextInt();
        int y = scanner.nextInt();

        int w = scanner.nextInt();
        int h = scanner.nextInt();

        int min = 10000;
        if(w-x < min)
            min = w-x;
        if(h-y<min)
            min = h-y;
        if(x-0<min)
            min = x-0;
        if(y-0<min)
            min = y-0;
        System.out.println(min);
        scanner.close();
    }
}