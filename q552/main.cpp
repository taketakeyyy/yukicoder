#include<iostream>
#include<string>
using namespace std;
int main(){
	string ans;
	cin >> ans;
	if(ans == "0"){
		cout << "0\n";
		return 0;
	}
	cout << ans + "0" << "\n";
	return 0;
}
