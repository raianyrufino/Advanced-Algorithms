#include <bits/stdc++.h>
using namespace std;

int main(){
	int i, n, aux=0, answer=0, substring1=0, substring2=0;
  cin >> n;
  vector<int> sushis(n);

	for(i = 0; i < n; i++){
		cin >> sushis[i];
	}
	
	if (sushis[0] == 1) substring1++;
	else substring2++;
		
	for(i = 1; i < n; i++){
		
    if (sushis[i-1] != sushis[i]) aux++;
	
		if (aux==2) {
			answer = max(answer, min(substring1, substring2));
			if (sushis[i] == 1) substring1 = 0;
			else substring2 = 0;
			aux = 1;
		}
		
    if (sushis[i]==1) substring1++;
		else substring2++;
	}

	answer = max(answer, min(substring1, substring2));
  
  cout << answer*2 << endl;
	
	return 0;
}
