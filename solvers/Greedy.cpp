#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
  cin.sync_with_stdio(0); cin.tie(0);
  cin.exceptions(cin.failbit);

  int n; cin >> n;
  int num[5];
  vi groupSizes;
  rep(s,2,5) rep(_,0,num[s]) groupSizes.push_back(s);
  reverse(all(groupSizes));

  cin >> num[2] >> num[3] >> num[4];
  cerr << "read a line or something" << endl;
  vector<pair<pii,set<string>>> pizzas(n);
  rep(i,0,n) {
    cin >> pizzas[i].first.first;
    pizzas[i].first.second = i;
    rep(_,0,pizzas[i].first.first) {
      string temp; cin >> temp;
      pizzas[i].second.insert(temp);
    }
  }
  sort(all(pizzas));

  reverse(all(pizzas));
  int groupIndex = 0;
  int pizzaIndex = 0;

  cerr << "this is where " << endl;

  vector<vi> output;
  while(groupIndex < sz(groupSizes) && pizzaIndex < sz(pizzas)) {
    vi temp;
    int pizzasRemaining = sz(pizzas) - pizzaIndex;
    if (pizzasRemaining < groupSizes[groupIndex]) {
      pizzaIndex++;
      continue;
    }
    rep(_,0,groupSizes[groupIndex]) {
      temp.push_back(pizzas[pizzaIndex].first.second);
      pizzaIndex++;
    }
    output.push_back(temp);
    groupIndex++;
  }
  cout << sz(output) << endl;
  trav(elem, output) {
    cout << sz(elem);
    trav(i, elem) cout << " " << i;
    cout << endl;
  }
  /*
  cerr << sz(output) << endl;
  trav(elem, output) {
    cerr << sz(elem);
    trav(i, elem) cerr << " " << i;
    cerr << endl;
  }*/
}
