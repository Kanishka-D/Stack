class Solution {
    public String simplifyPath(String path) {
        
        Stack<String> st=new Stack<String>();
        String[] words=path.split("/");
        
        
        for(String w:words){
            if(!st.isEmpty() &&  w.equals(".."))
                st.pop();
            else if(!w.equals("..") && !w.equals(".") &&  !w.equals(""))
                st.push(w);
        }
            
        ArrayList<String> list=new ArrayList(st);
      
        return "/"+String.join("/",list);
        
      
}
    }