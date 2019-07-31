#include <iostream>
using namespace std;
int main()
{
    int a[100] , N,flag=0;
    cin>>n;
     for(int i=0; i<N; i++)
     {
        cin>>a[i];
     }
    for(int i=0; i<N; i++)
     {
         for(int j=i+1; j<N; j++)
         {
             if(a[i]==a[j])
             {
                flag=1;
                cout<<a[i];
             }
        }
     }
     if(flag==0)
     {
         cout<<"unique";
     }
 return 0;
}
