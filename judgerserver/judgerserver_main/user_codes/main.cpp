#include<iostream>
using namespace std;
char num[25]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K'};
char ans[200];//inverse
int count=0;
int main()
{
    long long int n,p;
    int r=0,t=0;
    cin>>n>>r;
    p=n;
    while(n!=0)
    {
        t=n%r;
        n=n/r;
        while(t<0)
        {
            t-=r;
            n++;
        }
        ans[count]=num[t];
        count++;
    }
    cout<<p<<"=";
    for(count=count-1;count>=0;count--)
    {
        cout<<ans[count];
    }
    cout<<"(base"<<r<<")"<<endl;
    return 0;
}