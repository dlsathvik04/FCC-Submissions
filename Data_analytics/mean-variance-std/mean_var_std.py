import numpy as np

def calculate(lis):
    if (len(lis) != 9):
        raise ValueError("List must contain nine numbers.")
        
    result = {}
    nums = np.array(lis).reshape((3,3))
    result["mean"] = [list(np.mean(nums,axis=0)), list(np.mean(nums,axis=1)),  np.mean(nums.flatten())]
    result["variance"] = [list(np.var(nums,axis=0)), list(np.var(nums,axis=1)), np.var(nums.flatten())]
    result["standard deviation"] = [list(np.std(nums,axis=0)), list(np.std(nums,axis=1)), np.std(nums.flatten())]
    result["max"] = [list(np.max(nums,axis=0)), list(np.max(nums,axis=1)), np.max(nums.flatten())]
    result["min"] = [list(np.min(nums,axis=0)), list(np.min(nums,axis=1)), np.min(nums.flatten())]
    result["sum"] = [list(np.sum(nums,axis=0)), list(np.sum(nums,axis=1)), np.sum(nums.flatten())]
    return result
