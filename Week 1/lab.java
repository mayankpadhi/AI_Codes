import java.util.*;

public class snsocial {
    public static void main(String[] args){
        //System.out.println("hrmml");
        Scanner yo= new Scanner(System.in);
        
        int[] a= new int[5];
        
        System.out.println("Enter The 6 numbers: ");
        for(int i= 0; i< 6; i++){
            a[i]= yo.nextInt();
        }
        
        Random rand = new Random();
        int rNumber= rand.nextInt(900) + 100;
        System.out.println("Target Random Number: "+ rNumber);
        
        int minDiff= 100;        //minimum difference of the target and current Result
//        int currentResult;
        String exp="";
        
        while(minDiff!= 0){
            for(int j=0; j< 6; j++){
                int Diff= rNumber- a[j];
                if(Math.abs(Diff)< minDiff ){
                    minDiff= Math.abs(Diff);
                    exp= String.valueOf(a[j]);
                }
            }
            
            for(int j= 0; j< 6; j++){
                for(int k= 0; k< 6; k++){                   // j!= k deal this
                    if(j!= k){
                        int Diff= rNumber- (a[j]+ a[k]);
                        if(Math.abs(Diff)< minDiff ){
                            minDiff= Math.abs(Diff);
                            exp= String.valueOf(a[j]+ a[k]);
                        }

                        Diff= rNumber- (a[j]- a[k]);
                        if(Math.abs(Diff)< minDiff ){
                            minDiff= Math.abs(Diff);
                            exp= String.valueOf(a[j]- a[k]);
                        }

                        Diff= rNumber- (a[j]* a[k]);
                        if(Math.abs(Diff)< minDiff ){
                            minDiff= Math.abs(Diff);
                            exp= String.valueOf(a[j]* a[k]);
                        }

                        if(a[j]%a[k]== 0){
                            Diff= rNumber- (a[j]/ a[k]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]/ a[k]);
                            }
                        }
                    }
                }
            }
            
            for(int j= 0; j< 6; j++){
                for(int k=0; k< 6; k++){
                    for(int m= 0; m< 6; m++){
                        if(j!= k && m!= k && j!= m){
                            int Diff= rNumber- (a[j]* a[k]* a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]* a[k]* a[m]);
                            }
                            
                            Diff= rNumber- (a[j]* a[k]+ a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]* a[k]+ a[m]);
                            }
                            
                            Diff= rNumber- (a[j]+ a[k]+ a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]+ a[k]+ a[m]);
                            }
                            
                            Diff= rNumber- (a[j]* a[k]- a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]* a[k]- a[m]);
                            }
                            
                            Diff= rNumber- (a[j]* a[k]/ a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]* a[k]/ a[m]);
                            }
                            
                            Diff= rNumber- (a[j]- a[k]+ a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]- a[k]+ a[m]);
                            }
                            
                            Diff= rNumber- (a[j]- a[k]- a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]- a[k]- a[m]);
                            }
                            
                            Diff= rNumber- (a[j]- a[k]/ a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]- a[k]/ a[m]);
                            }
                            
                            Diff= rNumber- (a[j]/ a[k]+ a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]/ a[k]+ a[m]);
                            }
                            
                           Diff= rNumber- (a[j]/ a[k]/ a[m]);
                            if(Math.abs(Diff)< minDiff ){
                                minDiff= Math.abs(Diff);
                                exp= String.valueOf(a[j]/ a[k]/ a[m]);
                            }
                        }
                    }
                }
            }
            
            System.out.println("The expression nearest to target is "+ exp);
        }
    }
}