#include<iostream>
using namespace std;
  
class Person {
public:
    virtual void show() { cout << "Person::show \n"; }
    virtual ~Person() { cout << "Person::~Person \n"; }
};
  
class Doctor : public Person {
public:
    virtual void show() { cout << "Doctor::show \n"; }
    virtual ~Doctor() { cout << "Doctor::~Doctor \n"; }
};
  
void f(Person &person) { person.show(); }
void g(Person person) { person.show(); }

int main(void)
{
    Doctor doctor;

    f(doctor);
    g(doctor);

    Person *person = new Doctor();
    person->show();

    delete person;

    cout << "End \n";
    return 0;
}