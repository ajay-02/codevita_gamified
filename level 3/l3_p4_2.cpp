#include<iostream>
#include<string.h>
#define MAX_SIZE 15
using namespace std;
void digarr(int n,int dig_arr[],int *cnt){
	int i;
	*cnt=0;
	do{
		dig_arr[(*cnt)++]=n%10;
		n=n/10;
	}while(n>0);
	for(i=0;i<((*cnt)/2);i++){
		int t=dig_arr[i];
		dig_arr[i]=dig_arr[(*cnt)-1-i];
		dig_arr[(*cnt)-1-i]=t;
	}
}
void sort_arr(int a[], int n){
	int i,j;
	for(i=1;i<n;i++){
		int t=a[i];
		for(j=i-1;j>=0;j--){
			if(a[j]>t){
				a[j+1]=a[j];
			}
			else{
				break;
			}
		}
		a[j+1]=t;
	}
}
int permute(int a[],int n,int d,int order[],int used[],int index,int *lm){
  	int i;
    if(index==n){
		int num=0;
        for(i=0;i<n;i++){
            num=num*10+a[order[i]];
        }
		if(num%d==0){
			*lm=num;
			return 1;
		}
        return 0;
    }
    for(i=0;i<n;i++){
        if(used[i]==1){
            continue;
        }
        used[i]=1;
        order[index]=i;
        if(1==permute(a,n,d,order,used,index+1,lm)){
			return 1;
		}
        used[i]=0;
    }
	return 0;
}
int lmp(int a[],int n,int d){
    int order[MAX_SIZE]={},used[MAX_SIZE]={};
	int lmp1=-1;
    int isSuccess=permute(a,n,d,order,used,0,&lmp1);
	return lmp1;
}
int main()
{
  int n,d,dig_arr[MAX_SIZE],cnt;
  cin>>n>>d;
  digarr(n,dig_arr,&cnt);
  sort_arr(dig_arr,cnt);
  cout<<lmp(dig_arr,cnt,d);
  return 0;
}