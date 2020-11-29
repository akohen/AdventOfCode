from pathlib import Path
import sys

test_mode = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False

def execute_steps(steps):
    def pop_step(i):
        def pop(step):
            if step != None and i in step: step.remove(i)
            return step
        return pop

    order = ""
    # until we've executed all steps
    while len(order) < len(steps):
        # find the next step with 0 blocked step
        for i, step in enumerate(steps):
            if step != None and len(step) == 0:
                # pop from other steps
                steps = list(map(pop_step(i), steps)) 
                # add to done steps
                steps[i] = None
                order += chr(65+i)
                break
    return order

def execute_steps_workers(steps, worker_count=2, task_time=1):
    def get_job():
        for i, step in enumerate(steps):
            if step != None and len(step) == 0:
                steps[i] = None
                return i
        return False


    def pop_step(i):
        def pop(step):
            if step != None and i in step: step.remove(i)
            return step
        return pop
    
    
    done = ""
    total_time = 0
    workers = [[999] for i in range(worker_count)]
    while len(done) < len(steps):
        workers = sorted(workers) # workers are sorted by time left in task, idle workers at the end

        # assign workers
        while len(workers[-1]) == 1 and (job := get_job()) is not False:
            workers[-1] = [job+task_time, job]
            workers = sorted(workers)

        # remove completed tasks
        timestep = workers[0][0]
        total_time += timestep
        for i in range(worker_count):
            if len(workers[i]) > 1:
                workers[i][0] -= timestep
                if workers[i][0] <= 0:
                    done += chr(65+workers[i][1])
                    steps = list(map(pop_step(workers[i][1]), steps)) 
                    workers[i] = [999]

    return (done, total_time)

if __name__ == "__main__":
    with Path(__file__).parent.joinpath("input/day7_sample" if test_mode else "input/day7").open() as f:
        instructions = [(ord(line[5])-65,ord(line[36])-65) for line in f]
        step_count = 6 if test_mode else 26
        worker_count = 2 if test_mode else 15
        task_time = 1 if test_mode else 61
        steps = [[] for i in range(step_count)]
        steps2 = [[] for i in range(step_count)]
        for line in instructions:
            steps[line[1]].append(line[0])
            steps2[line[1]].append(line[0])
        
        print('Phase 1: {}'.format(execute_steps(steps)))
        print('Phase 2: {1}'.format(*execute_steps_workers(steps2, worker_count, task_time)))