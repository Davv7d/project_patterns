#include <iostream>
using namespace std;
class Wektor3D
{
    float x, y, z;

public:
    Wektor3D(float = 0,float = 0, float = 0);
    Wektor3D operator+(Wektor3D);
    friend ostream & operator<<(std::ostream&,const Wektor3D&);

	float getX() {return this -> x;}
	float getY() {return this -> y;}
	float getZ() {return this -> z;}
};

class fasadaWektor2D
{
    Wektor3D *fasadaW3D;

public:
    fasadaWektor2D(float = 0, float = 0);
    fasadaWektor2D operator+(fasadaWektor2D f2D);
    friend ostream& operator<<(ostream&,const fasadaWektor2D&);
};
int main()
{
    Wektor3D w3d1(11,22,33),w3d2;
    cout<<w3d1<<endl;
    w3d2 = w3d1 +w3d1;
    cout<<w3d2<<endl;

    fasadaWektor2D f2d1(11,22),f2d2;
    cout<<f2d1<<endl;
    f2d2 = f2d1 +f2d1;
    cout<<f2d2<<endl;
    return 0;
}

Wektor3D::Wektor3D(float w1,float w2, float w3)
{
    x = w1;
    y = w2;
    z = w3;
}
fasadaWektor2D::fasadaWektor2D(float a, float b)
{
    fasadaW3D = new  Wektor3D(a,b,0);
}

Wektor3D Wektor3D::operator+(Wektor3D temporaryW3D)
{
    x = temporaryW3D.x + x;
    y = temporaryW3D.y + y;
    z = temporaryW3D.z + z;
    return Wektor3D(x,y,z);
}
fasadaWektor2D fasadaWektor2D::operator+(fasadaWektor2D f2D)
{
   return fasadaWektor2D ( fasadaW3D -> getX() + f2D.fasadaW3D -> getX(), fasadaW3D -> getY() + f2D.fasadaW3D -> getY() );
}
ostream& operator<<(ostream& text,const Wektor3D& w3d)
{
	text <<"["<<w3d.x<<","<<w3d.y<<"."<<w3d.z<<"]";
	return text;
}

ostream& operator<<(ostream& text,const fasadaWektor2D& w2d)
{
	return text <<"["<<w2d.fasadaW3D -> getX()<<","<< w2d.fasadaW3D -> getY()<<"]";

}
