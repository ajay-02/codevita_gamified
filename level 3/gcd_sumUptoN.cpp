#include<iostream>
using namespace std;
int gcd(int a,int b){
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
int main(){
    int i,j,n,s=0;
    cin>>n;
    for(i=1;j<n;j++)
        for(j=i+1;j<=n;j++)
            s=s+gcd(i,j)
    cout<<s;
    return 0;
}
