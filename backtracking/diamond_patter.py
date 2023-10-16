# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

test_cases = sys.stdin.readline()

for idx in range(0,int(test_cases)):
    num_lines = int(sys.stdin.readline())
    print(f'Case #{idx+1}:')
    for line_num in range(0,num_lines):
        output = [" "]*(num_lines)
        mid_index = num_lines//2
        star_1_pos = mid_index - line_num
        star_2_pos = mid_index + line_num
        output[star_1_pos]="*"
        output[star_2_pos]="*"
        print(output)

    for line_num in range(num_lines//2,0,-1):
        output = [" "]*(num_lines)
        mid_index = num_lines//2
        star_1_pos = mid_index - line_num
        star_2_pos = mid_index + line_num
        output[star_1_pos]="*"
        output[star_2_pos]="*"
        print(output)










