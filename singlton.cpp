#include <iostream>
using namespace std;
class singleton
{
    int a,b;
    static singleton *instance;
protected:
    singleton();
public:
    static singleton* getInstance();
    friend ostream& operator<<(ostream&,const singleton&);
};
int main()
{
    singleton sin1();
    cout<<"1: "<<sin1<<endl;
    cout<<"2:" <<*singleton::getInstance()<<endl;
    cout<<"3:" <<*singleton::getInstance()<<endl;
    return 0;
}
singleton::singleton()
{
    a = 1;
    b = 2;
}
singleton* singleton::instance = 0;
singleton* singleton::getInstance()
{
    if(!instance)
    {
        cout<<"new instance"<<endl;
        instance = new singleton();
    }
    return instance;
}
ostream& operator<<(ostream& text,const singleton& sin)
{
    if(sin.a || sin.b)
    {
    text <<"["<<sin.a<<","<<sin.b<<"]";
	return text;
    }else
    {
        return text <<"0";
    }
}
