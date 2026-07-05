#include<iostream>
using namespace std;

class Student
{
    public: 
    string name;
    int age,roll_number;
    string grade;

    Student(string name,int age, int roll_number, string grade )
    {
        this->name=name;
        this->age=age;
        this->roll_number=roll_number;
        this->grade=grade;
    }

    void display()
    {
        cout<<"Name is "<<name<<",Age is "<<age<<",Roll_Number is "<<roll_number<<",Grade is "<<grade<<endl;
    }

};


int main()
{

Student S1("Siddharth",22,44,"A+");
S1.display();

Student S2("Mohit",22,33,"B+");
S2.display();

}