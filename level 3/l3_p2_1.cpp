#include <iostream>
using namespace std;
int bit(int n){
    int min=999,max=0;
    while(n!=0){
        int d=n%10;
        if(min>d)
            min=d;
        if(max<d)
            max=d;
        n/=10;
    }
    int res=(max*11+min*7)%100;
    return res;
}
int main()
{
    int i,j,n;
    cin>>n;
    if(n>0 && n<=500){
        int arr[n];
        for(i=0;i<n;i++){
            cin>>arr[i];
            int cnt=0;
            int t=arr[i];
            while(t){
                cnt++;
                t/=10;
            }
            if(cnt!=3){
                return 0;
            }
            arr[i]=bit(arr[i]);
        }
        int msb=0,pair=0;
        for(i=0;i<n;i++){
            msb=0;
            for(j=i+2;j<n;j=j+2){
                if(arr[i]==0)
                    break;
                else if(arr[i]/10==arr[j]/10){
                    msb++;
                    arr[j]=0;
                    if(msb<=2)
                        pair++;
                }
            }
        }
        cout<<pair;
    }
    else{
        return 0;
    }
    return 0;
}
