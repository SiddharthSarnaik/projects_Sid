#include<iostream>
using namespace std;

class Student
{
    public: 
    string name;
    int age,roll_number;
    string grade;

};


int main()
{

Student S1;
S1.name="Siddharth";
S1.age= 22;
S1.roll_number=44;
S1.grade="A+";
cout<<"Name is "<<S1.name<<",Age is "<<S1.age<<",Roll_Number is "<<S1.roll_number<<",Grade is "<<S1.grade<<endl;

Student S2;

S2.name="Mohit";
S2.age= 22;
S2.roll_number=33;
S2.grade="A+";
cout<<"Name is "<<S2.name<<",Age is "<<S2.age<<",Roll_Number is "<<S2.roll_number<<",Grade is "<<S2.grade<<endl;

}