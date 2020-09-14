#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> skills(n);
	for (int i = 0; i < n; ++i) {
		cin >> skills[i];
	}

	sort(skills.begin(), skills.end());

	int answer = 0;
	int j = 0;
	for (int i = 0; i < n; i++) {
		while (j < n && skills[j] - skills[i] <= 5) {
			j++;
			answer = max(answer, j - i);
		}
	}
	
	cout << answer << endl;
	
	return 0;
}
