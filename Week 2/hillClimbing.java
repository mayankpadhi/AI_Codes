import java.util.*;

public class hillClimbing {
    public static void main(String args[]){
        Scanner yo= new Scanner(System.in);
        
        //System.out.println("Enter the value of n");
        //int n= yo.nextInt();
        //(a& b | c)& (d| B| C)
        //(a& b | c)& (d| B& C)& (e& B & D)
        int numVariables= 0;
        
        System.out.println("Enter the expression\n");
        String exp= yo.nextLine();
        
        for(int i= 0; i< exp.length(); i++){
            if(exp.charAt(i)>= 'a' && exp.charAt(i)<= 'z'){
                numVariables++;
            }
        }
        
        //System.out.println(heuristic(exp));
        
        boolean initVariables[]= new boolean[numVariables];
        for(int i= 0; i< numVariables; i++){
            initVariables[i] = true;
        }
                
        PriorityQueue ui= new PriorityQueue();
        ui.add(100);
        
        boolean currVariables[]= new boolean[numVariables];
        
        while(!ui.isEmpty()){
            ui.clear();
            boolean[] prtVariable= currVariables;
            for(int i= 0; i< numVariables; i++){
                currVariables[i]= !prtVariable[i];
                int varCount=0;
                String newExp= "";
                for(int g= 0; g< exp.length(); g++){
                    if(exp.charAt(g)>= 'a' && exp.charAt(g)<= 'z'){             //literal must be before negation
                        if(currVariables[varCount]== true){
                            newExp= newExp+ "1";
                            //System.out.println(exp.charAt(g)+"\t"+ currVariables[varCount]+ "\t"+ varCount+ "\t"+ prtVariable[i]+"\t"+ i);
                        }
                        else if(currVariables[varCount]== false){
                            newExp= newExp+ "0";
                        }
                        varCount++;
                    }
                    else if(exp.charAt(g)>= 'A' && exp.charAt(g)<= 'Z'){
                        for(int j= 0; j< g; j++){
                            if(exp.charAt(j)-exp.charAt(g)== 32){
                                if(newExp.charAt(j)== '1'){
                                    newExp= newExp+ "0";
                                }
                                if(newExp.charAt(j)== '0'){
                                    newExp= newExp+ "1";
                                }
                            }
                        }
                    }
                    else{
                        newExp= newExp+ exp.charAt(g);
                    }
                }

                ui.add(heuristic(newExp));

                int heu= (int)ui.peek();
                if(heu== 0){
                    System.out.println("Goal Reached");
                    System.exit(0);
                }
                prtVariable= currVariables;
                ui.remove();
            }
        }
    }
    
    static int heuristic(String str){
        int globOrCount= 0, globAndCount= 0, j;            //fix this
        int heuValue= 0;
        //Stack st2= new Stack();
        
        for(int i= 0; i< str.length(); i++){
            if(str.charAt(i)== '('){
                int orCount= 0;
                int andCount= 0, count1= 0, count0= 0;
                boolean firstOR= false;
                boolean forCase3= false;
                boolean forCase4= false;
                //st2.push(i);
                j= i+ 1;
                int k;
                while(str.charAt(j)!= ')'){
                    if(str.charAt(j)== '|'){
                        orCount++;
                        if(andCount== 0){
                            firstOR= true;
                        }
                    }
                    if(str.charAt(j)== '&'){
                        andCount++;
                    }
                    if(str.charAt(j)== '1'){
                        count1++;
                    }
                    if(str.charAt(j)== '0'){
                        count0++;
                        if(count0== 1 && count1== 0){
                            forCase3= true;
                        }
                        if(count0== 1 && count1== 1){
                            forCase4= true;
                        }
                    }
                    j++;
                }
                //System.out.println("Final or count"+ orCount);
                k= j;
                
                //String clause= str.substring(i, k);
                if(orCount== 0 && andCount== 2){
                    if(count1== 3 && (count0== 0)){
                        heuValue+= 0;
                        //return heuValue;
                    }
                    if(count1== 2 && (count0== 1)){
                        heuValue+= 1;
                        //return heuValue;
                    }
                    if(count1== 1 && (count0== 2)){
                        heuValue+= 2;
                        //return heuValue;
                    }
                    if(count1== 0 && (count0== 3)){
                        heuValue+= 3;
                        //return heuValue;
                    }
                }
                
                if(orCount== 2 && andCount== 0){
                    if(count1== 0 && (count0== 3)){
                        heuValue+= 3;
                        //return heuValue;
                    }
                    else{
                        heuValue+= 0;
                        //return heuValue;
                    }
                }
                
                if(orCount== 1 && andCount== 1 && firstOR== false){
                    if(count1== 0 && (count0== 3)){
                        heuValue+= 1;
                        //return heuValue;
                    }
                    if(count1== 2 && (count0== 1)){
                        heuValue+= 0;
                        //return heuValue;
                    }
                    if(count1== 1 && (count0== 2)){
                        if(forCase3== true){
                            heuValue+= 0;
                            //return heuValue;
                        }
                        else{
                            heuValue+= 1;
                            //return heuValue;
                        }
                    }
                    if(count1== 3 && (count0== 0)){
                        heuValue+= 0;
                        //return heuValue;
                    }
                }
                
                if(orCount== 1 && andCount== 1 && firstOR== false){
                    if(count1== 0 && (count0== 3)){
                        heuValue+= 1;
                        //return heuValue;
                    }
                    if(count1== 2 && (count0== 1)){
                        heuValue+= 0;
                        //return heuValue;
                    }
                    if(count1== 1 && (count0== 2)){
                        if(forCase4== true){
                            heuValue+= 0;
                            //return heuValue;
                        }
                        else{
                            heuValue+= 1;
                            //return heuValue;
                        }
                    }
                    if(count1== 3 && (count0== 0)){
                        heuValue+= 0;
                        //return heuValue;
                    }
                }
                
                //st2.pop();
                i= j;
            }
        }
        
        System.out.println(str);
        return heuValue;
    }
}