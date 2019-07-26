#include <bits/stdc++.h>
using namespace std;

void solve(int t){
	//cout << "Case #" << t << ": ";
	
	
	
	vector<int> factors;
	
	for (int n : {5, 7, 9, 11, 13, 16, 17})
	{
	    for (int i = 0; i < 18; i++)
	    {
	        cout << n << " ";
	    }
	    cout << endl;
	
	    int bladeSum = 0;
	    for (int i = 0; i < 18; i++)
	    {
	        int blade;
	        cin >> blade;
	        bladeSum += blade;
	    }
	    
	    if (bladeSum % n == 0)
            factors.push_back(n);
    }
    
    int ans = 1;
    for (int x : factors)
    {
        ans *= x;
    }
    
    cout << ans << endl;
}

int main(){
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int T, N, M;
	cin >> T >> N >> M;
	for(int t = 1; t <= T; t++){
		solve(t);
	}
}
