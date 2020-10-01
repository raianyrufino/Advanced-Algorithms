#include<vector>
#include <iostream> 
using namespace std;

int GCD(int a,int b)
{
	if (a%b==0)
		return b;
	return GCD(b,a%b);
}

int main()
{
    int n;
    scanf("%d", &n);

    vector <int> aux;
    for(int i = 1; i <= n; i++)
    {
        int number;
        scanf("%d", &number);

        if (i == 1 || GCD(aux.back(), number) == 1) {
          aux.push_back(number);
        } else {
          aux.push_back(1);
          aux.push_back(number);
        }
    }
    
    printf("%d\n", int(aux.size() - n));
    for(int i = 0; i < aux.size(); i++)
      printf("%d ", aux[i]);

    return 0;
}
