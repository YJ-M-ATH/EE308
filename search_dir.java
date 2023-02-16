import java.util.*;
import java.io.*;

public class E1 {
	
	static int ifelse_num = 0;
	static int ifelseif_num = 0;
	static int switchNum = 0;
	static int caseNum[] = new int[100];
	
	public static void LodeFile(String path){
		Stack<String> str_Stack = new Stack<String>();
		Stack<String> switchCase = new Stack<String>();
		try {
			String str = "";
			BufferedReader br = new BufferedReader(new FileReader(path));	        
			while((str=br.readLine()) != null){
				if (isTarget(str, "else if")) {	
					System.out.println("ELSE IF");
			        str_Stack.push("else if");
			    }    
			    else if (isTarget(str, "else")) {
			    	System.out.println("ELSE");	            
			    	str_Stack.push("else");
			        countFunIf(str_Stack);
			    }
			    else if (isTarget(str, "if")) {
			        System.out.println("IF");
			        str_Stack.push("if");
			    }
			    else if (isTarget(str, "switch")) {
			        System.out.println("SWITCH");
			        switchCase.push("switch");
			    }
			    else if (isTarget(str, "case")) {
			        System.out.println("CASE");
			        switchCase.push("case");
			    }
		    }
			countFunSwitch(switchCase);
		}catch(FileNotFoundException e){
			e.printStackTrace();
		}catch(IOException e){
		    e.printStackTrace();
		}	    	    
	}
	
	public static boolean isTarget(String s, String tar) {
		int result = s.indexOf(tar);
		if (result == -1)
		    return false;
		else
		    return true;
	}
		
	public static void countFunSwitch(Stack<String> switchCase) {
		while(!switchCase.empty()) {
		    while (switchCase.peek() == "case") {
		    	caseNum[switchNum]++;
		    	switchCase.pop();
		    }     
		    if (switchCase.peek() == "switch") {
		    	switchNum++;
		    	switchCase.pop();
		    }        
		} 
    }
		
	public static void countFunIf(Stack<String> str_Stack) {
		int count = 0;
		while (!str_Stack.empty() && str_Stack.peek() != "if") {
		    if (str_Stack.peek() == "else if")        
		        count++;
		    str_Stack.pop();
		}
		if (count == 0) 
		    ifelse_num++;
		else 
		    ifelseif_num++;
		
		if(!str_Stack.empty()) 
		    str_Stack.pop();
	}
		
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("Please input file path:");
		String path = sc.nextLine();
		LodeFile(path);
		System.out.println("switch num:" + switchNum);
		System.out.println("case num:");
		for (int i = switchNum-1; i >= 0; i--) 
			System.out.print(caseNum[i] + " ");

		System.out.println();
		System.out.println("if-else num: " + ifelseif_num);
		System.out.println("if-else if-else num: " + ifelse_num);        	
	}
}