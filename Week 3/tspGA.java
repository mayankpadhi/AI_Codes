import java.util.*;

public class tspGA {
    public static void main(String args[]){
        Scanner yo= new Scanner(System.in);
        
        System.out.println("Enter the number of locations");
        int n= yo.nextInt();
        int[][] dist= new int[n][n];
        
        ArrayList<String> population = new ArrayList<String>();
        
        for(int i= 0; i< 30; i++){
            String popu= "";
            ArrayList<Integer> list = new ArrayList<Integer>();
            for(int k= 0; k< n; k++) {
                list.add(new Integer(k));
            }
            Collections.shuffle(list);
            
            for(int j= 0; j< n; j++){
                popu= popu+ list.get(j);
            }
            population.add(popu);
        }

        for(int i= 0; i< n; i++){
            for(int j= i+1; j< n; j++){
                System.out.println("Enter the distance from point "+ (i)+ " to point "+ (j));
                dist[i][j]= yo.nextInt();
            }
        }
        
        for(int i= 0; i< n; i++){
            for(int j= i+1; j< n; j++){
                dist[j][i]= dist[i][j];
            }
        }
        
        String canoTour= "";
        for(int i= 0; i< n; i++){
            canoTour= canoTour+ i;
        }
        
        int counter= 0;
        while(counter!= 1000){
            String child= "";
            String ordiRprtn1= createOrdinal(population, canoTour, n);
            String ordiRprtn2= createOrdinal(population, canoTour, n);

            child= child+ ordiRprtn1.substring(0, n/2);
            child= child+ ordiRprtn2.substring((n/2), n);

            String toInput= reverse(child, canoTour);
            population.add(toInput);

            Random rand= new Random();
            int mutIndex= rand.nextInt(((population.size()-1) - 0) + 1) + 0;
            String newMember= mutation(population.get(mutIndex));
            population.remove(mutIndex);
            population.add(newMember);
            
            while(population.size()> 10){
                int compete1= rand.nextInt(((population.size()-1) - 0) + 1) + 0;
                int compete2= rand.nextInt(((population.size()-1) - 0) + 1) + 0;
                
                int fitCompete1= fitness(dist, population.get(compete1));
                int fitCompete2= fitness(dist, population.get(compete2));
                
                if(fitCompete1< fitCompete2){
                    population.remove(compete1);
                }
                else{
                    population.remove(compete2);
                }
            }
            
            counter++;
        }
        
        System.out.println("Final Population");
        for(int i= 0; i< population.size(); i++){
            System.out.println(population.get(i)+ "\t"+ fitness(dist, population.get(i)));
        }
        
    }
    
    static int fitness(int[][] mat, String path){
        int FValue= 0, i= 0;
        while(i!= path.length()-1){
            //int val = Character.digit(path.charAt(i), 10);
            FValue+= mat[Character.digit(path.charAt(i), 10)][Character.digit(path.charAt(i+1), 10)];
            i++;
        }
        if(FValue== 0){
            return -1;
        }
        return FValue;
    }
    
    static String reverse(String ordiRprtn, String canoTour){
        String OpOrdi= "";
        StringBuilder sb = new StringBuilder(canoTour);
        
        for(int i= 0; i< canoTour.length(); i++){
            OpOrdi= OpOrdi+ sb.charAt(Character.getNumericValue(ordiRprtn.charAt(i)));
            sb.deleteCharAt(Character.getNumericValue(ordiRprtn.charAt(i)));
        }
        
        //System.out.println(sb);
        return OpOrdi;
    }
    
    static String mutation(String st1){
        Random rand= new Random();
        int myCntr1= rand.nextInt(((st1.length()-1) - 0) + 1) + 0;
        int myCntr2= rand.nextInt(((st1.length()-1) - 0) + 1) + 0;
        
        StringBuilder s4 = new StringBuilder(st1);
        char pt1= s4.charAt(myCntr1);
        char pt2= s4.charAt(myCntr2);
        
        s4.deleteCharAt(myCntr2);
        s4.insert(myCntr2, pt1);
        s4.deleteCharAt(myCntr1);
        s4.insert(myCntr1, pt2);
        
        return s4.toString();
    }
    
    static String createOrdinal(ArrayList<String> population, String canoTour, int n){
        String ordiRprtn1= "";
        Random rand= new Random();
        int myCntr1= rand.nextInt(((population.size()-1) - 0) + 1) + 0;
        
        StringBuilder s2 = new StringBuilder(canoTour);
        for(int i= 0; i< n; i++){
            for(int j= 0; j< s2.length(); j++){
                if(population.get(myCntr1).charAt(i)== s2.charAt(j)){
                    ordiRprtn1= ordiRprtn1+ j;
                    s2.deleteCharAt(j);
                    break;
                }
            }
        }
        return ordiRprtn1;
    }
}