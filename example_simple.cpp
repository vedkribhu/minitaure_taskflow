#include <bits/stdc++.h>
using namespace std;
#include "executor.hpp"
#include <unistd.h>
#define Sleep(X) usleep(X * 1000)
#include <chrono> 
using namespace std::chrono; 
  



//----------------------------------------Define required tasks or functions-----------------------
void fun1(){
	cout<<"Function 1 start!\n";
	Sleep(500);
	cout<<"Function 1 finish!\n";
}
void fun2(){
	cout<<"Function 2 start!\n";
	Sleep(500);
	cout<<"Function 2 finish!\n";
}
void fun3(){
	cout<<"Function 3 start!\n";
	Sleep(1000);
	cout<<"Function 3 finish!\n";
}
void fun4(){
	cout<<"Function 4 start!\n";
	Sleep(1000);
	cout<<"Function 4 finish!\n";
}
void fun5(){
	cout<<"Function 5 start!\n";
	Sleep(1000);
	cout<<"Function 5 finish!\n";
}
void fun6(){
	cout<<"Function 6 start!\n";
	Sleep(1000);
	cout<<"Function 6 finish!\n";
}
void fun7(){
	cout<<"Function 7 start!\n";
	Sleep(3000);
	cout<<"Function 7 finish!\n";
}
//----------------------------------------------------------------------------------

int main(){

	auto start = high_resolution_clock::now();		// for measuring runtime



	Taskflow myflow = Taskflow("myflow");

	auto A = myflow.add({
		fun1,
		fun2, 
		fun3, 
		fun4,
		fun5, 
		fun6,
		fun7
	});

	

	A[1]->precede({A[0]});
	A[2]->precede({A[0]});
	A[3]->precede({A[0]});
	A[4]->precede({A[3], A[1]});
	A[5]->precede({A[3],A[1]});
	A[6]->precede({A[4],A[2]});

	// Dump output into a dot file	
	ofstream myfile;
	myfile.open(myflow.name+"_graph.dot");
	myflow.dump(myfile);	
	
	Executor exe;

	exe.run({myflow});




	auto stop = high_resolution_clock::now(); 						// measure runtime
	auto duration = duration_cast<microseconds>(stop - start); 
	cout <<"Total time taken for mini-taskflow:"<< duration.count()/1e6 << endl; 
	return 0;


}