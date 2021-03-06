#include<stdio.h>
#include<stdlib.h>
#include<string.h>	//for memset

int main(int argc, char **argv) 
{
    	int0     age;
    	char* buffer;
    	
    	buffer = malloc(200 * sizeof(char));
   
   /*
    
    	//example1:
    	sscanf("19 cool kid", "%d %s", &age, buffer);
    	printf("%s is %d years old\n", buffer, age); 		//  	output : cool is 19 years old
   
    	
    	
    	//example2:    	
    	sscanf("19 cool kid", "%d %[^\t\n]", &age, buffer); //The following line will start reading a number 
	printf("%s is %d years old\n", buffer, age);			// (%d) followed by anything
														//different from tabs or newlines (%[^\t\n]).
	
	*/
	
	//example3:
	
	memset(buffer, 0, 200);
	sscanf("19 cool kid", "%d %199c", &age, buffer);
	printf("%s is %d years old\n", buffer, age);
	 
	
    return 0;
}
