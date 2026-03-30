class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        
        for (char x : s.toCharArray()){
            int sNum = 0;
            int tNum = 0;
            for(int i = 0 ; i < s.length() ; i ++ ){
                if(x == s.charAt(i)){
                    sNum++;
                }
                if(x == t.charAt(i)){
                    tNum ++;
                }
            }
            if(sNum != tNum)
                return false;
        }
        return true;
    }
}
