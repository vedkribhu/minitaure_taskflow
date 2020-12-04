#include <bits/stdc++.h>
#include "taskflow.hpp"

using namespace std;


// Execcutor is where all execution of threads is performed.
class Executor {
	public:
		Executor(){};
		mutex mtx, cv_mtx;
		int num_threads = 4;
		condition_variable cond_var;
		vector<Task*> task_list;
		int total_task=0; 


		static void execute_thread(Executor* exe){
			bool flag=true;
			do {
				// check if any task in task list.
				exe->mtx.lock();	
				if(exe->task_list.size()==0){
					exe->mtx.unlock();
					return;
				}
				else{
					Task* new_task = exe->task_list[exe->task_list.size()-1];
					exe->task_list.pop_back();
					// If dependencies not sorted
					if(new_task->dependency>0){
						exe->task_list.push_back(new_task);
						exe->mtx.unlock();	
						unique_lock<mutex> lck(exe->cv_mtx);
						exe->cond_var.wait(lck);
						//sleep
					}
					else{
						// Execute task and notify sleeping threads
						exe->mtx.unlock();
						new_task->execute_task();
						for(auto suc_task: new_task->successor){
							suc_task->dependency--;
						}
						unique_lock<mutex> lck(exe->cv_mtx);
						exe->cond_var.notify_all();
						// notify all
					}
					
				}



			} while(flag!=false);
		};
		// Start threads
		void start_threads(int num_of_threads){
			vector<thread> all_threads;
			for(int i=0;i<num_of_threads;i++){
				thread th(execute_thread, this);
				all_threads.push_back(move(th));
			}
			for(int i=0;i<num_of_threads;i++){
				all_threads[i].join();
			}
			return;
		}
		// Abstraction function
		void run(vector<Taskflow> taskflow_list){
			// graph build
			for(auto current_taskflow: taskflow_list){
				current_taskflow.build();
				for(Task* task: current_taskflow.topological_sort_list){
					task_list.push_back(task);
					total_task++;
				}
			} 

			int num_of_threads = this->num_threads;
			this->start_threads(num_of_threads);

		}

};
