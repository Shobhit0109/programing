#include <iostream>
#include <stdio.h>
using namespace std;

class New
{
  public:
	int a = 7;
	void fuc()
	{
		class New hey;
		cout << hey.a;
		hey.fuc();
	}
	static void yew()
	{
		class New hey;
		cout << hey.a;
		hey.yew();
	}
};

int main(int argc, char *argv[])
{
	class New hey;
	//	hey.fuc();
	//	hey.yew();
	return 0;
}