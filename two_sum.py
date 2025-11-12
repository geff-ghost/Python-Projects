from jovian.pythondsa import evaluate_test_case
test = {
    'input': {'nums': [3, 2, 4], 'target': 6},
    'output': [1, 2]
}


def two_sum1(nums, target):
    if not nums:
        return None
    
    for i in range(len(nums)):
        for j in range(i+1 ,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

def two_sum(nums, target):
    output = []
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in nums and nums.index(remaining) != i:
            output.append(i)
            output.append(nums.index(remaining))
            return output
        
output = two_sum(test['input']['nums'], test['input']['target'])
result = evaluate_test_case(two_sum, test)
