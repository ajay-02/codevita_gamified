#include<stdio.h>
int main(){
    int n,time,zombie[20],player,min,i,test,flag=0;
    scanf("%d",&test);
    while(test){
        scanf("%d %d",&n,&time);
        for(i=0;i<n;i++)
            scanf("%d",&zombie[i]);
        scanf("%d %d",&player,&min);
        if(min>0 && min<=2000 && player>0 && player<=500 && n>0 && n<=50 && time>0 && time<=100){
            if(time<n)
                flag++;
            for(i=0;i<n;i++){
                if(player>=zombie[i]){
                    player+=(player-zombie[i]);
                }
                else{
                    flag++;
                    break;
                }
            }
            if(player>=min && !flag)
                printf("Yes");
            else
                printf("No");
        }
        flag=0;
        test--;
    }
    return 0;
 }