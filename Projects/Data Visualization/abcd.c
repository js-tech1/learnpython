#include<stdio.h> 

int main()
{
   //Edit below this line
   
  float height;
  float weight;
  float bmi = weight/(height * height);
  scanf("%f%f",&height,&weight);
  if(bmi<19){
  printf("BMI = %f \n lean",bmi);
  }
  else if(bmi>=19 && bmi<=25){
  printf("BMI = %f \n normal",bmi);
  }
  else{
  printf("BMI = %f \n overweight",bmi);
  }
    return 0; 
}