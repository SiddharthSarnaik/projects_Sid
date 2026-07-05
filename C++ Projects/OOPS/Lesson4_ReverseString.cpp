#include<iostream>
using namespace std;

int main()

{
//Reverse a string.

string sRev="Measure";
int start=0, end=sRev.size()-1;

while (start<end)
{
   swap(sRev[start],sRev[end]);
   start++,end--;
}

cout<<"Reverse of the input string is  "<<sRev<<endl;

}

