#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1


int N, K;

unsigned int options (int* C, int* D, int start, int end, int shouldStart)
{
    int maxC = 0, maxPosC = 0;
    int maxD = 0, maxPosD = 0;

    #if DEBUG 
        cout << start << end << " ";
    #endif

    if (start >= end)
    {
        #if DEBUG
            cout << 0 << endl;
        #endif
        return 0;
    }

    for (int i = start; i < end; i++)
    {
        if (C[i] > maxC)
        {
            maxC = C[i];
            maxPosC = i;
        
        }
        
        if (D[i] > maxD)
        {
            maxD = D[i];
            maxPosD = i;
        
        }
    }

    if (maxC - maxD > K){
        #if DEBUG
            cout << 0 << endl;
        #endif
        return options(C, D, start, maxPosC, shouldStart) + (shouldStart ? 0 : options(C, D, maxPosC+1, end, shouldStart));
    }

    if (maxD - maxC > K){
        #if DEBUG
            cout << 0 << endl;
        #endif
        return options(C, D, start, maxPosD, shouldStart) + (shouldStart ? 0 : options(C, D, maxPosD+1, end, shouldStart));
    }

    #if DEBUG
        cout << 1 << endl;
    #endif
    int subStart = shouldStart? start : min(maxPosC, maxPosD);
    int subEnd = max(maxPosC, maxPosD);
    
    int sum = (end - subEnd) * (subStart - start+1);
    #if DEBUG
        cout << "test: " << subStart << " " << subEnd << " sum: " << sum << endl;
    #endif
    
    return sum + (shouldStart ? 0 : options(C, D, subStart+1, end, shouldStart)) + options(C, D, subStart, subEnd-1, true);
}

void solve(int t){
	cout << "Case #" << t << ": ";

	cin >> N >> K;
    int C[N];
    int D[N];

    for (int i = 0; i < N; i++)
    {
        cin >> C[i];
    }

    for (int i = 0; i < N; i++)
    {
        cin >> D[i];
    }

    int ans = options(C, D, 0, N, false);

    cout << ans << endl;
}

int main(){
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		solve(t);
	}
}