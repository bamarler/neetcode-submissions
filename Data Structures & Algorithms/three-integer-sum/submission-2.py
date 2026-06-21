class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets: List[List[int]] = []

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        triplet: List[int] = [nums[i], nums[j], nums[k]]
                        print(f"Triplet: {triplet}")
                        sorted_triplet: List[int] = sorted(triplet)
                        print(f"Sorted Triplet: {sorted_triplet}")
                        if (sorted_triplet not in triplets):
                            triplets.append(sorted_triplet)

        return triplets