class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


if __name__ == '__main__':
    nums1 = [9,9,9,9,9,9,9]
    nums2 = [9,9,9,9]

    list1 = ListNode()
    list2 = ListNode()
    head = ListNode()

    # 给链表1赋值
    idea = list1
    for i in range(len(nums1)):
        idea.val = nums1[i]
        if i != len(nums1) - 1:
            idea.next_node = ListNode()
            idea = idea.next_node
    # 给链表2赋值
    idea = list2
    for i in range(len(nums2)):
        idea.val = nums2[i]
        if i != len(nums2) - 1:
            idea.next_node = ListNode()
            idea = idea.next_node

    idea1 = list1
    idea2 = list2
    idea3 = head


    while True:
        ii = 0
        if idea1 is not None:
            if idea2 is not None:
                idea3.val = idea1.val + idea2.val + idea3.val
                idea1 = idea1.next_node
                idea2 = idea2.next_node
            else:
                idea3.val = idea1.val + idea3.val
                idea1 = idea1.next_node
        elif idea2 is not None:
            idea3.val = idea2.val + idea3.val
            idea2 = idea2.next_node



        if idea1 is None and idea2 is None:
            if idea3.val >= 10:
                ii = idea3.val // 10
                idea3.val = idea3.val % 10
                idea3.next_node = ListNode(ii)
            break
        elif idea3.val >= 10:
            ii = idea3.val // 10
            idea3.val = idea3.val % 10


        idea3.next_node = ListNode(ii)
        idea3 = idea3.next_node

    idea3 = head


    
    while idea3 is not None:
        print(idea3.val)
        idea3 = idea3.next_node

























