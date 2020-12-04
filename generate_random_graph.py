import os, subprocess
class union_find:

    def __init__(self, n):
        self.n = n
        self.rank = [0]*n
        self.parent = [int(j) for j in range(n)]
    
    def union(self,i,j):
        i = self.find(i)
        j = self.find(j)
        if self.rank[i] == self.rank[j]:
            self.parent[i] = j
            self.rank[j] += 1

        elif self.rank[i] > self.rank[j]:
            self.parent[j] = i
        else:
            self.parent[i] = j

    def find(self, i):
        temp = i
        if self.parent[temp] != temp:
            self.parent[temp] = self.find(self.parent[temp])
        return self.parent[temp]


import random 
input_graph = [30+10*x for x in range(6)]
for num_nodes in input_graph:
    # num_nodes = 60
    for randome in range(10):
        n = num_nodes
        num_edges = int((num_nodes**2)*(0.134))
        u = union_find(num_nodes)
        i = 0 
        gr = [[] for i in range(n)]
        fd = open("generated_cpp.cpp", "w")
        fd.write("""#include <bits/stdc++.h>
        #include <fstream>
        using namespace std;
        #include "executor.hpp"
        #include <unistd.h>
        #define Sleep(X) usleep(X * 100)
        #include <chrono> 
        using namespace std::chrono; 
          

        //dot -Tpng myflow_graph.dot > output.png && eog output.png


        void fun1(){
            cout<<"Function 1 start!\\n";
            Sleep(500);
            cout<<"Function 1 finish!\\n";
        }
        void fun2(){
            cout<<"Function 2 start!\\n";
            Sleep(500);
            cout<<"Function 2 finish!\\n";
        }
        void fun3(){
            cout<<"Function 3 start!\\n";
            Sleep(1000);
            cout<<"Function 3 finish!\\n";
        }
        void fun4(){
            cout<<"Function 4 start!\\n";
            Sleep(1000);
            cout<<"Function 4 finish!\\n";
        }
        void fun5(){
            cout<<"Function 5 start!\\n";
            Sleep(1000);
            cout<<"Function 5 finish!\\n";
        }
        void fun6(){
            cout<<"Function 6 start!\\n";
            Sleep(1000);
            cout<<"Function 6 finish!\\n";
        }
        void fun7(){
            cout<<"Function 7 start!\\n";
            Sleep(3000);
            cout<<"Function 7 finish!\\n";
        }
        void subflow_fun(){
            cout<<"subflow fun start\\n";
            cout<<"subflow fun end\\n";
        }

        int main(){
            
            Taskflow myflow = Taskflow("myflow");
            auto A = myflow.add({""")




        gr = [[] for i in range(n)]
        color = [0 for i in range(n)]

        for i in range(n-1):
            fd.write("      fun"+str(i%7+1)+",\n")
        fd.write("  fun"+str((n-1)%7+1)+"});\n")

        def dfs(a,b):
            color[a]=1
            if a==b:
                return 1
            for i in gr[a]:
                if color[i]==0:
                    if dfs(i,b)==1:
                        return 1
            return 0
        while(i<num_edges):
            a = random.choice([j for j in range(num_nodes)])
            b = random.choice([j for j in range(num_nodes)])
            # print(a,b)
            color = [0 for i in range(n)]
            if dfs(b,a)==0 and b not in gr[a]:
                i+=1
                # u.union(a,b)
                gr[a].append(b)
        # for i in range(n):
        #     # print("fun"+str(i%7+1)+",")
        #     fd.write(chr(65+(i%26))+str(i//26)+", ")
        for i in range(n):

            if(gr[i]):
                fd.write("A["+str(i)+"]->precede({")
            for j in gr[i][:-1]:
                fd.write("A["+str(j)+"], ")
            if gr[i]:
                fd.write("A["+str(gr[i][-1])+"]"+"});\n")

        fd.write("""ofstream times;
            times.open("main_data.csv",ios::app);
            Executor exe;
            // for(int i=1; i<16; i++){
                auto start = high_resolution_clock::now();
                exe.num_threads = 4;
                exe.run({myflow});

                auto stop = high_resolution_clock::now(); 
                auto duration = duration_cast<microseconds>(stop - start); 
                times<<duration.count()/1e6<<"\\n";
                // cout <<"Total time taken for mini-taskflow:"<< duration.count()/1e6 << endl; 
            // }



            return 0;}""")
        fd.close()

        subprocess.call("g++ -pthread -o try generated_cpp.cpp && ./try", shell=True)
        # print("\ndone\n")
        # for i in range(n):
        #     if(gr[i]):
        #         print(chr(65+(i%26))+str(i//26)+".succeed(", end="")
        #     for j in gr[i][:-1]:
        #         print(chr(65+(j%26))+str(j//26)+", ", end="")
        #     if gr[i]:
        #         print(chr(65+(gr[i][-1]%26))+str(gr[i][-1]//26)+");")
    # fdn = open("main_data.csv, "a+")






