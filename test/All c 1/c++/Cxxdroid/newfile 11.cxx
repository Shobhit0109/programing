#include <iostream>
#include <stdio.h>
using namespace std;

int main(int argc, char *argv[])
{
	char *a = 0;
	printf("%p\n", a);
	a = "hey";
	printf("%p\n", a);
	int *b = 0;
	printf("%p\n", b);
	b = {1, 4} //works for array only
	printf("%p", b);
	a[1] = 'h'; //read only memory
	cout << a;
	return 0;
}
/*
reference:
https://www.google.com/search?q=iso+c%2B%2B+does+not+allow+conversion+from+string+literal+to+char*&oq=iso+c%2B%2B+does+not+allow+conversation+from+syring&aqs=chrome.1.69i57j0i13j0i22i30j0i390.15871j0j16&sourceid=chrome-mobile&ie=UTF-8
https://stackoverflow.com/questions/20944784/why-is-conversion-from-string-constant-to-char-valid-in-c-but-invalid-in-c
https://www.google.com/search?q=is+string+literal+in+c&oq=is+string+literal+&aqs=chrome.3.69i57j0i512j0i22i30l2j0i15i22i30l2j0i22i30l3.7814j0j7&sourceid=chrome-mobile&ie=UTF-8
https://www.google.com/search?q=scalar+initializer+vs+string+literal+in+c&oq=scalar+initializer+vs+string+literal+in+c&aqs=chrome..69i57j33i160.8351j0j7&sourceid=chrome-mobile&ie=UTF-8
https://stackoverflow.com/questions/30533439/string-literals-vs-array-of-char-when-initializing-a-pointer
*/