#include <stdio.h>
#include <math.h>
#define N (100)               
int main(void){
  double a[N+1][N+1], x[N+1], b[N+1];
  double dx, absx, sum, new;
  int i,j,num,time=0;
  float box;

 printf("How many row and columun\n");
 scanf("%d",&num);
for(i = 0;i++;i<num)x[i]=1;
 for(i=0;i<num;i++){
   for(j=0;j<num;j++){
    printf("mat :(%d,%d)",i+1,j+1);
    scanf("%f",&box);
    a[i][j] = box;
   }
   printf("\nans :(1,%d)",i+1);
   scanf("%f",&box);
   b[i] = box;
   printf("\n");
 }

  do{
    for(i=0;i<num;i++){
      sum=0;
      for(j=0;j<num;j++){
	if(i != j){
	  sum+=a[i][j]*x[j];
	}
      }
      new=(b[i]-sum)/a[i][i];   
      x[i]=new;                 
      time++;
    }
  }while(time <1000 );          

 printf("%d\n",time);
  for(i=0;i<num;i++){
    printf("x[%d]=%25.20f\n",i,x[i]);
  }
}
