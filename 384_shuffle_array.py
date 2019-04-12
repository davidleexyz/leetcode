class Solution:

    def __init__(self, nums: List[int]):
    	self.elements = tuple(nums)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return list(self.elements)
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = list(self.elements)

        for i in reversed(range(len(res))):
        	j = random.randint(0, i)
        	res[i], res[j] = res[j], res[i]
        return res
