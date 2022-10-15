# Stack

Parenthesis Checker
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import java.util.*;
import java.lang.*;

public class Solution
{
    //Function to check if brackets are balanced or not.
    public static void main(String[] args)
    {
        // add your code here
        String x="[({[([{}])]})}";
        Stack<Character> s=new Stack<Character>();
        
        for(int i=0;i<x.length();i++){
            char ch=x.charAt(i);
            char check;
            
            if(ch=='{'|| ch=='[' || ch=='('){
                s.push(ch);
            }
            else if(s.isEmpty()){
               System.out.println(" false");
            }
            switch(ch){
                case '}':
                    check=s.peek();
                    if(check=='[' || check=='(')
                        System.out.println(" false");
                    else
                     s.pop();    
                    break;
                
                case ']':
                    check=s.peek();
                    if(check=='{' ||check=='(')
                        System.out.println(" false");
                    else    
                     s.pop();    
                    break;
                
                case ')':
                    check=s.peek();
                    if(check=='['|| check=='(')
                        System.out.println(" false");
                    else
                     s.pop();
                    break;   
                
            }
        }
        
        System.out.println (s.isEmpty());
    }
}
