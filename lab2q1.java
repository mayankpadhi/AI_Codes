import java.util.Random;
import java.util.Scanner;

public class JavaApplication72 {
    static int list[];
     static int i=0;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        
        Random r = new Random(); 
    int n;
    int k;
    int m;
   
   
        
        
        // TODO code application logic here
        //input from user 
        Scanner scan = new Scanner(System.in);
        // n - no. of varibles
        System.out.println("Enter no. of variables");
        n= scan.nextInt();
        // k - length of clause
        System.out.println("Enter length of clause");
        
        k = scan.nextInt();
        // to ensure odd length
        
        // no. of clauses
        System.out.println("Enter no. of clauses");
        m=scan.nextInt();
        
        
       // int max_v = k/2 +1;
        System.out.println("n:"+n);
       // System.out.println("max_v:"+max_v);
       
       for(int y=0;y<m;y++){
            String s ="";
        // to store the varibles used in a single clause 
            list = new int[k];
        
            i=0;
        // generate a single clause;
            int Result = r.nextInt(n) + 97;
            list[i]= Result;
            i++;
            int resolve = r.nextInt(2);
            if(resolve==0){
                Result = Result - 32;
            }
          // for negation 
            char c = (char) Result;
            s = s + c;
            int j=1;
            if(k==1)
            System.out.println(s);
        
            while(j!=k){
                int symbol = r.nextInt(2);
                if(symbol==0)
                {
                    s = s +" & "; 
                }
                else
                {
                    s=s+" | ";
                }
            
                boolean b = true;
         //Result = r.nextInt(26) + 97;
                while(b){
              
                    Result = r.nextInt(n) + 97;
               //System.out.println("result :"+Result);
                    b = get_unique(Result);
              
                }
          
                list[i] = Result;
                i++;
                j++;
          // for negation
                resolve = r.nextInt(2);
                if(resolve==0){
                    Result = Result - 32;
           
            
                }
                
                c = (char) Result;
                s = s+ c; 
                if(j==k)
                System.out.println("Clause: "+s);
         
            }
       
         
       }
   }
        
    
    // true if matches 
        public static  boolean get_unique(int num){
        boolean b =false;
        //System.out.println("checking for uniqueness");
         
             for(int l=0;l<i;l++){
                 //System.out.println(l+"value:"+list[l]);
                 if(list[l]==num){
                     b=true;
                     return b;
                 }
                 
    
    }
             
             
         //if(!b)
         //System.out.println("The char"+num);
         
         return b;
}
    }
    
    
    
    
    
    
    

