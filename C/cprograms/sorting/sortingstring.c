/* C program to read N names and sort them alphabetically. */
//***********************************************************

#include<stdio.h>
#include<string.h>

int main()
{
printf("************************************************************\n");
	char name[10][8], sname[10][8],temp[8];
	int i,j,n;
	
	printf("Enter how many names?\t");
	scanf("%d", &n);
	printf("\nOK Enter %d names: \n", n);
	
//storing names in a string called name[i] and then copying to another string
	for (i=0; i<n; i++)
	{
		scanf("%s", name[i]);		// name[i] is unsorted string
		strcpy(sname[i], name[i]);	// so, we make a copy of unsorted string and will sort that as sorted name(sname[i])
	}	
//implementing sorting strings 	(mnemonic: FOR FOR IF)
	for (i=0; i<n-1; i++)
	{
		for (j=i+1; j<n; j++)
		{
			if (strcmp(sname[i], sname[j])>0)		// strcpy(target,source)>0 means string1>string2. eg. 5>3 or t>s
			{
				strcpy(temp, sname[i]); 		// temp    = name[i]
				strcpy(sname[i], sname[j]);	// name[i] = name[j]
				strcpy(sname[j], temp);		// name[j] = temp
			}
		}
	}
		
// display sorted and unsorted names.......................
	printf("\n---------------------------------------------------\n");
	printf("Entered Names\tSorted names\n");
	printf("-----------------------------------------------------\n");
	
	for (i=0; i<n; i++)
	{
		printf("%s\t\t%s\n", name[i], sname[i]);
	}
	printf("----------------------------------------------------\n");
		
printf("************************************************************\n");
return 0;
}
