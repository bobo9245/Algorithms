#include <bits/stdc++.h>

using namespace std;

class stack_fun
{
	public:
		int idx = 0;
		void push()
		{
			idx++;
		}
		
		void pop()
		{
			idx--;
		}
};

int main()
{
	int a;
	cin >> a;
	while(a--)
	{
		stack_fun s;
		cin.tie(0);
		ios::sync_with_stdio(0);
		string str;
		cin >> str;
		for(auto c : str)
		{
			if(c == '(')
			{
			 	 s.push();
			}
			else if(c == ')')
			{
				s.pop();
				if(s.idx<0)
				{
					goto AAA;
				}
			}
		}
		AAA:
		if(s.idx == 0)
		{
			cout << "YES\n";
		}
		else
		{
			cout << "NO\n";
		}
		
	}
	return 0;
}