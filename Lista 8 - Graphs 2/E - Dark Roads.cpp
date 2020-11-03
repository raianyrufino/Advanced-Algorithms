#include <bits/stdc++.h>

using namespace std;

int aux[200000];

int Find(int a) {
  if (a == aux[a]) {
    return a;
  } else {
    return aux[a] = Find(aux[a]);
  }
}

int main()
{
    int n, m;
    while(scanf("%d%d", &n, &m) && (n || m)) {

        int a = 0, x, y, z;
        vector<pair<int, pair<int, int> > > tuple;

        for(int i = 0; i < m; i++) {
            scanf("%d%d%d", &x, &y, &z);
            a += z;
            tuple.push_back(make_pair(z, make_pair(x, y)));
        }

        sort(tuple.begin(), tuple.end());

        for(int i = 0; i < n; i++)
          aux[i] = i;

        int cont = 0;
        
        for(int i = 0; i < tuple.size(); i++) {
            z = tuple[i].first;
            x = tuple[i].second.first;
            y = tuple[i].second.second;

            x = Find(x);
            y = Find(y);

            if(x != y) {
              cont += z;
              aux[y] = x;
            }
        }
        printf("%d\n", a - cont);
    }
    return 0;
}
