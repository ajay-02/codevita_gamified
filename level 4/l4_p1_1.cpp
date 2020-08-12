#include<iostream>
using namespace std;
int main()
{
    int n,f,b,t,d;
    cin>>n;
    if(n>=1 && n<=100){
        while(n--){
            cin>>f>>b>>t>>d;
            int count=0;
            int currentpos=0;
            int totaltime=0;
            if(f>=b || d==0 || t==0)
                cout<<"Cannot park";
            else{
                while(1){
                    if(currentpos+b<d)
                        currentpos +=b;
                    else{
                        int remainingdist=d-currentpos;
                        totaltime=remainingdist*t;
                        break;
                    }
                    currentpos=currentpos-f;
                    count++;
                }
                totaltime=totaltime+(f+b)*count*t;
                cout<<totaltime<<endl;
            }
        }
    }
    else{
        cout<<"Invalid test case"; 
    }
    return 0;
}