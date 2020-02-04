#include <iostream>
using namespace std;
template <class item>
class list
{

public:
     List(long size = DEFAULT_LIST_SIZE);
     long Count() const;
     Item& Get(long index) const;
//..
};

template <class Item>
class Iterator
{
protected:
    Iterator();
public:
    virtual void First() = 0;
    virtual void Next() = 0;
    virtual bool IsDone() const = 0;
    virtual Item CurrentItem() const = 0;

};
