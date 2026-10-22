class ListNode:
    def __init__(self, val = 0, next_node = None):
        self.val = val
        self.next_node = next_node



if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 5, 6]
    lll = []


    list1 = ListNode()
    list2 = ListNode()
    new_nums = ListNode()


    idea = list1
    for i in nums1:
        idea.val = i
        if i != nums1[-1]:
            idea.next_node = ListNode()
            idea = idea.next_node

    idea = list2
    for i in nums2:
        idea.val = i
        if i != nums2[-1]:
            idea.next_node = ListNode()
            idea = idea.next_node

    idea1 = list1
    idea2 = list2
    idea3 = new_nums
    while True:
        if idea1 is not None:
            if idea2 is not None:
                if idea1.val > idea2.val:
                    idea3.next_node = ListNode(idea2.val)
                    idea3 = idea3.next_node
                    idea2 = idea2.next_node
                else:
                    idea3.next_node = ListNode(idea1.val)
                    idea3 = idea3.next_node
                    idea1 = idea1.next_node
            else:
                    idea3.next_node = ListNode(idea1.val)
                    idea1 = idea1.next_node
                    idea3 = idea3.next_node
        else:
            if idea2 is not None:
                idea3.next_node = ListNode(idea2.val)
                idea2 = idea2.next_node
                idea3 = idea3.next_node
            else:
                break
    idea3 = new_nums.next_node
    while idea3 is not None:
        print(idea3.val)
        idea3 = idea3.next_node
