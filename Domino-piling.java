import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Practise1{
    public void dominoPilling(){
        System.out.println("Please enter M&N squares separated by space, and (1<=M<=N<=16)");
        Scanner dimention=new Scanner(System.in);
        int m=dimention.nextInt();
        int n=dimention.nextInt();
        int num0=0;
        if((n%2)>0){
            num0=m/2;
        }
        int dominos=(n/2*m)+num0;
        System.out.println(dominos);
    }
}
class Run{
    public static void main(String[]args){
        Practise1 obj1=new Practise1();
        obj1.dominoPilling();
    }
}
