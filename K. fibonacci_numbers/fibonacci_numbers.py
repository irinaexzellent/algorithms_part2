def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def count_commits_for_next(n):
    count_for_next_students = fibonacci(n+1)
    return count_for_next_students 


if __name__ == '__main__':
    print(count_commits_for_next(int(input())))