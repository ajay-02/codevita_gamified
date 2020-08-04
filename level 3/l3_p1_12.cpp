#include<iostream>
using namespace std;
long long int fib(long int n){
    long long int l[n+1];
    long long int i;
    l[0]=1;l[1]=0;l[2]=1;
    for(i=3;i<=n;i++)
        l[i]=((i-1)*(l[i-1]+l[i-2]))%100000007;
    return l[n];
}
int main(){
    long long int n;
    cin>>n;
    cout<<fib(n);
    return 0;
}
